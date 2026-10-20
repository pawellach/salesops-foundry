# Golden Test Case 03 — Account Brief Builder

**Test ID:** golden-03  
**Skill:** `skills/02-account-intelligence/account-brief-builder/SKILL.md`  
**Date created:** 2026-10-20

---

## Input

> Build an account brief for Northlight Technologies. Use only the following two signals:
>
> Signal 1: Blog post titled "Scaling from 12 to 30 carriers — what we learned" published 2026-08-22 on their fictional company blog. Discusses data format complexity and reconciliation overhead.
>
> Signal 2: New VP Operations Jordan Rivera (fictional) joined from DHL (fictional) in October 2026. Observed on fictional LinkedIn.

---

## Expected output

A completed account brief (matching `templates/account-brief.md`) with:
1. Company overview — industry, size, location (marked "unknown" where not provided)
2. Target personas — Jordan Rivera listed with medium confidence and source
3. Signals section — both signals with source, date, and confidence
4. Fit score — scored only on what is known (carrier count signal, persona match); explicitly lower confidence due to missing data
5. Recommended angle — grounded in Signal 1 (the public blog post)
6. Open questions — at least 3 unanswered questions

The output must NOT:
- Fill in revenue, tech stack, or other fields without a source
- Invent additional signals
- Present fit score as high-confidence when key criteria are unknown

---

## Target scores

| Dimension | Target |
|---|---|
| Task Completion | 5 |
| Factual Accuracy | 5 |
| Evidence Quality | 5 |
| Contract Adherence | 5 |
| Practical Usefulness | 5 |
| Personalisation | 5 |
| Clarity | 4 |
| Appropriate Uncertainty | 5 |
| Privacy/Safety | 5 |
| Cost Efficiency | 4 |
| Reproducibility | 4 |
| Human-Approval Compliance | 5 |

**Target overall:** ≥ 4.8
