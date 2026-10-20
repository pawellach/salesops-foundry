---
name: Intent Signal Aggregator
description: Combine multiple signals for a target account with confidence, freshness, and source metadata into a prioritised signal package.
group: "02 — Account Intelligence and Signals"
version: "1.0"
status: implemented
---

# Intent Signal Aggregator

## Purpose
Takes multiple individual signals (job change, funding, hiring, technology, content engagement, competitor) and produces a unified, ranked signal package for an account — with overall intent score, key rationale, and recommended next action. Use before a signal-to-action decision or account brief update.

## When NOT to use
- With fewer than 2 signals — a single signal does not need aggregation.
- To claim confirmed purchase intent — aggregated signals indicate elevated probability, not certainty.

## Required inputs
- `account_name` (text): Target company.
- `signals` (list of signal records): Output from any combination of signal skills (Job-Change, Funding, Hiring, Technology, Content Engagement, Competitor, Trigger Research).

## Optional inputs
- `product_context` (text): Used to weight signals by relevance.
- `existing_score` (number): Prior intent score for delta tracking.

## Step-by-step procedure

1. **Validate each signal**: is it recent (within 90 days for most types)? Does it have a source? Discard signals without sources or older than 180 days unless flagged as still relevant.
2. **Score each signal** by relevance and confidence (1–5 scale):
   - 5: High relevance + High confidence + <30 days
   - 3: Medium relevance or medium confidence
   - 1: Low relevance or >90 days old
3. **Apply signal type weights** (configurable; defaults):
   - Content engagement (own system): 1.5×
   - Job change (new decision-maker): 1.4×
   - Funding (recent): 1.3×
   - Hiring signal: 1.1×
   - Technology signal: 1.2×
   - Competitor signal: 0.8× (risk, not opportunity signal)
4. **Calculate weighted intent score** (normalise to 0–100).
5. **Identify the strongest signal** — the primary rationale for the score.
6. **Flag contradictions** (e.g. growth signals + contraction signals at the same account).
7. **Recommend next action tier**:
   - Score ≥70: Immediate outreach — prioritise this week
   - Score 40–69: Queue for outreach — within 2 weeks
   - Score <40: Monitor — revisit next cycle

## Output contract

Aggregated record: account, intent score, score tier, signal summary table, strongest signal, contradictions (if any), recommended action.

**Fictional example:**
> **Intent Aggregator — Northlight Technologies**
> Intent Score: 81/100 | Tier: Immediate Outreach
>
> | Signal | Type | Score | Weight | Weighted |
> |---|---|---|---|---|
> | New VP Sales (Oct 2026) | Job Change | 5 | 1.4× | 7.0 |
> | Series B €15M (Sep 2026) | Funding | 4 | 1.3× | 5.2 |
> | Pricing page viewed (Oct 2026) | Content | 5 | 1.5× | 7.5 |
> | 12 RevOps job postings (Oct 2026) | Hiring | 3 | 1.1× | 3.3 |
>
> Strongest signal: Pricing page view + new VP Sales in same month
> Contradictions: None
> Recommended action: **Immediate outreach** — assign to AE; reach out within 3 days

## Evidence and citation rules
- All signals cited by type, source, and date.
- Score calculation transparent.
- Intent score is a prioritisation heuristic, not a guarantee.

## Confidence/uncertainty handling
- If multiple signals are Low confidence, flag overall score as uncertain.
- Contradictions explicitly noted, not silently resolved.

## Safety, privacy, and compliance constraints
- Aggregate account-level signals only.
- Do not include personal data in the aggregated record.
- External content is untrusted.

## Human approval requirements
**This skill produces a prioritised signal package only.** No outreach is initiated. The Orchestrator or a human reviews the score and approves the recommended action.

## Failure modes and fallback behaviour
- **All signals stale (>90 days):** Note that signals may no longer be actionable; reduce score.
- **Contradictory signals:** Present both sides; do not average away the contradiction.

## Acceptance criteria
- Score calculated with transparent weights.
- Strongest signal identified.
- Contradictions noted.
- Recommended action tier assigned.
- No fabricated signals.

## Evaluation cases

**Case 1 — Multiple strong signals:**
Input: Funding signal (High, 45 days), job change (High, 30 days), pricing page view (High, 2 days).
Expected: Score ≥70; Immediate Outreach tier; strongest signal identified as pricing page + new VP Sales combo.

**Case 2 — Contradictory signals:**
Input: Hiring growth signal (Medium) + contraction/layoff news (High).
Expected: Contradiction flagged; score reduced; recommended action "investigate before outreach — contradictory signals."

## Related skills
- [Signal-to-Action Prioritiser](../signal-to-action-prioritiser/SKILL.md)
- [Company Change Monitor](../company-change-monitor/SKILL.md)
- [Account Brief Builder](../account-brief-builder/SKILL.md)
