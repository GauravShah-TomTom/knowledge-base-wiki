#!/usr/bin/env python3
"""Download new Azure raw/* blobs that aren't already recorded in wiki/log.jsonl.

Each downloaded blob lands at raw/<name> and an idempotency entry is appended to
wiki/log.jsonl with status=seen so the next cron run skips it.

Required env:
    AZURE_STORAGE_ACCOUNT  Storage account name
    RAW_CONTAINER          Container name (default: 'raw')

Exit codes:
    0  done (downloaded zero or more blobs cleanly)
    1  configuration / az error
"""

import datetime
import json
import os
import pathlib
import subprocess
import sys

LOG = pathlib.Path("wiki/log.jsonl")


def already_seen() -> set[str]:
    if not LOG.exists():
        return set()
    seen = set()
    for line in LOG.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except Exception:
            continue
        for key in ("blob", "file", "path"):
            v = obj.get(key)
            if v:
                seen.add(v)
                break
    return seen


def list_blobs(account: str, container: str) -> list[dict]:
    out = subprocess.check_output([
        "az", "storage", "blob", "list",
        "--account-name", account,
        "--container-name", container,
        "--auth-mode", "login",
        "--query", "[].{name:name, etag:properties.etag, size:properties.contentLength}",
        "-o", "json",
    ])
    return json.loads(out)


def download_blob(account: str, container: str, name: str, dest: pathlib.Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "az", "storage", "blob", "download",
        "--account-name", account,
        "--container-name", container,
        "--name", name,
        "--file", str(dest),
        "--auth-mode", "login",
        "--no-progress",
    ], check=True, stdout=subprocess.DEVNULL)


def main() -> int:
    account = os.environ.get("AZURE_STORAGE_ACCOUNT")
    if not account:
        print("AZURE_STORAGE_ACCOUNT must be set", file=sys.stderr)
        return 1
    container = os.environ.get("RAW_CONTAINER", "raw")

    seen = already_seen()
    print(f"Listing blobs in {account}/{container}...", file=sys.stderr)
    blobs = list_blobs(account, container)

    new = [b for b in blobs if b["name"] not in seen]
    if not new:
        print("No new blobs.")
        return 0

    LOG.parent.mkdir(parents=True, exist_ok=True)
    log_lines = []
    for b in new:
        name = b["name"]
        size = b.get("size", 0)
        etag = (b.get("etag") or "").strip('"')
        local = pathlib.Path("raw") / name
        print(f"  -> raw/{name} ({size} bytes)")
        download_blob(account, container, name, local)
        log_lines.append(json.dumps({
            "blob": name,
            "etag": etag,
            "status": "seen",
            "size": size,
            "ts": datetime.datetime.now(datetime.timezone.utc)
                .replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        }))

    with LOG.open("a", encoding="utf-8") as f:
        f.write("\n".join(log_lines) + "\n")
    print(f"Downloaded {len(new)} new blob(s); log.jsonl updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
