# Using salesops-foundry with Amazon Q Desktop

## What is salesops-foundry?

salesops-foundry is a library of 72 Claude Code skills for Sales Operations practitioners — covering the full sales cycle from finding buyers through revenue reporting. Skills are structured step-by-step procedures that guide an AI assistant to produce consistent, evidence-based outputs.

Skill categories:
- **01 — Find Buyers**: ICP, account scoring, territory planning
- **02 — Account Intelligence**: signals, briefs, competitor tracking
- **03 — Run the Pipeline**: lead triage, routing, pipeline review
- **04 — Discovery and Deals**: call prep, proposals, mutual action plans
- **05 — Sales Enablement**: objection handling, battlecards, playbooks
- **06 — Revenue Operations**: forecasting, compensation, reporting
- **07 — Quality and Safety**: compliance, data quality, review gates

## Installation in Amazon Q Desktop

1. Generate Q-compatible skill files:
   ```bash
   python scripts/build_q.py
   # Output: dist/q-skills/ (72 files with trigger_phrases added)
   ```

2. In Amazon Q Desktop, open **Settings → Skills** (or equivalent in your version).

3. Add `dist/q-skills/` as a custom skills directory, or copy the individual skill folders you need into your Q skills path.

4. Restart Amazon Q Desktop to load the skills.

## Invoking skills

Each skill registers trigger phrases. Type any phrase that matches, and Q will load the skill's procedure.

| Trigger phrase | Skill |
|---|---|
| `lead triage` / `triage lead` | Lead Triage |
| `account fit scoring` / `score account` | Account Fit Scoring |
| `account brief` / `build account brief` | Account Brief Builder |
| `buyer committee mapper` | Buyer Committee Mapper |
| `first touch draft` | First-Touch Draft |
| `discovery call plan` | Discovery Call Plan |
| `pipeline review` | Pipeline Stage Recommendation |

You can also invoke by skill name directly: `@AccountFitScoring`, etc.

## Example invocations

**Lead Triage:**
```
lead triage

Lead name: Acme Corp
Source: inbound web form
Company size: ~200 employees
Region: EMEA
```

**Account Brief Builder:**
```
account brief

Account: Northlight Technologies
Purpose: Prep for discovery call on 2026-11-05
ICP: B2B SaaS, 100-500 employees, EU
```

**Buyer Committee Mapper:**
```
buyer committee mapper

Account: Northlight Technologies
Known contacts: Sarah (IT Director), Tom (Procurement)
Deal stage: Discovery
```

## Notes

- Skills in `skills/` are the canonical source. Files in `dist/q-skills/` are generated and should not be edited manually — re-run `build_q.py` after any skill updates.
- All skills follow the [salesops-foundry schema](../schemas/) — see `CONTRIBUTING.md` for authoring new skills.
- For Claude Code (CLI) usage, see the main `README.md`.
