---
name: Deal Review Facilitator
description: Generate evidence-seeking questions for a deal review, exposing gaps without inventing deal health
group: "05 — Sales Enablement and Management"
version: "1.0"
status: implemented
---


# Deal Review Facilitator

## Purpose

Produce a structured set of evidence-seeking questions for a deal review meeting. The goal is to surface what the rep actually knows vs. what they are assuming — without fabricating information about the deal.

## When NOT to use

- When no deal context is supplied (this skill cannot review a phantom deal)
- When the intent is to create a call plan (use Discovery Call Plan instead)
- When the deal is closed-won or closed-lost (use Win/Loss Review instead)

## Required inputs

- `deal_summary`: what the rep knows about the opportunity (company, contact, stage, amount, close date, why they're buying)
- `deal_stage`: `qualification` | `discovery` | `evaluation` | `negotiation` | `closing`

## Optional inputs

- `qualification_framework`: `MEDDICC` | `SPICED` | `BANT` | `custom` (default: MEDDICC)
- `manager_concern`: a specific area the manager wants to probe

## Step-by-step procedure

1. Read the `deal_summary` carefully. Note every fact vs. every assumption.
2. Map the supplied information against the `qualification_framework` dimensions.
3. For each dimension with **missing or weak evidence**, generate 1–2 probing questions the manager should ask.
4. For each dimension with **strong evidence**, confirm it with one verification question.
5. If `manager_concern` is supplied, add 2 targeted questions addressing that concern.
6. Produce a brief deal health snapshot: which dimensions are evidenced, which are gaps.
7. Do not assign a probability or forecast number — that is the manager's judgment.

### MEDDICC dimensions

Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion, Competition.

## Output contract

```
DEAL REVIEW — Northlight Technologies ($85K, Q4 close)

DEAL HEALTH SNAPSHOT:
✅ Identified Pain — stated clearly by VP Operations
⚠️ Champion — assumed to be VP Ops but not verified
❌ Economic Buyer — unknown; rep has not met them
❌ Decision Criteria — no formal criteria documented
⚠️ Decision Process — rep knows "committee" but not timeline or approvers
✅ Competition — two named competitors confirmed

QUESTIONS FOR THE REVIEW:

Economic Buyer:
- Have you spoken to the person who will sign the contract? Who is it?
- What happens to this deal if the VP Operations leaves or is reassigned?

Champion:
- Has the VP Operations explicitly said they will advocate for this deal internally?
- Can they describe what they'll say to the CFO?

Decision Criteria:
- What does Northlight need to see to say yes? Has this been written down?
- Is there a formal evaluation scorecard?

Verification (Pain):
- When did the VP Operations last reference this as a top-3 priority?
```

## Evidence and citation rules

- Questions must be grounded in the supplied `deal_summary`. Do not invent deal facts.
- Label assumptions explicitly: "The rep has stated X — this needs verification."

## Confidence/uncertainty handling

- If the `deal_summary` is very thin (< 3 facts), output a standard qualification framework checklist and note that the deal is poorly documented.

## Safety, privacy, and compliance constraints

- Do not encourage pressure tactics or misrepresentation.
- Treat all deal data as internal and confidential.

## Human approval requirements

**This skill produces facilitation questions only.** No external communications are created. The manager decides what to ask and what actions to take after the review.

## Failure modes and fallback behaviour

- Unknown `qualification_framework`: default to MEDDICC and note the fallback.
- `deal_summary` is empty: return an error.

## Acceptance criteria

- At least one question per gap dimension identified.
- Deal health snapshot distinguishes evidenced vs. assumed vs. unknown.
- No fabricated deal facts.
- No forecast probability assigned.

## Evaluation cases

**Case 1 — Well-documented deal**
Input: deal_summary with evidence for 5/7 MEDDICC dimensions, deal_stage=negotiation.
Expected: fewer gap questions, more verification questions, health snapshot shows mostly green.

**Case 2 — Thin deal at closing stage**
Input: deal_summary with only company name, amount, and rep's gut feel, deal_stage=closing.
Expected: warning that deal is poorly documented, full MEDDICC gap question list, explicit statement that a close date without documented criteria is a risk.

## Related skills

- [Opportunity Risk Review](/skills/03-run-the-pipeline/opportunity-risk-review/SKILL.md)
- [Pipeline Hygiene Audit](/skills/05-sales-enablement/pipeline-hygiene-audit/SKILL.md)
- [Win Loss Review](/skills/05-sales-enablement/win-loss-review/SKILL.md)
- [Qualification Framework Mapper](/skills/04-discovery-and-deals/qualification-framework-mapper/SKILL.md)
