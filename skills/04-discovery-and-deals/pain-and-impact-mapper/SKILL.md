---
name: Pain and Impact Mapper
description: Separate stated pain from inferred impact, quantify where possible, and identify the cost of inaction.
group: "04 — Discovery, Demos, and Deal Progression"
version: "1.0"
status: implemented
---

# Pain and Impact Mapper

## Purpose
From discovery notes, extract what the prospect explicitly said about their pain, distinguish it from impact you are inferring, and build a structured pain/impact map that supports a compelling business case — without inventing numbers.

## When NOT to use
- Without discovery notes or a call summary.
- To fabricate impact numbers that were not supplied or calculable from supplied data.
- Before discovery has occurred.

## Required inputs
- Discovery notes or call summary (from Skill 33 or manually supplied).

## Optional inputs
- Industry benchmarks or typical impact ranges (must be labelled as benchmarks, not as this prospect's numbers).
- Prospect's stated success metrics or goals.

## Step-by-step procedure

1. **Extract stated pain.** List every problem or frustration the prospect explicitly mentioned. Quote directly where possible.
2. **Classify each pain.** Type: Operational (process/efficiency), Strategic (goal/growth), Financial (cost/revenue), People (team/morale). Severity: High (mentioned unprompted, described as urgent), Medium (mentioned when asked), Low (acknowledged but deprioritised).
3. **Map stated pain to inferred impact.** For each pain, hypothesise the business impact. Label clearly as inferred: "If pipeline reviews take 2 hours and there are 8 AEs, that is ~16 hours of management time per week — but this is an estimate, not a confirmed figure."
4. **Identify the cost of inaction.** For each High-severity pain, describe what happens if the prospect does nothing. Be conservative and honest.
5. **Flag quantification gaps.** List any impact claims that need a number from the prospect to be credible. These become questions for the next conversation.
6. **Produce pain/impact map.**

## Output contract

```markdown
## Pain and Impact Map — Northlight Technologies
Based on: Discovery call notes 2026-10-22

### Stated pain (direct quotes where available)
1. "Pipeline reviews take 2 hours every Monday and still miss things" — Operational, High
2. "Deals are miscategorised by AEs; I find out too late" — Operational, High
3. "CEO wants clearer forecasts but I don't have confidence in the numbers" — Strategic, High

### Inferred impact (estimates — not confirmed figures)
| Pain | Inferred impact | Estimate basis |
|---|---|---|
| 2-hour Monday reviews × 8 AEs | ~16 hrs management time/week = ~£X/week at senior manager rate | Estimate only; confirm actual team size and cost |
| Late miscategorisation | Delayed interventions on at-risk deals; potential revenue leakage | Inferred from industry pattern; not confirmed |
| Forecast inaccuracy | Board credibility risk; poor resource allocation decisions | Stated by prospect (CEO pressure); magnitude unknown |

### Cost of inaction
- If pipeline review process is not improved in the next quarter: 8 AEs scaling to 15 without a system change = current problems at 2× scale.
- Forecast inaccuracy risk increases with headcount growth.
- No urgent external deadline identified; internal pressure from CEO is the primary driver.

### Quantification gaps (questions for next call)
- What is the average AE's time spent on admin vs. selling?
- Have any deals been lost specifically because of missed pipeline signals?
- What is the target headcount 12 months from now?
```

## Evidence and citation rules
- Stated pain uses quotes or close paraphrase with a label.
- Inferred impact is always labelled as an estimate or hypothesis.
- Never present an impact number as confirmed unless the prospect supplied it.

## Confidence/uncertainty handling
- Rate impact confidence: Confirmed (prospect supplied number), Estimated (calculable from supplied data), Hypothetical (industry pattern, not account-specific).
- Do not conflate "likely" impact with "confirmed" impact.

## Safety, privacy, and compliance constraints
- Do not share the pain/impact map with the prospect without seller review.
- Do not fabricate benchmarks to make the business case look stronger.

## Human approval requirements
**Pain/impact map is an internal preparation tool.** The seller reviews before using it in conversations or proposals. No external sharing without human approval.

## Failure modes and fallback behaviour
- **No discovery notes:** Return error; do not invent pain from the account brief alone.
- **Only generic pain mentioned:** Flag that the map is low-specificity; recommend a deeper discovery conversation.

## Acceptance criteria
- Stated pain is separated from inferred impact.
- Each inferred impact is labelled with its estimation basis.
- Quantification gaps are listed as follow-up questions.
- No numbers are fabricated.

## Evaluation cases

**Case 1 — Rich discovery notes.**
Input: Notes with 3 explicit pain points, one with a rough number ("2 hours every week").
Expected: Stated/inferred separation; the 2-hour figure used in an estimate (labelled as estimate); quantification gaps listed.

**Case 2 — Vague notes.**
Input: "Prospect mentioned they have some process challenges."
Expected: Low-specificity flag; generic pain/impact map; strong recommendation for a more structured discovery conversation.

## Related skills
- [Call Notes Structurer](/skills/04-discovery-and-deals/call-notes-structurer/SKILL.md) — provides the notes.
- [Qualification Framework Mapper](/skills/04-discovery-and-deals/qualification-framework-mapper/SKILL.md) — maps pain to MEDDICC Identify Pain dimension.
- [Proposal Outline](/skills/04-discovery-and-deals/proposal-outline/SKILL.md) — uses the pain/impact map.
