#!/usr/bin/env python3
"""Build GitHub Pages site from site/ Markdown files into _site/."""

import shutil
from pathlib import Path

ROOT = Path(__file__).parent.parent
SITE_SRC = ROOT / "site"
SITE_OUT = ROOT / "_site"

if SITE_OUT.exists():
    shutil.rmtree(SITE_OUT)
SITE_OUT.mkdir()

# Copy all Markdown and config files from site/ to _site/
for f in SITE_SRC.rglob("*"):
    if f.is_file():
        dest = SITE_OUT / f.relative_to(SITE_SRC)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, dest)

# Copy root docs for site reference
for name in ["README.md", "CHANGELOG.md", "CONTRIBUTING.md", "SECURITY.md"]:
    src = ROOT / name
    if src.exists():
        shutil.copy2(src, SITE_OUT / name)

print(f"[OK] Built site: {len(list(SITE_OUT.rglob('*')))} files in {SITE_OUT}")
