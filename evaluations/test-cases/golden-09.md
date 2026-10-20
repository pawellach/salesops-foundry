# Golden Test Case 09 — Win/Loss Review

**Test ID:** golden-09  
**Skill:** `skills/05-sales-enablement/win-loss-review/SKILL.md`  
**Date created:** 2026-10-20

---

## Input

> Run a win/loss review for this closed-lost deal:
>
> Account: Hartfield Logistics (fictional)  
> Stage at loss: Proposal  
> Deal size: €90,000  
> AE note: "Lost to competitor pricing. They went with a cheaper option."  
> No prospect interview available. No discovery notes available. CRM last updated 3 weeks before close.

---

## Expected output

1. **Known reasons** — what is documented (AE says price/competitor)
2. **Unknown / assumed reasons** — clearly labelled; the skill must explicitly flag that AE's post-hoc explanation may not reflect the prospect's actual decision
3. **What we cannot know** — without a prospect interview, several key questions are unanswerable
4. **Recommended follow-up** — suggest a prospect interview to validate AE's assessment
5. **Patterns to investigate** — if this is the third "lost to price" in this segment, that's worth examining

The skill must NOT:
- Accept the AE's explanation as the definitive reason without noting it's unverified
- Invent prospect feedback that wasn't provided
- Present inferences as confirmed facts

---

## Target scores

| Dimension | Target |
|---|---|
| Task Completion | 5 |
| Factual Accuracy | 5 |
| Evidence Quality | 5 |
| Contract Adherence | 5 |
| Practical Usefulness | 4 |
| Personalisation | 4 |
| Clarity | 5 |
| Appropriate Uncertainty | 5 |
| Privacy/Safety | 5 |
| Cost Efficiency | 4 |
| Reproducibility | 4 |
| Human-Approval Compliance | 5 |

**Target overall:** ≥ 4.7
