# Job Posting Analysis Prompt

**Purpose:** Extract strategic insights from a company's job postings to infer priorities and buying signals.

**Inputs:**
- `{{company_name}}` — company being researched
- `{{job_postings}}` — paste 1–5 relevant job posting descriptions
- `{{your_solution_area}}` — what your product does (e.g., "logistics data consolidation")

---

## Prompt template

```
Analyse the following job postings from {{company_name}} to identify strategic signals relevant to {{your_solution_area}}.

Job postings:
---
{{job_postings}}
---

Report:
1. **Roles being hired** (title, function, seniority)
2. **Technologies or tools mentioned** (what are they using or evaluating?)
3. **Initiatives implied** (what does this hiring pattern suggest they are building or changing?)
4. **Relevance to {{your_solution_area}}** (does this suggest a relevant problem or initiative? Explain)
5. **Confidence level** (High / Medium / Low — a single job ad is low confidence; a pattern across 3+ roles is medium)
6. **Suggested outreach angle** (one angle grounded only in the job posting facts)

Rules:
- Label every conclusion as [Inference] unless it is explicitly stated in the job text.
- Do not name specific individuals. Do not fabricate contact details.
- If the postings are unrelated to your solution area, say so — do not force a connection.
```

---

## Usage notes

- Job postings are signals, not proof of buying intent. Use them to start a conversation, not to claim you know their budget or plans.
- Combine with company news and account brief for a fuller picture.
