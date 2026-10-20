---
name: Objection Classifier
description: Identify the type of objection, its underlying concern, and what clarification is needed before responding.
group: "04 — Discovery, Demos, and Deal Progression"
version: "1.0"
status: implemented
---

# Objection Classifier

## Purpose
When a prospect raises an objection, classify its type and root cause before responding. Most failed objection handling happens because the seller responds to the stated objection rather than the underlying concern.

## When NOT to use
- Without the actual objection text or paraphrase.
- As a script to deflect legitimate concerns — this skill helps address, not dismiss.

## Required inputs
- The objection, as stated or closely paraphrased.
- Context: what was being discussed when the objection arose?

## Optional inputs
- Prior interaction notes.
- Stage of the deal.

## Step-by-step procedure

1. **State the objection verbatim or close paraphrase.**
2. **Classify the type:**
   - **Price/value:** "It's too expensive" / "We don't have budget"
   - **Timing:** "Not the right time" / "Come back in Q2"
   - **Priority:** "This isn't a top-3 priority right now"
   - **Trust/credibility:** "We haven't heard of you" / "We don't know if you can deliver"
   - **Authority:** "I need to check with [others]" — may be real or a stall
   - **Competitor/status quo:** "We already have [X]" / "We're happy with what we have"
   - **Technical/fit:** "I'm not sure this works for our use case"
   - **Brush-off:** Dismissive deflection, not a substantive objection
3. **Identify the underlying concern.** The stated type is the surface; the underlying concern is what must be addressed. Example: "It's too expensive" often means "I don't see enough value yet."
4. **Determine what clarification is needed.** What question would help you understand whether this is a real blocker or a resolvable concern?
5. **Assess deal impact.** Is this objection a: Showstopper (unresolvable blocker), Significant (resolvable but material), or Minor (routine friction)?
6. **Produce classification output.**

## Output contract

```markdown
## Objection Classification
Date: YYYY-MM-DD | Account: Northlight Technologies

**Stated objection:** "This looks interesting but we already have Salesforce dashboards for this."

**Type:** Competitor / Status quo
**Underlying concern (hypothesis):** "We've invested in Salesforce and changing would mean admitting that investment wasn't sufficient. There may also be an IT ownership question."
**Clarification needed:** "What does the current Salesforce dashboard give you, and what does it not give you that prompted you to take this call?"
**Deal impact:** Significant — not a showstopper; the status quo often has unmet gaps.

### Why this classification matters
Responding with product features before understanding the gap in their current solution is premature. The clarifying question surfaces whether the gap is real.
```

## Evidence and citation rules
- Underlying concern is a hypothesis; label it as such.
- Do not assume the objection is dishonest or a manipulation tactic unless there is evidence.

## Confidence/uncertainty handling
- If the objection is ambiguous, classify as the most likely type and note the alternative.
- Flag if the objection may be a polite brush-off vs. a real concern — they require different responses.

## Safety, privacy, and compliance constraints
- Do not classify objections in a way designed to manipulate or pressure the prospect.
- Do not dismiss privacy or compliance objections as "just a blocker to handle."

## Human approval requirements
**Classification is an internal preparation tool.** The seller uses it to prepare their response. No message is sent by this skill.

## Failure modes and fallback behaviour
- **Objection not provided:** Return error; cannot classify without the objection.
- **Objection is clearly a showstopper:** Flag immediately; recommend honest assessment before investing more time.

## Acceptance criteria
- Objection type from the defined list.
- Underlying concern stated and labelled as hypothesis.
- Clarifying question provided.
- Deal impact assessed.

## Evaluation cases

**Case 1 — Price objection.**
Input: "Your platform is twice the price of what we're currently paying."
Expected: Type = Price/value; underlying concern = value not yet demonstrated; clarifying question about ROI expectation; deal impact = Significant.

**Case 2 — Timing objection.**
Input: "We're in the middle of a restructuring. Come back in 6 months."
Expected: Type = Timing; underlying concern = capacity / internal uncertainty; clarifying question about whether timing is real or a stall; deal impact = Significant or Showstopper depending on answer.

## Related skills
- [Objection Handling Coach](/skills/04-discovery-and-deals/objection-handling-coach/SKILL.md) — next step: crafting the response.
- [Pain and Impact Mapper](/skills/04-discovery-and-deals/pain-and-impact-mapper/SKILL.md) — helps address value objections.
- [Qualification Framework Mapper](/skills/04-discovery-and-deals/qualification-framework-mapper/SKILL.md) — competitive objections map to Competition dimension.
