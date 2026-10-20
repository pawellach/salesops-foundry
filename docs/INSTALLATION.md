# Installation Guide — SalesOps Foundry

**Version:** 1.0

---

## Prerequisites

| Tool | Required | Notes |
|---|---|---|
| Git | Yes | Any recent version |
| Claude Code | Yes | For running skills and workflows |
| Python 3.9+ | Recommended | For running validation scripts |

No build step is required to use skills. No CRM or external API credentials are needed for MVP.

---

## Step 1: Clone the repository

```bash
git clone https://github.com/pawellach/salesops-foundry.git
cd salesops-foundry
```

---

## Step 2: Verify the structure

```bash
python scripts/validate_structure.py
```

Expected output: `[PASS] Structure valid.`

If you see errors, check that all required directories and files are present. See `docs/ARCHITECTURE.md` for the expected layout.

---

## Step 3: Run your first skill

Open Claude Code in the repository directory and reference a skill:

```
Use skills/01-find-buyers/icp-builder/SKILL.md to define our ICP.
Our hypothesis: we sell to mid-market logistics companies in Europe, 200-500 employees, who manage more than 10 carriers manually.
```

Claude Code will load the skill and follow its procedure.

---

## Step 4: Customise for your context

1. Copy the relevant template from `templates/` and fill in your account data.
2. Replace the fictional examples in `examples/` with your own (keep them in a local branch — do not commit real data).
3. Update `docs/DECISIONS.md` with any routing or naming choices you make.

---

## Troubleshooting

**"Skill not found" in Claude Code**

Make sure you are referencing the full path from the repository root: `skills/01-find-buyers/icp-builder/SKILL.md`

**validate_structure.py shows missing directories**

Run from the repository root: `python scripts/validate_structure.py`. If directories are missing, re-clone or check your git status.

**validate_frontmatter.py reports missing fields**

Open the flagged skill file and ensure the YAML frontmatter at the top of the file includes: `name`, `description`, `group`, `version`, `status`.

**Python not found**

On Windows, try `python3` instead of `python`, or install Python from python.org. The validation scripts require only the standard library.

---

## Next steps

- Read `docs/OPERATING_GUIDE.md` for how to use skills in practice.
- Browse the skills catalogue at `site/skills-catalog.md`.
- See `examples/` for three end-to-end scenario walkthroughs.
