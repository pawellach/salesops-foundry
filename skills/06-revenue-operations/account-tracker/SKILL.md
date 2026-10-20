---
name: Account Tracker
description: Define a CRM-agnostic account tracking structure with field definitions, update rules, and ownership
group: "06 — Revenue Operations"
version: "1.0"
status: implemented
---


# Account Tracker

## Purpose

Generate a configured account tracker template — as a Markdown table, CSV schema, or JSON schema — with field definitions, data types, update rules, and ownership assignments. Designed to work without a CRM for teams that need a lightweight starting point.

## When NOT to use

- When a full CRM migration is needed (use CRM Field Mapping Planner instead)
- When tracking deal-level data (use Pipeline Tracker instead)
- When researching a specific account (use Account Brief Builder instead)

## Required inputs

- `tracking_purpose`: what this tracker is for (e.g., "SDR prospecting", "AE active accounts", "strategic accounts")
- `team_size`: number of people who will use the tracker (affects complexity)

## Optional inputs

- `output_format`: `markdown_table` | `csv_schema` | `json_schema` (default: `markdown_table`)
- `required_fields`: fields the team has specifically requested
- `crm_context`: CRM the team plans to migrate to eventually (to align field names)

## Step-by-step procedure

1. Based on `tracking_purpose`, select appropriate field sets:
   - Core: account_name, industry, size, website, owner, status, last_updated
   - Prospecting: icp_fit_score, trigger, first_contact_date, outreach_status
   - Active deals: stage, amount, close_date, next_step, champion, economic_buyer
   - Strategic: health_score, renewal_date, exec_sponsor, risk_flag
2. Define each field: name, data type, allowed values (if picklist), update frequency, owner.
3. Add update rules: who updates what, when, and what triggers an update.
4. Add ownership rules: who is the primary account owner, and who can edit.
5. Format the output as requested.

## Output contract

```
ACCOUNT TRACKER SCHEMA — SDR Prospecting | 3-person team

FIELDS:
| Field | Type | Allowed Values | Update Frequency | Owner |
|---|---|---|---|---|
| account_name | text | — | On creation | Rep |
| industry | picklist | SaaS, Logistics, Manufacturing, Other | On creation | Rep |
| employee_count | number | — | On creation | Rep |
| website | url | — | On creation | Rep |
| icp_fit_score | picklist | Strong, Weak, Unknown | After research | Rep |
| trigger | text | — | When signal found | Rep |
| owner | text | — | On assignment | Manager |
| outreach_status | picklist | Not started, Contacted, Engaged, No response, Disqualified | After each touch | Rep |
| last_activity_date | date | ISO 8601 | After each activity | Rep |
| next_step | text | — | After each interaction | Rep |
| notes | text | — | As needed | Rep |

UPDATE RULES:
- outreach_status: update within 24 hours of any touch
- icp_fit_score: required before first outreach
- next_step: must be filled if status is Engaged

OWNERSHIP:
- Primary owner: assigned rep
- Manager can view and edit all fields
- No sharing outside the team without manager approval

NOTE: This is a starting template. Adapt field names to match your eventual CRM before migration.
```

## Evidence and citation rules

- Field recommendations are based on common sales tracking practices, not specific CRM documentation.

## Confidence/uncertainty handling

- If `tracking_purpose` is vague: default to a general-purpose tracker and note the assumption.

## Safety, privacy, and compliance constraints

- Account trackers may contain company and contact data. Restrict access to the team.
- Do not store personal contact data (personal email, phone) in a tracker not governed by a privacy policy.

## Human approval requirements

**This skill produces a schema definition only.** No data is created or written. The team reviews and adopts the tracker; a manager approves the field set before use.

## Failure modes and fallback behaviour

- Unsupported `output_format`: default to `markdown_table` and note the fallback.

## Acceptance criteria

- Every field has a type, update frequency, and owner.
- Update rules cover at minimum status and next step.
- Output format matches the requested format.

## Evaluation cases

**Case 1 — SDR tracker, markdown**
Input: tracking_purpose="SDR prospecting", team_size=3, output_format=markdown_table. Expected: 8–12 fields covering prospecting needs, update rules for status fields, ownership clearly defined.

**Case 2 — Strategic account tracker, JSON schema**
Input: tracking_purpose="strategic accounts", team_size=5, output_format=json_schema. Expected: JSON schema with health_score, renewal_date, exec_sponsor fields added; appropriate types and required flags.

## Related skills

- [Pipeline Tracker](/skills/06-revenue-operations/pipeline-tracker/SKILL.md)
- [Signal Tracker](/skills/06-revenue-operations/signal-tracker/SKILL.md)
- [Crm Field Mapping Planner](/skills/06-revenue-operations/crm-field-mapping-planner/SKILL.md)
- [Account Brief Builder](/skills/02-account-intelligence/account-brief-builder/SKILL.md)
