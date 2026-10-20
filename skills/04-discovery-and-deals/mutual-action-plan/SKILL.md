---
name: Mutual Action Plan
description: Propose a shared milestone plan with owners, dates, and dependencies for the buyer to validate — not a seller-imposed timeline.
group: "04 — Discovery, Demos, and Deal Progression"
version: "1.0"
status: implemented
---

# Mutual Action Plan

## Purpose
After a demo or expression of serious interest, propose a Mutual Action Plan (MAP) — a shared, transparent sequence of steps that both seller and buyer agree to, leading to a decision. The MAP is a collaborative document, not a seller's close plan.

## When NOT to use
- Before the prospect has expressed genuine interest in moving forward.
- As a pressure tool to force an artificial timeline.
- Without a defined decision date or at least a rough timeframe from the prospect.

## Required inputs
- Deal summary: stage, confirmed pain, decision-makers identified, and any stated timeline.
- Seller's internal milestones (e.g., approval process, legal review, provisioning).
- Prospect's stated timeline or key dates (if any).

## Optional inputs
- Qualification map (from Skill 35).
- Mutual Action Plan template (from `templates/mutual-action-plan.md`).

## Step-by-step procedure

1. **Define the target decision date.** Use the prospect's stated date if available; otherwise propose one that is realistic given the current stage and typical sales cycle. Label it as a proposal, not a given.
2. **Work backwards from the decision date.** Map the milestones needed to reach a decision, in reverse order: decision → legal/procurement review → final business case review → technical validation → economic buyer approval → etc.
3. **Assign owners.** For each milestone, name who is responsible: seller's side, buyer's side, or joint.
4. **Add durations and dependencies.** Estimate duration for each step. Flag dependencies: "Legal review cannot start until technical validation is complete."
5. **Surface the risks.** What is most likely to delay this plan? List top 2–3 risks and their mitigations.
6. **Frame for the prospect.** The MAP is introduced as "Here's what I'm thinking — can we work through this together?" not as a closed document.
7. **Produce MAP draft.**

## Output contract

```markdown
## Mutual Action Plan — Northlight Technologies
Target decision date: 2026-12-12 (proposed — to confirm with Sarah)
Proposed by: Alex Kowalski | Date: YYYY-MM-DD

| Week | Milestone | Owner | Duration | Dependency |
|---|---|---|---|---|
| Oct 28 | Product demo with Sarah + CFO | Joint | 45 min | — |
| Nov 4 | Technical deep-dive with IT team | Joint | 60 min | Demo approved by Sarah |
| Nov 11 | Seller sends business case draft | Seller | 3 days | Technical review complete |
| Nov 18 | Buyer reviews business case; feedback | Buyer (Sarah + CFO) | 5 days | — |
| Nov 25 | Final commercial proposal sent | Seller | 2 days | Business case approved |
| Dec 5 | Legal / procurement review | Buyer (Procurement) | 5 days | Proposal accepted in principle |
| Dec 12 | Decision | Buyer | — | Legal complete |

### Risks to this timeline
1. CFO not yet engaged — if CFO introduction is delayed, add 1–2 weeks to timeline.
2. Procurement process unknown — procurement review duration is an estimate; confirm with Sarah.

### Framing for the prospect
"I've mapped out what I think a sensible path to a decision looks like, based on our conversation. I'd like to walk through this with you and adjust it — you know your internal process better than I do. Does this feel realistic?"
```

## Evidence and citation rules
- Timeline is based on stated dates and typical cycle assumptions; label assumptions as such.
- Do not present the MAP as finalised before the prospect has agreed to it.

## Confidence/uncertainty handling
- If the decision date is completely unknown, propose one and explicitly ask the prospect to validate or revise it.
- Flag unknown procurement or legal process duration as a risk.

## Safety, privacy, and compliance constraints
- Do not include internal seller pricing or margin information in the MAP.
- The MAP is a shared document — review before sharing.

## Human approval requirements
**The MAP is a draft for the seller to present to the prospect.** It is not sent automatically. The seller reviews, adapts, and presents it collaboratively.

## Failure modes and fallback behaviour
- **No timeline context supplied:** Build a generic template with placeholders and flag that dates need to be filled in with the prospect.
- **Very early stage:** Flag that a MAP is premature; recommend completing discovery and demo first.

## Acceptance criteria
- All milestones have owners and estimated durations.
- Dependencies are explicit.
- Risks are listed.
- Framing language for presenting to the prospect is included.
- Timeline is labelled as a proposal, not a commitment.

## Evaluation cases

**Case 1 — Post-demo, interested prospect.**
Input: Demo completed; Sarah expressed interest; target decision "before year end"; typical cycle 6 weeks.
Expected: MAP with milestones from current date to target decision; owners split between seller and buyer; top risks named.

**Case 2 — No timeline available.**
Input: Deal is early; no decision date mentioned.
Expected: MAP template with placeholder dates; flag that dates are estimates pending prospect input; framing language for collaborative discussion.

## Related skills
- [Demo Readiness Review](/skills/04-discovery-and-deals/demo-readiness-review/SKILL.md) — precedes MAP creation.
- [Proposal Outline](/skills/04-discovery-and-deals/proposal-outline/SKILL.md) — milestone in the MAP.
- [Opportunity Risk Review](/skills/03-run-the-pipeline/opportunity-risk-review/SKILL.md) — risks that inform MAP planning.
