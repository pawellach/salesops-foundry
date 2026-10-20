---
name: Personalised Outreach Planner
description: Select a specific, evidence-grounded angle for outreach to a target contact based on their account brief and context.
group: "03 — Run the Pipeline"
version: "1.0"
status: implemented
---

# Personalised Outreach Planner

## Purpose
Identify the most relevant, specific angle for reaching out to a target contact, grounded in the account brief and any available signals. Produce a structured outreach plan that a seller reviews before any message is drafted.

## When NOT to use
- Without an account brief or signal — generic outreach planning belongs in a different workflow.
- When the contact has opted out of outreach from your organisation.
- As a replacement for genuine understanding of the prospect's situation.

## Required inputs
- Account Brief for the target account (from Skill 11 or manually supplied).
- Target contact name, role, and any interaction history.

## Optional inputs
- Active signals for the account (from Signal Aggregator, Skill 19).
- Warm-path map (from Skill 23).
- Seller's stated goal for the outreach (e.g., book discovery call, share a resource).

## Step-by-step procedure

1. **Identify the strongest signal or context.** From the account brief and signals, identify the single most specific, timely, and relevant fact about this account that a seller could reference credibly. Prefer: recent trigger events (funding, hiring, product launch) > stated company initiative > role-specific pain > industry trend.
2. **Map the signal to a potential problem.** State a hypothesis about the problem or opportunity this signal suggests. Label it as a hypothesis, not a confirmed fact.
3. **Connect to seller's value proposition.** Write one sentence connecting the hypothesis to what the seller offers. Do not claim to solve the problem before discovery.
4. **Select the outreach angle.** Choose one angle: Trigger-based, Problem-hypothesis, Peer/reference (if applicable), Resource/insight share, or Cold (if no signal available; note this as the weakest option).
5. **Define the ask.** State the specific, single ask for this outreach (e.g., "15-minute call to explore whether X is a priority"). Keep it low-commitment.
6. **Note personalisation elements.** List the specific facts from the brief that should appear in the message. Flag any element that needs verification before use.
7. **Produce outreach plan document.**

## Output contract

```markdown
## Outreach Plan — Sarah Okafor / Northlight Technologies
Date: YYYY-MM-DD

**Outreach angle:** Trigger-based
**Signal used:** Northlight raised Series B (£12M) on 2026-09-15 (source: TechCrunch, supplied in brief)
**Problem hypothesis:** Post-funding, they are likely scaling their sales team and may need better pipeline visibility tooling.
**Value connection:** Our pipeline analytics platform is designed for teams scaling from 5 to 20 AEs.
**Specific ask:** 20-minute call to understand their current pipeline review process.

### Personalisation elements to include
- Reference the Series B (verified, sourced)
- Reference Sarah's role transition to CTO (verify: was she VP Eng before?)
- Do NOT reference headcount figures from LinkedIn (not in brief; verify before using)

### Angle confidence
High — trigger is recent and directly relevant to our product.
```

## Evidence and citation rules
- The angle must trace to a specific, sourced fact in the brief or a supplied signal.
- Label problem hypotheses as hypotheses; do not state them as confirmed needs.
- Flag any personalisation element that is unverified.

## Confidence/uncertainty handling
- Angle confidence = High: recent verified trigger + clear hypothesis.
- Angle confidence = Medium: older signal or indirect relevance.
- Angle confidence = Low: no signal; generic industry angle.
- State confidence level in the output.

## Safety, privacy, and compliance constraints
- Do not use personal data (personal email, home address, family info) as personalisation.
- Do not imply you know more about the prospect's internal situation than the brief warrants.
- Do not craft manipulative angles that exploit personal vulnerabilities.

## Human approval requirements
**No message is drafted or sent at this stage.** The outreach plan is reviewed and approved by the seller before the First-Touch Draft skill (Skill 25) is invoked.

## Failure modes and fallback behaviour
- **No brief available:** Return "Insufficient context for personalised plan — complete Account Brief Builder first."
- **Only generic signals available:** Produce a Low-confidence plan and flag it clearly.
- **Contact has a do-not-contact flag:** Stop and surface the flag.

## Acceptance criteria
- One specific angle is selected and justified with evidence.
- Problem hypothesis is labelled as hypothesis.
- Personalisation elements list distinguishes verified from unverified items.
- No message is drafted or sent.

## Evaluation cases

**Case 1 — Trigger-based angle.**
Input: Brief includes Series B announcement for Northlight Technologies (2026-09-15). Contact = Sarah Okafor, CTO.
Expected: Angle = Trigger-based; signal cited; hypothesis about scaling stated; confidence = High.

**Case 2 — No signals available.**
Input: Brief contains only firmographic data. No signals.
Expected: Angle = Cold (generic industry); confidence = Low; flag that personalisation is limited.

## Related skills
- [Account Brief Builder](/skills/02-account-intelligence/account-brief-builder/SKILL.md) — provides the brief.
- [First-Touch Draft](/skills/03-run-the-pipeline/first-touch-draft/SKILL.md) — next step: drafts the actual message.
- [Intent Signal Aggregator](/skills/02-account-intelligence/intent-signal-aggregator/SKILL.md) — provides signals.
