---
name: Demo Readiness Review
description: Check whether the seller is ready to run a demo that will advance the deal — flag missing proof, stakeholders, and data.
group: "04 — Discovery, Demos, and Deal Progression"
version: "1.0"
status: implemented
---

# Demo Readiness Review

## Purpose
Before investing time in a demo, confirm that the conditions for a productive demo exist: the right people will attend, pain has been confirmed, the demo can be personalised, and a next step has been defined. A demo before these conditions are met rarely advances a deal.

## When NOT to use
- After the demo has already been scheduled with no flexibility — in that case, flag gaps as risks, not blockers.
- For introductory calls or webinars that are not targeted demos.

## Required inputs
- Discovery notes or qualification summary.
- List of planned attendees for the demo.
- Demo type: product walkthrough, proof of concept, or technical deep-dive.

## Optional inputs
- Demo storyline (from Skill 38, if already built).
- Access to a demo environment or test data availability.

## Step-by-step procedure

1. **Check stakeholder attendance.** Is the economic buyer (or a champion who can influence them) attending? If not, flag this as a High risk.
2. **Check pain confirmation.** Are at least 2 confirmed pain points documented from discovery? If not, flag as a High risk.
3. **Check personalisation readiness.** Can the demo be tailored to their context (their terminology, their use case, their pain)? If not, flag as Medium risk.
4. **Check demo environment.** Is there a clean, working demo environment available? Is there relevant demo data? Flag if not.
5. **Check next-step definition.** Has the seller defined what they will ask for at the end of the demo? If not, flag as Medium risk.
6. **Check proof availability.** If the prospect is likely to ask "do you have customers like us?", does the seller have approved case studies or references to share? Flag if not.
7. **Produce readiness report with go/no-go recommendation.**

## Output contract

```markdown
## Demo Readiness Review — Northlight Technologies
Demo type: Product walkthrough (45 min) | Planned date: 2026-10-28
Date of review: YYYY-MM-DD

### Readiness checklist

| Check | Status | Notes |
|---|---|---|
| Economic buyer attending | ❌ Risk | Only Sarah (CTO) confirmed; CFO not invited |
| Pain confirmed (≥2 points) | ✅ Ready | 3 confirmed pain points from discovery |
| Demo personalisation possible | ✅ Ready | Storyline built for Northlight's context |
| Demo environment available | ✅ Ready | Demo org configured; sample data loaded |
| Next-step ask defined | ✅ Ready | Plan to ask for mutual action plan agreement |
| Proof/reference available | ⚠️ Risk | No approved case study for Series B SaaS; seller to check with marketing |

### Go / No-go recommendation
**Proceed with caution.** Two risks to address before the demo:
1. Invite Sarah to bring CFO or delegate — even a brief intro at the start is better than not having them.
2. Prepare a one-liner for peer references in case the question arises.

### If you cannot resolve the risks
Proceed but be prepared: (a) ask Sarah during the demo how to involve the economic buyer, and (b) do not promise a reference you don't have.
```

## Evidence and citation rules
- Readiness checks are based on the supplied discovery notes and attendee list only.
- Do not assume checks are passed unless evidence is explicit.

## Confidence/uncertainty handling
- "Partial" is a valid status for checks where some but not all conditions are met.
- A demo with High risks is not necessarily cancelled — it is flagged so the seller goes in with eyes open.

## Safety, privacy, and compliance constraints
- Do not use real customer data in demo environments without consent.
- Do not promise reference customers without confirming their availability and consent.

## Human approval requirements
**The go/no-go decision is made by the seller.** This skill provides a recommendation; the seller decides whether to proceed, postpone, or address the gaps.

## Failure modes and fallback behaviour
- **No discovery notes:** All checks fail; recommend completing discovery before booking a demo.
- **Demo already booked and immovable:** Produce a risk-aware preparation note instead of a go/no-go.

## Acceptance criteria
- All 6 checks are addressed.
- Go/no-go recommendation is explicit.
- Risks are rated (High/Medium).
- Mitigation suggestions provided for each risk.

## Evaluation cases

**Case 1 — Ready to demo.**
Input: Economic buyer confirmed attending; 3 pain points; personalised storyline built; demo environment ready.
Expected: All checks pass (or minor risks only); recommendation = Go.

**Case 2 — Not ready.**
Input: No discovery completed; generic attendee list; no next-step defined.
Expected: Multiple High risks; recommendation = No-go until discovery completed.

## Related skills
- [Demo Storyline Builder](/skills/04-discovery-and-deals/demo-storyline-builder/SKILL.md) — builds the demo narrative.
- [Discovery Call Plan](/skills/04-discovery-and-deals/discovery-call-plan/SKILL.md) — provides the discovery foundation.
- [Mutual Action Plan](/skills/04-discovery-and-deals/mutual-action-plan/SKILL.md) — the likely next step after a successful demo.
