#!/usr/bin/env python3
"""convert-docx-to-md — convert .docx files to Markdown via pandoc.

Mirrors the convert-vtt-to-md.py / convert-eml-to-md.py CLI shape so it slots
into Phase 0 the same way. Requires pandoc on PATH (pre-installed on GitHub
ubuntu-latest; `brew install pandoc` on macOS).
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser(description="Convert .docx files to Markdown via pandoc.")
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--force", action="store_true", help="Reconvert even if .md already exists")
    args = ap.parse_args()

    if not shutil.which("pandoc"):
        print("  [ERROR] pandoc not on PATH — install via `brew install pandoc` (macOS) or `apt install pandoc` (Linux)", file=sys.stderr)
        return 1

    in_dir = Path(args.input_dir)
    if not in_dir.is_dir():
        print(f"  [INFO] {in_dir} not a directory, skipping silently")
        return 0

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    errors = 0
    for docx in sorted(in_dir.glob("*.docx")):
        md = out_dir / f"{docx.stem}.md"
        if md.exists() and not args.force:
            print(f"  [INFO] {md.name} exists, skipping (use --force to reconvert)")
            continue
        try:
            subprocess.run(
                ["pandoc", str(docx), "-t", "gfm", "--wrap=none", "-o", str(md)],
                check=True,
            )
            print(f"  [OK] wrote {md}")
        except subprocess.CalledProcessError as e:
            print(f"  [ERROR] {docx.name}: pandoc failed ({e})", file=sys.stderr)
            errors += 1
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
