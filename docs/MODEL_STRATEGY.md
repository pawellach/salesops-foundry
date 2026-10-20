# Model Strategy — SalesOps Foundry

**Version:** 1.0  
**Date:** 2026-10-20

---

## Verified model availability

As of 2026-10-20, the following models are verified available via Claude Code (Anthropic):

| Model ID | Capability tier | Context window | Notes |
|---|---|---|---|
| `claude-sonnet-4-6` | Strong general reasoning | 200K tokens | Default for most tasks |
| `claude-opus-5-5` | Strongest reasoning, adversarial evaluation | 200K tokens | Use for architecture, complex planning, release reviews |
| `claude-haiku-5-5` | Fast, low-cost, structured output | 200K tokens | Use for bulk classification, simple transformations |

**Important:** Model IDs change as new versions are released. Never hard-code a model name in a skill file. Refer to this document or a configurable settings file. Verify model availability with `claude --version` or the API.

---

## Routing policy

| Task | Recommended tier | Rationale |
|---|---|---|
| Orchestration and complex planning | Opus 5.5 | High-stakes decisions; benefits from strongest reasoning |
| Architecture and skill authoring | Opus 5.5 | Long-context, complex spec-following |
| Account brief and ICP building | Sonnet 4.6 | Good reasoning; structured output |
| Discovery call planning | Sonnet 4.6 | Reliable instruction-following |
| Web/source research and synthesis | Sonnet 4.6 | Reliable browsing and citation |
| First-touch and outreach drafts | Sonnet 4.6 | Creative but controlled generation |
| Bulk lead classification | Haiku 5.5 | Repetitive, low-risk; optimise cost |
| Independent quality review | Opus 5.5 | Adversarial evaluation benefits from strongest model |
| Security/privacy/red-team review | Opus 5.5 | High-stakes; needs adversarial reasoning |
| Pipeline report formatting | Haiku 5.5 | Low-complexity transformation |

---

## Context-window constraints

- Skills that process large pipeline exports or long research documents should chunk inputs to stay within 100K tokens per call to preserve headroom for reasoning.
- Workflows that chain multiple skills should pass only the necessary outputs between steps — do not carry the full history.

---

## Privacy implications

- Do not send confidential company or customer data to any external model unless the applicable data-processing terms permit it.
- For EU customer data, verify that the model provider's data processing agreement covers your use case.
- For sensitive negotiation or personal data, prefer on-premise or private-deployment models where available.

---

## Fallback behaviour

If the preferred model is unavailable:
1. Try the next tier down (Opus → Sonnet → Haiku).
2. Log the fallback in the run record.
3. For release-gate reviews and red-team passes, do not downgrade without human awareness.

---

## Benchmark method (placeholder)

Run the 12 golden test cases (see `evaluations/test-cases/`) on each candidate model. Score on the 12-dimension rubric. Select the least expensive model that scores ≥ 4.0 average on core workflows and passes all security cases.

Results to be recorded in `evaluations/results/model-benchmark.md` when first conducted.

---

## Escalation conditions

Escalate to a stronger model or human review when:
- A skill output contains a potential fabrication
- A prompt-injection attempt is detected in source material
- A forecast challenge reveals a significant gap in evidence
- A release-gate review fails any critical dimension
