---
name: Pipeline Stage Recommendation
description: Suggest the correct pipeline stage for an opportunity based on evidence and defined entry/exit criteria — not on optimism.
group: "03 — Run the Pipeline"
version: "1.0"
status: implemented
---

# Pipeline Stage Recommendation

## Purpose
Evaluate the available evidence for an opportunity and recommend the pipeline stage it should occupy, based on the team's defined stage criteria. Flag when the current stage is unsupported by evidence.

## When NOT to use
- When no stage definitions have been supplied (do not invent stage names or criteria).
- To justify a stage the seller wants rather than the stage the evidence supports.
- For accounts that are not yet in an active sales cycle.

## Required inputs
- Opportunity summary: account name, contact, deal description, and interaction history.
- Stage definitions document: each stage name with its entry criteria, required evidence, and exit criteria.

## Optional inputs
- Discovery notes or call summaries.
- Qualification framework output (from Skill 35).
- Prior stage history (to detect stale or regressed deals).

## Step-by-step procedure

1. **Extract the evidence.** List every confirmed fact about the opportunity: meetings held, stakeholders identified, needs confirmed, budget discussed, timeline stated, decision criteria known, next steps agreed.
2. **Map evidence to stage criteria.** For each stage in the pipeline, check how many entry criteria are met, partially met, or unmet. Use only confirmed evidence; do not infer.
3. **Identify the highest stage fully supported by evidence.** The recommended stage is the highest stage where all entry criteria are confirmed. If the current stage's criteria are not met, flag a downgrade.
4. **State the gap.** List which entry criteria for the next stage are unmet and what evidence would close the gap.
5. **Check for stale indicators.** If the last meaningful activity was >21 days ago, flag as potentially stale.
6. **Produce recommendation document.**

## Output contract

```markdown
## Pipeline Stage Recommendation — Northlight Technologies
Date: YYYY-MM-DD

**Recommended stage:** Discovery (Stage 2 of 6)
**Current stage (if known):** Qualification (Stage 3) ← Flagged: criteria not fully met
**Evidence basis:** 1 discovery call completed; pain hypothesis confirmed; no budget discussion yet.

### Evidence vs. criteria
| Stage | Criteria | Met? | Evidence |
|---|---|---|---|
| Prospecting | Meeting booked | ✅ | Discovery call held 2026-10-10 |
| Discovery | Pain confirmed | ✅ | Sarah confirmed pipeline visibility challenge |
| Qualification | Budget discussed | ❌ | Not discussed |
| Qualification | Decision criteria known | ❌ | Not discussed |

### Gap to next stage (Qualification)
- Budget range: not discussed — recommend raising in next call
- Decision criteria: not known — recommend asking who else is involved

### Stale indicator
Last activity: 2026-10-10 (10 days ago) — within normal range.
```

## Evidence and citation rules
- Each met criterion must cite the specific interaction or document that confirms it.
- "Implied" or "likely" does not count as meeting a criterion.

## Confidence/uncertainty handling
- If evidence is thin (only 1 interaction), note this and label recommendation as provisional.
- If the seller claims a stage but the evidence supports a lower stage, explicitly flag the discrepancy.

## Safety, privacy, and compliance constraints
- Do not update CRM records autonomously.
- Do not share stage analysis with contacts.

## Human approval requirements
**No CRM update is made by this skill.** The recommendation is for the seller or manager to review and action. The seller updates the pipeline stage after reviewing the output.

## Failure modes and fallback behaviour
- **Stage definitions not supplied:** Return error; do not invent stages.
- **Opportunity summary is too sparse:** Return "Insufficient evidence — minimum inputs are account name, at least one interaction, and stage definitions."

## Acceptance criteria
- Recommended stage traces to at least one confirmed evidence item per entry criterion.
- Any downgrade from current stage is explicitly flagged.
- Gap to next stage is itemised.
- No CRM record is updated.

## Evaluation cases

**Case 1 — Correct stage with evidence.**
Input: 1 discovery call held; pain confirmed; no budget discussion. Stage definitions: Discovery = pain confirmed; Qualification = budget + decision criteria known.
Expected: Recommended stage = Discovery; gap to Qualification lists budget and decision criteria.

**Case 2 — Stage inflation detected.**
Input: Seller has marked opportunity as Proposal stage; only one exploratory call has occurred; no formal requirement confirmed.
Expected: Recommended stage = Discovery; flag that Proposal criteria are not met; list all unmet criteria.

## Related skills
- [Qualification Framework Mapper](/skills/04-discovery-and-deals/qualification-framework-mapper/SKILL.md) — provides structured qualification data.
- [Opportunity Risk Review](/skills/03-run-the-pipeline/opportunity-risk-review/SKILL.md) — deeper risk analysis for a given opportunity.
- [Pipeline Hygiene Audit](/skills/05-sales-enablement/pipeline-hygiene-audit/SKILL.md) — portfolio-level stage audit.
