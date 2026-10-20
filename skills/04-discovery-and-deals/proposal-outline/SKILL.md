---
name: Proposal Outline
description: Structure a proposal from verified requirements — no unsupported claims, no generic filler.
group: "04 — Discovery, Demos, and Deal Progression"
version: "1.0"
status: implemented
---

# Proposal Outline

## Purpose
Create a proposal outline that is structured around the prospect's confirmed requirements. The proposal tells their story: their situation, the problem it creates, the solution and why it fits, the investment, the expected outcome, and the next step.

## When NOT to use
- Without confirmed requirements from discovery and qualification.
- To produce a generic template sent to all prospects — proposals must be personalised to be effective.

## Required inputs
- Pain and impact map (from Skill 34).
- Qualification notes (from Skill 35) — especially metrics, decision criteria, and stakeholders.
- Proposed solution description (seller-supplied: what is being proposed and at what price tier).

## Optional inputs
- Mutual Action Plan (from Skill 40) — for the next steps section.
- Approved case studies or references (seller-supplied).

## Step-by-step procedure

1. **Executive summary section.** 1 paragraph: their situation, the problem, the proposed solution, and the expected outcome. Written for the economic buyer who may not attend every meeting.
2. **Their situation and challenge.** Mirror back what you confirmed in discovery. Use their language. Cite confirmed facts, not inferences.
3. **Why now.** Connect the proposal to any known timing driver (funding round, growth milestone, compliance deadline). If none exists, acknowledge that and focus on opportunity cost.
4. **Proposed solution.** What is proposed, at what scope. One paragraph. Connect each element to a specific confirmed requirement.
5. **Expected outcomes.** What the prospect can reasonably expect. Use confirmed metrics where available; use benchmarks labelled as benchmarks when not.
6. **Investment.** Pricing as provided by the seller. Do not invent prices. Note any assumptions (e.g., based on 10 AEs; price scales with team size).
7. **Why us (if relevant).** 2–3 specific points relevant to this prospect's stated criteria. Not a generic company pitch.
8. **Next steps.** Reference the Mutual Action Plan if available. Name the specific next action and who owns it.
9. **Produce proposal outline (not a finished proposal — the seller writes the final version).**

## Output contract

```markdown
## Proposal Outline — Northlight Technologies
Prepared by: Alex Kowalski | Date: YYYY-MM-DD
For: Sarah Okafor (CTO), [CFO name TBC]

---
### 1. Executive summary
Northlight Technologies is scaling its sales team post-Series B and facing two compounding challenges: pipeline review meetings that consume ~2 hours per week while missing critical deal updates, and forecast inaccuracy that is creating pressure from the board. This proposal outlines how [Seller Company]'s pipeline management platform addresses both challenges for a team of Northlight's size and growth trajectory.

---
### 2. Your situation and challenge
[Confirmed facts from discovery — seller to verify and expand]
- Current state: 8 AEs, Salesforce CRM, custom dashboards
- Challenge 1: Monday pipeline reviews take 2 hours, still miss updates (Stated, 2026-10-22 call)
- Challenge 2: AE miscategorisation caught too late (Stated)
- Challenge 3: CEO requiring more reliable forecasts (Stated)

---
### 3. Why now
Post-Series B, the AE team is expected to grow from 8 to ~15 in the next 12 months. The current manual process does not scale. Addressing this before headcount doubles avoids a more disruptive transition later.

---
### 4. Proposed solution
[Seller to describe specific product/tier proposed here]
Key elements and why they fit:
- Live deal board → addresses 2-hour review time
- Automated stage validation → addresses miscategorisation
- Forecast scenario builder → addresses board visibility requirement

---
### 5. Expected outcomes
[Seller to complete with verified benchmarks or leave as questions to answer in the business case]
- Time saved in pipeline reviews: [estimate based on similar teams — label as estimate]
- Forecast accuracy improvement: [placeholder — benchmark data needed]

---
### 6. Investment
[Seller to insert pricing here]
Note: Pricing is based on a team of [X] AEs; confirm final headcount before presenting.

---
### 7. Why [Seller Company]
[Seller to add 2–3 points specific to Northlight's stated decision criteria]

---
### 8. Next steps
Per the Mutual Action Plan:
1. Seller sends this proposal to Sarah and CFO by [date]
2. Review meeting: [date TBC]
3. Technical deep-dive: [date TBC]
```

## Evidence and citation rules
- Every item in "Your situation and challenge" must trace to a stated or confirmed fact.
- Expected outcomes labelled as estimates unless prospect supplied the numbers.

## Confidence/uncertainty handling
- Flag any section where data is missing and recommend completing it before sending.

## Safety, privacy, and compliance constraints
- Do not include competitor disparagement.
- Do not make unverified performance claims.
- Pricing must come from the seller; do not invent prices.

## Human approval requirements
**This is an outline, not a finished proposal.** The seller writes, reviews, and approves the final document before sending. This skill does not send the proposal.

## Failure modes and fallback behaviour
- **No discovery data:** Return error; a proposal without confirmed requirements is generic and likely ineffective.
- **Pricing not supplied:** Leave pricing section as a placeholder and flag.

## Acceptance criteria
- All 8 sections present.
- Executive summary present.
- "Your situation" section uses confirmed facts only.
- Pricing section explicitly labelled as seller-supplied / placeholder.
- No fabricated metrics.

## Evaluation cases

**Case 1 — Full discovery available.**
Input: Pain map with 3 confirmed pains; qualification notes; seller describes solution (Team plan, £2k/month/10 users).
Expected: All 8 sections populated; confirmed facts cited; pricing as supplied; next steps reference MAP.

**Case 2 — Minimal discovery.**
Input: Account brief only; no discovery notes; pricing known.
Expected: Proposal outline with heavy placeholders in sections 2–5; flag that discovery data is missing; recommend completing discovery before sending.

## Related skills
- [Pain and Impact Mapper](/skills/04-discovery-and-deals/pain-and-impact-mapper/SKILL.md) — inputs for sections 2–5.
- [Mutual Action Plan](/skills/04-discovery-and-deals/mutual-action-plan/SKILL.md) — feeds section 8.
- [Negotiation Planner](/skills/04-discovery-and-deals/negotiation-planner/SKILL.md) — next step if the proposal generates commercial pushback.
