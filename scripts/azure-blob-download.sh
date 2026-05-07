#!/usr/bin/env bash
# Thin wrapper around scripts/azure-blob-download.py — kept for workflow compatibility.
set -euo pipefail
exec python3 "$(dirname "$0")/azure-blob-download.py" "$@"
