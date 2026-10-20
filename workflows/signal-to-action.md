---
name: Signal to Action
trigger: Buying signal detected for a tracked account
agents-involved:
  - Signal Monitor Agent
  - Account Intelligence Agent
  - Outreach Agent
  - Orchestrator
approval-gates:
  - AMBER: Human approves recommended action before execution
output: Approved action taken or action deferred with documented rationale
status: implemented
---

# Workflow: Signal to Action

## Overview

When a buying signal arrives — a job change, funding announcement, hiring pattern, product launch, or other trigger — this workflow normalises it, assesses its relevance to the target account's fit profile, recommends a next action, and presents it for human approval before anything is sent or done externally.

## Trigger condition

- A signal event is detected for a tracked account (manual entry or configured monitoring)
- Signal types: job change at target account, funding round announced, relevant hiring pattern, product/technology change, competitor engagement news, content engagement data

## Prerequisites

- Account brief exists (or can be built inline)
- ICP criteria defined
- Signal source is lawful and authorised (not scraped against terms, not personal data beyond professional context)

---

## Steps

| # | Step | Agent | Gate |
|---|---|---|---|
| 1 | Receive and normalise signal (event, source, timestamp, confidence) | Signal Monitor Agent | Green |
| 2 | Score signal relevance, freshness, and urgency against account fit | Signal Monitor Agent | Green |
| 3 | Cross-reference with existing account brief | Account Intelligence Agent | Green |
| 4 | Generate signal-to-action recommendation (next action, angle, timing) | Orchestrator | Green |
| 5 | Draft proposed action (outreach message, research task, or hold) | Outreach Agent / Orchestrator | Green |
| 6 | Present recommendation + draft to human for approval | Orchestrator | **AMBER: Human approves before external action** |
| 7 | Execute approved action (human sends message, books call, etc.) | Human | Red: human executes |

---

## Approval gates

| Gate | Action | Who approves |
|---|---|---|
| AMBER-1 (Step 6) | Any external communication or follow-up outreach | Human sales rep |
| Red (Step 7) | Actual send / calendar / CRM update | Human only |

---

## Expected output

- Signal record with: event, source URL, access date, confidence score, relevance score
- Recommended action with rationale
- Draft message or action plan ready for human execution
- Signal logged to tracker

---

## Failure handling

| Failure | Response |
|---|---|
| Signal cannot be verified from source | Note confidence = low; do not act on unverified signal alone |
| Signal is stale (>30 days) | Flag freshness; let human decide whether still relevant |
| No clear action recommended | Present signal record with open question to human |
| Account brief outdated | Trigger partial account brief refresh before recommendation |

---

## Example

**Scenario:** Signal Monitor detects that Northlight Technologies' VP Operations has posted a job ad for a "Head of Supply Chain Operations" and the company has announced a new partnership with a logistics AI vendor.

1. Signal normalised: hiring signal (confidence: high, source: public job board), partnership announcement (source: press release).
2. Relevance: 4/5 — scale-up + new vendor signals active evaluation period.
3. Account brief cross-referenced: existing brief notes Series B + CTO hire. Buying window likely open.
4. Recommendation: reach out within 7 days; angle on consolidating tools during scale-up.
5. Draft: personalised follow-up to VP Operations referencing operational scale challenges.
6. **AMBER gate**: Human reviews — edits tone, approves message.
7. Human sends via their email client.
