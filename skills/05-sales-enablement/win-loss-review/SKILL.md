---
name: Win/Loss Review
description: Distinguish documented reasons a deal was won or lost from post-hoc rationalisation and speculation
group: "05 — Sales Enablement and Management"
version: "1.0"
status: implemented
---


# Win/Loss Review

## Purpose

Produce a structured win/loss analysis that separates what was actually documented during the sales process from what the rep or manager is inferring retrospectively. The goal is to extract genuine learning, not to assign blame or justify the outcome.

## When NOT to use

- When no deal notes or context are supplied (this skill cannot review a phantom deal)
- When the deal is still open (use Deal Review Facilitator instead)
- When the goal is to estimate forecast accuracy (use Forecast Challenge)

## Required inputs

- `deal_outcome`: `won` | `lost`
- `deal_summary`: what is known about the opportunity (company, contact, product, amount, why they were evaluating)
- `stated_reason`: what the rep or prospect said was the reason for the outcome

## Optional inputs

- `deal_notes`: notes from discovery, demo, and follow-up calls
- `competitor_info`: which competitors were involved, if known
- `qualification_data`: MEDDICC or SPICED data captured during the deal

## Step-by-step procedure

1. Read all supplied inputs. Note every claim in `stated_reason`.
2. For each claim, assess its evidence basis:
   - **Documented**: supported by `deal_notes` or `qualification_data`
   - **Inferred**: plausible given the deal context but not explicitly documented
   - **Speculative**: no supporting evidence; rep's post-hoc interpretation
3. Categorise the outcome into primary and secondary reasons using only documented and inferred evidence.
4. Identify 1–2 actionable lessons for future deals.
5. Flag any assumptions made in this analysis.
6. If competitor information is available, summarise the competitive dynamic without fabricating competitor capabilities.

## Output contract

```
WIN/LOSS REVIEW — Northlight Technologies | LOST
Deal amount: $85K | Competitor: Vendor X (confirmed)

STATED REASON: "They went with Vendor X because of price."

EVIDENCE ASSESSMENT:
- "Price was the issue" — INFERRED: prospect mentioned budget constraints in discovery (documented); no explicit price comparison given by prospect
- "Vendor X was cheaper" — SPECULATIVE: pricing gap not confirmed; rep did not receive a formal rejection with pricing rationale
- "Champion advocacy was weak" — INFERRED: champion never introduced rep to economic buyer (documented in notes)

PRIMARY REASON (documented/inferred): Champion did not have enough internal influence to drive the deal
SECONDARY REASON (inferred): Budget sensitivity was present from discovery; pricing may have been a factor but was not the sole cause

ACTIONABLE LESSONS:
1. Confirm champion authority earlier — ask: "Can you arrange a meeting with the person who controls budget?"
2. Address price sensitivity explicitly in evaluation stage rather than waiting for procurement

ASSUMPTIONS IN THIS REVIEW:
- Vendor X identity confirmed; Vendor X pricing not verified
- Rep's notes from discovery call used as primary source; no post-decision call with prospect

NOTE: This review is based on internally supplied data. A post-decision call with the prospect would significantly improve accuracy.
```

## Evidence and citation rules

- Every claim must be labelled as documented, inferred, or speculative.
- Do not fabricate competitor capabilities, prospect motivations, or deal facts.
- A recommendation for a post-decision customer conversation is always included if no such conversation occurred.

## Confidence/uncertainty handling

- If deal notes are absent: note that the review is based on stated reasons alone and has low evidential value.
- If stated reason conflicts with deal notes: flag the conflict explicitly.

## Safety, privacy, and compliance constraints

- Do not share the review with the prospect without explicit manager approval.
- Do not make personal negative assessments of the rep's character — focus on process and skills.

## Human approval requirements

**This skill produces an internal review document.** The manager reviews it before any action, including sharing with the rep or adjusting coaching plans. No external communications are taken.

## Failure modes and fallback behaviour

- `deal_outcome` missing: return an error.
- `stated_reason` is empty: note the absence and produce a framework for gathering it.
- Deal notes are in a foreign language: flag and attempt partial analysis.

## Acceptance criteria

- Every element of `stated_reason` is assessed as documented, inferred, or speculative.
- Primary reason is supported by ≥1 piece of evidence.
- At least 1 actionable lesson present.
- Assumptions section non-empty.

## Evaluation cases

**Case 1 — Lost deal with good notes**
Input: lost deal, detailed notes showing champion never met economic buyer, pricing mentioned once in discovery. Expected: documented evidence for champion weakness, inferred status for price, two actionable lessons about qualification.

**Case 2 — Won deal, minimal notes**
Input: won deal, stated reason "they loved the demo", no notes. Expected: all claims labelled speculative, recommendation to conduct a win interview to understand what actually drove the decision, low-confidence warning.

## Related skills

- [Deal Review Facilitator](/skills/05-sales-enablement/deal-review-facilitator/SKILL.md)
- [Sales Call Coach](/skills/05-sales-enablement/sales-call-coach/SKILL.md)
- [Qualification Framework Mapper](/skills/04-discovery-and-deals/qualification-framework-mapper/SKILL.md)
- [Sales Experiment Designer](/skills/05-sales-enablement/sales-experiment-designer/SKILL.md)
