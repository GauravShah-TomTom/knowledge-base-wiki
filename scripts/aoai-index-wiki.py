#!/usr/bin/env python3
"""Index wiki/<topic>/*.md into Azure AI Search.

Idempotent — recreates the index schema if the existing one is stale, then
upserts every wiki page. Auth via Azure CLI's logged-in identity (resource
audience https://search.azure.com).

Required env:
    AZURE_SEARCH_ENDPOINT      e.g. https://srch-team-wiki-ulkrw5.search.windows.net
    AZURE_SEARCH_INDEX_NAME    e.g. team-wiki
    AZURE_SEARCH_API_VERSION   e.g. 2024-07-01
"""
import datetime
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys

import requests
import yaml


WIKI_DIR = pathlib.Path("wiki")
TOPICS = ("competition", "concepts", "conversations", "decisions", "people", "problems", "projects", "systems")
BATCH_SIZE = 100


def az_token() -> str:
    out = subprocess.check_output(
        ["az", "account", "get-access-token", "--resource", "https://search.azure.com", "--query", "accessToken", "-o", "tsv"],
        text=True,
    )
    return out.strip()


def index_schema(name: str) -> dict:
    return {
        "name": name,
        "fields": [
            {"name": "id", "type": "Edm.String", "key": True, "filterable": True, "retrievable": True},
            {"name": "path", "type": "Edm.String", "filterable": True, "retrievable": True, "searchable": False},
            {"name": "title", "type": "Edm.String", "searchable": True, "retrievable": True},
            {"name": "body", "type": "Edm.String", "searchable": True, "retrievable": True},
            {"name": "topic", "type": "Edm.String", "filterable": True, "facetable": True, "retrievable": True, "searchable": False},
            {"name": "feedback_count_negative", "type": "Edm.Int32", "filterable": True, "sortable": True, "retrievable": True},
            {"name": "last_feedback_negative", "type": "Edm.String", "filterable": True, "sortable": True, "retrievable": True},
        ],
        "semantic": {
            "configurations": [
                {
                    "name": "default",
                    "prioritizedFields": {
                        "titleField": {"fieldName": "title"},
                        "prioritizedContentFields": [{"fieldName": "body"}],
                        "prioritizedKeywordsFields": [{"fieldName": "topic"}],
                    },
                }
            ]
        },
        "corsOptions": {"allowedOrigins": ["*"], "maxAgeInSeconds": 60},
    }


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, m.group(2)


def make_doc_id(path: str) -> str:
    # Azure Search keys must be URL-safe; SHA-1 hex is bulletproof.
    return hashlib.sha1(path.encode("utf-8")).hexdigest()


def title_from(body: str, fallback: str) -> str:
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return s.removeprefix("# ").strip()
    return fallback


def collect_docs() -> list[dict]:
    docs = []
    for topic in TOPICS:
        topic_dir = WIKI_DIR / topic
        if not topic_dir.is_dir():
            continue
        for path in topic_dir.glob("*.md"):
            if path.name.startswith("_"):
                continue
            text = path.read_text(encoding="utf-8")
            fm, body = parse_frontmatter(text)
            rel = str(path).replace("\\", "/")
            doc = {
                "@search.action": "mergeOrUpload",
                "id": make_doc_id(rel),
                "path": rel,
                "title": title_from(body, path.stem),
                "body": body.strip(),
                "topic": topic,
                "feedback_count_negative": int(fm.get("feedback_count_negative") or 0),
                "last_feedback_negative": str(fm.get("last_feedback_negative") or ""),
            }
            docs.append(doc)
    return docs


def put_index(endpoint: str, name: str, api_version: str, token: str) -> None:
    url = f"{endpoint}/indexes/{name}?api-version={api_version}"
    body = index_schema(name)
    r = requests.put(
        url,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json=body,
        timeout=30,
    )
    if r.status_code not in (200, 201, 204):
        print(f"PUT index failed: {r.status_code} {r.text}", file=sys.stderr)
        r.raise_for_status()
    print(f"Index `{name}` schema is current.")


def push_docs(endpoint: str, name: str, api_version: str, token: str, docs: list[dict]) -> None:
    if not docs:
        print("No docs to push.")
        return
    url = f"{endpoint}/indexes/{name}/docs/index?api-version={api_version}"
    for i in range(0, len(docs), BATCH_SIZE):
        batch = docs[i : i + BATCH_SIZE]
        r = requests.post(
            url,
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            json={"value": batch},
            timeout=60,
        )
        if r.status_code not in (200, 201, 207):
            print(f"POST docs failed: {r.status_code} {r.text}", file=sys.stderr)
            r.raise_for_status()
        print(f"Pushed {i + len(batch)} / {len(docs)} docs.")


def main() -> int:
    endpoint = os.environ["AZURE_SEARCH_ENDPOINT"].rstrip("/")
    name = os.environ["AZURE_SEARCH_INDEX_NAME"]
    api_version = os.environ.get("AZURE_SEARCH_API_VERSION", "2024-07-01")

    token = az_token()
    put_index(endpoint, name, api_version, token)
    docs = collect_docs()
    print(f"Collected {len(docs)} wiki docs.")
    push_docs(endpoint, name, api_version, token, docs)

    print(f"\nDone — index `{name}` populated as of {datetime.datetime.now(datetime.timezone.utc).isoformat()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
