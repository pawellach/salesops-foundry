---
name: Call Notes Template
description: Structure raw or unstructured call notes into a consistent, CRM-agnostic format with clear sections
group: "06 — Revenue Operations"
version: "1.0"
status: implemented
---


# Call Notes Template

## Purpose

Transform raw call notes (or a transcript) into a structured, consistently formatted notes document that captures the key facts, pain points, next steps, and open questions from the conversation. Designed to be CRM-agnostic — output can be pasted into any system.

## When NOT to use

- When no notes or transcript are supplied (this skill cannot reconstruct a call)
- When coaching feedback on the call is needed (use Sales Call Coach instead)
- When the intent is a follow-up email (use Follow-up Email template instead)

## Required inputs

- `raw_notes`: unstructured notes or transcript from the call
- `call_type`: `discovery` | `demo` | `follow-up` | `negotiation`

## Optional inputs

- `deal_context`: opportunity name, company, contact
- `rep_name`: name of the rep who conducted the call
- `call_date`: date of the call

## Step-by-step procedure

1. Read the `raw_notes` fully before structuring.
2. Extract and categorise:
   - **Key facts**: company situation, role, context — sourced from the call
   - **Stated problems/pain**: what the prospect explicitly said (quote or close paraphrase)
   - **Unstated/inferred**: what the rep observed but the prospect did not explicitly state — label as inferred
   - **Product/solution discussed**: what was shown or described
   - **Objections raised**: any concerns the prospect expressed
   - **Agreed next step**: what both parties committed to, with owner and date
   - **Open questions**: things that need follow-up or were not answered
3. Do not add information not present in the `raw_notes`.
4. Label every inferred item clearly.

## Output contract

```
CALL NOTES — Discovery Call
Company: Northlight Technologies | Contact: Sarah Chen, VP Operations
Rep: Alex M. | Date: 2026-10-15 | Duration: ~35 min

KEY FACTS:
- Team of 200 across 3 distribution centres
- Currently using a manual spreadsheet-based tracking system
- Evaluating 2 other vendors (names not disclosed)
- Decision expected by end of Q4

STATED PROBLEMS (prospect's words):
- "We lose 2–3 hours a day reconciling inventory between sites"
- "Our biggest issue is the delay between a pick happening and the system updating"

INFERRED (not stated explicitly):
- High frustration with current system — repeated the reconciliation issue unprompted [inferred from emphasis and tone]

PRODUCT/SOLUTION DISCUSSED:
- Demonstrated real-time sync feature; prospect asked about API integration
- Pricing not discussed

OBJECTIONS RAISED:
- Concern about IT resource required for implementation

AGREED NEXT STEP:
- Rep: send technical integration overview by 2026-10-17 (owner: Alex M.)
- Prospect: introduce us to IT Director by end of week

OPEN QUESTIONS:
- Who else is in the buying committee?
- What is their current contract renewal date with the spreadsheet vendor?
```

## Evidence and citation rules

- Stated problems must be quotes or close paraphrases. Label as "prospect's words" or "paraphrase."
- Inferred items must be labelled as inferred with a brief reason.
- Do not invent facts not in the notes.

## Confidence/uncertainty handling

- If the notes are fragmentary, note what sections cannot be completed: "Next steps: not captured in notes — follow up with rep."

## Safety, privacy, and compliance constraints

- Call notes may contain personal data. Handle as confidential.
- Do not share structured notes externally without manager review.

## Human approval requirements

**This skill produces an internal document.** No external actions. Rep or manager reviews and decides whether and where to store the notes.

## Failure modes and fallback behaviour

- `raw_notes` empty: return an error.
- Notes too short to structure meaningfully: output what can be extracted, note the limitations.

## Acceptance criteria

- All sections present (even if some are "not captured").
- Stated vs. inferred items clearly distinguished.
- Agreed next step includes owner and date (if available in notes).
- No fabricated content.

## Evaluation cases

**Case 1 — Full discovery call notes**
Input: detailed notes with stated problems, objections, and an agreed next step. Expected: all sections populated, at least 2 stated problems in prospect's words, next step with owner and date.

**Case 2 — Sparse notes**
Input: 3 lines of notes with no next step and no objections mentioned. Expected: sections populated with available info, missing sections flagged as "not captured", no fabricated content.

## Related skills

- `discovery-notes` template (templates/)
- [Sales Call Coach](/skills/05-sales-enablement/sales-call-coach/SKILL.md)
- `call-plan` template (templates/)
- [Call Notes Structurer](/skills/04-discovery-and-deals/call-notes-structurer/SKILL.md)
