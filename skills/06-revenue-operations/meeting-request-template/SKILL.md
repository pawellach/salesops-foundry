---
name: Meeting Request Template
description: Generate a concise, relevant, permission-respecting meeting request for a specific prospect and context
group: "06 — Revenue Operations"
version: "1.0"
status: implemented
---


# Meeting Request Template

## Purpose

Produce a meeting request message (email or LinkedIn) that is concise, states a clear reason for the meeting, respects the prospect's time, and does not pressure or deceive. Produced as a draft for human review before sending.

## When NOT to use

- For initial cold outreach (use Initial Outreach Template instead)
- When a meeting has already been agreed (use Meeting Booking Preparation, Group 3)
- When the prospect has not previously engaged

## Required inputs

- `prospect_context`: who the prospect is and what prior interaction has occurred
- `meeting_purpose`: what the meeting is for (discovery, demo, follow-up, evaluation check-in)
- `sender_context`: who is sending and their relationship to the prospect

## Optional inputs

- `proposed_times`: 2–3 specific time slots to offer (recommended)
- `meeting_duration`: how long the meeting will take (default: 30 minutes)
- `channel`: `email` | `linkedin` (default: `email`)

## Step-by-step procedure

1. Reference the prior interaction or context that makes this meeting request relevant.
2. State the meeting purpose clearly in one sentence.
3. Articulate the value to the prospect: what will they get from attending?
4. Propose a specific duration and 2–3 time options (or offer a scheduling link if configured).
5. End with an easy opt-out: "If the timing doesn't work, happy to find another slot."
6. Keep the message under 100 words.
7. Mark as draft for human review.

## Output contract

```
MEETING REQUEST — Email | Post-Demo Follow-up

Subject: 30 minutes to review next steps — Northlight + Acme Corp

Hi [First Name],

Following our demo last week, I'd like to set aside 30 minutes to walk through your evaluation criteria and answer any outstanding questions before you present to your team.

Could any of these work for you?
- Tuesday 28 Oct, 10:00–10:30 CET
- Wednesday 29 Oct, 14:00–14:30 CET
- Thursday 30 Oct, 11:00–11:30 CET

If none of those work, happy to find something that does.

— [Sender Name]

---
DRAFT — Review before sending. Human approval required.
Word count: 84
```

## Evidence and citation rules

- The prior interaction referenced in the message must match `prospect_context`. Do not invent prior meetings.

## Confidence/uncertainty handling

- If `proposed_times` are not supplied, include a placeholder: "[Insert 2–3 time options or scheduling link]" rather than fabricating times.

## Safety, privacy, and compliance constraints

- Do not use manipulative urgency language ("respond today or lose your slot").
- Do not send — this is a draft requiring human approval.

## Human approval requirements

**Human review and approval required before sending.** No message is dispatched by this skill.

## Failure modes and fallback behaviour

- `prospect_context` is empty: return an error. A meeting request without context will be irrelevant.

## Acceptance criteria

- Under 100 words.
- States a clear meeting purpose.
- Includes time options or scheduling link placeholder.
- Includes easy opt-out phrasing.
- Marked as draft.

## Evaluation cases

**Case 1 — Post-demo follow-up**
Input: prospect_context="completed demo, evaluating 2 vendors", meeting_purpose="evaluation review", proposed_times=3 slots. Expected: references the demo, states purpose, includes all 3 slots, soft opt-out, under 100 words.

**Case 2 — No proposed times**
Input: meeting_purpose="discovery call", no proposed_times. Expected: message with placeholder for times rather than fabricated slots.

## Related skills

- [Initial Outreach Template](/skills/06-revenue-operations/initial-outreach-template/SKILL.md)
- [Meeting Booking Preparation](/skills/03-run-the-pipeline/meeting-booking-preparation/SKILL.md)
- [Follow Up Sequence Template](/skills/06-revenue-operations/follow-up-sequence-template/SKILL.md)
