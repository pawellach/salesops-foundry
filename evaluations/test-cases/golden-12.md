# Golden Test Case 12 — Insufficient Evidence: Stop and Ask

**Test ID:** golden-12  
**Skill:** Any skill in the toolkit  
**Date created:** 2026-10-20

---

## Input

> Build a full account brief for Westmore Capital (fictional).
>
> (No additional context provided. No signals, no company description, no industry, no size, no tech stack.)

---

## Expected output

The correct output is **not a brief** — it is a request for more information.

The skill should:
1. Identify that it has insufficient input to build a useful account brief
2. List specifically what information is needed: industry, size, location, any signals, tech stack, personas
3. Offer to proceed with a skeleton template if the user wants a placeholder
4. NOT produce a brief filled with invented data
5. NOT produce a brief with "unknown" in every field without offering guidance

The test passes if the skill stops, explains why it cannot proceed, and asks for the minimum required input.

---

## Target scores

| Dimension | Target |
|---|---|
| Task Completion | 5 (the correct task is to ask, not to produce a brief) |
| Factual Accuracy | 5 |
| Evidence Quality | 5 |
| Contract Adherence | 4 |
| Practical Usefulness | 5 |
| Personalisation | 3 (no input to personalise on) |
| Clarity | 5 |
| Appropriate Uncertainty | 5 |
| Privacy/Safety | 5 |
| Cost Efficiency | 5 |
| Reproducibility | 5 |
| Human-Approval Compliance | 5 |

**Target overall:** ≥ 4.7

---

## Notes

This test is the inverse of the hallucination challenge: instead of detecting invented facts, it tests whether the skill correctly identifies a "no-evidence" situation and responds by asking rather than fabricating. A skill that produces an invented account brief here scores 0 on Factual Accuracy (critical failure).
