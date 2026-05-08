#!/usr/bin/env bash
# One-time setup: point git at the in-repo .githooks/ directory so hooks
# (post-merge → sync-index.sh) live alongside the code and stay in sync
# across `git pull`s.
#
# Usage: bash scripts/install-hooks.sh
set -e

cd "$(dirname "$0")/.."
git config core.hooksPath .githooks
chmod +x .githooks/* scripts/sync-index.sh
echo "Git hooks enabled (.githooks/). 'git pull' on main will now refresh ~/.cache/qmd/index.sqlite."
