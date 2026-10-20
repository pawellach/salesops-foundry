---
name: Qualification Framework Mapper
description: Map discovery evidence to a configurable qualification framework (MEDDICC, SPICED, or BANT) without treating any framework as universal truth.
group: "04 — Discovery, Demos, and Deal Progression"
version: "1.0"
status: implemented
---

# Qualification Framework Mapper

## Purpose
Assess an opportunity against a chosen qualification framework using only discovered evidence. Identify confirmed, partial, and missing dimensions. Produce an honest qualification snapshot — not a score to satisfy a manager.

## When NOT to use
- Without discovery notes or a call summary.
- To manufacture a qualification score that is better than the evidence supports.
- When the team has no defined framework — in that case, recommend selecting one first.

## Required inputs
- Discovery notes or structured notes (from Skill 33).
- Chosen framework: MEDDICC, SPICED, BANT, or custom (if custom, supply dimension definitions).

## Optional inputs
- Pain and impact map (from Skill 34).
- Stage definitions for context.

## Step-by-step procedure

1. **State the framework.** List all dimensions with their definitions (as per the chosen framework).
2. **Map evidence to each dimension.** For each dimension, extract the relevant evidence from the discovery notes. Status: Confirmed (explicit evidence), Partial (some evidence, gaps remain), Missing (not discussed or unknown).
3. **Do not invent evidence.** If a dimension has no supporting evidence, mark it Missing.
4. **Identify the deal-qualification risk.** Which Missing dimensions are most likely to kill the deal if not addressed? Flag as High Risk.
5. **Recommend qualification actions.** For each Missing or Partial dimension, name the specific question or action to address it.
6. **Produce framework map.**

## Output contract (MEDDICC example)

```markdown
## Qualification Map — Northlight Technologies
Framework: MEDDICC | Based on: Discovery call 2026-10-22

| Dimension | Status | Evidence | Risk if missing |
|---|---|---|---|
| Metrics | Partial | Pain confirmed (2hr reviews, forecast inaccuracy); no ROI metrics defined | Medium — needed for business case |
| Economic Buyer | Missing | Sarah is CTO; CFO likely involved for >£20k; not engaged yet | High — deal cannot close without EB approval |
| Decision Criteria | Missing | Not discussed | High — competitor could win on criteria we don't know |
| Decision Process | Missing | Not discussed | High — timeline and process unknown |
| Identify Pain | Confirmed | 3 explicit pain points stated by Sarah | — |
| Champion | Partial | Sarah is engaged and interested; has not committed to championing | Medium — need to test champion strength |
| Competition | Missing | Not asked | Medium — we may be in a competitive evaluation |

### High-risk qualification gaps
1. Economic Buyer not engaged — deal cannot close without this
2. Decision Criteria unknown — we may be optimising for the wrong things
3. Decision Process unknown — close date estimate is unreliable

### Recommended qualification actions
- Next call: "Who else would need to be involved in approving a decision of this size?"
- Next call: "What criteria would you use to evaluate options like this?"
- Next call: "Is there a process or timeline you're working to?"

### Overall qualification: Partial — do not forecast as Commit
```

## Evidence and citation rules
- Each confirmed dimension must cite the specific evidence.
- Partial status requires noting exactly what is known and what is missing.
- Never mark a dimension as Confirmed based on assumption.

## Confidence/uncertainty handling
- If framework dimensions are partially covered, use Partial — never round up to Confirmed.
- Qualification frameworks are guides, not guarantees. A fully-confirmed MEDDICC does not guarantee a win.

## Safety, privacy, and compliance constraints
- Qualification maps are internal documents; do not share with prospects.
- Do not use qualification data to make discriminatory decisions about which prospects deserve service.

## Human approval requirements
**Qualification assessment is an internal tool.** Forecast categorisation changes (e.g., moving to Commit) require human manager review; this skill does not update forecasts.

## Failure modes and fallback behaviour
- **Framework not specified:** Default to MEDDICC; flag that this was the default choice.
- **Notes too sparse for meaningful mapping:** Produce a mostly-Missing map; recommend a structured re-discovery.

## Acceptance criteria
- All dimensions of the chosen framework are addressed.
- At least one dimension is explicitly confirmed with cited evidence.
- High-risk Missing dimensions are flagged.
- Qualification actions are specific, not generic.

## Evaluation cases

**Case 1 — Post-first-discovery MEDDICC.**
Input: Call notes with confirmed pain, partial champion, missing EB and decision criteria.
Expected: MEDDICC map with Confirmed/Partial/Missing per dimension; 2–3 High-risk flags; specific next-call questions.

**Case 2 — No notes, just account brief.**
Input: Account brief only; no discovery notes.
Expected: All dimensions = Missing; output flagged as "Pre-discovery — not a qualification map; complete discovery first."

## Related skills
- [Call Notes Structurer](/skills/04-discovery-and-deals/call-notes-structurer/SKILL.md) — notes input.
- [Pain and Impact Mapper](/skills/04-discovery-and-deals/pain-and-impact-mapper/SKILL.md) — evidence for Metrics and Identify Pain dimensions.
- [Opportunity Risk Review](/skills/03-run-the-pipeline/opportunity-risk-review/SKILL.md) — uses qualification gaps as risk inputs.
