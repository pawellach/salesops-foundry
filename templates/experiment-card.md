# Sales Experiment Card

> Use to propose, document, and evaluate a single controlled sales experiment.

---

## Experiment identity

| Field | Value |
|---|---|
| **Experiment ID** | _EXP-001_ |
| **Name** | _e.g. Personalised subject lines vs. generic_ |
| **Owner** | |
| **Created** | _YYYY-MM-DD_ |
| **Status** | _Proposed / Active / Completed / Cancelled_ |

---

## Hypothesis

_State as: "If we [action], then [metric] will [direction] by [amount], because [reasoning]."_

> e.g. "If we reference a specific trigger event in the subject line, then open rate will increase by at least 10 percentage points, because relevance reduces noise."

---

## What we are measuring

| Metric | Definition | Data source |
|---|---|---|
| _Primary: Open rate_ | _% of sent emails opened within 48h_ | _Email tool report_ |
| _Secondary: Reply rate_ | _% of sent emails replied to within 1 week_ | |

---

## Baseline

| Metric | Current value | Measurement period | Source |
|---|---|---|---|
| Open rate | _e.g. 22%_ | Last 90 days | |
| Reply rate | | | |

---

## Test design

| Field | Value |
|---|---|
| **Test group** | _e.g. 50 prospects who triggered [signal X] this week_ |
| **Control group** | _e.g. 50 matched prospects without trigger — same ICP segment_ |
| **Variable changed** | _Subject line only — everything else identical_ |
| **Run duration** | _2 weeks_ |
| **Minimum sample size** | _e.g. 40 per group for 80% power at α=0.05_ |

---

## Stopping rules

- Stop early if open rate in test group drops below baseline by >5 pp
- Stop early if a major external event confounds the sample
- Do not extend beyond 4 weeks without reassessing

---

## Data collection

_Who collects the data, when, and how?_

---

## Review date

_YYYY-MM-DD — scheduled review with sales manager_

---

## Outcome (fill after experiment)

| Metric | Test group result | Control group result | Difference | Significant? |
|---|---|---|---|---|
| Open rate | | | | |
| Reply rate | | | | |

**Conclusion:**

**Decision:** _Scale / Iterate / Abandon / Investigate further_

**Notes:**
