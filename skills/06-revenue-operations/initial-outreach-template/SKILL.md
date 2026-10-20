---
name: Initial Outreach Template
description: Generate a configurable first-touch outreach message for a specific role, context, and channel
group: "06 — Revenue Operations"
version: "1.0"
status: implemented
---


# Initial Outreach Template

## Purpose

Produce a first-touch outreach message (email, LinkedIn, or voice message script) configured for a specific prospect role, situation, and channel. The message must be relevant, low-hype, and written for human review before sending.

## When NOT to use

- When a follow-up message is needed (use Follow-up Sequence Template instead)
- When the prospect has already engaged (use Follow-up Sequence Builder, Group 3)
- When bulk-sending without personalisation (this skill produces individual or small-batch personalised messages)

## Required inputs

- `prospect_role`: the target's job title or function
- `company_context`: what is known about the target company (size, industry, recent signal if any)
- `channel`: `email` | `linkedin` | `voicemail`
- `sender_context`: who is sending and why (company, product, relevant angle)

## Optional inputs

- `trigger`: a specific buying signal or context (e.g., "just raised Series B", "recently hired 10 SDRs")
- `tone`: `formal` | `conversational` (default: `conversational`)
- `max_words`: word limit for the message (default: email=100 words, LinkedIn=80 words, voicemail=30 seconds)

## Step-by-step procedure

1. Identify the most relevant angle given `company_context` and `trigger`. If no trigger is available, use the most plausible reason someone in this role would care about the sender's offering.
2. Open with a specific, relevant observation — not a generic compliment.
3. Connect the observation to a problem the target role typically faces.
4. Introduce the sender's product or capability in one sentence. No feature list.
5. End with a low-commitment call to action: a question, not a meeting request.
6. Check the draft against the outreach compliance checklist (see Skill 69): ensure no deceptive claims, opt-out is respected, channel is appropriate.
7. Mark the draft clearly for human review before sending.

## Output contract

```
INITIAL OUTREACH — Email | VP of Sales | Northlight Technologies

Subject: SDR ramp times at companies scaling past 50 reps

Hi [First Name],

Saw that Northlight hired 12 SDRs last quarter — impressive growth. At that pace, onboarding and ramp time usually become the hidden bottleneck before the team starts hitting numbers.

Acme Corp [fictional sender] helps sales teams cut ramp time by structuring the first 60 days around real deal patterns rather than generic training content. One team we worked with went from 90-day ramp to 55 days after restructuring their playbook process.

Worth a 20-minute conversation to see if there's a fit?

— [Sender Name]

---
DRAFT — Review before sending. Do not send without human approval.
Word count: 92 | Channel: Email
```

## Evidence and citation rules

- Any specific metric in the message (e.g., "55-day ramp") must be replaced with a verified figure or removed before sending.
- Do not fabricate case studies. If no verified examples exist, remove the social proof element.
- Prospect observations must be based on supplied `company_context`, not invented.

## Confidence/uncertainty handling

- If `company_context` is minimal: draft a more generic version and flag: "Personalisation is limited — add a specific observation before sending."

## Safety, privacy, and compliance constraints

- Output is always marked as a draft requiring human review before sending.
- Do not include unverified metrics or fabricated customer references in the final message.
- Respect opt-out status if supplied. Do not draft a message to a prospect who has previously opted out.

## Human approval requirements

**This skill produces a draft message only. Human review and approval is required before sending.** No message is dispatched by this skill under any circumstances.

## Failure modes and fallback behaviour

- No `sender_context` supplied: return an error. The message cannot be written without knowing who is sending it.
- `channel` is not supported: default to `email` and note the fallback.

## Acceptance criteria

- Message fits within the `max_words` limit.
- Opens with a specific observation (not "I hope this finds you well").
- Ends with a low-commitment call to action.
- Explicitly marked as draft requiring human approval.

## Evaluation cases

**Case 1 — Email with a trigger**
Input: role=VP Sales, channel=email, trigger="recently hired 12 SDRs", sender_context="SDR onboarding platform". Expected: opening references the hiring, problem connects to ramp time, CTA is a question, marked as draft.

**Case 2 — LinkedIn, no trigger**
Input: role=Head of Revenue Operations, channel=linkedin, no trigger, sender_context="sales analytics tool". Expected: generic but relevant angle for RevOps, flagged as having limited personalisation, CTA appropriate for LinkedIn tone, within 80 words.

## Related skills

- [First Touch Draft](/skills/03-run-the-pipeline/first-touch-draft/SKILL.md)
- [Follow Up Sequence Template](/skills/06-revenue-operations/follow-up-sequence-template/SKILL.md)
- [Outreach Compliance Checklist](/skills/07-quality-and-safety/outreach-compliance-checklist/SKILL.md)
- [Personalised Outreach Planner](/skills/03-run-the-pipeline/personalised-outreach-planner/SKILL.md)
