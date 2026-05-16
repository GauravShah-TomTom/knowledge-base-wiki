#!/usr/bin/env python3
"""Index wiki/<topic>/*.md into Azure AI Search with hybrid (BM25 + vector) retrieval.

Auth: Azure AI Search admin API key (matches what the chat handler uses).

Required env:
    AZURE_SEARCH_ENDPOINT             e.g. https://srch-team-wiki-ulkrw5.search.windows.net
    AZURE_SEARCH_INDEX_NAME           e.g. team-wiki
    AZURE_SEARCH_API_VERSION          e.g. 2024-07-01
    AZURE_SEARCH_API_KEY              admin key from the search service
    AZURE_OPENAI_ENDPOINT             e.g. https://api.chatgpt.tomtom-global.com
    AZURE_OPENAI_API_KEY              key for the embedding deployment
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT e.g. dep-text-embedding-3-small
    AZURE_OPENAI_API_VERSION          e.g. 2024-10-21
"""
from __future__ import annotations

import datetime
import hashlib
import os
import pathlib
import re
import sys

import requests
import yaml


WIKI_DIR = pathlib.Path("wiki")
TOPICS = ("competition", "concepts", "conversations", "decisions", "people", "problems", "projects", "systems")
BATCH_SIZE = 50  # smaller batches because each doc carries a 1536-float vector
EMBEDDING_DIMS = 1536  # text-embedding-3-small default
MAX_BODY_CHARS = 8000  # truncate body for embedding only — full body still indexed for BM25


