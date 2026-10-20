---
name: Follow-up Sequence Template
description: Build a configurable multi-touch follow-up sequence with cadence, stop conditions, and opt-out respect
group: "06 — Revenue Operations"
version: "1.0"
status: implemented
---


# Follow-up Sequence Template

## Purpose

Generate a bounded, configurable follow-up sequence for a specific prospect context — with a defined number of touches, channel mix, timing, stop rules, and an opt-out statement in every message. The sequence is produced as a draft for human review.

## When NOT to use

- For a first-touch message (use Initial Outreach Template instead)
- For a post-demo structured follow-up (use Follow-up Sequence Builder, Group 3)
- When the prospect has previously asked not to be contacted

## Required inputs

- `prospect_context`: who the prospect is and what stage they are at
- `sequence_goal`: what the sequence is trying to achieve (e.g., book a meeting, re-engage after going dark)

## Optional inputs

- `num_touches`: number of messages in the sequence (default: 3, max: 5)
- `cadence_days`: days between touches (default: [3, 5, 7])
- `channels`: list of channels to use (default: `["email", "email", "linkedin"]`)
- `value_angles`: different value angles to vary across touches

## Step-by-step procedure

1. Plan the sequence structure: number of touches, timing, channels.
2. For each touch, select a distinct angle (do not repeat the same ask):
   - Touch 1: relevant observation + initial ask
   - Touch 2: different angle or piece of value (resource, insight, question)
   - Touch 3: low-pressure "last try" with easy opt-out
3. Draft each message. Keep each under 80 words.
4. Include an opt-out option in every email: "If this isn't relevant, just let me know and I won't reach out again."
5. Define stop conditions: stop if prospect replies (positive or negative), stop after final touch, stop if prospect opts out.
6. Mark entire sequence as draft for human review.

## Output contract

```
FOLLOW-UP SEQUENCE — Re-engage after going dark
Prospect: VP Sales, Northlight Technologies | Goal: Book a discovery call
Touches: 3 | Cadence: Day 0, Day 3, Day 8

TOUCH 1 (Day 0) — Email
Subject: Quick question about SDR ramp at Northlight

Hi [First Name], I noticed Northlight has been scaling its SDR team — curious whether ramp time has become a priority this quarter.
Happy to share what we've seen work at similar companies in 20 minutes.
If this isn't a fit, no worries at all — just let me know.
— [Sender]

TOUCH 2 (Day 3) — Email
Subject: One thing that helped a team scale from 10 to 40 reps

Hi [First Name], in case it's useful — we put together a short guide on SDR onboarding structure based on what worked across 15 scaling teams. Happy to send it over.
Still happy to chat if timing is right.
— [Sender]

TOUCH 3 (Day 8) — LinkedIn
Message: Hi [First Name] — this is my last note on this topic. If SDR ramp isn't a priority right now, completely understand. Feel free to reach out when the timing changes.

STOP CONDITIONS:
- Stop immediately if prospect replies (positive or negative)
- Stop immediately if prospect opts out
- Sequence ends after Touch 3 regardless of outcome

---
DRAFT — Human review required before sending any message.
```

## Evidence and citation rules

- "What we've seen work at similar companies" must be replaced with a verified reference or removed before sending.
- Do not fabricate case studies or statistics.

## Confidence/uncertainty handling

- If `value_angles` are not supplied, use generic angles and flag: "Add specific value angles before sending."

## Safety, privacy, and compliance constraints

- Every email must include an opt-out option.
- Sequence must stop upon opt-out with no further messages.
- Sequence ends after the defined number of touches — do not continue indefinitely.
- Do not send — draft only, requires human approval.

## Human approval requirements

**Every message in the sequence requires human review before sending.** The sequence is a draft. Human decides when and whether to send each touch.

## Failure modes and fallback behaviour

- `num_touches` > 5: cap at 5 and note the override.
- `prospect_context` empty: return an error.

## Acceptance criteria

- Each touch has a distinct angle.
- Every email includes an opt-out option.
- Stop conditions clearly defined.
- Each message under 80 words.
- Marked as draft.

## Evaluation cases

**Case 1 — Standard 3-touch re-engagement**
Input: prospect_context="went dark after demo", sequence_goal="re-engage", 3 touches, email+email+linkedin. Expected: 3 distinct angles, opt-out in both emails, stop conditions defined, all under 80 words.

**Case 2 — Too many touches requested**
Input: num_touches=8. Expected: capped at 5 with a note, sequence generated for 5 touches.

## Related skills

- [Initial Outreach Template](/skills/06-revenue-operations/initial-outreach-template/SKILL.md)
- [Follow Up Sequence Builder](/skills/03-run-the-pipeline/follow-up-sequence-builder/SKILL.md)
- [Outreach Compliance Checklist](/skills/07-quality-and-safety/outreach-compliance-checklist/SKILL.md)
- [Meeting Request Template](/skills/06-revenue-operations/meeting-request-template/SKILL.md)
