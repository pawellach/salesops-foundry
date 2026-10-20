---
name: Opportunity Risk Review
description: Identify gaps, blockers, competitive threats, and unsupported optimism in a specific opportunity.
group: "03 — Run the Pipeline"
version: "1.0"
status: implemented
---

# Opportunity Risk Review

## Purpose
Challenge the assumptions behind an opportunity to surface risks that could cause a deal to stall, shrink, or be lost. Produce an actionable risk list with severity ratings and suggested next steps.

## When NOT to use
- On opportunities in early prospecting with no confirmed stakeholder engagement.
- As a rubber-stamp exercise to justify existing forecast assumptions.

## Required inputs
- Opportunity summary: stage, deal size, close date, contacts, interaction history.
- Current stage and forecast category (commit, best case, pipeline).

## Optional inputs
- Qualification framework output (Skill 35).
- Mutual Action Plan if one exists (Skill 40).
- CRM history (exported as text or CSV).

## Step-by-step procedure

1. **Extract key deal facts.** Stage, expected close date, deal size, champion, economic buyer, decision criteria, competition, next steps.
2. **Check for absent critical information.** For each MEDDICC dimension (or equivalent), mark as Confirmed, Partial, or Missing.
3. **Identify risks.** Evaluate: (a) No economic buyer identified or engaged; (b) Close date is optimistic relative to stage and activity; (c) Single-threaded (only one contact); (d) No confirmed next step; (e) Competition not understood; (f) No compelling event or deadline; (g) Budget is assumed, not confirmed; (h) Decision criteria unknown or not mapped to our offering.
4. **Rate each risk.** High (likely to block or lose deal), Medium (could slow or shrink deal), Low (worth monitoring).
5. **Suggest a specific next step for each High and Medium risk.** Be concrete: "Ask Sarah in the next call: 'Who else needs to approve a decision of this size?'"
6. **Challenge the close date.** Based on stage, activity cadence, and typical sales cycle, state whether the close date is Realistic, Optimistic, or Unlikely.
7. **Produce risk review document.**

## Output contract

```markdown
## Opportunity Risk Review — Northlight Technologies
Date: YYYY-MM-DD
Stage: Qualification | Forecast: Best Case | Close date: 2026-11-30

### MEDDICC completeness
| Dimension | Status | Notes |
|---|---|---|
| Metrics | Partial | Pain confirmed; no success metrics defined |
| Economic Buyer | Missing | Only spoke to CTO; no CFO or CEO engagement |
| Decision Criteria | Missing | Not discussed |
| Decision Process | Missing | Unknown |
| Identify Pain | Confirmed | Pipeline visibility confirmed as a challenge |
| Champion | Partial | Sarah is engaged but has not committed to championing |
| Competition | Missing | Not asked |

### Risk register
| Risk | Severity | Suggested next step |
|---|---|---|
| No economic buyer engaged | High | Ask Sarah: "Who approves a budget of this size?" |
| Single-threaded | High | Map the buying committee in next call |
| Close date optimistic | High | Close date 2026-11-30 is 40 days out; current stage is Qualification. Realistic close: Q1 2027 |
| No success metrics defined | Medium | Ask: "What would success look like in 6 months?" |
| Competition unknown | Medium | Ask: "Are you looking at other options?" |

### Close date assessment
Optimistic. Current stage (Qualification) + 40 days to close date is below typical 60–90-day cycle for deals of this size. Recommend updating forecast to Pipeline until at least Proposal stage.
```

## Evidence and citation rules
- Risk ratings must be based on evidence gaps, not pessimism or optimism.
- Do not rate a risk as Low simply because the seller is confident.

## Confidence/uncertainty handling
- If information is missing, rate the absence as a risk, not as "probably fine."
- Distinguish between "not discussed yet" (recoverable) and "buyer said no" (material blocker).

## Safety, privacy, and compliance constraints
- Do not share risk review content with the prospect.
- Do not update CRM forecast fields autonomously.

## Human approval requirements
**No forecast or CRM changes are made by this skill.** The seller and manager review the risk document and decide which actions to take and whether to adjust the forecast.

## Failure modes and fallback behaviour
- **Opportunity summary too sparse:** Return minimum input requirements and ask for more.
- **No stage definitions supplied:** Use generic MEDDICC framework and flag that stage-specific criteria were not available.

## Acceptance criteria
- Every MEDDICC dimension is addressed (or equivalent framework).
- Each High-severity risk has a concrete suggested next step.
- Close date assessment is explicit.
- No CRM changes made.

## Evaluation cases

**Case 1 — High-risk deal in commit.**
Input: Deal in Commit; no economic buyer; single-threaded; close date in 30 days.
Expected: 2–3 High risks; close date rated Optimistic or Unlikely; concrete next steps for each High risk.

**Case 2 — Well-progressed deal.**
Input: Economic buyer met; mutual action plan agreed; close date 60 days out; competition identified.
Expected: Few or no High risks; any Medium risks noted; close date rated Realistic.

## Related skills
- [Qualification Framework Mapper](/skills/04-discovery-and-deals/qualification-framework-mapper/SKILL.md) — structures the qualification data.
- [Pipeline Stage Recommendation](/skills/03-run-the-pipeline/pipeline-stage-recommendation/SKILL.md) — stage assessment.
- [Deal Review Facilitator](/skills/05-sales-enablement/deal-review-facilitator/SKILL.md) — manager-level deal review.
