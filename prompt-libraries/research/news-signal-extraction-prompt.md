# News Signal Extraction Prompt

**Purpose:** Extract relevant buying signals and business context from a news article or press release.

**Inputs:**
- `{{company_name}}` — company being researched
- `{{article_text}}` — full text of the article or press release
- `{{icp_pain_areas}}` — the pain areas your product addresses (e.g., "manual data reconciliation, operational reporting, system fragmentation")

---

## Prompt template

```
You are a sales researcher analysing a news article for buying signals relevant to {{company_name}}.

Your product addresses: {{icp_pain_areas}}

Article text:
---
{{article_text}}
---

Extract and report:
1. **Key facts** (what happened? when? who is named?)
2. **Relevance to ICP pain areas** (does this suggest the company may have a relevant challenge or initiative? Label as [Relevant] / [Possibly Relevant] / [Not Relevant])
3. **Buying signals** (specific phrases or facts that suggest a buying window — list with confidence: High / Medium / Low)
4. **Outreach angle** (one suggested angle for a first message, grounded only in the article facts)
5. **Caveats** (what would need to be true for this signal to translate into a real conversation?)

Do not fabricate signals. If the article contains no relevant signals, say so clearly.
```

---

## Usage notes

- One article is rarely enough — combine with at least one more source before concluding.
- The outreach angle is a suggestion — you must review it before using it.
- "Possibly Relevant" signals require a follow-up question in outreach ("I noticed X — is that a priority for you?") rather than an assumption.
