# Pain and Impact Mapper Prompt

**Purpose:** Transform raw discovery notes into a structured pain and impact map.

**Inputs:**
- `{{discovery_notes}}` — your raw notes from a discovery call
- `{{company_name}}` — the prospect's company

---

## Prompt template

```
Map the pain and impact from the following discovery call notes for {{company_name}}.

Discovery notes:
---
{{discovery_notes}}
---

Structure your output as follows:

**Stated pains** (things the prospect explicitly said):
- [Pain 1]: [exact quote or close paraphrase] — Source: [note line or timestamp if available]
- [Pain 2]: ...

**Inferred impacts** (business consequences, based on what they said — label as [Inference]):
- [Impact 1]: [what the pain likely costs the business — time, money, quality, risk]
- [Impact 2]: ...

**Unconfirmed hypotheses** (things you believe but they didn't explicitly confirm):
- [Hypothesis 1]: [what you think is true but needs to be confirmed]

**Gaps** (things you still need to learn):
- [Gap 1]: [what question was not answered?]

Rules:
- Distinguish between what they said (stated) and what you inferred
- Do not fabricate quotes or details not in the notes
- If the notes are too sparse to draw conclusions, say so
```

---

## Usage notes

- The stated/inferred distinction is essential — don't conflate what you heard with what you assume.
- Gaps become your next set of discovery questions.
- This output feeds directly into the Qualification Framework Mapper.
