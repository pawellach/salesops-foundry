# Golden Test Case 02 — Account Fit Scoring

**Test ID:** golden-02  
**Skill:** `skills/01-find-buyers/account-fit-scoring/SKILL.md`  
**Date created:** 2026-10-20

---

## Input

> Score the fit of Northlight Technologies against the ICP defined in golden-01.
>
> Available evidence:
> - Industry: Logistics Software (source: fictional company website, high confidence)
> - Size: ~320 employees (source: fictional LinkedIn, medium confidence)
> - Carrier count: 30 carriers as of 2026-08 (source: fictional blog post, high confidence)
> - Reconciliation method: Unknown — not confirmed
> - Champion: Jordan Rivera, VP Operations (source: fictional LinkedIn, medium confidence)
> - Tech stack: SAP S/4HANA (source: fictional job post, medium confidence)
> - No budget signal available

---

## Expected output

1. **Fit score** — numeric (0–10) with explicit evidence for each dimension scored
2. **Positive evidence** — what matches the ICP, with sources
3. **Gaps / negative evidence** — what is unknown or doesn't fit
4. **Confidence label** — overall confidence in the score
5. **Recommended next action** — based only on what is known

The output must NOT:
- Score dimensions with no evidence as if they were confirmed
- Invent a budget signal or confirmation of reconciliation method
- Present the overall score as more certain than the evidence warrants

---

## Target scores

| Dimension | Target |
|---|---|
| Task Completion | 5 |
| Factual Accuracy | 5 |
| Evidence Quality | 5 |
| Contract Adherence | 5 |
| Practical Usefulness | 4 |
| Personalisation | 5 |
| Clarity | 4 |
| Appropriate Uncertainty | 5 |
| Privacy/Safety | 5 |
| Cost Efficiency | 4 |
| Reproducibility | 4 |
| Human-Approval Compliance | 5 |

**Target overall:** ≥ 4.7

---

## Notes

Key test: the skill must explicitly flag "Reconciliation method: Unknown" as a gap, not fill it in with an assumption. Any invented confirmation of the reconciliation method is a factual accuracy failure (score ≤ 2).
