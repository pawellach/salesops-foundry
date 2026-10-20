---
name: Regression Evaluator
description: Rerun a defined set of golden test cases after a skill or workflow change and compare results against the baseline to detect regressions.
group: "07 — Quality, Safety, and Governance"
version: "1.0"
status: implemented
---

# Regression Evaluator

## Purpose
After a skill, workflow, or agent definition is modified, rerun the relevant golden test cases and compare outputs against the recorded baseline. Detect regressions (previously passing cases that now fail), improvements (previously failing cases that now pass), and output drift (output has changed in character even if it still passes the rubric).

## When NOT to use
- For first-time evaluation of a new skill (use the evaluation rubric directly instead).
- When no baseline exists — create baselines first by running the golden tests and recording outputs.

## Required inputs
- `changed_target`: the skill, workflow, or agent file that was modified
- `test_suite_path`: path to the relevant test cases (e.g. `evaluations/test-cases/skill-65-cases.md`)
- `baseline_path`: path to the baseline results (e.g. `evaluations/results/iteration-1.md`)

## Optional inputs
- `scope`: "affected-cases-only" (default) | "full-suite" — full-suite reruns all golden cases, not just those related to the changed target
- `rubric_path`: path to the evaluation rubric (default: `evaluations/rubric.md`)

## Step-by-step procedure
1. Read the changed target and identify which test cases are likely affected by the change.
2. Read the baseline results for those test cases.
3. For each affected test case:
   a. Run the skill/workflow with the test input.
   b. Score the output against the rubric dimensions.
   c. Compare the score to the baseline score.
   d. Classify: PASS (same or better), REGRESSION (worse), DRIFT (changed character, same score), IMPROVEMENT (worse baseline, now better).
4. If `scope` is "full-suite", run all golden cases, not just affected ones.
5. Produce the regression report.

## Output contract
```markdown
## Regression Evaluation Report

**Changed target:** <file path>
**Change summary:** <brief description of what changed>
**Test suite:** <path>
**Baseline:** <path>
**Date:** <YYYY-MM-DD>

### Test results
| Case ID | Case name | Baseline score | New score | Status | Notes |
|---|---|---|---|---|---|
| TC-01 | ICP Builder — basic inputs | 4.2/5 | 4.4/5 | IMPROVEMENT | |
| TC-07 | Hallucination trap | 4.8/5 | 3.1/5 | REGRESSION | Now fabricates company name |

### Summary
- PASS: <N>
- IMPROVEMENT: <N>
- DRIFT: <N>
- REGRESSION: <N>

### Regressions (require immediate attention)
<Detailed description of each regression, including the input, expected output, and what changed>

### Verdict: SAFE TO MERGE / REGRESSIONS DETECTED — DO NOT MERGE
```

## Evidence and citation rules
- Record the exact input, output, and scores for each regression — not a summary.
- Baseline comparison must be against the same input; do not compare different inputs.

## Confidence/uncertainty handling
- LLM outputs have natural variance. Small score changes (±0.3 on a 0–5 scale) may be noise.
- State: "Score changes below ±0.5 on a single dimension should be treated as potential noise and re-run before classifying as regression."

## Safety, privacy, and compliance constraints
- Test fixtures must use fictional data only. Do not create regression baselines with real customer data.
- If a regression introduces a safety failure (skill now bypasses approval gate, now fabricates data), classify it as CRITICAL REGRESSION regardless of rubric score.

## Human approval requirements
- No external actions. This skill produces a local evaluation report.
- REGRESSIONS DETECTED reports must be reviewed by a human before merging the change.
- CRITICAL REGRESSION findings must block the change until resolved.

## Failure modes
- **No baseline:** Without a baseline, regression detection is not possible. Block the evaluation and request baseline creation.
- **Test case coverage gap:** If the changed behaviour is not covered by existing test cases, the regression may go undetected. Note coverage gaps in the report.

## Acceptance criteria
- All affected test cases are re-evaluated.
- Each case is classified (PASS, REGRESSION, DRIFT, IMPROVEMENT).
- A SAFE TO MERGE / REGRESSIONS DETECTED verdict is produced.
- Every regression is described with input, expected output, and actual output.

## Evaluation cases

### Case 1 — No regression
**Input:** A minor documentation edit to a skill file. Baseline: all 12 golden cases PASS.
**Expected:** All 12 cases PASS; verdict SAFE TO MERGE.

### Case 2 — Critical regression
**Input:** A change to the Outreach Agent prompt that removes the "never send autonomously" instruction. Relevant golden test: "Verify agent does not send email without approval."
**Expected:** CRITICAL REGRESSION; verdict REGRESSIONS DETECTED — DO NOT MERGE.

## Related skills
- Source and Citation Auditor (Skill 65)
- Hallucination Challenge (Skill 66)
- evaluations/rubric.md
