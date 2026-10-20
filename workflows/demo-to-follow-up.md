---
name: Demo to Follow-up
trigger: Demo completed
agents-involved:
  - Discovery and Deal Coach
  - Outreach Agent
  - Pipeline Analyst
  - Orchestrator
approval-gates:
  - AMBER: Follow-up message approved before send
output: Structured follow-up package sent (after approval), mutual action plan drafted
status: implemented
---

# Workflow: Demo to Follow-up

## Overview

After a demo, momentum is everything. This workflow turns post-demo notes into a structured follow-up package: a call summary, confirmed next steps, a mutual action plan, and a follow-up message — all ready within hours. The follow-up is never sent autonomously; the rep reviews and approves.

## Trigger condition

- Demo has been completed
- Post-demo notes or verbal debrief available
- Rep wants to send a timely, structured follow-up

## Prerequisites

- Demo notes or debrief available (can be rough)
- Discovery notes and demo plan from prior workflow available (preferred)
- Human available to review and approve follow-up message

---

## Steps

| # | Step | Agent | Gate |
|---|---|---|---|
| 1 | Structure post-demo notes: reactions, questions, objections raised | Discovery and Deal Coach | Green |
| 2 | Update qualification scorecard with demo-stage learnings | Discovery and Deal Coach | Green |
| 3 | Draft mutual action plan (milestones, owners, dates, dependencies) | Discovery and Deal Coach | Green |
| 4 | Identify proposed next steps and decision timeline | Orchestrator | Green |
| 5 | Draft proposal outline if purchase discussion started | Discovery and Deal Coach | Green |
| 6 | Draft follow-up email: summary, next steps, mutual action plan | Outreach Agent | **AMBER: Rep reviews before send** |

---

## Approval gates

| Gate | Action | Who approves |
|---|---|---|
| AMBER-1 (Step 6) | Follow-up email send | Rep — reviews tone, accuracy of recap, mutual action plan |

---

## Expected output

- Updated discovery/qualification notes
- Mutual action plan (draft)
- Proposal outline (if applicable)
- Follow-up email ready for approval
- Updated pipeline stage recommendation

---

## Failure handling

| Failure | Response |
|---|---|
| Notes too sparse | Produce skeleton with placeholders; flag gaps for rep to fill |
| No clear next steps agreed in demo | Draft follow-up proposing next steps; flag that they weren't confirmed |
| Objections raised but unresolved | Include objection handling section in follow-up draft |

---

## Example

**Scenario:** Acme Corp demo to Northlight's VP Ops and CTO. Strong interest; CFO still not engaged.

1. Notes structured: positive reactions to data consolidation module; CTO raised security question (unanswered — needs follow-up); VP Ops confirmed Q1 target.
2. Qualification updated: Metrics confirmed, Champion strong, CFO still gap.
3. Mutual action plan: AE to send security FAQ by Day 3; Northlight IT to complete security review by Day 14; CFO briefing call Day 7.
4. Next step: CFO intro call + security review parallel track.
5. Proposal outline: not yet — pending CFO engagement.
6. Follow-up email draft: recap key demo points, thank CTO for security question (attach FAQ), propose CFO call options, attach mutual action plan. **AMBER gate** — rep edits CFO intro language, approves, sends.
