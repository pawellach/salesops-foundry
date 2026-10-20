---
name: Follow-up Sequence Builder
description: Draft a bounded follow-up sequence with stop rules, opt-out respect, and diminishing frequency — never sends autonomously.
group: "03 — Run the Pipeline"
version: "1.0"
status: implemented
---

# Follow-up Sequence Builder

## Purpose
After a first-touch message receives no reply, create a short, bounded sequence of follow-up drafts with clear stop rules. Each follow-up adds new value or varies the angle; none repeats the previous message.

## When NOT to use
- Before the first-touch message has been sent and the no-reply window has elapsed.
- When the contact has replied (even negatively) — use a different response approach.
- When the contact has unsubscribed, opted out, or marked a message as spam.
- For sequences longer than 3 follow-ups; beyond that, the account should be deprioritised.

## Required inputs
- First-touch draft and its outreach plan.
- Channel: email or LinkedIn.
- No-reply wait period (default: 5 business days between touches).
- Maximum number of follow-ups (default: 3; maximum: 4).

## Optional inputs
- Additional value angles (new signals, relevant content, peer reference, event invitation).
- Preferred tone and word-count target.

## Step-by-step procedure

1. **Review the first-touch.** Note the angle used. Each follow-up must use a different angle or add new context.
2. **Plan the sequence.** Define the number of touches, the angle for each, and the wait period. Default: Touch 2 at T+5 days, Touch 3 at T+10 days, Touch 4 (final) at T+18 days.
3. **Draft Touch 2.** Different angle or new information. Shorter than Touch 1. Ends with a lower-commitment ask or an easy out ("If this isn't a priority right now, just let me know").
4. **Draft Touch 3.** Brief. One sentence of new value. Clear easy-out.
5. **Draft Touch 4 (final, if included).** "Break-up" format. Acknowledge silence. Remove them from follow-up without guilt.
6. **Define stop rules explicitly:** (a) Any reply from the contact stops the sequence; (b) any opt-out or unsubscribe stops the sequence permanently; (c) if the account enters an active sales cycle, stop cold outreach.
7. **Flag unverified elements** in each draft as in Skill 25.

## Output contract

```markdown
## Follow-up Sequence — Sarah Okafor / Northlight Technologies
Channel: Email | No-reply window: 5 business days
Date built: YYYY-MM-DD

**Stop rules:**
- Any reply → stop sequence immediately
- Any opt-out/unsubscribe → stop permanently; flag in CRM
- Account enters active deal → stop cold outreach

---
### Touch 2 — T+5 business days
Subject: Quick follow-up on pipeline visibility

Hi Sarah,

I wanted to follow up briefly. I know post-Series B the priorities pile up fast.

One thing we've seen with similar-stage teams: as headcount grows, deal review quality often drops — more deals, same time. Happy to share how others have handled it if it's relevant.

Worth a 15-minute chat?

[Seller name]

*Review note: "similar-stage teams" — verify AE count assumption before sending.*

---
### Touch 3 — T+10 business days
Subject: One more thought

Hi Sarah,

Last note, I promise. If pipeline visibility isn't a current challenge for Northlight, totally understand — not every tool is the right fit at every stage.

If it ever becomes relevant, you know where to find me.

[Seller name]

---
### Touch 4 (Final) — T+18 business days
Subject: Closing the loop

Hi Sarah,

I'll stop reaching out after this — I don't want to be a nuisance. If the timing is ever right, feel free to pick this back up.

Good luck with the scale-up.

[Seller name]
```

## Evidence and citation rules
- Each touch that references a new fact must have that fact sourced.
- Do not invent new signals to freshen a touch; use only supplied or verifiable information.

## Confidence/uncertainty handling
- If no new angle is available for Touch 2 or 3, flag this and recommend sending fewer touches rather than repeating the same point.

## Safety, privacy, and compliance constraints
- Maximum sequence length is 4 touches (including first-touch = 5 total contacts). Do not generate longer sequences.
- An opt-out must immediately and permanently stop the sequence. This is non-negotiable.
- Do not produce "stealth" follow-ups that disguise their commercial intent.
- Sequences are drafts only; sender is responsible for compliance with CAN-SPAM, GDPR, CASL, and other applicable laws.

## Human approval requirements
**This skill NEVER sends messages.** Each touch in the sequence is a draft for the seller to review and send individually. The seller must verify each message, check stop rules, and send manually or via an approved tool.

## Failure modes and fallback behaviour
- **Contact opted out:** Do not produce a sequence; flag immediately.
- **No new angles available:** Produce a 2-touch sequence (not 3–4) and note the limitation.
- **First-touch missing:** Return an error; do not generate follow-ups without context.

## Acceptance criteria
- Maximum 4 follow-up drafts (beyond first-touch).
- Stop rules are explicit and listed at the top.
- Each touch has a different angle or adds new value.
- Final touch is a clear "break-up" message.
- No messages are sent; drafts only.

## Evaluation cases

**Case 1 — Standard 3-touch sequence.**
Input: First-touch used Series B angle; email channel; 5-day window; 3 follow-ups requested.
Expected: Touch 2 uses a different angle; Touch 3 is short with an easy out; Touch 4 is a break-up; stop rules listed.

**Case 2 — Opt-out detected.**
Input: Contact has unsubscribed from previous campaign.
Expected: No sequence generated; output = "Contact has opted out — sequence cannot be created."

## Related skills
- [First-Touch Draft](/skills/03-run-the-pipeline/first-touch-draft/SKILL.md) — prerequisite.
- [Outreach Compliance Checklist](/skills/07-quality-and-safety/outreach-compliance-checklist/SKILL.md) — compliance review.
- [Pipeline Stage Recommendation](/skills/03-run-the-pipeline/pipeline-stage-recommendation/SKILL.md) — if a reply is received.
