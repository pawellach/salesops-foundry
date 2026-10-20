---
name: Objection Handling Coach
description: Propose ethical, evidence-based responses to classified objections — without pressure tactics or manipulation.
group: "04 — Discovery, Demos, and Deal Progression"
version: "1.0"
status: implemented
---

# Objection Handling Coach

## Purpose
After an objection has been classified, generate one or more candidate responses for the seller to choose from, evaluate, and adapt. Responses must be honest, evidence-based, and non-manipulative.

## When NOT to use
- Without a classified objection (Skill 36 must run first).
- To produce scripted lines for bypassing legitimate prospect concerns.
- When the objection is a genuine showstopper — in that case, the response is an honest acknowledgement, not a counter.

## Required inputs
- Objection classification output (from Skill 36).
- Account Brief or discovery notes (to ground the response in real context).

## Optional inputs
- Reference customers or case studies (fictional for examples; seller supplies real ones).
- Pain and impact map (from Skill 34).

## Step-by-step procedure

1. **Review the classification.** Note the objection type, underlying concern, clarifying question, and deal impact.
2. **If deal impact is Showstopper:** Draft an honest acknowledgement response and recommend disqualifying rather than continuing. Do not draft a persuasion attempt.
3. **If deal impact is Significant or Minor:** Draft a 3-step response:
   - **Acknowledge:** Show you heard and understood the concern. Do not dismiss or deflect.
   - **Clarify:** Ask the clarifying question from the classification. Do not respond to the surface objection before understanding the root.
   - **Respond:** Only after the clarifying question is answered (hypothetically) — provide one evidence-based response per likely answer.
4. **Offer a second candidate response** if a different framing might suit a different personality or relationship stage.
5. **Flag what NOT to say.** List tactics that would be manipulative or undermine trust.

## Output contract

```markdown
## Objection Handling Coach — Northlight Technologies
Objection: "We already have Salesforce dashboards for this."
Type: Competitor / Status quo

---
### Response A (recommended)

**Acknowledge:** "That's completely fair — Salesforce is a big investment and you've clearly built something on it."

**Clarify first:** "Before I say anything more, I'm curious — what does your Salesforce setup give you today, and is there anything it doesn't do well that prompted you to take this call?"

**Respond (if gap exists):** "What we typically see is that Salesforce is great for data storage and reporting, but the live, collaborative pipeline review experience is where teams run into friction. If that's what you're experiencing, that's exactly what we focus on."

**Respond (if no gap):** "If Salesforce is working well for you, it might not be the right moment for this. Would it be worth picking this up when you hit a scale point where the current setup gets harder to manage?"

---
### Response B (more direct)
"The companies we work best with often start with Salesforce and reach a point where it's not quite enough for the kind of review process a growing team needs. What's driving the Monday 2-hour review time — is that a Salesforce limitation or a process one?"

---
### What NOT to say
- "Salesforce is not built for this" — too dismissive; may damage trust if Sarah's team built the dashboards
- "Our customers who switched from Salesforce all saw [X]% improvement" — do not cite metrics unless you have verified, approved case studies
- "Are you sure you're getting value from Salesforce?" — feels confrontational at this stage
```

## Evidence and citation rules
- Responses must not cite metrics, case studies, or performance claims unless they are verified and the seller has approved them for use.
- Fictional case study references in this template use placeholders only.

## Confidence/uncertainty handling
- If the clarifying question would likely reveal the objection is valid, note that honestly.
- Do not coach responses designed to wear down a legitimate concern.

## Safety, privacy, and compliance constraints
- No response may use psychological pressure, false scarcity, or manufactured urgency.
- No response may misrepresent the product's capabilities.
- If the objection involves a legal, compliance, or data privacy concern, recommend involving a specialist rather than handling it as a routine objection.

## Human approval requirements
**No response is sent by this skill.** The seller reviews the candidate responses, adapts them to their voice and relationship, and delivers them in the actual conversation.

## Failure modes and fallback behaviour
- **Showstopper objection:** Produce an honest disqualification acknowledgement; do not produce a rebuttal.
- **Classification missing:** Return error; run Objection Classifier (Skill 36) first.

## Acceptance criteria
- Response follows Acknowledge → Clarify → Respond structure.
- At least 2 candidate responses provided.
- "What NOT to say" list included.
- No manipulative tactics recommended.

## Evaluation cases

**Case 1 — Status quo objection.**
Input: "We already have Salesforce dashboards." Classification: Competitor/status quo; underlying concern = sunk cost + ownership.
Expected: Acknowledge + clarify structure; two candidates; no dismissal of Salesforce; what-not-to-say list.

**Case 2 — Showstopper (genuine).**
Input: "We've just signed a 3-year contract with a direct competitor." Classification: Showstopper.
Expected: Honest acknowledgement; recommendation to disqualify or revisit at contract renewal; no rebuttal.

## Related skills
- [Objection Classifier](/skills/04-discovery-and-deals/objection-classifier/SKILL.md) — prerequisite.
- [Pain and Impact Mapper](/skills/04-discovery-and-deals/pain-and-impact-mapper/SKILL.md) — evidence for value objections.
- [Negotiation Planner](/skills/04-discovery-and-deals/negotiation-planner/SKILL.md) — for late-stage objections related to terms.
