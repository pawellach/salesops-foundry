#!/usr/bin/env python3
"""Validate YAML frontmatter in skill and agent Markdown files."""

import sys
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent

SKILL_REQUIRED = {"name", "description", "group", "version", "status"}
AGENT_REQUIRED = {"name", "role", "scope"}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    block = m.group(1)
    result = {}
    for line in block.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            result[key.strip()] = val.strip()
    return result


errors = []
checked = 0

for skill_file in ROOT.glob("skills/**/**/SKILL.md"):
    checked += 1
    text = skill_file.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    rel = skill_file.relative_to(ROOT)
    if fm is None:
        errors.append(f"NO FRONTMATTER: {rel}")
        continue
    missing = SKILL_REQUIRED - set(fm.keys())
    if missing:
        errors.append(f"MISSING FIELDS {sorted(missing)}: {rel}")
    if len(text.splitlines()) < 30:
        errors.append(f"TOO SHORT (<30 lines): {rel}")

for agent_file in ROOT.glob("agents/*.md"):
    if agent_file.name == "README.md":
        continue
    checked += 1
    text = agent_file.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    rel = agent_file.relative_to(ROOT)
    if fm is None:
        errors.append(f"NO FRONTMATTER: {rel}")
        continue
    missing = AGENT_REQUIRED - set(fm.keys())
    if missing:
        errors.append(f"MISSING FIELDS {sorted(missing)}: {rel}")

if checked == 0:
    print("[WARN] No skill or agent files found — repository may be empty.")
    sys.exit(0)

if errors:
    print(f"\n[FAIL] {len(errors)} frontmatter error(s) in {checked} files:\n")
    for e in errors:
        print(f"  {e}")
    sys.exit(1)
else:
    print(f"[PASS] Frontmatter valid in all {checked} files.")
    sys.exit(0)
