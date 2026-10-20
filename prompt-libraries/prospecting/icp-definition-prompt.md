# ICP Definition Prompt

**Purpose:** Convert an ICP hypothesis into explicit, testable criteria.

**Inputs:**
- `{{product_description}}` — what your product does
- `{{icp_hypothesis}}` — your current rough ICP ("we work best with...")
- `{{best_customers}}` — describe 2–3 of your best existing customers (no names needed)

---

## Prompt template

```
Help me define an Ideal Customer Profile based on the following inputs.

Product: {{product_description}}
Current ICP hypothesis: {{icp_hypothesis}}
Best customers (described anonymously): {{best_customers}}

Generate an ICP with explicit criteria in these dimensions:
1. **Firmographic** (company size range, sector, geography, ownership type)
2. **Technographic** (systems or tools they use that indicate fit)
3. **Situational** (specific situation, trigger, or stage that makes them ready — not just "they have the problem")
4. **Behavioural** (how they typically buy, who initiates, what their process looks like)
5. **Exclusion criteria** (who is explicitly NOT a fit, even if they look like the above)

For each criterion:
- State the criterion specifically (not "mid-market" but "50–500 employees")
- Note confidence level (High = confirmed from best customers / Medium = hypothesis / Low = assumption)
- Note how you would verify it during a discovery call

Rules:
- Treat this as a hypothesis to test, not a final definition
- Do not list criteria you have no evidence for
- Exclusions are as important as inclusions — be specific
```

---

## Usage notes

- The confidence levels tell you which criteria to validate first.
- Review after every 5 discovery calls — the ICP should evolve as you learn.
- Exclusions prevent wasted time on poor-fit accounts; don't skip them.
