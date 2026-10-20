---
name: Account to Meeting
trigger: Account selected for outreach
agents-involved:
  - Account Intelligence Agent
  - Prospecting Agent
  - Outreach Agent
  - Orchestrator
approval-gates:
  - AMBER: Outreach message review before send
  - AMBER: Meeting booking confirmation before calendar invite
output: Approved outreach sent, meeting booked or follow-up sequence active
status: implemented
---

# Workflow: Account to Meeting

## Overview

This workflow takes a single target account and drives it from initial selection through fit assessment, account intelligence, signal review, approved outreach, and meeting booking preparation. It ends when an outreach message has been approved and sent (by the human), or when a meeting booking option has been presented for confirmation.

## Trigger condition

- A specific company name has been identified as a target account, OR
- An account has cleared the ICP Builder criteria in Group 1, OR
- A sales rep has decided to pursue an account from their territory plan

## Prerequisites

- Account name and at least one public data point (website, LinkedIn, news) available
- ICP criteria defined (use Skill: ICP Builder if not yet done)
- Human is available to review and approve outreach before sending

---

## Steps

| # | Step | Agent | Approval gate |
|---|---|---|---|
| 1 | Score account fit against ICP criteria | Account Intelligence Agent | Green |
| 2 | Identify likely buying committee roles | Account Intelligence Agent | Green |
| 3 | Build sourced one-page account brief | Account Intelligence Agent | Green |
| 4 | Aggregate available signals (hiring, funding, product changes) | Signal Monitor Agent | Green |
| 5 | Prioritise signal-to-action recommendation | Orchestrator | Green |
| 6 | Draft personalised first-touch outreach | Outreach Agent | **AMBER: Human reviews and edits before any send** |
| 7 | Prepare meeting booking options (times, format, agenda) | Outreach Agent | **AMBER: Human confirms before sending calendar invite** |

---

## Approval gates

| Gate | Action class | Who approves | What is reviewed |
|---|---|---|---|
| AMBER-1 (Step 6) | Outreach message send | Human sales rep | Relevance, tone, factual accuracy, personalisation quality |
| AMBER-2 (Step 7) | Calendar invitation send | Human sales rep | Meeting format, agenda, proposed times |

No message is sent and no calendar invite is created without explicit human approval. The Outreach Agent prepares drafts only.

---

## Expected output

- `templates/account-brief.md` completed for the target account
- Outreach draft ready for human approval (saved to working file)
- Meeting booking options document
- Signal summary with recommended next action

---

## Failure handling

| Failure | Response |
|---|---|
| Insufficient public data for account brief | Flag to human; proceed with partial brief; note gaps explicitly |
| Fit score below threshold | Present score with evidence; let human decide whether to proceed |
| No relevant signals found | Proceed without signal angle; note absence in outreach draft |
| Human declines outreach draft | Return to Outreach Agent with feedback; redraft once |

---

## Example

**Scenario:** Acme Corp (fictional B2B SaaS) is targeting Northlight Technologies (fictional 200-person logistics software company).

1. Account Intelligence Agent scores Northlight: fit 4/5 (strong ICP match — logistics sector, 150–300 employees, recent Series B).
2. Buyer committee mapped: VP Operations (economic buyer), Director of IT (technical influencer), Procurement (gatekeeper).
3. Account brief built: recent funding round ($12M Series B), new CTO hired 3 months ago, hiring 4 data engineers.
4. Signal Monitor identifies: CTO hire + data engineering hiring = active tech modernisation; funding announcement 8 weeks ago.
5. Orchestrator recommends: first touch to VP Operations, angle on operational efficiency during scale-up.
6. Outreach Agent drafts email to VP Operations — Amber gate. Human reviews, edits opening line, approves.
7. Meeting prep: 30-min discovery call options, draft agenda. Human confirms and sends.
