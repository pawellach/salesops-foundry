# Golden Test Case 05 — Lead Triage

**Test ID:** golden-05  
**Skill:** `skills/03-run-the-pipeline/lead-triage/SKILL.md`  
**Date created:** 2026-10-20

---

## Input

> Triage this inbound lead:
>
> Name: (blank)  
> Company: Apex Freight (fictional)  
> Email: contact@apexfreight.example  
> Message: "Hi, I'd like to learn more about your product."  
> Source: Website contact form  
> Date received: 2026-10-20

---

## Expected output

1. **Classification** — Lead quality: Low (insufficient information)
2. **Missing information list** — Name, role, company size, specific interest area, timeline, budget (all missing)
3. **Recommended next step** — Send a qualification email asking specific questions (draft for approval, not sent)
4. **Routing recommendation** — Suggest assigning to SDR for qualification; do not route to AE without more info
5. **Flag** — Message is generic ("learn more") — low intent signal

The output must NOT:
- Assume the lead is qualified based on "showing interest"
- Route directly to an AE
- Make up information about Apex Freight

---

## Target scores

| Dimension | Target |
|---|---|
| Task Completion | 5 |
| Factual Accuracy | 5 |
| Evidence Quality | 4 |
| Contract Adherence | 5 |
| Practical Usefulness | 5 |
| Personalisation | 3 (limited input) |
| Clarity | 5 |
| Appropriate Uncertainty | 5 |
| Privacy/Safety | 5 |
| Cost Efficiency | 5 |
| Reproducibility | 5 |
| Human-Approval Compliance | 5 |

**Target overall:** ≥ 4.7
