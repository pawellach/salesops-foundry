---
name: Data Quality Rules
description: Generate a set of data quality validation rules for sales trackers or CRM fields, detecting missing, conflicting, and implausible values
group: "06 — Revenue Operations"
version: "1.0"
status: implemented
---


# Data Quality Rules

## Purpose

Produce a set of data quality rules that can be applied manually or programmatically to a sales pipeline, account, or signal tracker to detect missing required fields, conflicting values, stale data, and implausible entries.

## When NOT to use

- When you want to audit an existing pipeline (use Pipeline Hygiene Audit instead)
- When you want a tracker schema (use Account Tracker or Pipeline Tracker instead)

## Required inputs

- `data_object`: `pipeline` | `accounts` | `signals` | `contacts` | `custom`
- `tracker_fields`: the fields in the tracker to generate rules for

## Optional inputs

- `stage_field`: the field that drives stage-based validation (default: `stage`)
- `severity_level`: `critical_only` | `all` (default: `all`)

## Step-by-step procedure

1. Parse `tracker_fields` and `data_object`.
2. Generate rules in the following categories:
   - **Completeness**: required fields that must not be empty
   - **Stage-based requirements**: fields required once the record reaches a certain stage
   - **Date logic**: close date must be in the future, last_activity_date must not be blank if stage ≥ qualified
   - **Consistency**: fields that must be consistent (e.g., stage=Negotiation but close_date >180 days out is unusual)
   - **Staleness**: records with no activity beyond a threshold
3. Assign severity to each rule: Critical, High, Medium, Low.
4. Format as a rule table with: rule ID, description, condition, severity, suggested fix.

## Output contract

```
DATA QUALITY RULES — Pipeline Tracker

| Rule ID | Description | Condition | Severity | Suggested Fix |
|---|---|---|---|---|
| DQ-001 | Amount missing | amount IS NULL or amount = 0 | Critical | Enter expected contract value |
| DQ-002 | Close date missing | close_date IS NULL | Critical | Enter expected close date |
| DQ-003 | Close date in the past | close_date < today_date AND stage NOT IN (Closed-Won, Closed-Lost) | Critical | Update close date or move to closed |
| DQ-004 | No activity since creation | last_activity_date IS NULL | High | Log first activity |
| DQ-005 | Stale: no activity >14 days | (today - last_activity_date) > 14 AND stage NOT IN (Closed-*) | High | Log activity or escalate |
| DQ-006 | Champion missing at Evaluation | stage IN (Evaluation, Negotiation) AND champion IS NULL | High | Identify and document champion |
| DQ-007 | Economic buyer missing at Negotiation | stage = Negotiation AND economic_buyer IS NULL | High | Identify economic buyer before proceeding |
| DQ-008 | Next step missing | next_step IS NULL AND stage NOT IN (Closed-*) | Medium | Add specific next step with owner and date |
| DQ-009 | Very distant close date at Negotiation | stage = Negotiation AND close_date > today + 60 days | Medium | Verify close date with prospect |
| DQ-010 | Amount very high (outlier) | amount > [team median] * 5 | Low | Verify amount is correct |
```

## Evidence and citation rules

- Rules are derived from common sales data quality practices, not a specific CRM's validation logic.
- Thresholds (14 days staleness, 60-day negotiation close window) are configurable defaults — adapt to your team's actual cycle.

## Confidence/uncertainty handling

- Note that rule thresholds are starting points. Calibrate against the team's historical win data before enforcing as hard rules.

## Safety, privacy, and compliance constraints

- Do not write data quality rules that expose personal contact data in output logs.

## Human approval requirements

**This skill produces a rule set document.** No validation is run against live data. A manager or RevOps owner reviews and configures the rules before applying them.

## Failure modes and fallback behaviour

- `tracker_fields` is empty: generate a generic rule set for the `data_object` type and note the assumption.

## Acceptance criteria

- Rules cover all 5 categories (completeness, stage-based, date logic, consistency, staleness).
- Every rule has an ID, condition, severity, and suggested fix.
- Thresholds are labelled as configurable defaults.

## Evaluation cases

**Case 1 — Pipeline rules, all severities**
Input: data_object=pipeline, tracker_fields=[amount, close_date, stage, champion, next_step, last_activity_date]. Expected: ≥8 rules covering all 5 categories, severities from Critical to Low.

**Case 2 — Critical only**
Input: data_object=pipeline, severity_level=critical_only. Expected: only Critical-severity rules returned (amount missing, close date missing, past close date).

## Related skills

- [Pipeline Hygiene Audit](/skills/05-sales-enablement/pipeline-hygiene-audit/SKILL.md)
- [Pipeline Tracker](/skills/06-revenue-operations/pipeline-tracker/SKILL.md)
- [Account Tracker](/skills/06-revenue-operations/account-tracker/SKILL.md)
- [Crm Field Mapping Planner](/skills/06-revenue-operations/crm-field-mapping-planner/SKILL.md)
