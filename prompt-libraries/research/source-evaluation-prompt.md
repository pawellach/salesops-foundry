# Source Evaluation Prompt

**Purpose:** Assess whether a source or claim is reliable enough to include in an account brief or outreach message.

**Inputs:**
- `{{source_url}}` — URL of the source
- `{{claim}}` — the specific claim you want to verify
- `{{source_excerpt}}` — the relevant text from the source

---

## Prompt template

```
Evaluate the following source and claim for reliability and recency.

Source URL: {{source_url}}
Claim: {{claim}}
Source excerpt: {{source_excerpt}}

Assess and report:
1. **Source type** (company press release, news article, LinkedIn post, job board, analyst report, etc.)
2. **Publication date** (if visible — if not, note it is unknown)
3. **Reliability assessment** (is this a primary source, secondary, or opinion? What are the limitations?)
4. **Claim accuracy** (does the excerpt actually support the claim? Exactly, partially, or not at all?)
5. **Confidence rating** (High / Medium / Low — explain why)
6. **Recommended use** (safe to cite in an account brief / use with caveat / do not use — explain)

Do not add information not present in the excerpt. Do not look up additional sources.
```

---

## Usage notes

- Use this before including any claim in a customer-facing document.
- A "do not use" recommendation means find a better source or remove the claim.
- Confidence ratings are for your internal use — do not share them in outreach messages.
