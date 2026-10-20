# Discovery Question Generator Prompt

**Purpose:** Generate prioritised discovery questions for a specific pain area and prospect context.

**Inputs:**
- `{{pain_hypothesis}}` — the problem you think they have
- `{{prospect_role}}` — the role of the person you're speaking to
- `{{what_you_need_to_learn}}` — the 2–3 most important things to confirm or rule out

---

## Prompt template

```
Generate discovery questions for a sales call.

Context:
- Pain hypothesis: {{pain_hypothesis}}
- Prospect role: {{prospect_role}}
- Most important things to learn: {{what_you_need_to_learn}}

Generate:
1. **Current state questions** (2–3): Open questions to understand how they currently handle this area
2. **Problem confirmation questions** (2–3): Questions to confirm whether the pain hypothesis is real for them
3. **Impact questions** (2): Questions to understand the business impact of the problem
4. **Priority and urgency questions** (2): Questions to understand whether this is a current priority
5. **Decision process questions** (2): Questions to understand who else is involved and how decisions are made

Rules:
- All questions must be open (not yes/no)
- No leading questions (don't embed the answer)
- Order by learning value — most important first
- Do not include more than 11 questions total (you won't have time for all of them)
```

---

## Usage notes

- You will not use all questions in one call. Treat this as a prioritised list — pick the top 5–6.
- Follow the prospect's lead — if they volunteer information, skip the question that would have asked for it.
- The best discovery question is often a follow-up: "Tell me more about that."
