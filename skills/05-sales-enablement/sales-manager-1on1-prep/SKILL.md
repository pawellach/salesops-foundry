---
name: Sales Manager 1:1 Prep
description: Structure a rep coaching session from supplied goals, activity data, and manager observations
group: "05 — Sales Enablement and Management"
version: "1.0"
status: implemented
---


# Sales Manager 1:1 Prep

## Purpose

Prepare a structured agenda and coaching questions for a manager's 1:1 with a sales rep, based on supplied goals, pipeline data, recent activity, and manager observations. The goal is a coaching conversation, not a performance evaluation.

## When NOT to use

- When the intent is a formal performance review (this skill is for coaching, not evaluation)
- When no context about the rep is supplied
- When the meeting has already happened (use Win/Loss Review or Call Coach for retrospective)

## Required inputs

- `rep_context`: role, tenure, current quarter performance vs. target
- `coaching_focus`: what the manager wants to improve or reinforce this session

## Optional inputs

- `recent_pipeline`: the rep's current pipeline snapshot
- `recent_call_notes`: summary of recent calls or coaching feedback
- `rep_stated_goals`: what the rep has said they want to work on
- `prior_session_notes`: notes from the last 1:1

## Step-by-step procedure

1. Review all supplied inputs. Note areas where rep performance is strong vs. gaps.
2. If `recent_pipeline` is supplied, identify 1–2 specific deals to discuss based on risk or opportunity.
3. Structure a 30-minute agenda:
   - 5 min: rep check-in (rep leads — do not script this)
   - 10 min: deals discussion (specific, evidence-based)
   - 10 min: skill or behaviour focus (the `coaching_focus`)
   - 5 min: commitments and next steps
4. For the deals section, generate 2–3 questions grounded in the pipeline data.
5. For the skill/behaviour section, generate 2–3 coaching questions using "explore, don't tell" framing.
6. Suggest 1 concrete commitment for the rep to make by the next session.

## Output contract

```
1:1 PREP — Rep: Alex M. | Manager: [supplied or redacted]
Date: 2026-10-20 | Focus: pipeline progression

AGENDA (30 min)

5 min — Check-in (Alex leads)
  Manager: open with "How are you feeling about your pipeline heading into Q4 close?"

10 min — Deals discussion
  Northlight Technologies ($85K):
    Q: "What's the next concrete step and who owns it?"
  Meridian Logistics ($120K):
    Q: "Have you met the economic buyer? What's their role in the decision?"

10 min — Skill focus: qualification
  Q: "When you look at your pipeline, which deals are you most confident in — and what makes you confident?"
  Q: "Is there a deal where you realise you need more information before calling it committed?"

5 min — Commitment
  Suggested commitment: "By next Thursday, you'll have met or spoken to the economic buyer on Meridian Logistics."

NOTES FOR MANAGER:
- Prior session commitment was to update pipeline by Monday — check if completed.
- Alex is at 73% of Q4 target with 6 weeks remaining.
```

## Evidence and citation rules

- Deal questions must reference specific deals from the supplied pipeline, not generic examples.
- Do not fabricate rep behaviours or pipeline events.

## Confidence/uncertainty handling

- If `recent_pipeline` is not supplied, note: "Deal-specific questions omitted — no pipeline data supplied."
- Do not make performance judgments without supplied evidence.

## Safety, privacy, and compliance constraints

- 1:1 prep documents are confidential HR/management material.
- Do not send the prep document to the rep — it is for the manager only.

## Human approval requirements

**This skill produces a prep document for the manager's use only.** No external actions, no sharing with the rep without manager review. Manager controls how the coaching is conducted.

## Failure modes and fallback behaviour

- `rep_context` missing: output a generic coaching agenda and note the limitation.
- `coaching_focus` missing: default to pipeline and deal progression.

## Acceptance criteria

- Agenda covers all 4 sections with time allocations.
- Deal questions reference specific deals from input (if supplied).
- Coaching questions use open, non-leading framing.
- One concrete commitment suggested.

## Evaluation cases

**Case 1 — Full context supplied**
Input: rep at 70% target, pipeline with 6 deals, coaching focus on qualification, prior session notes. Expected: agenda with specific deal questions, skill questions referencing prior session, one targeted commitment.

**Case 2 — Minimal context**
Input: rep name and coaching focus only. Expected: generic agenda with open questions, explicit note that deal-specific coaching requires pipeline data.

## Related skills

- [Deal Review Facilitator](/skills/05-sales-enablement/deal-review-facilitator/SKILL.md)
- [Sales Call Coach](/skills/05-sales-enablement/sales-call-coach/SKILL.md)
- [Win Loss Review](/skills/05-sales-enablement/win-loss-review/SKILL.md)
- [Pipeline Hygiene Audit](/skills/05-sales-enablement/pipeline-hygiene-audit/SKILL.md)
