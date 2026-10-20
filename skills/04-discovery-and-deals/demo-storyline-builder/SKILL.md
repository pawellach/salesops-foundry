---
name: Demo Storyline Builder
description: Connect product capabilities to confirmed prospect needs in a narrative that flows from their world to your solution.
group: "04 — Discovery, Demos, and Deal Progression"
version: "1.0"
status: implemented
---

# Demo Storyline Builder

## Purpose
Design a demo storyline that starts in the prospect's world (their stated pain, role, context), moves through the problem, and arrives at demonstrated capabilities — rather than a feature tour. The demo tells the prospect's story, not the product's story.

## When NOT to use
- Without confirmed discovery (pain, stakeholders, context must be known).
- As a generic product walkthrough — generic demos rarely convert.
- Before Demo Readiness Review (Skill 39) has confirmed you are ready to demo.

## Required inputs
- Confirmed pain points (from Skill 34 or discovery notes).
- Contact roles and what they care about.
- The 2–3 capabilities most directly relevant to confirmed pain.

## Optional inputs
- Qualification notes (from Skill 35).
- Seller's product or service description (supplied as plain text).
- Time allocation for the demo.

## Step-by-step procedure

1. **Set the stage (prospect's world).** Open by describing the prospect's current situation back to them — as they told you. This confirms you were listening and anchors everything that follows.
2. **Introduce the tension.** State the gap between their current state and where they want to be. Use their words.
3. **Sequence the capabilities.** For each confirmed pain point, select the one capability that most directly addresses it. Order from "biggest pain first."
4. **Write the transition phrases.** Connect each capability demo to the pain it addresses: "You mentioned that X is a challenge — let me show you how we handle that."
5. **Define the "aha moment" for each capability.** What is the single most powerful thing you can show? Plan to land there, not just demo around it.
6. **Plan the closing question.** After the demo, ask: "Does this match what you were hoping to see?" — not "What do you think?" (too broad) and not "Are you ready to buy?" (too early).
7. **Produce demo storyline document.**

## Output contract

```markdown
## Demo Storyline — Northlight Technologies
Contact: Sarah Okafor (CTO) | Duration: 45 min
Date: YYYY-MM-DD

### Scene setting (2–3 min)
"Sarah, before I show you anything, let me just play back what I heard in our last conversation to make sure I've understood your situation correctly..."
- 8-person AE team, scaling post-Series B
- Monday pipeline reviews: 2 hours, still incomplete
- CEO asking for more reliable forecasts
- Currently using Salesforce custom dashboards

"Does that still reflect where you are?"

### Pain → Capability sequence

**Pain 1: 2-hour reviews with incomplete visibility**
Capability: Live deal board with AI-flagged status changes
Transition phrase: "You mentioned Monday reviews take 2 hours because you're manually chasing updates. Here's what that looks like for a team your size."
Aha moment: Show a review that would have taken 2 hours being completed in 20 minutes with automatic flagging of at-risk deals.

**Pain 2: AE miscategorisation caught too late**
Capability: Automated stage-validation rules
Transition phrase: "You also mentioned finding out deals were miscategorised after the fact. Here's how stage rules surface that in real time."
Aha moment: Show a deal that would have been miscategorised being flagged automatically.

**Pain 3: Forecast confidence for CEO**
Capability: Forecast scenario builder
Transition phrase: "Finally — for the board visibility challenge — let me show you what a one-click forecast looks like with confidence weighting."
Aha moment: Generate a forecast summary in under 60 seconds.

### Closing question
"Does what you've seen today match the problems you were hoping to solve? What's missing from what I've shown you?"

### What to avoid
- Do not open with the product; open with their situation
- Do not demo features that were not connected to a confirmed pain
- Do not rush past the aha moments to show more features
```

## Evidence and citation rules
- Every capability shown must trace to a confirmed pain point.
- Do not promise capabilities that have not been verified against the actual product.

## Confidence/uncertainty handling
- If a pain point is only partially confirmed, note it in the storyline and plan a confirmation question at the start of the demo.

## Safety, privacy, and compliance constraints
- Do not use real customer data in demo environments.
- Do not make performance claims (e.g., "saves 80% of time") without verified evidence.

## Human approval requirements
**The demo is conducted by a human.** This storyline is a preparation tool. The seller adapts it in real time.

## Failure modes and fallback behaviour
- **No confirmed pain:** Return "Insufficient discovery — cannot build a personalised storyline; use Demo Readiness Review (Skill 39) to assess readiness."
- **Generic product tour requested:** Produce a generic flow but flag that it is unlikely to convert without personalisation.

## Acceptance criteria
- Each capability demo is connected to a specific confirmed pain.
- Opening scene-setting section present.
- Closing question is defined.
- "What to avoid" section present.

## Evaluation cases

**Case 1 — Discovery-backed demo.**
Input: 3 confirmed pain points; 3 relevant capabilities; 45-min demo for CTO.
Expected: Scene-setting; 3 pain → capability transitions; aha moments defined; closing question present.

**Case 2 — No discovery context.**
Input: Request for a demo storyline with no discovery notes.
Expected: Generic flow built; prominent flag that personalisation is missing; recommendation to run discovery first.

## Related skills
- [Pain and Impact Mapper](/skills/04-discovery-and-deals/pain-and-impact-mapper/SKILL.md) — confirms pain.
- [Demo Readiness Review](/skills/04-discovery-and-deals/demo-readiness-review/SKILL.md) — pre-demo checklist.
- [Discovery Call Plan](/skills/04-discovery-and-deals/discovery-call-plan/SKILL.md) — discovery that feeds this skill.
