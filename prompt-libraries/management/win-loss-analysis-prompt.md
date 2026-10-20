# Win/Loss Analysis Prompt

**Purpose:** Analyse a closed deal (won or lost) to extract learnings and distinguish evidence from speculation.

**Inputs:**
- `{{deal_outcome}}` — Won or Lost
- `{{deal_summary}}` — key facts: company, size, duration, close date
- `{{deal_notes}}` — everything you know about the deal (discovery notes, emails, objections, close summary)

---

## Prompt template

```
Analyse the following {{deal_outcome}} deal and extract learnings.

Deal summary: {{deal_summary}}

Deal notes:
---
{{deal_notes}}
---

Structure your analysis:
1. **Documented reasons** (what the prospect explicitly said or did that explains the outcome — cite specific notes)
2. **Inferred reasons** (what you believe contributed, based on the pattern of the deal — label as [Inference])
3. **Speculation to discard** (post-hoc explanations that have no evidence — call them out, don't use them as lessons)
4. **What worked** (specific actions or approaches that contributed positively)
5. **What to change** (specific, actionable changes for future deals)
6. **ICP implication** (does this deal suggest any revision to your ICP or exclusion criteria?)

Rules:
- Clearly separate documented reasons from inferences from speculation
- Do not generate lessons from speculation — only from evidence or clearly labelled inferences
- Be specific: "qualification was weak because CFO was never engaged" beats "we didn't qualify well"
- A lost deal is not always a sales failure — sometimes the product genuinely wasn't a fit
```

---

## Usage notes

- Run this within 48 hours of a close while details are fresh.
- Share with the team only the "What worked" and "What to change" sections — the full analysis is internal.
- ICP implications are the most valuable long-term output — prioritise those for team review.
