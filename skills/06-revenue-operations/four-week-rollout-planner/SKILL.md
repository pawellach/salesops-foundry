---
name: Four-Week Rollout Planner
description: Generate a phased 4-week adoption plan for rolling out SalesOps Foundry or a new sales process to a team
group: "06 — Revenue Operations"
version: "1.0"
status: implemented
---


# Four-Week Rollout Planner

## Purpose

Produce a structured 4-week rollout plan for adopting a new sales tool, process, or skill set — including training, baseline measurement, coaching checkpoints, and a review cadence. Designed to be realistic about adoption friction.

## When NOT to use

- When the rollout is longer than 4 weeks (adapt the plan structure)
- When the team has fewer than 2 people (a full rollout plan is overkill)
- When the change is a single skill, not a process change

## Required inputs

- `rollout_subject`: what is being rolled out (e.g., "SalesOps Foundry skills", "new discovery framework", "pipeline tracking process")
- `team_context`: team size, current process, and readiness level

## Optional inputs

- `success_metric`: how adoption success will be measured (default: "80% of reps using the new process after 4 weeks")
- `training_format`: `self-paced` | `live_sessions` | `mixed` (default: `mixed`)
- `manager_involvement`: `high` | `medium` | `low` (default: `medium`)

## Step-by-step procedure

1. Define the rollout goal: what does "success" look like at the end of 4 weeks?
2. Establish a baseline: what is the current state of the metric being improved? (Required before starting.)
3. Plan Week 1: awareness + training.
4. Plan Week 2: guided practice with coaching.
5. Plan Week 3: independent use with check-in.
6. Plan Week 4: review, reinforce, and measure.
7. Define the post-rollout cadence: what happens in Week 5+?
8. List 2 adoption risks with mitigations.

## Output contract

```
4-WEEK ROLLOUT PLAN — SalesOps Foundry Discovery Skills
Team: 4 SDRs + 1 AE | Manager involvement: medium

PRE-ROLLOUT (Before Week 1):
- Measure baseline: avg. discovery call score using Call Coach rubric (2 calls per rep)
- Manager reviews baseline scores and sets improvement target

GOAL: 80% of reps using the discovery call plan skill consistently by end of Week 4.

WEEK 1 — Awareness and training
- Day 1: 30-min team session introducing the discovery-question-planner and discovery-call-plan skills
- Days 2–5: Each rep reads their skill files and prepares a mock call plan
- Manager: review 1 mock plan per rep and give written feedback

WEEK 2 — Guided practice
- Each rep uses the skill on 2 real calls
- Manager joins 1 call per rep (live or recording) and coaches using Call Coach rubric
- Friday: 20-min team debrief — what's working, what's hard?

WEEK 3 — Independent use
- Reps use skills on all discovery calls
- Manager reviews structured call notes for quality (1 per rep per week)
- Flag blockers in weekly 1:1s

WEEK 4 — Review and measure
- Re-run Call Coach scoring on 2 calls per rep
- Compare to baseline: has the target improvement been reached?
- Decide: reinforce, adjust, or graduate to next skill group

POST-ROLLOUT (Week 5+):
- Monthly: manager spot-checks 1 call note per rep
- Quarterly: re-score 2 calls to track ongoing quality

ADOPTION RISKS:
1. Reps skip the call plan under time pressure — mitigate by keeping the plan to a 10-min prep habit
2. Manager coaching drops off after Week 2 — mitigate by scheduling 1:1 check-in as a recurring calendar item

NOTE: Baseline measurement before Week 1 is mandatory. Without it, success cannot be assessed.
```

## Evidence and citation rules

- Rollout timelines and adoption rates cited here are general guidance, not research findings. Do not use them as guaranteed outcomes.

## Confidence/uncertainty handling

- If the team has never done a structured rollout before, note: "First rollout typically takes 5–6 weeks rather than 4."

## Safety, privacy, and compliance constraints

- Rollout plans may reference rep performance data. Treat as confidential.

## Human approval requirements

**This skill produces a plan draft.** The manager reviews and approves before execution. No changes to team workflows are made by this skill.

## Failure modes and fallback behaviour

- `team_context` too vague: produce a generic plan and note the assumptions.

## Acceptance criteria

- All 4 weeks defined with specific activities.
- Baseline measurement requirement called out explicitly.
- Post-rollout cadence defined.
- At least 2 adoption risks with mitigations.

## Evaluation cases

**Case 1 — Standard team rollout**
Input: rollout_subject="discovery skills", team_context="5 SDRs, no current structure, manager is involved", training_format=mixed. Expected: 4-week plan with baseline measurement, training in Week 1, coaching in Week 2, independent use in Week 3, review in Week 4.

**Case 2 — Low-involvement manager**
Input: manager_involvement=low. Expected: plan adapted to reduce manager checkpoints; self-paced activities increased; adoption risk note about lack of coaching support.

## Related skills

- [Sales Experiment Designer](/skills/05-sales-enablement/sales-experiment-designer/SKILL.md)
- [Enablement Content Builder](/skills/05-sales-enablement/enablement-content-builder/SKILL.md)
- [Sales Metrics Dictionary](/skills/06-revenue-operations/sales-metrics-dictionary/SKILL.md)
- [Discovery Call Plan](/skills/04-discovery-and-deals/discovery-call-plan/SKILL.md)
