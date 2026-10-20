# Company Overview Prompt

**Purpose:** Summarise a company from publicly available sources into a structured overview suitable for an account brief.

**Inputs:**
- `{{company_name}}` — name of the company
- `{{company_website}}` — company website URL
- `{{source_texts}}` — paste relevant excerpts from public pages, press releases, LinkedIn

---

## Prompt template

```
You are a sales research analyst. Summarise {{company_name}} based only on the source texts provided below.

Structure your summary as follows:
1. **What the company does** (one sentence, specific — not generic)
2. **Size and stage** (employees, funding stage if known, revenue range if public)
3. **Sector and market** (specific, not just "B2B")
4. **Recent notable events** (funding, leadership changes, product launches, partnerships — with source and date)
5. **Likely challenges or priorities** (inferred from the above — label as inference, not fact)
6. **Confidence and gaps** (what do you know with high confidence vs. what is inferred or unknown?)

Rules:
- Only use information from the provided source texts. Do not add knowledge not present in the sources.
- Label every inference as "[Inference]" and every confirmed fact as "[Source: <URL or document name>]".
- If information is missing, say so explicitly. Do not fill gaps with plausible-sounding guesses.
- Do not fabricate contact names, email addresses, phone numbers, or financial figures.

Source texts:
---
{{source_texts}}
---
```

---

## Usage notes

- Paste at least 2–3 source excerpts (company website, LinkedIn, recent news) for a reliable summary.
- The "[Inference]" labels are intentional — they tell the sales rep what is evidence vs. hypothesis.
- Review the output before using it in an account brief; correct any errors.
