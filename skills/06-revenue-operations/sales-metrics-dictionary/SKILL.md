---
name: Sales Metrics Dictionary
description: Define sales metrics with explicit numerator, denominator, time window, exclusions, and source for each
group: "06 — Revenue Operations"
version: "1.0"
status: implemented
---


# Sales Metrics Dictionary

## Purpose

Generate a metrics dictionary for a sales team that defines each metric precisely: numerator, denominator, time window, exclusions, data source, and known limitations. Prevents misaligned reporting and dashboard confusion.

## When NOT to use

- When you want to analyse current metric values (this skill defines metrics, not analyses data)
- When you want a forecast (use Forecast Challenge or Weekly Pipeline Report)

## Required inputs

- `metrics_list`: list of metrics to define (or "standard" for a default set)

## Optional inputs

- `team_context`: team size and stage (affects which metrics are most relevant)
- `crm_context`: CRM used (affects available data sources)
- `output_format`: `markdown_table` | `markdown_cards` (default: `markdown_cards`)

## Step-by-step procedure

1. If `metrics_list = "standard"`, use the default set (see below).
2. For each metric, define:
   - Name and common aliases
   - Formula (numerator / denominator)
   - Time window (daily, weekly, monthly, quarterly, rolling 30/90)
   - Exclusions (what should not be counted)
   - Data source (where to pull each component)
   - Known limitations
3. Note which metrics are lagging (report on the past) vs. leading (predict future performance).

### Default standard metric set

Reply rate, meeting-booked rate, show rate, SQLs created, pipeline created, average deal size, win rate, average sales cycle length, pipeline coverage ratio, quota attainment, time to first meeting.

## Output contract

```
SALES METRICS DICTIONARY

---
METRIC: Win Rate
Aliases: Close rate, conversion rate (stage-to-won)
Formula: Closed-Won opportunities / (Closed-Won + Closed-Lost opportunities)
Time window: Rolling 90 days (quarterly is also common)
Exclusions: Exclude opportunities closed before formal qualification (Suspect stage); exclude deals lost before discovery call (no real evaluation occurred)
Data source: CRM closed opportunities with close date in the window
Indicator type: Lagging
Known limitations: Denominator definition is critical — including very early-stage losses will artificially deflate win rate; teams often disagree on what counts as "qualified"
---

METRIC: Pipeline Coverage Ratio
Aliases: Pipeline multiple, coverage ratio
Formula: Total open pipeline value / Remaining quota for the period
Time window: Measured at a point in time (e.g., start of each month)
Exclusions: Exclude Suspect-stage opportunities; exclude opportunities past their close date
Data source: CRM pipeline snapshot; current-period quota from finance/sales ops
Indicator type: Leading
Known limitations: A high coverage ratio only matters if pipeline quality is high — a 4x multiple of unlikely deals provides false confidence
---

METRIC: Average Sales Cycle Length
Aliases: Average deal duration, time-to-close
Formula: Sum of (close_date − created_date) for Closed-Won deals / Count of Closed-Won deals
Time window: Rolling 90 days or last completed quarter
Exclusions: Exclude outliers (deals >3x the median cycle length may skew the average — use median instead)
Data source: CRM closed-won opportunities with both created_date and close_date
Indicator type: Lagging
Known limitations: created_date may not match when the deal was truly qualified; cycle length from first meaningful meeting is often more actionable
---
```

## Evidence and citation rules

- Metric definitions are general sales practice standards, not from a specific vendor or research publication.
- Do not cite specific benchmark values (e.g., "top teams have a 25% win rate") without a verified source.

## Confidence/uncertainty handling

- Known limitations section must be present for every metric. Incomplete metrics definitions are not acceptable.

## Safety, privacy, and compliance constraints

- Metrics may use CRM data. Access to underlying records must be governed by the team's data access policy.

## Human approval requirements

**This skill produces a reference document.** No dashboards are created, no data is queried. The RevOps owner or manager reviews and adopts the definitions before use.

## Failure modes and fallback behaviour

- Unknown metric requested: note it is not in the standard set and define it with the available context.
- `metrics_list` empty: use the default standard set.

## Acceptance criteria

- Every defined metric has formula, time window, exclusions, data source, and known limitations.
- Lagging vs. leading indicator type is specified.
- No benchmark claims without a cited source.

## Evaluation cases

**Case 1 — Standard set**
Input: metrics_list=standard. Expected: all 11 standard metrics defined with complete fields, leading/lagging labels, known limitations for each.

**Case 2 — Custom metric**
Input: metrics_list=["Time to first meeting"]. Expected: single metric defined with formula (first meeting date − lead created date), exclusions (exclude no-shows), data source notes.

## Related skills

- [Roi Time Saved Estimator](/skills/06-revenue-operations/roi-time-saved-estimator/SKILL.md)
- [Sales Experiment Designer](/skills/05-sales-enablement/sales-experiment-designer/SKILL.md)
- [Pipeline Tracker](/skills/06-revenue-operations/pipeline-tracker/SKILL.md)
- [Weekly Pipeline Report](/skills/05-sales-enablement/weekly-pipeline-report/SKILL.md)
