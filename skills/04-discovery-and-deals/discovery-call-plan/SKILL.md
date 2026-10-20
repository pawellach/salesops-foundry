---
name: Discovery Call Plan
description: Build a complete discovery call plan: objectives, hypotheses, time allocation, questions, and post-call commitments.
group: "04 — Discovery, Demos, and Deal Progression"
version: "1.0"
status: implemented
---

# Discovery Call Plan

## Purpose
Prepare a structured, time-allocated discovery call plan that gives the seller a clear objective, prioritised questions, a logical flow, and a defined next-step ask to close the call.

## When NOT to use
- For calls that are not discovery in nature (demos, check-ins, negotiations — use appropriate skills).
- As a substitute for reading the account brief before the call.

## Required inputs
- Discovery question plan (from Skill 31) or a list of questions.
- Call duration (default: 30 minutes).
- Seller's primary objective for this call.
- Contact name and role.

## Optional inputs
- Account Brief.
- Prior interaction notes.
- Any pre-call research or signals.

## Step-by-step procedure

1. **State the primary objective.** One sentence: what must happen for this call to be a success?
2. **State the secondary objective.** What would make this call excellent, beyond the minimum?
3. **Allocate time.** For a 30-minute call: 2 min rapport, 3 min agenda-setting, 15 min discovery questions, 5 min solution hypothesis / mutual understanding, 5 min next steps.
4. **Select top 3 questions.** From the question plan, identify the 3 questions you must ask. List them in order.
5. **Plan the agenda statement.** One or two sentences to open the call that sets expectations and shows respect for the contact's time.
6. **Define the next-step ask.** What specific commitment will you ask for at the end? (e.g., "Book a follow-up demo", "Introduce us to your CFO", "Send over your current tool contract for comparison").
7. **List what you will NOT do on this call.** This keeps scope clear.
8. **Produce call plan document.**

## Output contract

```markdown
## Discovery Call Plan — Sarah Okafor / Northlight Technologies
Date: YYYY-MM-DD | Duration: 30 min

**Primary objective:** Confirm pipeline visibility is a top-3 priority and identify the economic buyer.
**Secondary objective:** Understand current tooling and what "good" looks like for them.

### Time allocation
| Segment | Time | Notes |
|---|---|---|
| Rapport | 2 min | Reference shared context (Series B congratulations) |
| Agenda setting | 3 min | See agenda statement below |
| Discovery questions | 15 min | Top 3 questions + follow-ups |
| Solution hypothesis | 5 min | If pain confirmed, share one-sentence hypothesis about fit |
| Next steps | 5 min | Ask for the commit |

### Agenda statement (to read/paraphrase at call start)
"Thanks for making time, Sarah. I want to make sure this is useful for you, not just for me. I'd like to spend the first half understanding your pipeline review process today, and then if it makes sense, I'll share why we've been working with similar-stage companies. And I'd like to leave time at the end to agree a clear next step — does that work?"

### Top 3 questions
1. "As you scale post-funding, what's your biggest challenge in keeping visibility across the whole pipeline?" → *Follow-up: What does that cost you?*
2. "Walk me through how you currently run your weekly pipeline review." → *Follow-up: What would you change?*
3. "Who else would be involved in evaluating a tool like this?" → *Frame: 'I want to make sure I'm involving the right people from the start.'*

### Next-step ask
"Would it make sense for me to come back with a more tailored walkthrough — and could we include [economic buyer name if known] in that conversation?"

### What I will NOT do on this call
- Pitch features
- Discuss pricing
- Assume pain before it is confirmed
```

## Evidence and citation rules
- Agenda statement and questions must reflect the actual account context, not generic language.

## Confidence/uncertainty handling
- If hypothesis is weak, note it in the plan and use a more exploratory opening question.

## Safety, privacy, and compliance constraints
- Do not record calls without the contact's knowledge and consent.
- Do not share call plan content with the prospect before the call.

## Human approval requirements
**The call is conducted by a human.** This plan is a preparation tool, not a script. The seller adapts it in real time based on the actual conversation.

## Failure modes and fallback behaviour
- **No question plan supplied:** Generate a basic call plan with generic discovery questions and flag it.
- **Call duration under 15 minutes:** Compress to 1 primary objective and 2 questions only.

## Acceptance criteria
- Primary objective is stated.
- Time allocation sums to the call duration.
- At least 3 questions listed with follow-ups.
- Next-step ask is specific.
- "Will NOT do" list is present.

## Evaluation cases

**Case 1 — Standard 30-min discovery.**
Input: 30 min call; objective = confirm pain and find economic buyer; 5 questions from Question Planner.
Expected: Time allocation for 30 min; top 3 questions selected; agenda statement; specific next-step ask.

**Case 2 — Short call (15 min).**
Input: 15-min introductory call; minimal account context.
Expected: Compressed plan with 1 objective, 2 questions, 2-minute next-step ask; flag that context is thin.

## Related skills
- [Discovery Question Planner](/skills/04-discovery-and-deals/discovery-question-planner/SKILL.md) — questions input.
- [Call Notes Structurer](/skills/04-discovery-and-deals/call-notes-structurer/SKILL.md) — post-call.
- [Meeting Booking Preparation](/skills/03-run-the-pipeline/meeting-booking-preparation/SKILL.md) — booked the call.
