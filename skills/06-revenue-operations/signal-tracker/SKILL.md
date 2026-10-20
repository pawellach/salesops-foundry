---
name: Signal Tracker
description: Define and populate a signal tracking schema preserving event, source, timestamp, confidence, and recommended action
group: "06 — Revenue Operations"
version: "1.0"
status: implemented
---


# Signal Tracker

## Purpose

Generate a signal tracking schema that preserves the full provenance of each buying signal — event, source, access date, confidence level, affected account, and recommended action — to support evidence-based prioritisation and auditability.

## When NOT to use

- When you want to analyse signals (use Intent Signal Aggregator, Group 2)
- When you want to act on a signal (use Signal-to-Action Prioritiser, Group 2)
- When you want to find signals (use Buying-Trigger Research, Group 1)

## Required inputs

- `output_format`: `markdown_table` | `csv_schema` | `json_schema`

## Optional inputs

- `signal_types`: list of signal types to include (default: all — hiring, funding, product, job-change, content, competitor)
- `team_context`: who will use this tracker (affects field complexity)

## Step-by-step procedure

1. Define the core signal record fields (see below).
2. Add signal-type-specific fields if needed.
3. Define confidence levels (0–3 scale with explicit definitions).
4. Define recommended action classification (research, engage, alert, hold).
5. Add retention and review rules: when to archive or remove stale signals.
6. Format as requested.

### Core signal fields

| Field | Type | Description |
|---|---|---|
| signal_id | text | Unique identifier (e.g., SIG-001) |
| account_name | text | Target account this signal relates to |
| signal_type | picklist | hiring, funding, product, job-change, content, competitor, other |
| event_description | text | What happened (specific, factual, not interpretive) |
| source | url or text | Where the signal was found |
| source_date | date | When the signal was published or occurred |
| detected_date | date | When the signal was found by the team |
| confidence | 0–3 | 0=unverified, 1=single-source, 2=multi-source, 3=confirmed |
| relevance | picklist | High, Medium, Low, Unknown |
| recommended_action | picklist | research, engage, alert, hold |
| owner | text | Who is responsible for acting on this signal |
| status | picklist | New, In review, Actioned, Archived |
| notes | text | Free text for context |

## Output contract

```
SIGNAL TRACKER SCHEMA — CSV format

signal_id,account_name,signal_type,event_description,source,source_date,detected_date,confidence,relevance,recommended_action,owner,status,notes

EXAMPLE ROW:
SIG-001,Northlight Technologies,hiring,"Posted 5 Senior Logistics Engineer roles on LinkedIn","https://linkedin.com/jobs [access: 2026-10-15]",2026-10-14,2026-10-15,1,High,engage,Alex M.,New,"Potential capacity expansion — align with infrastructure pitch"

CONFIDENCE DEFINITIONS:
0 = Unverified (single mention, no corroboration)
1 = Single-source (one reliable public source)
2 = Multi-source (2+ independent sources confirm)
3 = Confirmed (direct statement from prospect or trusted third party)

RETENTION RULES:
- Archive signals older than 90 days with no action taken
- Re-review High relevance signals every 2 weeks if not actioned
```

## Evidence and citation rules

- Source field must include a URL or publication reference. Vague sources like "saw on LinkedIn" are insufficient.
- `event_description` must be factual, not interpretive. "Posted 5 engineer roles" not "planning to scale infrastructure."

## Confidence/uncertainty handling

- Confidence 0 signals should not trigger outreach without additional research.
- Confidence levels are self-assessed — note this limitation.

## Safety, privacy, and compliance constraints

- Signal trackers may contain company data and limited personal data (job-change signals). Restrict access.
- Do not store personal contact data (personal email, home address) in signal records.
- Use only publicly available or authorised data sources.

## Human approval requirements

**This skill defines a schema only.** No signals are created, no outreach is triggered. A human reviews each High-relevance signal and approves any engagement action.

## Failure modes and fallback behaviour

- Unsupported `output_format`: default to markdown_table.

## Acceptance criteria

- Schema includes all 13 core fields.
- Confidence scale is explicitly defined.
- Retention rules present.
- Example row uses fictional data.

## Evaluation cases

**Case 1 — CSV schema request**
Input: output_format=csv, signal_types=[hiring, funding]. Expected: CSV header with all core fields, example row with fictional data, confidence definitions.

**Case 2 — JSON schema request**
Input: output_format=json_schema. Expected: valid JSON schema with type definitions for all core fields, enum constraints for picklist fields.

## Related skills

- [Intent Signal Aggregator](/skills/02-account-intelligence/intent-signal-aggregator/SKILL.md)
- [Signal To Action Prioritiser](/skills/02-account-intelligence/signal-to-action-prioritiser/SKILL.md)
- [Account Tracker](/skills/06-revenue-operations/account-tracker/SKILL.md)
- [Buying Trigger Research](/skills/01-find-buyers/buying-trigger-research/SKILL.md)