def search_api_key() -> str:
    return os.environ["AZURE_SEARCH_API_KEY"]


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
            {"name": "superseded", "type": "Edm.Boolean", "filterable": True, "retrievable": True},
            {
                "name": "contentVector",
                "type": "Collection(Edm.Single)",
                "searchable": True,
                "retrievable": False,
                "dimensions": EMBEDDING_DIMS,
                "vectorSearchProfile": "default-vector-profile",
            },
        ],
        "vectorSearch": {
            "profiles": [{"name": "default-vector-profile", "algorithm": "default-hnsw"}],
            "algorithms": [{"name": "default-hnsw", "kind": "hnsw"}],
        },
        "semantic": {
            "configurations": [
                {
                    "name": "default-semantic",
                    "prioritizedFields": {
                        "titleField": {"fieldName": "title"},
                        "prioritizedContentFields": [{"fieldName": "body"}],
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
    return hashlib.sha1(path.encode("utf-8")).hexdigest()


def title_from(body: str, fallback: str) -> str:
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return s.removeprefix("# ").strip()
    return fallback


def embed_text(text: str) -> list[float]:
    """Call Azure OpenAI's embedding deployment for a single string."""
    endpoint = os.environ["AZURE_OPENAI_ENDPOINT"].rstrip("/")
    deployment = os.environ["AZURE_OPENAI_EMBEDDING_DEPLOYMENT"]
    api_version = os.environ.get("AZURE_OPENAI_API_VERSION", "2024-10-21")
    api_key = os.environ["AZURE_OPENAI_API_KEY"]

    url = f"{endpoint}/openai/deployments/{deployment}/embeddings?api-version={api_version}"
    body = {"input": text[:MAX_BODY_CHARS] or " "}
    r = requests.post(url, headers={"api-key": api_key, "Content-Type": "application/json"}, json=body, timeout=30)
    if r.status_code != 200:
        raise RuntimeError(f"embedding call failed: {r.status_code} {r.text}")
    return r.json()["data"][0]["embedding"]


def doc_for_path(rel: str) -> dict | None:
    """Build the index doc for a single wiki/<topic>/<file>.md path. Returns
    None if the path is outside scope (wrong topic, _index.md, missing file)."""
    parts = rel.split("/")
    if len(parts) < 3 or parts[0] != "wiki" or parts[1] not in TOPICS:
        return None
    if not rel.endswith(".md"):
        return None
    fname = parts[-1]
    if fname.startswith("_"):
        return None
    fpath = pathlib.Path(rel)
    if not fpath.is_file():
        return None

    topic = parts[1]
    text = fpath.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    title = title_from(body, fpath.stem)
    embedding_input = f"{title}\n\n{body}".strip()
    print(f"  embedding {rel} ...", file=sys.stderr)
    vector = embed_text(embedding_input)
    return {
        "@search.action": "mergeOrUpload",
        "id": make_doc_id(rel),
        "path": rel,
        "title": title,
        "body": body.strip(),
        "topic": topic,
        "feedback_count_negative": int(fm.get("feedback_count_negative") or 0),
        "last_feedback_negative": str(fm.get("last_feedback_negative") or ""),
        "superseded": bool(fm.get("superseded") or False),
        "contentVector": vector,
    }


def collect_docs(paths: list[str] | None = None) -> list[dict]:
    """Embed and return docs for the given paths, or for the full wiki tree if
    paths is None."""
    if paths is None:
        # Full walk
        rels: list[str] = []
        for topic in TOPICS:
            topic_dir = WIKI_DIR / topic
            if not topic_dir.is_dir():
                continue
            for path in topic_dir.glob("*.md"):
                if path.name.startswith("_"):
                    continue
                rels.append(str(path).replace("\\", "/"))
    else:
        rels = paths

    docs: list[dict] = []
    for rel in rels:
        doc = doc_for_path(rel)
        if doc:
            docs.append(doc)
    return docs


def deletion_docs(paths: list[str]) -> list[dict]:
    """Build delete-action docs for paths that were removed from the wiki."""
    out: list[dict] = []
    for rel in paths:
        if not rel.endswith(".md"):
            continue
        parts = rel.split("/")
        if len(parts) < 3 or parts[0] != "wiki" or parts[1] not in TOPICS:
            continue
        if parts[-1].startswith("_"):
            continue
        out.append({"@search.action": "delete", "id": make_doc_id(rel)})
    return out


def put_index(endpoint: str, name: str, api_version: str, api_key: str) -> None:
    url = f"{endpoint}/indexes/{name}?api-version={api_version}"
    body = index_schema(name)
    r = requests.put(
        url,
        headers={"api-key": api_key, "Content-Type": "application/json"},
        json=body,
        timeout=30,
    )
    if r.status_code not in (200, 201, 204):
        print(f"PUT index failed: {r.status_code} {r.text}", file=sys.stderr)
        r.raise_for_status()
    print(f"Index `{name}` schema is current.")


def push_docs(endpoint: str, name: str, api_version: str, api_key: str, docs: list[dict]) -> None:
    if not docs:
        print("No docs to push.")
        return
    url = f"{endpoint}/indexes/{name}/docs/index?api-version={api_version}"
    for i in range(0, len(docs), BATCH_SIZE):
        batch = docs[i : i + BATCH_SIZE]
        r = requests.post(
            url,
            headers={"api-key": api_key, "Content-Type": "application/json"},
            json={"value": batch},
            timeout=120,
        )
        if r.status_code not in (200, 201, 207):
            print(f"POST docs failed: {r.status_code} {r.text}", file=sys.stderr)
            r.raise_for_status()
        print(f"Pushed {i + len(batch)} / {len(docs)} docs.")


def parse_path_list(env_value: str) -> list[str]:
    return [line.strip() for line in env_value.splitlines() if line.strip()]


def main() -> int:
    endpoint = os.environ["AZURE_SEARCH_ENDPOINT"].rstrip("/")
    name = os.environ["AZURE_SEARCH_INDEX_NAME"]
    api_version = os.environ.get("AZURE_SEARCH_API_VERSION", "2024-07-01")

    api_key = search_api_key()
    put_index(endpoint, name, api_version, api_key)

    mode = os.environ.get("WIKI_INDEX_MODE", "full").lower()
    changed = parse_path_list(os.environ.get("WIKI_CHANGED_FILES", ""))
    deleted = parse_path_list(os.environ.get("WIKI_DELETED_FILES", ""))

    if mode == "incremental":
        print(f"Incremental run: {len(changed)} added/modified, {len(deleted)} deleted.")
        docs = collect_docs(paths=changed) if changed else []
        if deleted:
            docs = docs + deletion_docs(deleted)
        if not docs:
            print("Nothing changed under wiki/<topic>/*.md — index unchanged.")
        else:
            push_docs(endpoint, name, api_version, api_key, docs)
    else:
        print("Full re-embed: walking entire wiki tree ...")
        docs = collect_docs()
        print(f"Collected {len(docs)} docs.")
        push_docs(endpoint, name, api_version, api_key, docs)

    print(f"\nDone — index `{name}` updated as of {datetime.datetime.now(datetime.timezone.utc).isoformat()} (mode={mode})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
