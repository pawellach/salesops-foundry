---
name: Sales Experiment Designer
description: Propose a measurable, bounded sales experiment with a clear hypothesis, baseline, treatment, measurement plan, and stopping rules
group: "05 — Sales Enablement and Management"
version: "1.0"
status: implemented
---


# Sales Experiment Designer

## Purpose

Help a sales team design a controlled experiment to test a sales hypothesis — for example, "does a shorter first email improve reply rates?" — with a defined baseline, treatment, success metric, sample size guidance, and stopping rules.

## When NOT to use

- When the team has no ability to split-test or compare conditions (use a single best-practice recommendation instead)
- When the question requires statistical analysis beyond what this skill provides (consult a data analyst)
- When the hypothesis is about a strategic direction change, not a tactical test

## Required inputs

- `hypothesis`: the claim to test (e.g., "Personalised subject lines increase reply rate for SDR outreach")
- `current_approach`: what the team is currently doing (the baseline)
- `proposed_change`: the specific change to test (the treatment)

## Optional inputs

- `metric`: the primary success metric (default: `reply_rate`)
- `sample_size_available`: how many prospects or touchpoints are available per week
- `test_duration_weeks`: how long the team can run the test (default: 4 weeks)
- `minimum_detectable_effect`: the smallest improvement that would justify changing the approach (default: 10%)

## Step-by-step procedure

1. Restate the hypothesis in testable form: "If we [treatment], then [metric] will [direction] by [magnitude] compared to [baseline], because [mechanism]."
2. Define the baseline: what metric value does the current approach produce? If not known, note this as a required pre-experiment measurement.
3. Define the treatment group and control group clearly (avoid contamination).
4. Specify the primary metric and how it will be measured (source, definition, timing).
5. Provide rough sample size guidance: "To detect a 10% difference at reasonable confidence, you typically need 50–100 data points per group — adjust for your actual baseline rate."
6. Set stopping rules: when will you declare success, failure, or inconclusive?
7. List 2 risks that could invalidate the experiment (e.g., seasonal effects, rep assignment bias).

## Output contract

```
EXPERIMENT DESIGN — SDR Outreach Subject Line Test

HYPOTHESIS: If SDRs use personalised subject lines referencing a prospect's recent hiring activity, then reply rate will increase by ≥10% compared to generic subject lines, because relevance signals effort and reduces delete-on-sight behaviour.

BASELINE: Current average reply rate = [REQUIRED — measure over 2 weeks before starting]
TREATMENT: Personalised subject line referencing a specific signal (hiring, funding, product launch)
CONTROL: Current generic subject line template

MEASUREMENT:
- Metric: reply rate (replies / emails sent)
- Source: email tracking tool (manual count if tool unavailable)
- Duration: 4 weeks after baseline established
- Assignment: alternate weeks (control week / treatment week) to reduce rep-level bias

SAMPLE SIZE GUIDANCE:
- At 5% baseline reply rate, detecting a 10% lift requires ~400 emails per group
- At 10% baseline, ~200 per group
- These are rough guides, not statistically certified minimums

STOPPING RULES:
- Declare success: treatment reply rate ≥ baseline + 10% after 4 weeks
- Declare failure: treatment reply rate ≤ baseline after 4 weeks
- Declare inconclusive: difference < 5% — extend by 2 weeks or accept null

RISKS:
1. If reps know which week is "treatment", they may try harder — blind assignment preferred if possible
2. Q4 end-of-quarter effects may inflate both conditions — note in analysis

NOTE: These are estimated guidance figures, not certified statistical analysis. Treat results as directional.
```

## Evidence and citation rules

- Sample size guidance is approximate. Label all numbers as estimates.
- Do not claim the experiment will prove causation — it provides evidence for a decision.

## Confidence/uncertainty handling

- If baseline metric is unknown: always require it as a pre-step. Do not proceed without a baseline.
- If sample size is too small: flag that results will have high uncertainty.

## Safety, privacy, and compliance constraints

- Experiments involving outreach must respect opt-out/stop requirements and applicable email compliance rules.
- Do not design experiments that involve deceptive representations or manipulative tactics.

## Human approval requirements

**This skill produces an experiment design for human review.** The manager approves the design before it is run. Any outreach-related treatment requires human review of the messages before sending.

## Failure modes and fallback behaviour

- `hypothesis` is too vague: ask for a specific, testable statement before proceeding.
- `current_approach` is unknown: note that a baseline measurement period is required first.

## Acceptance criteria

- Hypothesis is in testable form with mechanism.
- Baseline and treatment clearly differentiated.
- Stopping rules cover success, failure, and inconclusive.
- At least 2 invalidation risks listed.
- Numbers labelled as estimates.

## Evaluation cases

**Case 1 — SDR email test**
Input: hypothesis about email personalisation, current approach="generic templates", metric="reply rate", 4 weeks available. Expected: full design with testable hypothesis, alternate-week assignment, sample size guidance, 2 risks including rep-awareness bias.

**Case 2 — Vague hypothesis**
Input: hypothesis="we should personalise more". Expected: error or clarification request — hypothesis is not specific enough to test; output asks for a specific metric and treatment.

## Related skills

- [Win Loss Review](/skills/05-sales-enablement/win-loss-review/SKILL.md)
- [Sales Metrics Dictionary](/skills/06-revenue-operations/sales-metrics-dictionary/SKILL.md)
- [Roi Time Saved Estimator](/skills/06-revenue-operations/roi-time-saved-estimator/SKILL.md)
- [Enablement Content Builder](/skills/05-sales-enablement/enablement-content-builder/SKILL.md)
