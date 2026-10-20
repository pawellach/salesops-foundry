#!/usr/bin/env python3
"""
Fix iteration-1 High findings:
  H-01: Add # Title heading to Groups 5+6 skills missing it
  H-02: This script does NOT attempt auto-fix for H-02 (related-skills link format)
         because safe conversion requires understanding prose context per file.
         H-02 is fixed manually via targeted edits.
  H-03: Standardise frontmatter group field to "0N — Name" format across all 72 skills
  M-02: Standardise section heading "Safety, privacy, and compliance constraints"
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

FRONTMATTER_RE = re.compile(r"^(---\s*\n.*?\n---\s*\n)", re.DOTALL)
NAME_RE = re.compile(r"^name:\s*(.+)$", re.MULTILINE)

# Canonical group names (zero-padded, em dash —)
GROUP_CANONICAL = {
    "01": "01 — Find Buyers and Accounts",
    "02": "02 — Account Intelligence and Signals",
    "03": "03 — Run the Pipeline",
    "04": "04 — Discovery, Demos, and Deal Progression",
    "05": "05 — Sales Enablement and Management",
    "06": "06 — Revenue Operations",
    "07": "07 — Quality, Safety, and Governance",
}

# All known group-field variants → canonical
GROUP_VARIANTS = {
    # Group 01
    "01 - Find Buyers and Accounts": "01 — Find Buyers and Accounts",
    "01 — Find Buyers and Accounts": "01 — Find Buyers and Accounts",
    "1 - Find Buyers and Accounts": "01 — Find Buyers and Accounts",
    "1 — Find Buyers and Accounts": "01 — Find Buyers and Accounts",
    # Group 02
    "02 - Account Intelligence and Signals": "02 — Account Intelligence and Signals",
    "02 — Account Intelligence and Signals": "02 — Account Intelligence and Signals",
    "2 - Account Intelligence and Signals": "02 — Account Intelligence and Signals",
    "2 — Account Intelligence and Signals": "02 — Account Intelligence and Signals",
    # Group 03
    "03 - Run the Pipeline": "03 — Run the Pipeline",
    "03 — Run the Pipeline": "03 — Run the Pipeline",
    "3 - Run the Pipeline": "03 — Run the Pipeline",
    "3 — Run the Pipeline": "03 — Run the Pipeline",
    # Group 04
    "04 - Discovery, Demos, and Deal Progression": "04 — Discovery, Demos, and Deal Progression",
    "04 — Discovery, Demos, and Deal Progression": "04 — Discovery, Demos, and Deal Progression",
    "4 - Discovery, Demos, and Deal Progression": "04 — Discovery, Demos, and Deal Progression",
    "4 — Discovery, Demos, and Deal Progression": "04 — Discovery, Demos, and Deal Progression",
    "04 - Discovery and Deals": "04 — Discovery, Demos, and Deal Progression",
    "04 — Discovery and Deals": "04 — Discovery, Demos, and Deal Progression",
    "4 - Discovery and Deals": "04 — Discovery, Demos, and Deal Progression",
    # Group 05
    "05 - Sales Enablement and Management": "05 — Sales Enablement and Management",
    "05 — Sales Enablement and Management": "05 — Sales Enablement and Management",
    "5 - Sales Enablement and Management": "05 — Sales Enablement and Management",
    "5 — Sales Enablement and Management": "05 — Sales Enablement and Management",
    # Group 06
    "06 - Revenue Operations": "06 — Revenue Operations",
    "06 — Revenue Operations": "06 — Revenue Operations",
    "6 - Revenue Operations": "06 — Revenue Operations",
    "6 — Revenue Operations": "06 — Revenue Operations",
    "06 - Templates, Trackers, and Revenue Operations": "06 — Revenue Operations",
    "6 - Templates, Trackers, and Revenue Operations": "06 — Revenue Operations",
    "6 — Templates, Trackers, and Revenue Operations": "06 — Revenue Operations",
    # Group 07
    "07 - Quality, Safety, and Governance": "07 — Quality, Safety, and Governance",
    "07 — Quality, Safety, and Governance": "07 — Quality, Safety, and Governance",
    "7 - Quality, Safety, and Governance": "07 — Quality, Safety, and Governance",
    "7 — Quality, Safety, and Governance": "07 — Quality, Safety, and Governance",
}

h01_fixed = []
h03_fixed = []
m02_fixed = []
errors = []


def get_group_from_path(skill_file):
    """Derive canonical group from directory path."""
    parts = skill_file.parts
    for p in parts:
        if p.startswith("0") and "-" in p:
            num = p.split("-")[0]
            return GROUP_CANONICAL.get(num)
    return None


for skill_file in ROOT.glob("skills/**/**/SKILL.md"):
    text = skill_file.read_text(encoding="utf-8")
    original = text
    rel = skill_file.relative_to(ROOT)

    # --- H-03: Standardise group field ---
    def fix_group_field(m):
        val = m.group(1).strip().strip('"').strip("'")
        canonical = GROUP_VARIANTS.get(val)
        if canonical and canonical != val:
            return f'group: "{canonical}"'
        # Try path-based fallback
        path_canonical = get_group_from_path(skill_file)
        if path_canonical and val != path_canonical:
            return f'group: "{path_canonical}"'
        return m.group(0)

    text_after_group = re.sub(r'^group:\s*["\']?(.+?)["\']?\s*$', fix_group_field, text, flags=re.MULTILINE)
    if text_after_group != text:
        h03_fixed.append(str(rel))
        text = text_after_group

    # --- H-01: Add # Title heading if missing ---
    fm_match = FRONTMATTER_RE.match(text)
    if fm_match:
        after_fm = text[fm_match.end():]
        first_line = after_fm.lstrip("\n").split("\n")[0] if after_fm.strip() else ""
        if not first_line.startswith("# "):
            name_match = NAME_RE.search(fm_match.group(1))
            if name_match:
                skill_name = name_match.group(1).strip().strip('"').strip("'")
                text = text[:fm_match.end()] + f"\n# {skill_name}\n\n" + after_fm.lstrip("\n")
                h01_fixed.append(str(rel))

    # --- M-02: Standardise section heading ---
    text_after_m02 = re.sub(
        r'^## Safety, privacy, and compliance\s*$',
        '## Safety, privacy, and compliance constraints',
        text,
        flags=re.MULTILINE
    )
    if text_after_m02 != text:
        m02_fixed.append(str(rel))
        text = text_after_m02

    if text != original:
        skill_file.write_text(text, encoding="utf-8")


print(f"\n[H-01] Added # Title heading to {len(h01_fixed)} files:")
for f in h01_fixed[:5]:
    print(f"  {f}")
if len(h01_fixed) > 5:
    print(f"  ... and {len(h01_fixed)-5} more")

print(f"\n[H-03] Standardised group field in {len(h03_fixed)} files:")
for f in h03_fixed[:5]:
    print(f"  {f}")
if len(h03_fixed) > 5:
    print(f"  ... and {len(h03_fixed)-5} more")

print(f"\n[M-02] Fixed section heading in {len(m02_fixed)} files")

print(f"\nH-02 note: Related-skills link conversion requires manual verification.")
print("The most important cross-reference paths are validated by check_links.py after H-02 fix.")

if errors:
    print(f"\nErrors: {errors}")
    sys.exit(1)
else:
    print(f"\n[DONE] No errors.")
