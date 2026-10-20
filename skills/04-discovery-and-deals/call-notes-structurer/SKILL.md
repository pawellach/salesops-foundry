---
name: Call Notes Structurer
description: Transform raw post-call notes or a supplied transcript into structured, actionable CRM-ready notes.
group: "04 — Discovery, Demos, and Deal Progression"
version: "1.0"
status: implemented
---

# Call Notes Structurer

## Purpose
Convert messy, unstructured post-call notes or a transcript into a clean, structured summary that captures pain, context, stakeholders, next steps, and open questions — ready for CRM entry or team sharing.

## When NOT to use
- On calls where no notes or transcript were taken (do not reconstruct from memory alone; flag the gap).
- To fabricate or infer details not present in the notes.

## Required inputs
- Raw notes or transcript from the call (as plain text).
- Call date and participants.

## Optional inputs
- Account Brief (to cross-reference context).
- Discovery Call Plan (to check what was and wasn't covered).

## Step-by-step procedure

1. **Extract key facts.** From the raw notes, extract: stated pains, goals, current process, constraints, stakeholders named, decisions made, and commitments.
2. **Separate stated from inferred.** Mark anything the contact explicitly said as "Stated." Mark anything you inferred as "Inferred — not confirmed." Do not present inferences as facts.
3. **Identify open questions.** Any question in your call plan that was not answered becomes an open question to follow up.
4. **List next steps.** Separate: seller's commitments (what you will do), prospect's commitments (what they agreed to do), and agreed timeline.
5. **Flag risks or concerns.** Anything that could indicate the deal is at risk, that a stakeholder is missing, or that the prospect's stated situation is inconsistent.
6. **Produce structured notes document.**

## Output contract

```markdown
## Call Notes — Sarah Okafor / Northlight Technologies
Call date: 2026-10-22 | Duration: 32 min | Seller: Alex Kowalski

### Participants
- Sarah Okafor, CTO (Northlight Technologies)
- Alex Kowalski, VP Sales (Seller)

### Stated pain
- "We run pipeline reviews every Monday but they take 2 hours and still miss things" (Stated)
- Deals are being miscategorised by AEs; Sarah finds out too late (Stated)

### Inferred (not confirmed)
- CFO may be involved in budget decisions for tools >£20k (Inferred — not confirmed; Sarah said "I'd need to check with finance")

### Current state
- Using Salesforce for CRM; pipeline views built in custom dashboards
- Monday reviews run by Sarah; 8 AEs currently
- No formal stage criteria enforced

### Stakeholders identified
- Sarah Okafor: CTO, engaged, not yet confirmed as champion
- Finance team: unnamed; involved at budget stage (inferred)
- CEO: mentioned once as "wanting clearer forecasts" — not yet engaged

### Next steps
**Seller commits:**
- Send a one-page overview of how similar teams use the platform (by Fri 25 Oct)
- Draft a suggested agenda for a 45-min follow-up including a demo

**Prospect commits:**
- Sarah will check whether CFO needs to be involved at evaluation stage (by Mon 28 Oct)

**Agreed next meeting:** TBC pending Sarah's response

### Open questions (not answered on this call)
- Decision criteria: not discussed
- Budget range: not discussed
- Existing contracts / switch cost: not discussed
- Who is the economic buyer?

### Risks / flags
- Single-threaded: only Sarah engaged; economic buyer unknown
- No decision criteria discussed — risk of losing to a competitor on criteria we didn't know existed
```

## Evidence and citation rules
- Use verbatim quotes where available to anchor stated pain.
- Clearly label inferences vs. stated facts.
- Do not fill in gaps with plausible-sounding details.

## Confidence/uncertainty handling
- If notes are fragmentary, produce what can be extracted and flag what is missing.
- If a key field (economic buyer, decision criteria) has no data, list it as an open question.

## Safety, privacy, and compliance constraints
- Do not include personal data about contacts beyond their professional role.
- If a transcript was recorded, note the recording consent status.
- Do not share notes with the prospect without the seller's review.

## Human approval requirements
**Notes are for internal use until the seller reviews and approves them.** CRM entry is a human action. Do not push notes to any system.

## Failure modes and fallback behaviour
- **No notes supplied:** Return error; do not reconstruct from memory or account brief alone.
- **Notes are too brief to extract structure:** Return what can be extracted; flag missing sections.

## Acceptance criteria
- Stated pain is separated from inferred.
- Next steps are split: seller commits and prospect commits.
- Open questions list is present.
- No detail is fabricated.

## Evaluation cases

**Case 1 — Full notes available.**
Input: 400-word raw notes from a 30-min call; multiple pain points mentioned; one explicit next step agreed.
Expected: Structured output with stated/inferred separation; seller and prospect commits listed; open questions itemised.

**Case 2 — Very sparse notes.**
Input: "Good call with Sarah. She's interested. Follow up next week."
Expected: Output extracts what it can; flags all critical missing sections (pain, stakeholders, next steps, open questions); does not invent detail.

## Related skills
- [Discovery Call Plan](/skills/04-discovery-and-deals/discovery-call-plan/SKILL.md) — provides the call plan to check coverage.
- [Pain and Impact Mapper](/skills/04-discovery-and-deals/pain-and-impact-mapper/SKILL.md) — deepens pain analysis.
- [Qualification Framework Mapper](/skills/04-discovery-and-deals/qualification-framework-mapper/SKILL.md) — structured qualification from these notes.
