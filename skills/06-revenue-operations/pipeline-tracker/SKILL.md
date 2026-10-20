---
name: Pipeline Tracker
description: Define a consistent, CRM-agnostic opportunity tracking schema with stage definitions, required fields, and update rules
group: "06 — Revenue Operations"
version: "1.0"
status: implemented
---


# Pipeline Tracker

## Purpose

Generate a pipeline tracker schema — Markdown, CSV, or JSON — with opportunity fields, explicit stage definitions, required-field rules per stage, and update discipline guidelines. Designed to be CRM-agnostic for teams not yet on a CRM.

## When NOT to use

- When reviewing pipeline health (use Pipeline Hygiene Audit)
- When generating a pipeline report (use Weekly Pipeline Report)
- When tracking accounts rather than opportunities (use Account Tracker)

## Required inputs

- `output_format`: `markdown_table` | `csv_schema` | `json_schema`

## Optional inputs

- `qualification_framework`: `MEDDICC` | `SPICED` | `BANT` | `none` (default: MEDDICC)
- `team_context`: company stage (e.g., "10-person startup, no CRM")

## Step-by-step procedure

1. Define the opportunity fields (see below).
2. Define pipeline stages with clear entry criteria for each.
3. Define which fields are required at each stage.
4. Specify update rules: how often and who updates what.
5. Format as requested.

### Core opportunity fields

| Field | Type | Notes |
|---|---|---|
| opp_id | text | Unique ID (e.g., OPP-001) |
| account_name | text | |
| contact_name | text | Primary contact |
| contact_role | text | Job title |
| stage | picklist | See stage definitions |
| amount | number | Expected contract value |
| close_date | date | Expected close date |
| probability | number | 0–100% (rep estimate or stage-default) |
| champion | text | Name and role of internal champion |
| economic_buyer | text | Name and role of decision-maker |
| next_step | text | Specific action with owner and date |
| last_activity_date | date | |
| owner | text | Rep responsible |
| created_date | date | |
| notes | text | |

### Stage definitions (MEDDICC-aligned)

| Stage | Entry criteria |
|---|---|
| Suspect | Identified as a potential fit; no contact yet |
| Qualified | Pain confirmed; budget range known; decision process understood |
| Discovery | Discovery call completed; needs documented |
| Evaluation | Proposal or demo delivered; evaluating against criteria |
| Negotiation | Commercial terms being discussed |
| Closed-Won | Contract signed |
| Closed-Lost | Prospect chose another option or did not proceed |

## Output contract

```
PIPELINE TRACKER — CSV Schema

FIELDS: opp_id, account_name, contact_name, contact_role, stage, amount, close_date, probability, champion, economic_buyer, next_step, last_activity_date, owner, created_date, notes

STAGE REQUIRED FIELDS:
- Qualified and above: amount, close_date, next_step required
- Evaluation and above: champion, economic_buyer required
- Negotiation: all fields required

UPDATE RULES:
- next_step: update after every interaction
- stage: update when entry criteria for next stage are met (not aspirationally)
- close_date: must reflect current best estimate; flag if more than 30 days past original

EXAMPLE ROW (fictional):
OPP-001,Northlight Technologies,Sarah Chen,VP Operations,Evaluation,$85000,2026-11-30,40,Sarah Chen (VP Ops),Marcus Wren (CFO),"Send technical assessment by 2026-10-22 (Alex M.)",2026-10-15,Alex M.,2026-09-01,""
```

## Evidence and citation rules

- Stage definitions are general best-practice guidelines. Teams should adapt entry criteria to their actual sales motion.

## Confidence/uncertainty handling

- Probability values are rep estimates unless otherwise configured. Label as estimates.

## Safety, privacy, and compliance constraints

- Pipeline data is commercially sensitive. Access restricted to sales team and leadership.
- Do not share the pipeline tracker externally.

## Human approval requirements

**This skill produces a schema definition only.** No data is written. The team reviews and adopts the schema; a manager approves before use.

## Failure modes and fallback behaviour

- Unknown `qualification_framework`: default to MEDDICC.

## Acceptance criteria

- All 15 core fields defined with type.
- Stage definitions have explicit entry criteria.
- Required-field rules vary by stage.
- Example row uses fictional data.

## Evaluation cases

**Case 1 — CSV with MEDDICC**
Input: output_format=csv, qualification_framework=MEDDICC. Expected: all fields with MEDDICC-aligned stage required fields, example row.

**Case 2 — JSON schema**
Input: output_format=json_schema. Expected: valid JSON schema with enum for stage, number type for amount and probability, date format for date fields.

## Related skills

- [Pipeline Hygiene Audit](/skills/05-sales-enablement/pipeline-hygiene-audit/SKILL.md)
- [Weekly Pipeline Report](/skills/05-sales-enablement/weekly-pipeline-report/SKILL.md)
- [Account Tracker](/skills/06-revenue-operations/account-tracker/SKILL.md)
- [Crm Field Mapping Planner](/skills/06-revenue-operations/crm-field-mapping-planner/SKILL.md)
