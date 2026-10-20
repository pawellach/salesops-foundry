---
name: Sales Call Coach
description: Evaluate supplied call notes or transcript against a transparent rubric and return prioritised coaching feedback
group: "05 — Sales Enablement and Management"
version: "1.0"
status: implemented
---


# Sales Call Coach

## Purpose

Review a sales call (from notes or transcript) against a structured rubric and return specific, evidence-based coaching feedback — not vague impressions. Designed for post-call review by the rep themselves or by a manager.

## When NOT to use

- When no notes or transcript are supplied (this skill cannot invent call content)
- When the call is a customer support interaction rather than a sales conversation
- When you want forward-looking call preparation (use Discovery Call Plan instead)

## Required inputs

- `call_notes_or_transcript`: the raw or cleaned notes or transcript from the call
- `call_type`: `discovery` | `demo` | `follow-up` | `negotiation` | `closing`

## Optional inputs

- `rep_goal`: what the rep intended to achieve on this call
- `deal_context`: brief background on the opportunity
- `rubric_override`: custom rubric dimensions to emphasise

## Step-by-step procedure

1. Read the full `call_notes_or_transcript`. Do not skip ahead.
2. Score the call on each rubric dimension (0–3 scale defined below). Base every score on a quote or paraphrase from the notes.
3. Identify the **top 2 strengths** with specific evidence.
4. Identify the **top 2 improvement areas** with a concrete, actionable suggestion for each.
5. Flag any compliance or safety concerns (manipulative pressure, inaccurate claims, inappropriate data requests).
6. Summarise in ≤5 lines. Do not fabricate events that are not in the notes.

### Rubric dimensions (0 = absent, 1 = weak, 2 = adequate, 3 = strong)

| Dimension | Description |
|---|---|
| Active listening | Rep paraphrased or acknowledged prospect's statements |
| Question quality | Questions were open, relevant, and ordered logically |
| Needs confirmation | Rep confirmed stated needs before proposing a solution |
| Value articulation | Value connected to a specific, stated problem |
| Next step clarity | A concrete next step with owner and date was agreed |
| Prospect engagement | Prospect asked questions or elaborated willingly |
| Objection handling | Objections were acknowledged before responding |

## Output contract

```
CALL COACH REVIEW — Discovery Call
Rep: [supplied or unknown]
Call type: discovery

SCORES:
Active listening:      2/3 — Rep paraphrased the budget concern ("so timing is the real constraint")
Question quality:      3/3 — 6 open questions, well-ordered from situation to implication
Needs confirmation:    1/3 — Solution features mentioned before needs were confirmed
Value articulation:    1/3 — Generic ROI claim with no connection to prospect's stated problem
Next step clarity:     2/3 — Follow-up call agreed but no date set
Prospect engagement:   3/3 — Prospect asked 4 unprompted questions
Objection handling:    2/3 — "Interesting point" acknowledgement before responding

TOP STRENGTHS:
1. Strong question sequencing — built rapport before going deep on problems
2. Prospect was highly engaged; rep maintained space for them to elaborate

TOP IMPROVEMENTS:
1. Confirm needs before presenting: ask "Does that match what you're trying to solve?" before demoing any feature
2. Set a specific date for the follow-up: "Can we put 30 minutes in the calendar for Thursday?"

COMPLIANCE NOTE: None.
```

## Evidence and citation rules

- Every score must cite a quote or paraphrase from the notes. Do not score without evidence.
- Label inferences as inferences: "It appears the rep was…" not "The rep was…"

## Confidence/uncertainty handling

- If the notes are fragmentary (<200 words), flag: "Notes are brief — scores for dimensions with no evidence are marked N/A."
- Do not invent call content.

## Safety, privacy, and compliance constraints

- Flag any call behaviour that appears manipulative, deceptive, or coercive.
- Do not store or repeat personal contact data beyond what is in the input.
- Coaching feedback is for internal use only.

## Human approval requirements

**No external actions are taken by this skill.** Output is a coaching document for internal review. The manager or rep decides what to share, escalate, or act on.

## Failure modes and fallback behaviour

- No notes supplied: return an error asking for call notes.
- Notes are in a foreign language: flag the limitation; attempt to score if language is parseable, note uncertainty.
- Call type is ambiguous: default to `discovery` rubric and note the assumption.

## Acceptance criteria

- Every non-N/A score includes a specific quote or paraphrase.
- Exactly 2 strengths and 2 improvements identified.
- Compliance note present even if empty.
- No fabricated call events.

## Evaluation cases

**Case 1 — Strong discovery call**
Input: transcript of a well-structured discovery call with good questions, confirmed needs, and a concrete next step. Expected: scores of 2–3 on most dimensions, strengths that cite specific quotes, improvement areas that are minor.

**Case 2 — Weak call, pushy closing**
Input: notes showing rep interrupting prospect, making unverified ROI claims, and pressuring for same-day decision. Expected: low scores on listening/needs-confirmation, a compliance flag for pressure tactics, specific actionable improvements.

## Related skills

- [Deal Review Facilitator](/skills/05-sales-enablement/deal-review-facilitator/SKILL.md)
- [Discovery Call Plan](/skills/04-discovery-and-deals/discovery-call-plan/SKILL.md)
- [Win Loss Review](/skills/05-sales-enablement/win-loss-review/SKILL.md)
- [Objection Classifier](/skills/04-discovery-and-deals/objection-classifier/SKILL.md)
