# Golden Test Case 07 — Pipeline Hygiene Audit

**Test ID:** golden-07  
**Skill:** `skills/05-sales-enablement/pipeline-hygiene-audit/SKILL.md`  
**Date created:** 2026-10-20

---

## Input

> Audit these 3 pipeline opportunities:
>
> 1. Northbridge Corp (fictional) — Prospecting, €80K, close date 2026-12-31, last activity: 2026-08-01 (80 days ago), no next step, AE note: "promising"
> 2. Westfall Industries (fictional) — Demo, €55K, close date 2026-11-15, last activity: 2026-10-18 (2 days ago), next step: send proposal, champion confirmed
> 3. Coastal Logistics (fictional) — Negotiation, €200K, close date 2026-10-25 (5 days), last activity: 2026-10-15, no legal review scheduled, AE note: "should close"

---

## Expected output

For each opportunity:
1. **Hygiene score** (good/acceptable/at risk/poor)
2. **Findings** — specific gaps with severity (High/Medium/Low)
3. **Recommended actions** — specific and actionable

Key expected findings:
- Opp 1 (Northbridge): At risk / poor — 80 days inactive, placeholder close date, AE note "promising" is not a qualification
- Opp 2 (Westfall): Acceptable — recent activity, clear next step; minor: budget not confirmed
- Opp 3 (Coastal): At risk — "should close" is not evidence; no legal review; 5-day close date without documented process

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
| Clarity | 5 |
| Appropriate Uncertainty | 5 |
| Privacy/Safety | 5 |
| Cost Efficiency | 4 |
| Reproducibility | 5 |
| Human-Approval Compliance | 5 |

**Target overall:** ≥ 4.9
