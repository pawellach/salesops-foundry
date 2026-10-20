---
name: Negotiation Planner
description: Prepare options, trade-offs, walk-away constraints, and approval points for a commercial negotiation.
group: "04 — Discovery, Demos, and Deal Progression"
version: "1.0"
status: implemented
---

# Negotiation Planner

## Purpose
Before a commercial negotiation, prepare a structured plan: what you can trade, what you cannot, what the prospect most values, and where the walk-away points are. Negotiation preparation prevents both over-conceding and unnecessary deal loss.

## When NOT to use
- Without a proposal in flight and confirmed commercial interest.
- For early-stage conversations about price — that is premature pricing discussion, not negotiation.
- To produce tactics designed to manipulate or pressure the prospect.

## Required inputs
- Proposal summary: deal structure, total value, key terms.
- Seller's stated flexibility limits (what you can and cannot negotiate — seller-supplied; do not invent).
- Any signals about what the prospect cares most about (price, timeline, support terms, flexibility, etc.).

## Optional inputs
- Qualification map (from Skill 35) — especially budget signals.
- Objection history — any pricing objections already raised.
- Internal approval process: what requires manager sign-off?

## Step-by-step procedure

1. **Define the target outcome.** Ideal deal structure, including price, terms, start date, and scope.
2. **Define the acceptable range.** For each negotiable dimension, state the range from Target to Walk-away. Do not confuse Walk-away with "least preferred" — walk-away is the point at which the deal is worse than no deal.
3. **Identify what the prospect most values.** Based on discovery and signals: is it price, flexibility, speed to implement, support, contract length, or something else? Prioritise giving concessions on things they value but that cost you less.
4. **Identify value trades.** Things you can offer (implementation support, extended trial, phased pricing, multi-year discount) and what you expect in return (larger scope, earlier start, multi-year commit, reference customer agreement).
5. **Define approval requirements.** Which concessions require manager or VP approval? List them. The seller should not offer these without approval.
6. **Plan the opening position.** Start at or near the proposal; do not pre-emptively discount.
7. **Produce negotiation plan document.**

## Output contract

```markdown
## Negotiation Plan — Northlight Technologies
Date: YYYY-MM-DD | Deal: Team plan, £24k/year

### Target outcome
£24k/year, 12-month contract, start date 2026-12-15, standard support.

### Negotiable dimensions

| Dimension | Target | Acceptable range | Walk-away |
|---|---|---|---|
| Annual price | £24k | £20k–£24k | Below £19k (below cost of service) |
| Contract length | 12 months | 12–24 months | Month-to-month with no commit |
| Implementation support | Standard | Standard → Enhanced (at cost) | Free enhanced support not approved |
| Start date | Dec 15 | Dec 15 – Jan 15 | Later than Jan 31 (misses Q1 budget cycle) |

### What the prospect most values (based on discovery signals)
- Speed: Sarah mentioned "before year end" twice — timeline is important
- Confidence: they want to see it work for teams like them

### Value trades to consider
- Offer: Enhanced onboarding (2 extra sessions) in exchange for 24-month commit
- Offer: Locked pricing for 24 months in exchange for multi-year deal
- Avoid: Blanket discounts not linked to a concession — devalues the product

### Approval requirements
- Any price below £21k requires VP Sales sign-off before offering
- Multi-year pricing requires Finance approval
- Do not offer free professional services without manager approval

### Opening position
Present the proposal as is. Do not pre-emptively discount. Wait for the prospect to raise a concern before trading.

### If they ask for a discount immediately
"I want to make sure I'm giving you the best deal for your situation — can you help me understand what's driving the ask? Is it the total budget, the payment structure, or something else?" — clarify before conceding.
```

## Evidence and citation rules
- Walk-away points must be seller-supplied; do not invent them.
- Prospect's priorities must trace to discovery evidence or stated signals.

## Confidence/uncertainty handling
- If prospect's priorities are unknown, note this as a risk and plan a clarifying question for the negotiation.

## Safety, privacy, and compliance constraints
- Do not use false scarcity, fabricated competing offers, or psychological pressure tactics.
- Do not make concessions that violate company policy.
- Approval requirements are listed because exceeding authority without sign-off can void agreements.

## Human approval requirements
**The negotiation is conducted by a human.** This plan is preparation only. No commercial offer is made by this skill. Concessions requiring approval must be obtained before the negotiation conversation.

## Failure modes and fallback behaviour
- **Flexibility limits not supplied:** Return "Walk-away points cannot be defined without seller-supplied limits — consult manager."
- **No proposal in flight:** Return "Negotiation planning is premature without an active proposal."

## Acceptance criteria
- All negotiable dimensions have a Target, Acceptable range, and Walk-away.
- Approval requirements are listed.
- Value trades are specific (not "offer a discount if needed").
- Opening position instruction present.

## Evaluation cases

**Case 1 — Price-sensitive prospect.**
Input: Proposal = £24k/year; seller flexibility = down to £20k with manager approval below £21k; prospect signalled budget is tight.
Expected: Price dimension fully ranged; approval requirement noted; trade ideas to get something in return for price movement; clarifying question for opening.

**Case 2 — No flexibility limits supplied.**
Input: Proposal outlined; seller did not supply flexibility limits.
Expected: Error or strong warning — "Walk-away points not supplied; negotiate without this plan or consult your manager first."

## Related skills
- [Proposal Outline](/skills/04-discovery-and-deals/proposal-outline/SKILL.md) — the proposal being negotiated.
- [Objection Handling Coach](/skills/04-discovery-and-deals/objection-handling-coach/SKILL.md) — for objections raised during negotiation.
- [Mutual Action Plan](/skills/04-discovery-and-deals/mutual-action-plan/SKILL.md) — timeline context.
