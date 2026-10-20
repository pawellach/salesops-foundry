---
name: Forecast Challenge
description: Challenge forecast confidence with evidence requirements, scenario analysis, and questions that expose unsupported optimism
group: "05 — Sales Enablement and Management"
version: "1.0"
status: implemented
---


# Forecast Challenge

## Purpose

Help a sales manager or revenue leader stress-test a sales forecast by identifying which committed deals have sufficient evidence, which are optimistic assumptions, and what the realistic range of outcomes is.

## When NOT to use

- When you want a deal-level health review (use Deal Review Facilitator)
- When you want pipeline hygiene issues (use Pipeline Hygiene Audit)
- When the intent is to produce the forecast itself (this skill challenges it, not builds it)

## Required inputs

- `forecast_data`: the submitted forecast — at minimum, a list of committed deals with amounts and close dates
- `today_date`: current date (ISO 8601)

## Optional inputs

- `team_target`: the period's revenue target
- `evidence_fields`: fields that indicate deal strength (e.g., `champion`, `next_step`, `economic_buyer_met`)
- `historical_win_rate`: the team's average win rate for context

## Step-by-step procedure

1. Parse `forecast_data`. For each committed deal, assess evidence strength based on available fields.
2. Categorise each committed deal:
   - **Strongly evidenced**: ≥3 qualification signals present, recent activity
   - **Weakly evidenced**: 1–2 signals, no recent activity, or close date in <7 days with no documented next step
   - **Unsupported**: no qualification signals, no activity, or rep's gut feeling only
3. Calculate three scenarios:
   - **Conservative**: only strongly evidenced deals close
   - **Base**: strongly evidenced + 50% of weakly evidenced deals close
   - **Optimistic**: all committed deals close (the rep's forecast)
4. Generate 3–5 challenge questions for the manager to ask in the forecast review meeting.
5. Flag specific deals where the evidence gap is largest.
6. Do not produce a single "correct" forecast number — produce a range and a question list.

## Output contract

```
FORECAST CHALLENGE — Q4 Week 3 (2026-10-20)
Team target: $800K | Rep forecast: $520K

COMMITTED DEAL ASSESSMENT:
| Deal | Amount | Evidence Level | Key Gap |
|---|---|---|---|
| Northlight Technologies | $85K | Strong | None — champion confirmed, next step set |
| Meridian Logistics | $120K | Weak | Economic buyer not met |
| Acme Corp | $95K | Unsupported | No activity 28 days; no next step |

SCENARIO ANALYSIS:
Conservative (strong only): $85K
Base (strong + 50% weak): $145K
Optimistic (all committed): $300K

GAP TO TARGET: $455K–$715K depending on scenario

CHALLENGE QUESTIONS FOR THE REVIEW:
1. For Meridian Logistics: "Who will sign the contract? Have you spoken to them?"
2. For Acme Corp: "When did you last speak to the champion? What's the agreed next step?"
3. For the full forecast: "Which of these deals can you lose and still hit target?"

NOTE: This analysis is based on supplied data only. Actual outcomes depend on factors not visible here.
```

## Evidence and citation rules

- Every evidence level must cite which fields were present or absent.
- Never claim to predict actual revenue outcomes.
- Scenario ranges are illustrative, not forecasts.

## Confidence/uncertainty handling

- If evidence fields are not in the data, note: "Evidence assessment is limited — only stage and amount available."
- Historical win rate, if supplied, is used as context only. Do not use it to adjust individual deal probabilities.

## Safety, privacy, and compliance constraints

- Forecast data is commercially sensitive. Treat as confidential.
- Do not share, email, or post output — produce a draft for the manager's review.

## Human approval requirements

**This skill produces a draft challenge document.** The manager reviews it before using it in a forecast call. No external actions taken. Output is clearly labelled as a draft.

## Failure modes and fallback behaviour

- Empty `forecast_data`: return an error.
- All deals have identical data: note the lack of differentiation and produce generic questions.
- `today_date` missing: note assumption.

## Acceptance criteria

- Each committed deal is categorised with a reason.
- Three scenario amounts are present.
- At least 3 challenge questions referencing specific deals.
- No single forecast number claimed as correct.

## Evaluation cases

**Case 1 — Strong forecast**
Input: 4 committed deals, all with champion, next step, and recent activity. Expected: all categorised as Strong; conservative scenario = optimistic scenario; minimal challenge questions.

**Case 2 — Overoptimistic forecast**
Input: 5 committed deals, 3 with no activity in 3+ weeks and no qualification data, close dates all end of quarter. Expected: 3 unsupported, scenario gap clearly shows $200K+ shortfall vs. rep forecast, pointed challenge questions.

## Related skills

- [Pipeline Hygiene Audit](/skills/05-sales-enablement/pipeline-hygiene-audit/SKILL.md)
- [Weekly Pipeline Report](/skills/05-sales-enablement/weekly-pipeline-report/SKILL.md)
- [Deal Review Facilitator](/skills/05-sales-enablement/deal-review-facilitator/SKILL.md)
- [Sales Experiment Designer](/skills/05-sales-enablement/sales-experiment-designer/SKILL.md)
