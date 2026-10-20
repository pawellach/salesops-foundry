---
name: Discovery Question Planner
description: Generate a prioritised set of discovery questions ordered by learning value for a specific account and hypothesis.
group: "04 — Discovery, Demos, and Deal Progression"
version: "1.0"
status: implemented
---

# Discovery Question Planner

## Purpose
Build a set of discovery questions tailored to a specific account, contact, and hypothesis. Order the questions by what you most need to learn, not by what is easiest to ask.

## When NOT to use
- Without a hypothesis about the prospect's situation — generic question lists belong in the Playbook, not here.
- As a script to read verbatim; questions are a starting point for a real conversation.
- After a discovery call has already been completed (use Call Notes Structurer instead).

## Required inputs
- Account Brief (from Skill 11) or equivalent context.
- Your current hypothesis about the prospect's problem or situation.
- Call objective (e.g., "confirm pain, identify economic buyer, understand decision process").

## Optional inputs
- Prior interaction notes.
- Qualification framework (MEDDICC, SPICED, or BANT — from Skill 35).
- Known signals (from Skill 19).

## Step-by-step procedure

1. **State the hypothesis.** Write out your current belief about the prospect's situation in one sentence. This is what you are testing.
2. **Identify what you most need to learn.** List 3–5 "must-know" facts that would either confirm or reject the hypothesis, change the deal strategy, or reveal a showstopper.
3. **Generate questions for each must-know.** For each, write: one open question, one follow-up if the first gets a vague answer, and one challenging question if you need to dig.
4. **Order by learning value.** Most important unknown = first question. Do not start with company background questions that the brief already answers.
5. **Add stakeholder-mapping questions.** At least one question to identify other decision-makers.
6. **Add a hypothesis-testing question.** One question that would falsify your hypothesis if answered in a certain way.
7. **Flag questions that may feel sensitive.** Budget and authority questions can feel intrusive; note how to frame them.

## Output contract

```markdown
## Discovery Question Plan — Sarah Okafor / Northlight Technologies
Date: YYYY-MM-DD
Hypothesis: Post-Series B scaling is creating pipeline visibility problems as the AE team grows.

### Must-know facts
1. Whether pipeline visibility is actually a felt pain (not just an assumption)
2. Who owns the decision to buy new tooling
3. What they are currently using and why it is or is not working
4. Whether there is a budget and timeline

### Ordered questions

**Question 1 — Test the hypothesis**
"As you scale the team post-funding, what's your biggest challenge in keeping visibility across the whole pipeline?"
*Follow-up:* "What does that actually cost you — in time or missed deals?"
*Hypothesis falsifier:* If Sarah says "Pipeline visibility is not a challenge — we have a great system," deprioritise this angle.

**Question 2 — Current state**
"Walk me through how you currently run your weekly pipeline review."
*Follow-up:* "What do you wish was different about that process?"

**Question 3 — Stakeholder mapping**
"Who else would be involved in evaluating a tool like this — is it just you, or would finance or the CEO weigh in?"
*Note:* Frame naturally after building rapport; don't make it feel like a qualification trap.

**Question 4 — Budget signal**
"Do you have a rough sense of what you'd be willing to invest to solve this? Even a range helps me understand what's realistic."
*Note:* Ask only after confirming pain; position as helping you tailor the conversation.

**Question 5 — Timeline**
"Is there a point in the next quarter where this needs to be solved — a hiring milestone, a board review, anything like that?"
```

## Evidence and citation rules
- Questions must reference the account's specific context from the brief, not generic industry facts.
- Hypothesis must be stated explicitly so you know what you are testing.

## Confidence/uncertainty handling
- Label the hypothesis as a hypothesis. If the first question falsifies it, pivot.
- Do not stick to the question plan if the conversation reveals a different and more important problem.

## Safety, privacy, and compliance constraints
- Do not ask questions designed to extract confidential competitor information.
- Do not ask about personal financial circumstances of the contact.

## Human approval requirements
**The question plan is a preparation tool.** No question is asked without a human conducting the conversation. This skill does not automate calls or interviews.

## Failure modes and fallback behaviour
- **No account brief available:** Generate a generic question set and flag that it lacks personalisation.
- **Hypothesis is too vague:** Ask the seller to sharpen it before generating questions.

## Acceptance criteria
- At least 4 questions, each with a follow-up.
- Questions are ordered by learning value, not ease.
- A hypothesis-falsifying question is present.
- At least one stakeholder-mapping question included.

## Evaluation cases

**Case 1 — Hypothesis-driven questions.**
Input: Brief for Northlight; hypothesis about pipeline visibility pain post-Series B.
Expected: First question tests hypothesis; follow-up digs for evidence; falsifier question present; stakeholder question present.

**Case 2 — No brief, generic account.**
Input: Account name only; no brief; hypothesis = "they may have data quality issues."
Expected: Generic questions generated; output flagged as low-personalisation; recommendation to complete account brief first.

## Related skills
- [Account Brief Builder](/skills/02-account-intelligence/account-brief-builder/SKILL.md) — provides account context.
- [Discovery Call Plan](/skills/04-discovery-and-deals/discovery-call-plan/SKILL.md) — full call plan using these questions.
- [Qualification Framework Mapper](/skills/04-discovery-and-deals/qualification-framework-mapper/SKILL.md) — structures qualification dimensions.
