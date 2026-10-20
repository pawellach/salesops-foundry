---
name: Meeting Booking Preparation
description: Prepare scheduling options and a meeting request draft — never books a meeting without human action.
group: "03 — Run the Pipeline"
version: "1.0"
status: implemented
---

# Meeting Booking Preparation

## Purpose
After a prospect expresses interest, prepare a concise meeting request including scheduling options, a brief agenda, and any pre-meeting preparation notes. This skill produces materials for the seller to use; it does not book, calendar-invite, or confirm the meeting.

## When NOT to use
- Before the prospect has expressed interest in a meeting.
- When the seller has not confirmed their own availability.
- As an automated booking flow without human involvement.

## Required inputs
- Prospect's expressed interest (reply text or verbal confirmation, paraphrased).
- Meeting type: discovery call, demo, check-in, etc.
- Seller's available time slots (seller-supplied; do not invent).
- Channel for the request: email or calendar link.

## Optional inputs
- Account Brief and outreach plan (for agenda context).
- Meeting duration preference (default: 30 minutes for discovery, 45 for demo).
- Any special logistics (time zone, video platform preference).

## Step-by-step procedure

1. **Confirm the context.** State what triggered this booking request (e.g., "prospect replied positively to Touch 1").
2. **Define the meeting objective.** One sentence: what both parties will get from the meeting.
3. **Prepare the agenda.** 2–3 points maximum. Frame as questions or topics, not a sales pitch.
4. **List the seller's available slots.** Use exactly the slots the seller supplied. Do not invent slots.
5. **Draft the meeting request message.** Short (60–80 words), includes the objective, 2–3 available slots or a calendar link placeholder, and a gentle ask.
6. **Note pre-meeting preparation.** What the seller should review before the call (account brief, recent signals, etc.).

## Output contract

```markdown
## Meeting Booking Preparation — Sarah Okafor / Northlight Technologies
Meeting type: Discovery call (30 min)
Date: YYYY-MM-DD

**Meeting objective:** Understand Northlight's current pipeline review process and whether there is a fit worth exploring further.

**Suggested agenda:**
1. How does Northlight currently run pipeline reviews?
2. What are the biggest challenges as the team scales?
3. Is there anything specific that prompted the response to my note?

**Available slots (seller-supplied):**
- Tuesday 22 Oct, 10:00–12:00 BST
- Wednesday 23 Oct, 14:00–16:00 BST
- Thursday 24 Oct, 09:00–10:30 BST

---
### Meeting request draft (email)
Subject: Discovery call — two options this week

Hi Sarah,

Thanks for replying — great to hear from you. Would either of these work for a 30-minute call?

- Tue 22 Oct, 10:00 BST
- Wed 23 Oct, 14:00 BST

If neither works, feel free to grab a slot here: [CALENDAR LINK — seller to insert]

Looking forward to it.

[Seller name]

---
### Pre-meeting notes for seller
- Review account brief (latest update: YYYY-MM-DD)
- Check if any new signals since brief was built
- Prepare 2–3 hypothesis questions based on Series B context
```

## Evidence and citation rules
- Agenda is derived from the account brief and outreach context; do not invent topics.
- Available slots must be seller-supplied; never fabricate availability.

## Confidence/uncertainty handling
- If the prospect's interest is ambiguous, note this and recommend confirming before sending the request.

## Safety, privacy, and compliance constraints
- Do not include calendar integration that books without human confirmation.
- Do not share the seller's full calendar or internal scheduling system details.
- Calendar links are placeholders; the seller inserts their own tool.

## Human approval requirements
**No meeting is booked by this skill.** The seller reviews the draft, inserts the calendar link, and sends the request. Confirmation of the meeting happens between the two humans.

## Failure modes and fallback behaviour
- **No available slots supplied:** Return an error; do not invent times.
- **Prospect interest is ambiguous:** Flag it; do not assume a meeting is wanted.

## Acceptance criteria
- Agenda is 2–3 points maximum.
- Available slots come from seller-supplied input only.
- Draft is ≤100 words.
- No meeting is booked; draft only.

## Evaluation cases

**Case 1 — Standard discovery booking.**
Input: Prospect replied positively; seller has 3 slots available; discovery call, 30 min.
Expected: Agenda with 2–3 hypothesis questions; meeting request draft with exactly the supplied slots; pre-meeting notes.

**Case 2 — No slots supplied.**
Input: Seller forgot to provide availability.
Expected: Error returned — "Available slots not supplied; cannot generate booking materials."

## Related skills
- [First-Touch Draft](/skills/03-run-the-pipeline/first-touch-draft/SKILL.md) — the outreach that prompted the reply.
- [Discovery Call Plan](/skills/04-discovery-and-deals/discovery-call-plan/SKILL.md) — next step: preparing for the actual call.
- [Account Brief Builder](/skills/02-account-intelligence/account-brief-builder/SKILL.md) — pre-meeting context.
