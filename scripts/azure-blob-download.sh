#!/usr/bin/env bash
# Downloads any blobs in Azure raw/ that aren't already recorded in wiki/log.jsonl.
# Each new blob lands at the matching local raw/<subfolder>/<filename>.
#
# Idempotency: each downloaded blob is appended to wiki/log.jsonl with status=seen.
# The next run skips it.
#
# Usage:
#   AZURE_STORAGE_ACCOUNT=stteamwikiulkrw5 RAW_CONTAINER=raw \
#     bash scripts/azure-blob-download.sh
#
# Required env:
#   AZURE_STORAGE_ACCOUNT  Storage account name
#   RAW_CONTAINER          Blob container name (typically "raw")
#
# Exit codes:
#   0  Done (whether or not anything was downloaded)
#   1  Configuration error / az failure

set -euo pipefail

: "${AZURE_STORAGE_ACCOUNT:?AZURE_STORAGE_ACCOUNT must be set}"
: "${RAW_CONTAINER:=raw}"

LOG="wiki/log.jsonl"
SEEN_FILE=$(mktemp)
trap 'rm -f "$SEEN_FILE"' EXIT

# Build the set of already-processed blob paths (each line in log.jsonl is one entry)
if [[ -f "$LOG" ]]; then
    # The log entry uses key "blob" (preferred) or "file" (legacy from existing converters)
    python3 -c '
import json, sys, pathlib
for line in pathlib.Path("'"$LOG"'").read_text(encoding="utf-8").splitlines():
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
            print(v)
            break
' > "$SEEN_FILE"
fi

# List blobs in the container
echo "Listing blobs in $AZURE_STORAGE_ACCOUNT/$RAW_CONTAINER..." >&2
ALL_BLOBS=$(az storage blob list \
    --account-name "$AZURE_STORAGE_ACCOUNT" \
    --container-name "$RAW_CONTAINER" \
    --auth-mode login \
    --query "[].{name:name, etag:properties.etag, size:properties.contentLength}" \
    -o json)

# Diff against seen set; download what's new
mkdir -p raw
new_count=0
echo "$ALL_BLOBS" | python3 -c '
import json, os, subprocess, sys, pathlib

seen_path = os.environ["SEEN_FILE"]
seen = set(pathlib.Path(seen_path).read_text(encoding="utf-8").splitlines()) if os.path.exists(seen_path) else set()

blobs = json.load(sys.stdin)
to_download = []
for b in blobs:
    name = b["name"]                 # e.g. "transcripts/2026-05-07 sprint-12.vtt"
    if name in seen:
        continue
    # Also check the local raw/<name> path; if file already there, just record + skip
    local_path = pathlib.Path("raw") / name
    to_download.append({
        "name": name,
        "etag": (b.get("etag") or "").strip(\'"\'),
        "size": b.get("size", 0),
        "exists_local": local_path.exists(),
    })

print(json.dumps(to_download))
' > /tmp/to_download.json

# Process downloads + log entries
python3 -c '
import json, os, pathlib, subprocess, datetime

cfg = json.load(open("/tmp/to_download.json"))
account = os.environ["AZURE_STORAGE_ACCOUNT"]
container = os.environ["RAW_CONTAINER"]
log_path = pathlib.Path("wiki/log.jsonl")
log_path.parent.mkdir(parents=True, exist_ok=True)

new_lines = []
for b in cfg:
    name = b["name"]
    local = pathlib.Path("raw") / name
    local.parent.mkdir(parents=True, exist_ok=True)
    print(f"  -> raw/{name} ({b[\"size\"]} bytes)")
    subprocess.run([
        "az", "storage", "blob", "download",
        "--account-name", account,
        "--container-name", container,
        "--name", name,
        "--file", str(local),
        "--auth-mode", "login",
        "--no-progress",
    ], check=True, stdout=subprocess.DEVNULL)
    # Append idempotency record (the "seen" entry) — schema co-exists with finalize logs
    new_lines.append(json.dumps({
        "blob": name,
        "etag": b["etag"],
        "status": "seen",
        "size": b["size"],
        "ts": datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z",
    }))

if new_lines:
    with open(log_path, "a", encoding="utf-8") as f:
        f.write("\n".join(new_lines) + "\n")
    print(f"Downloaded {len(new_lines)} new blob(s); log.jsonl updated.")
    print(f"::set-env-marker::DOWNLOADED_COUNT={len(new_lines)}")
else:
    print("No new blobs.")
'

echo "Done." >&2
