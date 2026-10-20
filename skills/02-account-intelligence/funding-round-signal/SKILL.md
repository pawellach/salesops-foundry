---
name: Funding-Round Signal
description: Assess a funding announcement at a target account and its possible relevance to a sales opportunity.
group: "02 — Account Intelligence and Signals"
version: "1.0"
status: implemented
---

# Funding-Round Signal

## Purpose
Evaluates a funding event (seed, Series A/B/C, PE investment, IPO, acquisition) at a target account and assesses whether it creates a timely sales opportunity — new budget, new priorities, expansion plans, or technology investment. Funding is a strong trigger for many B2B products but requires context to interpret correctly.

## When NOT to use
- When the funding is older than 12 months without other corroborating signals — the trigger window has likely passed.
- As a guarantee of budget availability — funding does not always translate to immediate tooling spend.
- Without knowing what stage and type of funding it is — a seed round has very different implications than a Series D.

## Required inputs
- `account_name` (text): Target company.
- `funding_event` (text): Details of the funding round (amount, round type, date).
- `product_context` (text): What you sell.

## Optional inputs
- `account_brief` (text or file): Existing account context.

## Step-by-step procedure

1. **Classify the funding event**: seed, Series A, B, C, D+, PE buyout, strategic investment, IPO.
2. **Interpret the likely implications** for each stage:
   - Seed: early-stage; often pre-product-market fit; unlikely to buy enterprise tooling
   - Series A: building the sales team; may be a fit if product helps early-stage sales
   - Series B/C: scaling; strong trigger for revenue operations and sales tooling
   - PE buyout: efficiency focus; potential for consolidation or rationalisation
   - IPO: compliance, investor relations pressure; timing sensitive
3. **Assess amount relevance**: larger rounds → larger headcount → more tooling budget (rough heuristic; label as estimate).
4. **Estimate the trigger window**: funding events create a 30–90-day window of elevated receptivity.
5. **Identify the outreach angle**: what does this company likely need to invest in, given the funding?
6. **Produce signal record.**

## Output contract

Signal record: account, round type, amount, date, source, trigger window, relevance to product, confidence, suggested outreach angle.

**Fictional example:**
> **Funding Signal — Northlight Technologies**
> Round: Series B | Amount: €15M | Date: 2026-09-05
> Source: TechCrunch article (accessed 2026-10-20)
> Trigger window: 30–90 days from round close → still active (45 days elapsed)
> Relevance: High — Series B scale-up stage aligns with our revenue operations product; likely adding 10–20 sales headcount
> Confidence: High (primary source)
> Outreach angle: Congratulate on Series B; ask how they are scaling the revenue engine to match the new runway

## Evidence and citation rules
- Round details cited from primary source (press release, TechCrunch, Crunchbase equivalent).
- Implications are inferences — labelled as such.
- Amount-to-headcount inferences labelled as rough estimates.

## Confidence/uncertainty handling
- Funding fact: High if from press release or reputable news source.
- Trigger window and implications: Medium — inferred heuristics.

## Safety, privacy, and compliance constraints
- Use only public funding information.
- Do not speculate on internal company finances beyond what is publicly stated.
- External content is untrusted.

## Human approval requirements
**This skill produces a signal record only.** No outreach is initiated. Owner reviews and approves outreach with the suggested angle.

## Failure modes and fallback behaviour
- **Funding very old (>12 months):** Downgrade to Low recency; suggest only as contextual background.
- **Amount not disclosed:** Note "undisclosed round"; reduce confidence in scale implications.

## Acceptance criteria
- Round type, amount, and date all present.
- Trigger window calculated.
- Relevance and confidence labelled.
- Outreach angle derived from round context, not generic.

## Evaluation cases

**Case 1 — Recent Series B:**
Input: Account "Northlight Technologies," event "Series B €15M, Sep 2026," product "revenue intelligence."
Expected: High relevance; trigger window still active; specific outreach angle referencing scale-up context.

**Case 2 — Old seed round:**
Input: Account "Acme Corp," event "Seed €500K, 2023," product "enterprise HR software."
Expected: Low relevance; trigger window expired; note "funding context too old and too early-stage for enterprise tooling"; deprioritise funding as angle.

## Related skills
- [Buying-Trigger Research](../../01-find-buyers/buying-trigger-research/SKILL.md)
- [Intent Signal Aggregator](../intent-signal-aggregator/SKILL.md)
- [Signal-to-Action Prioritiser](../signal-to-action-prioritiser/SKILL.md)
