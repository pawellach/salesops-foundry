#!/usr/bin/env python3
"""Validate the SalesOps Foundry repository directory structure."""

import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

REQUIRED_DIRS = [
    "agents",
    "skills",
    "workflows",
    "playbooks",
    "prompt-libraries",
    "templates",
    "schemas",
    "examples",
    "evaluations",
    "evaluations/results",
    "evaluations/test-cases",
    "integrations",
    "scripts",
    "docs",
    "site",
    ".github/workflows",
    ".github/ISSUE_TEMPLATE",
]

REQUIRED_ROOT_FILES = [
    "README.md",
    "CLAUDE.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    ".gitignore",
    ".editorconfig",
]

REQUIRED_DOC_FILES = [
    "docs/PROJECT_CHARTER.md",
    "docs/REQUIREMENTS.md",
    "docs/ARCHITECTURE.md",
    "docs/DELIVERY_PLAN.md",
    "docs/DECISIONS.md",
    "docs/RISK_REGISTER.md",
    "docs/ACCEPTANCE_CRITERIA.md",
]

REQUIRED_SKILL_GROUPS = [
    "skills/01-find-buyers",
    "skills/02-account-intelligence",
    "skills/03-run-the-pipeline",
    "skills/04-discovery-and-deals",
    "skills/05-sales-enablement",
    "skills/06-revenue-operations",
    "skills/07-quality-and-safety",
]

errors = []
warnings = []


def check(path, kind="dir"):
    full = ROOT / path
    if kind == "dir":
        if not full.is_dir():
            errors.append(f"MISSING DIR:  {path}")
    else:
        if not full.is_file():
            errors.append(f"MISSING FILE: {path}")


for d in REQUIRED_DIRS:
    check(d, "dir")

for f in REQUIRED_ROOT_FILES:
    check(f, "file")

for f in REQUIRED_DOC_FILES:
    check(f, "file")

for g in REQUIRED_SKILL_GROUPS:
    check(g, "dir")
    group_dir = ROOT / g
    if group_dir.is_dir():
        skill_dirs = [x for x in group_dir.iterdir() if x.is_dir()]
        if not skill_dirs:
            warnings.append(f"EMPTY GROUP:  {g} (no skill subdirectories)")
        for sd in skill_dirs:
            skill_file = sd / "SKILL.md"
            if not skill_file.is_file():
                errors.append(f"MISSING SKILL.md: {sd.relative_to(ROOT)}")

if errors:
    print(f"\n[FAIL] {len(errors)} structure error(s):\n")
    for e in errors:
        print(f"  {e}")
    if warnings:
        print(f"\n[WARN] {len(warnings)} warning(s):\n")
        for w in warnings:
            print(f"  {w}")
    sys.exit(1)
else:
    if warnings:
        print(f"[PASS] Structure valid. {len(warnings)} warning(s):")
        for w in warnings:
            print(f"  {w}")
    else:
        print("[PASS] Structure valid.")
    sys.exit(0)
