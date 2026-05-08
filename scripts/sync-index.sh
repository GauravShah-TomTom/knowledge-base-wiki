#!/usr/bin/env bash
# Download the latest QMD SQLite index from Azure Blob into ~/.cache/qmd/.
#
# Hooked from .githooks/post-merge so `git pull` on main keeps the local
# index fresh — but you can also run it manually any time.
#
# Required: `az login` (uses --auth-mode login).
# Optional env:
#   AZURE_STORAGE_ACCOUNT   default: stteamwikiulkrw5
#   INDEX_CONTAINER         default: wiki-index
#   INDEX_BLOB              default: index.sqlite.gz
#
# Exits 0 on success or any non-fatal skip (no blob yet, az unavailable,
# auth needed) — never blocks a merge.
set -euo pipefail

ACCOUNT="${AZURE_STORAGE_ACCOUNT:-stteamwikiulkrw5}"
CONTAINER="${INDEX_CONTAINER:-wiki-index}"
BLOB="${INDEX_BLOB:-index.sqlite.gz}"

CACHE_DIR="$HOME/.cache/qmd"
DEST="$CACHE_DIR/index.sqlite"
DEST_GZ="$DEST.gz"

mkdir -p "$CACHE_DIR"

if ! command -v az &>/dev/null; then
    echo "[sync-index] az CLI not found — skipping. Install: brew install azure-cli" >&2
    exit 0
fi

ERR_FILE="$(mktemp)"
trap 'rm -f "$ERR_FILE"' EXIT

echo "[sync-index] $ACCOUNT/$CONTAINER/$BLOB → $DEST_GZ"
if ! az storage blob download \
        --account-name "$ACCOUNT" \
        --container-name "$CONTAINER" \
        --name "$BLOB" \
        --file "$DEST_GZ" \
        --auth-mode login \
        --no-progress \
        2>"$ERR_FILE"; then
    err=$(cat "$ERR_FILE")
    if echo "$err" | grep -qiE 'BlobNotFound|ResourceNotFound|specified blob does not exist'; then
        echo "[sync-index] No index uploaded yet — nothing to sync." >&2
        exit 0
    fi
    if echo "$err" | grep -qiE 'AuthorizationFailed|AADSTS|Please run.*az login|not authorized'; then
        echo "[sync-index] Auth needed — run 'az login', then re-run this script." >&2
        exit 0
    fi
    echo "[sync-index] az download failed:" >&2
    echo "$err" >&2
    exit 1
fi

gunzip -f "$DEST_GZ"
SIZE=$(stat -f%z "$DEST" 2>/dev/null || stat -c%s "$DEST")
echo "[sync-index] OK — $DEST ($SIZE bytes)"
