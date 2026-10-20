---
name: Weekly Pipeline Review
trigger: Weekly cadence (typically Monday morning or Friday end-of-week)
agents-involved:
  - Pipeline Analyst
  - Discovery and Deal Coach
  - Sales Enablement Agent
  - Orchestrator
approval-gates:
  - Green throughout (analysis and report preparation only)
output: Weekly pipeline summary with risk flags, forecast, and 1:1 prep notes
status: implemented
---

# Workflow: Weekly Pipeline Review

## Overview

A structured weekly review across all active opportunities. Produces a pipeline summary, identifies deals at risk, challenges forecast assumptions, and prepares manager coaching notes. Designed for a sales manager or AE doing a self-review. Inputs are supplied pipeline data — no direct CRM connection in MVP.

## Trigger condition

- Weekly recurring review (Monday or Friday)
- Pre-forecast call preparation
- New quarter starting

## Prerequisites

- Pipeline snapshot available (filled-in pipeline tracker template, exported CSV, or manual list)
- Prior week's review available for comparison (optional but improves quality)
- Team activity log available (optional)

---

## Steps

| # | Step | Agent | Gate |
|---|---|---|---|
| 1 | Run Pipeline Hygiene Audit across all open opportunities | Pipeline Analyst | Green |
| 2 | Produce weekly pipeline report (changes, risks, next steps) | Pipeline Analyst | Green |
| 3 | Challenge forecast confidence for current quarter | Pipeline Analyst | Green |
| 4 | Identify top 3 deals needing attention and why | Orchestrator | Green |
| 5 | Prepare Sales Manager 1:1 notes per rep (if applicable) | Sales Enablement Agent | Green |

---

## Approval gates

All steps are analysis only. The manager or rep reviews output before using it in meetings.

---

## Expected output

- Pipeline hygiene report (missing fields, stale deals, unrealistic close dates)
- Weekly pipeline summary (new, progressed, stalled, closed)
- Forecast challenge memo (assumptions, scenarios, risks)
- Top 3 deals needing attention with specific recommended actions
- 1:1 prep notes per rep (if team review)

---

## Failure handling

| Failure | Response |
|---|---|
| Pipeline data incomplete | Produce report with gaps marked; flag which deals lack sufficient data |
| No prior week data for comparison | Note absence; skip delta analysis; produce point-in-time report |
| Forecast data missing | Challenge what exists; flag that full forecast challenge requires complete data |

---

## Example

**Scenario:** Sales manager at Acme Corp prepares Friday pipeline review for a 3-AE team.

1. Hygiene audit: 2 deals missing close dates, 1 deal has had no activity in 21 days, 4 deals missing economic buyer identified.
2. Pipeline summary: 1 new deal (Meridian Logistics, inbound), 2 progressed (Northlight to Evaluation, Greenfield to Proposal), 1 stalled (Apex Industries, no response in 3 weeks).
3. Forecast challenge: Q4 commit = $480K. Challenge: Northlight close date optimistic (CFO gap). Realistic = $320K commit, $480K best case.
4. Top 3: (1) Northlight — CFO engagement needed this week, (2) Apex Industries — decide pursue or deprioritise, (3) Meridian Logistics — fast-track triage (high-intent inbound).
5. 1:1 prep: AE-1 (Northlight focus), AE-2 (Apex decision + Meridian handoff), AE-3 (pipeline building — low coverage).
