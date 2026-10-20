# Account Fit Scoring Prompt

**Purpose:** Score a specific account against ICP criteria with transparent evidence.

**Inputs:**
- `{{account_name}}` — the account being scored
- `{{account_data}}` — what you know about the account (paste relevant facts)
- `{{icp_criteria}}` — your ICP criteria (from ICP Definition prompt or ICP Builder skill)

---

## Prompt template

```
Score {{account_name}} against the ICP criteria below.

Account data:
---
{{account_data}}
---

ICP criteria:
---
{{icp_criteria}}
---

For each ICP dimension, score 0–2:
- 2 = Strong match (supported by specific evidence)
- 1 = Partial match or insufficient data
- 0 = Does not match or clear exclusion criterion applies

Format:
| Dimension | Score (0–2) | Evidence | Confidence |
|---|---|---|---|
| Firmographic | | | |
| Technographic | | | |
| Situational | | | |
| Behavioural | | | |

Total score: [X / 8]
Recommendation: Strong Fit (7–8) / Good Fit (5–6) / Marginal (3–4) / Poor Fit (0–2)
Priority: [High / Medium / Low / Do Not Pursue]

Reasoning: [2–3 sentences on the most important factors driving the score]

Rules:
- Only score based on data provided — do not infer without labelling as [Inference]
- If a dimension cannot be assessed, score 1 (partial / insufficient data) and note the gap
- Exclusion criteria that trigger: override total score → Poor Fit regardless of other scores
```

---

## Usage notes

- The total score is a guide, not a rule. Use your judgment alongside it.
- A "Do Not Pursue" recommendation from an exclusion criterion should be respected — it's there for a reason.
- Low-confidence scores indicate what to verify in the first discovery call.
