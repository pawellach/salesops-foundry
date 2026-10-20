---
name: Discovery to Demo
trigger: Discovery call completed and demo requested or agreed
agents-involved:
  - Discovery and Deal Coach
  - Account Intelligence Agent
  - Orchestrator
approval-gates:
  - Green throughout (preparation only; no external actions)
output: Demo-ready plan with confirmed needs, stakeholder map, and storyline
status: implemented
---

# Workflow: Discovery to Demo

## Overview

**Prerequisite:** Use the [Discovery Call playbook](../playbooks/discovery-call.md) to prepare and run the call first — this workflow processes the output of that call.

After a discovery call, this workflow transforms raw notes and observations into a structured demo plan. It organises what was learned, identifies what is still missing, maps the buying committee, and builds a demo storyline grounded in confirmed needs — not assumptions. No external actions are taken; this is a preparation workflow.

## Trigger condition

- Discovery call has been completed and notes/transcript are available
- Demo has been requested or agreed with the prospect
- AE wants to prepare a tailored, evidence-based demonstration

## Prerequisites

- Discovery call notes or transcript available (can be rough notes)
- Account brief exists or can be built inline
- Demo has been agreed within a reasonable timeframe (not yet booked is fine)

---

## Steps

| # | Step | Agent | Gate |
|---|---|---|---|
| 1 | Structure discovery notes into canonical format | Discovery and Deal Coach | Green |
| 2 | Map stated pain vs. inferred impact | Discovery and Deal Coach | Green |
| 3 | Apply qualification framework (MEDDICC / SPICED / BANT — configurable) | Discovery and Deal Coach | Green |
| 4 | Identify gaps: missing stakeholders, unconfirmed criteria, unanswered questions | Discovery and Deal Coach | Green |
| 5 | Update buyer committee map with discovery learnings | Account Intelligence Agent | Green |
| 6 | Run Demo Readiness Review — flag blockers | Discovery and Deal Coach | Green |
| 7 | Build demo storyline connecting capabilities to confirmed needs | Discovery and Deal Coach | Green |

---

## Approval gates

No external actions in this workflow. All steps are preparation only and do not require human approval before execution. The AE reviews the output before using it.

---

## Expected output

- Structured discovery notes (canonical format)
- Pain and impact map
- Qualification scorecard (configurable framework)
- Gap list with recommended follow-up questions
- Updated buyer committee map
- Demo readiness assessment (blockers listed)
- Demo storyline document

---

## Failure handling

| Failure | Response |
|---|---|
| Notes too sparse to structure | Flag gaps; produce partial output; list what needs to be confirmed |
| Qualification framework not configured | Default to MEDDICC; flag that framework can be changed |
| Demo readiness review flags critical blocker | Surface blocker prominently; recommend addressing before booking demo |
| Conflicting information in notes | Flag contradiction; do not resolve — present both versions for AE to clarify |

---

## Example

**Scenario:** AE at Acme Corp completes a 45-minute discovery call with Northlight Technologies' VP Operations and CTO.

1. Notes structured: pain = "manual reconciliation of freight data across 3 systems takes 2 FTEs weekly"; timeline = "want something live before Q1".
2. Pain mapped: stated pain (manual reconciliation) → inferred impact (operational cost, error rate, delayed reporting).
3. MEDDICC applied: Metrics (2 FTE cost confirmed), Economic Buyer (CFO not yet spoken to — gap), Decision Criteria (TBD), Decision Process (IT review required), Identify Pain (confirmed), Champion (VP Ops, engaged), Competition (one incumbent named).
4. Gaps: CFO not engaged, security review process unknown.
5. Buyer map updated: VP Ops (champion), CTO (technical), CFO (economic buyer — not yet engaged), IT Security (gatekeeper).
6. Demo readiness: CFO engagement missing = moderate risk; recommend pre-demo CFO intro.
7. Demo storyline: open with freight reconciliation time-cost frame → show automated data consolidation → close with Q1 deployment timeline.
