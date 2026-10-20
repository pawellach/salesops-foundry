---
name: Inbound Lead Triage
trigger: New inbound lead received
agents-involved:
  - Prospecting Agent
  - Account Intelligence Agent
  - Outreach Agent
  - Orchestrator
approval-gates:
  - AMBER: Lead routing recommendation confirmed by human
  - AMBER: First-touch response approved before send
output: Lead scored, routed, and first response approved
status: implemented
---

# Workflow: Inbound Lead Triage

## Overview

When a new lead arrives — form submission, email inquiry, event follow-up, or referral — this workflow classifies it, scores it against the ICP, identifies the right owner, and prepares a first-touch response for human approval. It does not route or respond autonomously.

## Trigger condition

- Inbound form submission received
- Email inquiry from a potential buyer
- Event or conference lead (business card, badge scan, list)
- Referral from existing customer or partner

## Prerequisites

- ICP criteria defined
- Lead routing rules defined (optional — workflow proceeds without them but flags the gap)
- Human available to confirm routing and approve response

---

## Steps

| # | Step | Agent | Gate |
|---|---|---|---|
| 1 | Classify lead: source, intent signals, data completeness | Prospecting Agent | Green |
| 2 | Flag missing information (email, company, role, use case) | Orchestrator | Green |
| 3 | Score lead against ICP (firmographic, situational fit) | Account Intelligence Agent | Green |
| 4 | Research company if score ≥3/5 (brief account context) | Account Intelligence Agent | Green |
| 5 | Recommend routing: which team member / queue | Orchestrator | **AMBER: Human confirms routing** |
| 6 | Draft first-touch response (personalised to lead context) | Outreach Agent | **AMBER: Human approves before send** |

---

## Approval gates

| Gate | Action | Who approves |
|---|---|---|
| AMBER-1 (Step 5) | Lead assignment to team member | Sales manager or lead owner |
| AMBER-2 (Step 6) | First-touch reply or follow-up message | Assigned rep |

---

## Expected output

- Lead classification record (source, intent, data completeness)
- ICP fit score with evidence
- Routing recommendation with rationale
- Draft first response ready for approval
- Flag list of missing data to gather

---

## Failure handling

| Failure | Response |
|---|---|
| Lead has no company or role data | Score as incomplete; flag for human enrichment before routing |
| Lead is clearly outside ICP | Present score evidence; recommend disqualify but let human decide |
| Routing rules not defined | Flag gap; present options based on available context |
| Duplicate lead detected | Flag possible duplicate; do not create two records |

---

## Example

**Scenario:** Meridian Logistics (fictional freight company, 400 employees) submits a demo request form. Contact: Jamie Okafor, Head of Logistics Technology.

1. Lead classified: demo request, high intent, complete data.
2. No missing fields — company, role, email, use case all present.
3. ICP score: 5/5 — logistics sector, right size, decision-maker title.
4. Account brief pulled: Meridian is in active digital transformation, no known incumbent vendor.
5. Routing recommended: assign to Senior AE (logistics vertical). **AMBER gate** — manager confirms.
6. First-touch draft: acknowledges demo request, confirms 30-min slot availability, references Meridian's logistics context. **AMBER gate** — AE reviews and sends.
