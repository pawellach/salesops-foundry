# Proof Point Selector Prompt

**Purpose:** Select the most relevant proof points (case studies, benchmarks, references) for a specific prospect.

**Inputs:**
- `{{prospect_profile}}` — sector, size, pain area
- `{{available_proof_points}}` — paste your list of available case studies, anonymised benchmarks, or references

---

## Prompt template

```
Select the most relevant proof points for a prospect with the following profile:
{{prospect_profile}}

Available proof points:
---
{{available_proof_points}}
---

For each recommended proof point:
1. **Which proof point** (title or identifier)
2. **Why it's relevant** (specific match to the prospect's sector, size, or pain)
3. **How to introduce it** (one sentence, natural — not "as a case study shows...")
4. **What to omit** (any detail in the proof point that doesn't apply or could confuse)

Rules:
- Only recommend proof points that genuinely match the prospect's situation
- Do not fabricate proof points, outcomes, or customer names
- If no proof points are a strong match, say so — do not force a weak connection
- Flag any proof points that require permission to share (e.g., named customer references)
```

---

## Usage notes

- Always verify you have permission to share a proof point before using it in a prospect conversation.
- Anonymised benchmarks ("a logistics company similar in size to yours") are generally safer than named references.
- One strong, relevant proof point beats three weak ones.
