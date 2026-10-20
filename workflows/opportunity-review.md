---
name: Opportunity Review
trigger: Weekly or deal-stage change
agents-involved:
  - Pipeline Analyst
  - Discovery and Deal Coach
  - Orchestrator
approval-gates:
  - Green throughout (analysis and recommendations only)
output: Opportunity health assessment with risk flags and recommended next actions
status: implemented
---

# Workflow: Opportunity Review

## Overview

A structured review of a single open opportunity. Assesses deal health, identifies risks, checks qualification completeness, and recommends next actions — all from supplied pipeline data and notes. No CRM writes; analysis only.

## Trigger condition

- Weekly cadence for active opportunities
- Stage change (e.g., moved to Proposal/Evaluation)
- Manager requests deal review before forecast call
- Rep senses deal is stalling

## Prerequisites

- Opportunity record available (can be a filled-in template, not necessarily CRM export)
- Latest discovery/qualification notes available
- Deal history (previous interactions, emails, mutual action plan if exists)

---

## Steps

| # | Step | Agent | Gate |
|---|---|---|---|
| 1 | Review qualification completeness (framework-based) | Discovery and Deal Coach | Green |
| 2 | Run Opportunity Risk Review: gaps, blockers, unsupported optimism | Pipeline Analyst | Green |
| 3 | Check mutual action plan adherence (are milestones on track?) | Orchestrator | Green |
| 4 | Assess pipeline stage validity against evidence | Pipeline Analyst | Green |
| 5 | Generate next-best-action recommendations | Orchestrator | Green |
| 6 | Produce opportunity health summary | Pipeline Analyst | Green |

---

## Approval gates

All steps are analysis only. No external actions taken.

---

## Expected output

- Qualification completeness score with gap list
- Risk register for this opportunity (blockers, missing stakeholders, timeline risks)
- Pipeline stage validity assessment (correct / overstated / understated)
- Mutual action plan status
- Prioritised next 3 actions with rationale

---

## Failure handling

| Failure | Response |
|---|---|
| Insufficient data to assess | Produce partial report; flag specific data needed |
| Qualification framework not matched | Default to MEDDICC; note in output |
| Multiple conflicting signals | Present conflict explicitly; do not resolve unilaterally |

---

## Example

**Scenario:** Northlight Technologies opportunity, 6 weeks in, currently in "Evaluation" stage.

1. Qualification check: Metrics ✓, Economic Buyer (CFO) ✗ — gap, Decision Criteria ✓, Decision Process ✓, Champion ✓, Competition (incumbent named but not addressed).
2. Risks: CFO not engaged = high risk; incumbent not addressed = medium risk; Q1 close target requires legal sign-off which hasn't started.
3. MAP: AE sent security FAQ (done); CFO call not yet scheduled (overdue by 3 days); IT security review in progress.
4. Stage validity: "Evaluation" is accurate but close date of Q1 is optimistic without CFO engagement.
5. Next actions: (1) Schedule CFO call this week — highest priority, (2) Ask champion to arrange legal pre-read, (3) Prepare competitive differentiation talking points.
