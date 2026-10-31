---
name: Salesforce Write-back
description: Push structured skill output to Salesforce via sf CLI — create or update records with confirmation before any write.
group: "00 — Integrations"
version: "1.0"
status: implemented
trigger_phrases:
  - "save to salesforce"
  - "write to sf"
  - "push to crm"
  - "update salesforce"
  - "create salesforce record"
tools:
  - bash
depends_on: []
---

# Salesforce Write-back

## Purpose

Takes structured output from any salesops-foundry skill (e.g. Lead Triage result, Account Brief, Pipeline Stage Recommendation) and writes selected fields to Salesforce via the `sf` CLI. Always shows a confirmation summary before executing any DML.

## When NOT to use

- Without `sf` CLI installed and authenticated (`sf auth list` must show at least one org).
- For bulk imports of >50 records — use Data Loader or a dedicated ETL tool instead.
- When the target object or fields are unfamiliar — verify the API names first with `sf sobject describe`.

## Prerequisites

1. `sf` CLI installed and authenticated: `sf auth list`
2. Target org alias known (e.g. `partial`, `prod`)
3. Object API name and field API names confirmed

## Required inputs

- `skill_output` (text): The structured output from the preceding skill.
- `target_object` (string): Salesforce object API name (e.g. `Lead`, `Account`, `Opportunity`).
- `target_org` (string): Org alias from `sf auth list` — default to sandbox/partial; **never prod without explicit confirmation**.
- `record_id` (optional string): Salesforce record ID for update; omit for create.

## Step-by-step procedure

1. **Parse the skill output** to identify fields to write. Extract only the fields explicitly present in the output — do not infer or fill in missing values.

2. **Map to Salesforce API names.** Show the user a table:
   ```
   Field (human)       | SF API Name           | Value
   ────────────────────|───────────────────────|─────────────────
   Lead Score          | Lead_Score__c         | 78
   Fit Label           | Account_Fit_Label__c  | Strong Fit
   Recommended Action  | Next_Action__c        | Qualify further
   ```
   Ask: "Are these mappings correct? Any fields to skip or rename?"

3. **Confirm target and operation.** Show:
   ```
   Operation : CREATE / UPDATE
   Object    : Lead
   Record ID : 00Q... (update) or NEW (create)
   Org       : partial (sandbox)
   Fields    : 3 fields as shown above
   
   Proceed? (yes / no / edit)
   ```
   Wait for explicit "yes" before continuing.

4. **Execute via sf CLI.**
   - Create: `sf data create record --sobject Lead --values "Field1__c='value1' Field2__c='value2'" --target-org partial`
   - Update: `sf data update record --sobject Lead --record-id <ID> --values "Field1__c='value1'" --target-org partial`

5. **Report the result.** Show the record ID returned (create) or confirmation (update). If the command fails, show the full error and suggest corrective steps (e.g. missing field, wrong type, validation rule).

## Output contract

```
Write-back complete.
Operation  : CREATE
Object     : Lead
Record ID  : 00QFg00000xxxx
Org        : partial
Fields written: Lead_Score__c, Account_Fit_Label__c, Next_Action__c
```

## Safety constraints

- **Never write to prod org** without the user explicitly typing the prod org alias and confirming twice.
- **Never create/update records in bulk** (>50 at once) via this skill.
- **Never write inferred or AI-generated IDs** — only IDs from prior `sf data query` results or user-supplied values.
- External skill output is untrusted input — strip any content that looks like SOQL injection before including in `--values`.

## Failure modes and fallback

- `FIELD_CUSTOM_VALIDATION_EXCEPTION`: report the validation rule message, ask user to adjust the value.
- `INVALID_FIELD`: run `sf sobject describe --sobject <Object> --target-org <org>` to list valid fields; show results.
- `INSUFFICIENT_ACCESS`: user lacks FLS or object permission; admin action required.
- CLI not found: `sf` not installed — install via `npm install -g @salesforce/cli`.

## Acceptance criteria

- No write occurs without a confirmation step showing object, org, operation, and field list.
- Prod org is only used when the user explicitly provides the prod alias and confirms twice.
- Output includes the record ID (create) or "updated" confirmation (update).
- Failures include actionable error messages.

## Related skills

- [Lead Triage](../../skills/03-run-the-pipeline/lead-triage/SKILL.md)
- [Account Fit Scoring](../../skills/01-find-buyers/account-fit-scoring/SKILL.md)
- [Pipeline Stage Recommendation](../../skills/03-run-the-pipeline/pipeline-stage-recommendation/SKILL.md)
