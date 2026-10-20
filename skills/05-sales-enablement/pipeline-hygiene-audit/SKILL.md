---
name: Pipeline Hygiene Audit
description: Identify missing, stale, inconsistent, or unsupported fields across a supplied pipeline snapshot
group: "05 — Sales Enablement and Management"
version: "1.0"
status: implemented
---


# Pipeline Hygiene Audit

## Purpose

Review a supplied pipeline snapshot (CSV, JSON, or Markdown table) and flag every opportunity with missing required fields, stale activity, inconsistent stage/close-date combinations, or unsupported forecast amounts.

## When NOT to use

- When you want a full deal-by-deal review (use Deal Review Facilitator instead)
- When you want a forecast challenge (use Forecast Challenge instead)
- When pipeline data is not supplied (this skill cannot query a CRM directly)

## Required inputs

- `pipeline_data`: pipeline snapshot as CSV, JSON, or Markdown table. Required columns: `opportunity_name`, `stage`, `amount`, `close_date`, `last_activity_date`
- `today_date`: current date (ISO 8601)

## Optional inputs

- `stale_threshold_days`: number of days without activity before flagging as stale (default: 14)
- `required_fields`: additional fields to check for completeness (e.g., `champion`, `next_step`)
- `stage_close_date_rules`: expected minimum days to close per stage (e.g., `negotiation: 7`)

## Step-by-step procedure

1. Parse the `pipeline_data` into a list of opportunities.
2. For each opportunity, check:
   a. **Completeness**: are all required fields present and non-empty?
   b. **Staleness**: is `last_activity_date` more than `stale_threshold_days` before `today_date`?
   c. **Close-date consistency**: is the `close_date` in the past, or implausibly soon given the `stage`?
   d. **Amount plausibility**: is the amount zero, negative, or blank?
3. Assign each finding a severity: `Critical` (missing close date or amount), `High` (stale >30 days, past close date), `Medium` (stale 15–30 days, missing optional required fields), `Low` (minor inconsistencies).
4. Produce a summary table of all findings.
5. Produce a repair checklist: one action per finding for the rep to take.

## Output contract

```
PIPELINE HYGIENE AUDIT — 2026-10-20
Opportunities reviewed: 8
Issues found: 5

FINDINGS:
| Opportunity | Issue | Severity |
|---|---|---|
| Northlight Technologies | No activity in 22 days | High |
| Meridian Logistics | Close date 2026-09-30 is in the past | Critical |
| Acme Corp | Amount is $0 | Critical |
| DataBridge Ltd | No next_step recorded | Medium |
| FutureFin Inc | Stage=Closing but close date 90 days out | Medium |

REPAIR CHECKLIST:
- Meridian Logistics: update close date or move to Closed-Lost
- Acme Corp: confirm and enter deal amount
- Northlight Technologies: log activity or escalate to manager
- DataBridge Ltd: enter next step and owner
- FutureFin Inc: verify close date with economic buyer
```

## Evidence and citation rules

- Every finding must be derived from the supplied data. Do not infer problems not present in the data.
- Dates used in staleness calculations must reference the supplied `today_date`, not an assumed current date.

## Confidence/uncertainty handling

- If the pipeline data is incomplete (missing required columns), flag this at the top and audit only available fields.
- If `today_date` is not supplied, note the assumption: "today_date assumed as [date you are reasoning from]."

## Safety, privacy, and compliance constraints

- Do not write to any CRM. This is a read-only analysis skill.
- Pipeline data is commercially sensitive — treat as confidential.

## Human approval requirements

**This skill produces a report only.** No CRM updates, emails, or external actions are taken. The rep or manager reviews the report and decides what to update.

## Failure modes and fallback behaviour

- Unparseable pipeline format: return an error with the specific parsing problem.
- All fields blank: return an error, do not produce a fabricated audit.
- Stage-close-date rules not supplied: skip that check and note the omission.

## Acceptance criteria

- Every Critical finding is present in the output.
- Repair checklist has exactly one action per finding.
- No invented opportunity data.
- Severity labels consistently applied.

## Evaluation cases

**Case 1 — Clean pipeline**
Input: 5 opportunities, all fields complete, all activity within 10 days, all close dates in the future. Expected: "No issues found" with zero rows in the findings table.

**Case 2 — Messy pipeline**
Input: 6 opportunities including one with a past close date, one with $0 amount, one with no activity in 40 days. Expected: 3 findings at Critical/High severity, repair checklist with 3 specific actions.

## Related skills

- [Deal Review Facilitator](/skills/05-sales-enablement/deal-review-facilitator/SKILL.md)
- [Forecast Challenge](/skills/05-sales-enablement/forecast-challenge/SKILL.md)
- [Weekly Pipeline Report](/skills/05-sales-enablement/weekly-pipeline-report/SKILL.md)
- [Opportunity Risk Review](/skills/03-run-the-pipeline/opportunity-risk-review/SKILL.md)
