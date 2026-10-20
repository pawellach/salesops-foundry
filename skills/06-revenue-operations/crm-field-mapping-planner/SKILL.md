---
name: CRM Field Mapping Planner
description: Map SalesOps Foundry's CRM-agnostic field concepts to a target CRM's field structure, without writing data
group: "06 — Revenue Operations"
version: "1.0"
status: implemented
---


# CRM Field Mapping Planner

## Purpose

Produce a field mapping plan that maps the team's current field concepts (from account, signal, and pipeline trackers) to a target CRM's field structure. The output is a mapping document for human review — no data is written to any CRM.

## When NOT to use

- When you want a tracker schema (use Account Tracker or Pipeline Tracker instead)
- When you want to write data to a CRM (this skill never writes to external systems)
- When the CRM has not been identified (use a generic mapping to common CRM patterns instead)

## Required inputs

- `target_crm`: `salesforce` | `hubspot` | `pipedrive` | `airtable` | `custom`
- `source_fields`: the team's current field list (from their trackers or described in text)

## Optional inputs

- `custom_objects`: any custom objects the team uses
- `migration_priority`: `accounts` | `contacts` | `opportunities` | `all` (default: `all`)

## Step-by-step procedure

1. Parse `source_fields` into a normalised list.
2. For each source field, identify the most likely corresponding field in the `target_crm`:
   - Use standard CRM field names (e.g., in Salesforce: Account Name = `Name`, Close Date = `CloseDate`)
   - Flag fields that don't have a standard equivalent — these require custom field creation
3. Produce the mapping table.
4. Identify fields that require picklist configuration in the CRM.
5. Note any data type conversions needed (e.g., text → picklist, free-text date → date).
6. List the top 3 migration risks.
7. Recommend the migration sequence (accounts first, then contacts, then opportunities).

## Output contract

```
CRM FIELD MAPPING PLAN — SalesOps Foundry → Salesforce
Migration priority: Opportunities

FIELD MAPPING:
| Source Field | Type | Salesforce Standard Field | Salesforce API Name | Notes |
|---|---|---|---|---|
| account_name | text | Account Name | Name | Standard field |
| amount | number | Amount | Amount | Standard field |
| close_date | date | Close Date | CloseDate | Standard field; ISO 8601 → Salesforce Date |
| stage | picklist | Opportunity Stage | StageName | Must configure picklist values to match stages |
| champion | text | (no standard field) | Champion__c | Custom field required |
| economic_buyer | text | (no standard field) | EconomicBuyer__c | Custom field required |
| next_step | text | Next Step | NextStep | Standard field (limited to 255 chars) |
| probability | number | Probability | Probability | Standard field; verify auto-calc vs. manual |
| icp_fit_score | picklist | (no standard field) | ICPFitScore__c | Custom field required |

PICKLIST FIELDS TO CONFIGURE:
- StageName: Suspect, Qualified, Discovery, Evaluation, Negotiation, Closed-Won, Closed-Lost
- ICPFitScore__c: Strong, Weak, Unknown

DATA TYPE CONVERSIONS:
- close_date: confirm ISO 8601 dates convert correctly during import
- probability: confirm whether Salesforce auto-calculates from Stage or uses manual entry

TOP MIGRATION RISKS:
1. Custom fields must be created before data import — coordinate with Salesforce admin
2. Picklist values must match exactly or import will fail
3. champion and economic_buyer as text fields lose structured data — consider a Lookup or custom object

RECOMMENDED SEQUENCE: Accounts → Contacts → Opportunities

NOTE: This is a planning document. No data has been written to Salesforce.
Validate with a Salesforce admin before executing the migration.
```

## Evidence and citation rules

- Salesforce standard field names are based on publicly documented API names. Verify against your Salesforce instance version.
- Do not guarantee that a mapping will work without a sandbox test.

## Confidence/uncertainty handling

- Flag fields where the mapping is uncertain as "Verify with admin."

## Safety, privacy, and compliance constraints

- This skill does not connect to or write to any CRM. It produces a planning document only.
- Do not include actual customer data in the mapping plan.

## Human approval requirements

**No CRM writes occur.** This skill produces a mapping document for human and admin review. A Salesforce admin (or equivalent) must validate before any import is executed.

## Failure modes and fallback behaviour

- Unknown `target_crm`: use generic CRM field patterns and note the limitation.
- `source_fields` not parseable: ask for a clearer list format.

## Acceptance criteria

- Every source field has a mapping (to a standard field, custom field, or "no equivalent").
- Custom fields are identified with suggested API names.
- Migration risks section has ≥3 risks.
- Explicitly states no data has been written.

## Evaluation cases

**Case 1 — Salesforce mapping**
Input: target_crm=salesforce, source_fields=[account_name, amount, close_date, stage, champion, icp_fit_score]. Expected: standard field matches for name/amount/close_date/stage, custom field recommendations for champion and icp_fit_score, picklist configuration noted.

**Case 2 — Unknown CRM**
Input: target_crm=custom, source_fields=[basic list]. Expected: generic mapping using common CRM field patterns, note about needing CRM-specific validation.

## Related skills

- [Account Tracker](/skills/06-revenue-operations/account-tracker/SKILL.md)
- [Pipeline Tracker](/skills/06-revenue-operations/pipeline-tracker/SKILL.md)
- [Data Quality Rules](/skills/06-revenue-operations/data-quality-rules/SKILL.md)
