---
layout: page
title: Getting Started
---

# Getting Started

## Prerequisites

- **Git** — any recent version
- **Claude Code** — [claude.ai/code](https://claude.ai/code)
- **Python 3.9+** — for running validation scripts (optional but recommended)

No external API keys or CRM access needed for MVP.

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/pawellach/salesops-foundry.git
cd salesops-foundry
```

### 2. Verify the structure

```bash
python scripts/validate_structure.py
```

Expected: `[PASS] Structure valid.`

### 3. Run your first skill

Open Claude Code in the repository directory:

```
Use skills/01-find-buyers/icp-builder/SKILL.md.
My hypothesis: we sell to mid-market logistics companies in Europe,
200-500 employees, managing more than 10 carriers manually.
```

---

## Your first workflow: Account to Meeting

This walkthrough uses fictional data to show the full workflow.

**Step 1: Build the ICP**
```
Use skills/01-find-buyers/icp-builder/SKILL.md with my hypothesis: [your hypothesis]
```

**Step 2: Score a target account**
```
Use skills/01-find-buyers/account-fit-scoring/SKILL.md.
Account: [paste company info and any signals you have]
ICP: [paste ICP output from Step 1]
```

**Step 3: Build the account brief**
```
Use skills/02-account-intelligence/account-brief-builder/SKILL.md.
Input: [paste account data and fit score]
```

**Step 4: Draft outreach (for approval)**
```
Use skills/03-run-the-pipeline/first-touch-draft/SKILL.md.
Account brief: [paste from Step 3]
```
The skill will produce a **DRAFT** requiring your approval before any message is sent.

---

## Troubleshooting

**Skill not loading:** Reference the full path — `skills/01-find-buyers/icp-builder/SKILL.md`

**validate_structure.py errors:** Run from the repository root directory, not a subdirectory.

**Python not found:** Try `python3` instead of `python` on macOS/Linux.

**"I need more input":** The skill is correctly asking for information it needs. Follow the Required inputs section in the skill file.
