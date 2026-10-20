---
name: Weekly Pipeline Report
description: Summarise pipeline changes, risks, next steps, and assumptions from a supplied pipeline snapshot
group: "05 — Sales Enablement and Management"
version: "1.0"
status: implemented
---


# Weekly Pipeline Report

## Purpose

Generate a structured weekly pipeline report for a sales manager or revenue leader, based on two pipeline snapshots (this week and last week) or a single snapshot with change annotations.

## When NOT to use

- When you want a deal-by-deal health review (use Deal Review Facilitator instead)
- When you want a forecast challenge (use Forecast Challenge instead)
- When no pipeline data is supplied

## Required inputs

- `current_pipeline`: this week's pipeline snapshot (CSV, JSON, or Markdown)
- `today_date`: current date (ISO 8601)

## Optional inputs

- `previous_pipeline`: last week's snapshot for comparison
- `team_target`: the team's monthly or quarterly revenue target
- `reporting_period`: week label (e.g., "Week of 2026-10-20")

## Step-by-step procedure

1. Parse `current_pipeline`. If `previous_pipeline` is supplied, diff the two snapshots.
2. Calculate: total pipeline value, weighted pipeline (amount × close probability if available), number of open opportunities.
3. Identify changes since last week (new opportunities added, deals progressed, deals lost/removed, amounts changed).
4. Identify top 3 risks: largest deals with no recent activity, deals with past close dates, deals with missing qualification data.
5. List the 3–5 most important next steps across the pipeline (not invented — derived from next_step fields or stage logic).
6. Flag assumptions: any field used in calculations that was blank or estimated.
7. Structure the output using the template below. Do not fabricate deal outcomes.

## Output contract

```
WEEKLY PIPELINE REPORT — Week of 2026-10-20
Prepared by: SalesOps Foundry (draft — review before sharing)

SUMMARY
Open opportunities: 12
Total pipeline value: $1,240,000
Weighted pipeline: $496,000 (40% avg. probability)
Target attainment (Q4): 62% of $800K target closed so far [ASSUMPTION: target supplied by user]

CHANGES THIS WEEK
+ Added: Northlight Technologies ($85K) — new inbound
+ Progressed: Meridian Logistics — moved from Evaluation to Negotiation
- Lost: DataBridge Ltd ($40K) — moved to Closed-Lost

TOP RISKS
1. Acme Corp ($120K) — no activity in 28 days; close date next week
2. FutureFin Inc ($95K) — Economic Buyer not identified; in Negotiation stage
3. Westpark Media ($60K) — close date passed; not updated

NEXT STEPS (from pipeline data)
1. Acme Corp — re-engage VP Operations (rep: J. Smith)
2. Northlight Technologies — send technical assessment (due 2026-10-22)
3. Meridian Logistics — draft contract for legal review

ASSUMPTIONS
- Probabilities not in data; used stage-based defaults (Discovery=20%, Evaluation=40%, Negotiation=70%)
- Target figure supplied by user; not verified against CRM
```

## Evidence and citation rules

- All figures must come from the supplied pipeline data or be labelled as assumptions.
- Do not invent deal outcomes, contacts, or probabilities.

## Confidence/uncertainty handling

- Weighted pipeline is only meaningful if probability data is reliable. Note if probabilities are estimated.
- If `previous_pipeline` is not supplied, omit the "Changes this week" section and note the absence.

## Safety, privacy, and compliance constraints

- Pipeline reports are commercially sensitive. Treat as confidential.
- Do not send the report — output is a draft for human review and distribution.

## Human approval requirements

**This skill produces a draft report.** It must be reviewed and approved by the manager before distribution. The report is marked "draft — review before sharing" in all outputs.

## Failure modes and fallback behaviour

- Unparseable pipeline: return an error with the specific problem.
- No `today_date` supplied: note assumption and use reasoning-time date.
- Both pipeline snapshots empty: return an error.

## Acceptance criteria

- Summary section includes opportunity count, total value, and weighted value.
- Top risks section has ≥1 risk with specific opportunity name.
- Assumptions section is present and non-empty if any estimates were made.
- Output is labelled as draft.

## Evaluation cases

**Case 1 — No previous pipeline**
Input: current pipeline with 8 opportunities, no previous pipeline, no probabilities. Expected: report with "Changes this week" section omitted and noted; stage-based probability estimates listed in assumptions.

**Case 2 — Pipeline with changes**
Input: current and previous pipeline with 2 new deals, 1 progressed, 1 closed-lost. Expected: changes section listing all 4 events; risks derived from actual data; no fabricated next steps.

## Related skills

- [Pipeline Hygiene Audit](/skills/05-sales-enablement/pipeline-hygiene-audit/SKILL.md)
- [Forecast Challenge](/skills/05-sales-enablement/forecast-challenge/SKILL.md)
- [Pipeline Tracker](/skills/06-revenue-operations/pipeline-tracker/SKILL.md)
- [Deal Review Facilitator](/skills/05-sales-enablement/deal-review-facilitator/SKILL.md)
