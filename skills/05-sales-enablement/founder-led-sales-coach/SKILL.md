---
name: Founder-Led Sales Coach
description: Lightweight discovery, positioning, and follow-up guidance for founders doing early sales without a sales team
group: "05 — Sales Enablement and Management"
version: "1.0"
status: implemented
---


# Founder-Led Sales Coach

## Purpose

Help founders structure their own early sales conversations — discovery, positioning, and follow-up — using a repeatable, lightweight framework that does not require a full sales operations function.

## When NOT to use

- When a trained AE or SDR is running the deal (use Sales Call Coach instead)
- When the company has a defined sales process with a manager reviewing deals
- When the input is a full call transcript (use Call Notes Structurer instead)

## Required inputs

- `company_stage`: brief description of the founder's company (stage, product, target customer)
- `prospect_context`: what is known about the prospect (role, company, why they're talking)
- `conversation_stage`: `discovery` | `demo` | `follow-up` | `negotiation`

## Optional inputs

- `founder_concern`: specific question or situation the founder wants to handle (e.g., "they asked about pricing too early")
- `previous_notes`: notes from prior conversations with this prospect

## Step-by-step procedure

1. Confirm the `conversation_stage` to select the appropriate framework section.
2. For **discovery**: generate 5–7 open questions ordered by learning value (situation → problem → implication → need-payoff). Flag any question that might feel intrusive given the prospect context.
3. For **demo**: draft a 3-sentence value-framing opener that connects the product's capabilities to the stated problem. Remind the founder to confirm the stated problem before demonstrating.
4. For **follow-up**: draft a 3–5 sentence email that summarises what was agreed, the single clearest next step, and a specific date or deadline. Mark the draft for human review before sending.
5. For **negotiation**: identify the founder's walk-away constraint (if supplied), propose 2–3 trade-off options, and flag decisions that require board or co-founder approval.
6. Append a "Watch out for" note: one or two red flags to monitor based on the prospect context.

## Output contract

```
CONVERSATION STAGE: discovery

RECOMMENDED QUESTIONS:
1. What's prompting you to look at this now?
2. Walk me through how you currently handle [problem area].
3. What happens if this problem is still unsolved six months from now?
4. Who else is affected when this goes wrong?
5. What would a good outcome look like for your team?

WATCH OUT FOR:
- Northlight Technologies is evaluating 3 vendors simultaneously — ask early about decision timeline and criteria.
```

## Evidence and citation rules

- Questions and frameworks are synthesis from public sales methodology literature (SPIN, MEDDICC, SPICED). They are guidance, not evidence.
- Do not claim any question technique has a specific conversion rate.

## Confidence/uncertainty handling

- If the `prospect_context` is thin (fewer than 2 facts), flag this: "Prospect context is limited — the questions below are generic and may need adjustment after the first 5 minutes."
- Never invent details about the prospect.

## Safety, privacy, and compliance constraints

- Do not store or repeat personal contact information beyond what the founder supplied.
- Follow-up email drafts must be clearly labelled as drafts. Do not send.

## Human approval requirements

**All external actions require human approval.** This skill produces drafts and frameworks only. The founder reviews and decides before sending any email, making any commitment, or sharing any pricing information.

## Failure modes and fallback behaviour

- If `conversation_stage` is unclear: ask the founder to clarify before proceeding.
- If the product description is too vague to write specific questions: output a generic discovery framework and note the limitation.

## Acceptance criteria

- Output includes ≥5 discovery questions OR a follow-up email draft OR a negotiation options list, depending on stage.
- Watch out for note references a specific detail from the input (not generic).
- No invented prospect facts.
- Follow-up draft is explicitly marked for human review.

## Evaluation cases

**Case 1 — Discovery, thin context**
Input: stage=discovery, prospect_context="CFO at a mid-size logistics company", company_stage="early-stage freight visibility SaaS"
Expected: 5+ questions, explicit warning about thin context, no invented facts about the CFO.

**Case 2 — Follow-up draft**
Input: stage=follow-up, prospect_context="Meridian Logistics, VP Operations, demo completed, asked about API integration", previous_notes="agreed to introduce us to IT director"
Expected: email draft that mentions the API integration, references the IT director introduction, proposes a specific next step. Explicitly marked as draft.

## Related skills

- [Sales Call Coach](/skills/05-sales-enablement/sales-call-coach/SKILL.md)
- [Discovery Question Planner](/skills/04-discovery-and-deals/discovery-question-planner/SKILL.md)
- [First Touch Draft](/skills/03-run-the-pipeline/first-touch-draft/SKILL.md)
- [Objection Handling Coach](/skills/04-discovery-and-deals/objection-handling-coach/SKILL.md)
