#!/usr/bin/env python3
"""
Fix H-02: Convert Related Skills text/backtick references to relative Markdown links.

Handles two patterns found in Groups 3–7:
  Pattern A (Group 3–4): **Skill Name** (Group N, Skill NN) — description
  Pattern B (Group 5–7): `skill-slug` (Group N)

Builds a slug→path index from all SKILL.md files, then replaces the references.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

# --- Build slug-to-path and name-to-path indexes ---
slug_to_path = {}   # "icp-builder" -> "skills/01-find-buyers/icp-builder"
name_to_path = {}   # "ICP Builder" -> "skills/01-find-buyers/icp-builder"
name_re = re.compile(r"^name:\s*[\"']?(.+?)[\"']?\s*$", re.MULTILINE)

for skill_file in ROOT.glob("skills/**/**/SKILL.md"):
    skill_dir = skill_file.parent
    slug = skill_dir.name
    rel_dir = str(skill_dir.relative_to(ROOT)).replace("\\", "/")
    slug_to_path[slug] = rel_dir

    fm_text = skill_file.read_text(encoding="utf-8")[:500]
    m = name_re.search(fm_text)
    if m:
        name = m.group(1).strip()
        name_to_path[name.lower()] = rel_dir
        # Also index common name variations
        name_to_path[name.lower().replace(" / ", " ")] = rel_dir
        name_to_path[name.lower().replace(",", "")] = rel_dir

# Pattern A: **Skill Name** (Group N, Skill NN) — description
PATTERN_A = re.compile(r"\*\*([^*]+)\*\*\s*\(Group\s*\d+[,\s]+Skill\s*\d+\)\s*(?:—\s*(.+))?")
# Pattern B: `skill-slug` (Group N)
PATTERN_B = re.compile(r"`([a-z0-9-]+)`\s*\(Group\s*\d+[^)]*\)")


def make_link(current_file, target_rel_dir, display_name, description=None):
    """Create a relative Markdown link from current_file to target_rel_dir/SKILL.md."""
    current_dir = current_file.parent
    target_path = ROOT / target_rel_dir / "SKILL.md"
    try:
        rel = target_path.relative_to(current_dir)
        link = str(rel).replace("\\", "/")
    except ValueError:
        # Not relative — use repo-root relative path
        link = f"/{target_rel_dir}/SKILL.md"
    if description:
        return f"[{display_name}]({link}) — {description}"
    return f"[{display_name}]({link})"


fixed_files = []
unresolved = []

for skill_file in ROOT.glob("skills/**/**/SKILL.md"):
    text = skill_file.read_text(encoding="utf-8")
    original = text
    rel = skill_file.relative_to(ROOT)

    # Find "Related skills" section
    related_section_re = re.compile(r"(## Related skills\s*\n)(.*?)(?=\n##|\Z)", re.DOTALL)
    match = related_section_re.search(text)
    if not match:
        continue

    section_header = match.group(1)
    section_body = match.group(2)
    original_body = section_body

    # Fix Pattern A: **Bold Name**
    def replace_pattern_a(m):
        skill_name = m.group(1).strip()
        desc = m.group(2).strip() if m.group(2) else None
        target = name_to_path.get(skill_name.lower())
        if target:
            return make_link(skill_file, target, skill_name, desc)
        # Try partial match
        for known_name, path in name_to_path.items():
            if skill_name.lower() in known_name or known_name in skill_name.lower():
                return make_link(skill_file, path, skill_name, desc)
        unresolved.append(f"{rel}: could not resolve '{skill_name}'")
        return m.group(0)  # leave unchanged

    section_body = PATTERN_A.sub(replace_pattern_a, section_body)

    # Fix Pattern B: `skill-slug`
    def replace_pattern_b(m):
        slug = m.group(1).strip()
        target = slug_to_path.get(slug)
        if target:
            display = " ".join(w.capitalize() for w in slug.split("-"))
            return make_link(skill_file, target, display)
        unresolved.append(f"{rel}: could not resolve slug '{slug}'")
        return m.group(0)

    section_body = PATTERN_B.sub(replace_pattern_b, section_body)

    if section_body != original_body:
        text = text[:match.start()] + section_header + section_body + text[match.end():]

    if text != original:
        skill_file.write_text(text, encoding="utf-8")
        fixed_files.append(str(rel))

print(f"\n[H-02] Converted Related Skills links in {len(fixed_files)} files.")
if unresolved:
    print(f"\nUnresolved references ({len(unresolved)}):")
    for u in unresolved[:10]:
        print(f"  {u}")
    if len(unresolved) > 10:
        print(f"  ... and {len(unresolved)-10} more")
else:
    print("  All references resolved.")

sys.exit(0)
