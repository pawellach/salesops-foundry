---
name: Model/Cost Router
description: Select and document the most appropriate AI model for a given task based on capability requirements, cost, latency, context-window size, and privacy constraints.
group: "07 — Quality, Safety, and Governance"
version: "1.0"
status: implemented
---

# Model/Cost Router

## Purpose
Given a task description and its requirements, recommend the appropriate model tier, record the routing rationale, and flag any privacy or policy constraints that affect model selection. This skill ensures model assignments are deliberate, documented, and cost-efficient — not defaulting to the most powerful (and expensive) model for every task.

## When NOT to use
- When the runtime environment has only one model available (no routing decision to make).
- For real-time latency-critical decisions where this analysis would add unacceptable overhead.

## Required inputs
- `task_description`: what the agent is trying to do
- `task_type`: one of: orchestration | research | bulk-classification | skill-authoring | code | quality-review | privacy-review | summary-formatting
- `available_models`: list of models available in the current environment with their tier labels (e.g. `[{id: "claude-opus-5-5", tier: "strong-reasoning"}, {id: "claude-haiku-5-5", tier: "fast-low-cost"}]`)

## Optional inputs
- `context_length_required`: estimated token count for input + output
- `data_sensitivity`: "public" | "internal" | "confidential" (affects whether external model APIs are appropriate)
- `latency_budget`: "real-time (<2s)" | "interactive (<15s)" | "background (minutes OK)"

## Step-by-step procedure
1. Read the task type and map it to the routing table in `docs/MODEL_STRATEGY.md`.
2. Check context-window requirements against available model limits.
3. Check data sensitivity: if "confidential", only models deployed in approved private infrastructure are candidates.
4. Select the least expensive model that satisfies: (a) required capability tier, (b) context-window, (c) privacy constraint.
5. Record the routing decision with rationale.
6. If no available model meets all requirements, return a BLOCKED routing with explanation.

### Default routing table (override with MODEL_STRATEGY.md)
| Task type | Capability tier | Default to |
|---|---|---|
| Orchestration, complex planning | strong-reasoning | Strongest available |
| Research and synthesis | search-capable | Search model or general strong |
| Bulk classification, first drafts | fast-low-cost | Smallest capable |
| Skill authoring, architecture | strong-reasoning + long-context | Strong general |
| Code and schema work | strong-coding | Code-capable model |
| Quality review, adversarial | strong-reasoning, ideally different family | Strong general (different family from author if possible) |
| Privacy/security review | strong-reasoning | Strong general |
| Summaries and formatting | fast-low-cost | Smallest capable |

## Output contract
```markdown
## Model Routing Decision

**Task:** <task_description>
**Task type:** <type>
**Date:** <YYYY-MM-DD>

### Recommended model
- **Model ID:** <exact model ID from available list>
- **Tier:** <tier label>
- **Rationale:** <why this model for this task>

### Constraints applied
- Context window: <required vs available>
- Data sensitivity: <public/internal/confidential>
- Latency budget: <requirement>

### Cost note
<Brief note on relative cost vs. alternatives considered>

### Fallback
If <recommended model> is unavailable: use <fallback model> with the following caveats: <any limitations>.

### Status: ROUTED / BLOCKED
```

## Evidence and citation rules
- Model IDs must come from the `available_models` input — never invent model IDs.
- Routing rationale must reference the capability tier required, not just assert "best model."

## Confidence/uncertainty handling
- If the task type is ambiguous, default to the stronger tier and note the ambiguity.
- State: "Model capabilities and costs change. Verify routing against current MODEL_STRATEGY.md."

## Safety, privacy, and compliance constraints
- Confidential data must never be routed to external model APIs not approved under the applicable data-processing policy.
- Document the data-sensitivity classification in every routing decision.

## Human approval requirements
- No external actions. This skill produces a local routing record.
- Routing decisions for confidential data are advisory — the human operator confirms the privacy classification.

## Failure modes
- **Stale model list:** If `available_models` is outdated, the routing may select a deprecated model.
- **Capability mismatch:** A "fast-low-cost" model may produce unacceptable quality for a task rated as requiring strong reasoning. Monitor output quality.

## Acceptance criteria
- A specific model ID is recommended (not a tier label alone).
- Rationale references the task type and capability requirement.
- Data sensitivity is assessed and recorded.
- A fallback model is named.

## Evaluation cases

### Case 1 — Bulk outreach classification
**Input:** Task: classify 200 inbound leads as high/medium/low fit. Available models: strong-reasoning (expensive) and fast-low-cost.
**Expected:** Routed to fast-low-cost; rationale: bulk classification, structured output, low reasoning requirement; cost note provided.

### Case 2 — Security review with confidential data
**Input:** Task: review outreach template that contains internal pricing. Data sensitivity: confidential.
**Expected:** Only models in approved private infrastructure eligible; if none available, BLOCKED with explanation.

## Related skills
- Human Approval Gate (Skill 70)
- Regression Evaluator (Skill 72)
- docs/MODEL_STRATEGY.md (configuration file)
