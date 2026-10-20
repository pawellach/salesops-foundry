---
name: Enablement Content Builder
description: Create reusable sales guidance, playbook sections, or training assets from approved source material
group: "05 — Sales Enablement and Management"
version: "1.0"
status: implemented
---


# Enablement Content Builder

## Purpose

Transform approved source material (call notes, win/loss reviews, product updates, methodology references) into reusable enablement content — playbook sections, objection-handling guides, onboarding checklists, or training assets.

## When NOT to use

- When no source material is supplied (do not invent sales guidance from scratch)
- When the goal is a specific outreach message (use First-Touch Draft or Follow-up Sequence Builder)
- When the content requires legal review (compliance checklists, regulatory claims)

## Required inputs

- `source_material`: approved content to transform (call notes, win/loss summaries, product documentation, etc.)
- `content_type`: `playbook_section` | `objection_guide` | `onboarding_checklist` | `training_scenario` | `quick_reference`

## Optional inputs

- `audience`: `sdr` | `ae` | `manager` | `founder` (default: `ae`)
- `topic`: specific topic to focus on (e.g., "handling procurement delays")
- `format_preference`: `markdown` | `table` | `checklist`

## Step-by-step procedure

1. Read the `source_material` carefully. Identify the key insights, patterns, or facts that are directly useful to the target audience.
2. Separate factual claims (from the source) from inferences (patterns you are drawing).
3. Structure the content for the `content_type`:
   - `playbook_section`: situation → recommended actions → what good looks like → watch out for
   - `objection_guide`: objection statement → what it usually means → response options → what to avoid
   - `onboarding_checklist`: numbered steps with done criteria
   - `training_scenario`: fictional situation → challenge question → model answer → debrief notes
   - `quick_reference`: table of key terms, questions, or steps
4. Label every claim with its source (e.g., "from win/loss review 2026-09" or "inferred from call pattern").
5. Flag any gap where the source material is insufficient to support the guidance being written.

## Output contract

```
ENABLEMENT CONTENT — Objection Guide: "We already have a solution"
Audience: AE | Source: Win/Loss reviews Q3 2026 (3 reviews)

OBJECTION: "We already have a solution in place."

WHAT IT USUALLY MEANS (from source — 2/3 reviews):
The prospect has an incumbent vendor but is dissatisfied with it — otherwise they would not be taking the meeting. The objection signals risk aversion, not satisfaction.

RESPONSE OPTIONS:
Option A — Curiosity approach:
  "That makes sense — you wouldn't be here if everything was working perfectly. What made you agree to this conversation?"
  [Source: call pattern noted in 2 win reviews]

Option B — Contrast approach:
  "Understood. Most of our best customers said the same thing six months before switching. What would have to be true for you to reconsider?"
  [Inferred — not directly from source; treat as hypothesis]

WHAT TO AVOID:
- Immediately listing features (rep hasn't confirmed what the problem with the current solution is)
- Dismissing the current vendor by name (damages credibility)

GAPS IN SOURCE MATERIAL:
The source material covers enterprise deals only. This guide may not apply to SMB prospects with simpler setups.
```

## Evidence and citation rules

- Every piece of guidance must trace to the source material or be labelled as inferred.
- Do not invent case studies, statistics, or customer examples.
- If the source is thin, say so. Do not pad content with generic sales advice.

## Confidence/uncertainty handling

- Label inferred guidance clearly: "Inferred — treat as hypothesis until validated."
- Recommend pilot testing before deploying new enablement content at scale.

## Safety, privacy, and compliance constraints

- Do not include specific customer names, emails, or identifiable deal data in reusable content.
- Content for external use (e.g., customer-facing) requires additional human review.

## Human approval requirements

**This skill produces draft enablement content.** A manager or enablement lead reviews it before distribution to the team. Content intended for external use requires additional approval.

## Failure modes and fallback behaviour

- `source_material` is empty or generic: return an error. Do not produce guidance without a source.
- Source material is in a format that cannot be parsed: note the limitation and ask for clarification.

## Acceptance criteria

- Every claim is traced to the source or labelled as inferred.
- Gaps in source material are explicitly noted.
- Output format matches the `content_type` structure.
- No fabricated case studies or customer data.

## Evaluation cases

**Case 1 — Good source material**
Input: 3 win/loss reviews with consistent pattern about champion weakness, content_type=playbook_section, topic="champion development". Expected: structured playbook section with specific guidance sourced from reviews, inferred claims labelled, no invented examples.

**Case 2 — Thin source material**
Input: single call note with limited detail, content_type=objection_guide. Expected: draft guide with explicit gaps noted, recommendation to gather more data before deploying, no fabricated patterns.

## Related skills

- [Win Loss Review](/skills/05-sales-enablement/win-loss-review/SKILL.md)
- [Sales Call Coach](/skills/05-sales-enablement/sales-call-coach/SKILL.md)
- `playbooks/discovery-call.md`
- [Sales Experiment Designer](/skills/05-sales-enablement/sales-experiment-designer/SKILL.md)
