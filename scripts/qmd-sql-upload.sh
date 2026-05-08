#!/usr/bin/env bash
# Upload the gzipped QMD SQLite index to the wiki-index/ Azure Blob container.
# Used by .github/workflows/wiki-rebuild-index.yml after `qmd update && qmd embed`.
#
# Required env:
#   AZURE_STORAGE_ACCOUNT   Storage account name
# Optional env:
#   INDEX_CONTAINER         Container name (default: wiki-index)
#   INDEX_BLOB              Blob name     (default: index.sqlite.gz)
#
# Usage: qmd-sql-upload.sh <path-to-index.sqlite.gz>
set -euo pipefail

INDEX_FILE="${1:?Missing path to index.sqlite.gz — usage: $0 <path>}"
[[ -f "$INDEX_FILE" ]] || { echo "ERROR: $INDEX_FILE does not exist" >&2; exit 1; }

ACCOUNT="${AZURE_STORAGE_ACCOUNT:?AZURE_STORAGE_ACCOUNT must be set}"
CONTAINER="${INDEX_CONTAINER:-wiki-index}"
BLOB="${INDEX_BLOB:-index.sqlite.gz}"

SIZE=$(stat -c%s "$INDEX_FILE" 2>/dev/null || stat -f%z "$INDEX_FILE")
echo "Uploading $INDEX_FILE ($SIZE bytes) → $ACCOUNT/$CONTAINER/$BLOB ..."

az storage blob upload \
    --account-name "$ACCOUNT" \
    --container-name "$CONTAINER" \
    --name "$BLOB" \
    --file "$INDEX_FILE" \
    --auth-mode login \
    --overwrite \
    --no-progress

echo "Upload complete."
