# Forecast Scenario Prompt

**Purpose:** Build explicit, assumption-labelled forecast scenarios for a given period.

**Inputs:**
- `{{pipeline_data}}` — current open deals with stage, amount, close date, and your confidence notes
- `{{period}}` — the forecast period (e.g., Q4 2026)
- `{{quota}}` — the team or individual quota for this period

---

## Prompt template

```
Build three forecast scenarios for {{period}}.

Quota: {{quota}}

Pipeline data:
---
{{pipeline_data}}
---

For each scenario:
- **Name**: Commit / Best Case / Upside
- **Amount**: total expected closed-won revenue
- **Deals included**: which specific deals, and why each is included or excluded
- **Key assumptions**: what must be true for this scenario to materialise
- **Key risks**: what could prevent this scenario

Then provide:
- **Forecast confidence**: for each scenario, rate confidence Low / Medium / High with a reason
- **Top 2 actions** to improve the Commit scenario (specific, actionable)

Rules:
- Every deal inclusion/exclusion must be justified
- Label every assumption as [Assumption]
- Do not adjust amounts without explaining why
- Do not claim confidence levels without evidence from the pipeline data
- If data is insufficient to forecast reliably, say so explicitly
```

---

## Usage notes

- Forecast scenarios are a management tool, not a commitment to the CEO. Use them to have better conversations, not to avoid them.
- The Commit scenario should be deals you would genuinely be surprised not to close.
- Review the assumptions with your manager — many forecasting problems are assumption disagreements in disguise.
