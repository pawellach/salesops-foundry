#!/usr/bin/env python3
"""Check internal Markdown links in the repository."""

import sys
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
HTTP_RE = re.compile(r"^https?://")

errors = []
checked_files = 0
checked_links = 0

for md_file in ROOT.rglob("*.md"):
    if ".git" in md_file.parts:
        continue
    checked_files += 1
    text = md_file.read_text(encoding="utf-8")
    for match in LINK_RE.finditer(text):
        target = match.group(2)
        # skip external links, anchors-only, and site-absolute links (valid in GitHub Pages)
        if HTTP_RE.match(target) or target.startswith("#") or target.startswith("/"):
            continue
        # strip anchor
        path_part = target.split("#")[0]
        if not path_part:
            continue
        checked_links += 1
        resolved = (md_file.parent / path_part).resolve()
        if not resolved.exists():
            rel_source = md_file.relative_to(ROOT)
            errors.append(f"BROKEN LINK [{match.group(1)}]({target}) in {rel_source}")

if errors:
    print(f"\n[FAIL] {len(errors)} broken internal link(s) across {checked_files} files:\n")
    for e in errors:
        print(f"  {e}")
    sys.exit(1)
else:
    print(f"[PASS] All {checked_links} internal links valid in {checked_files} files.")
    sys.exit(0)
