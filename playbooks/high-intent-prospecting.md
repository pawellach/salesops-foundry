---
name: High-Intent Prospecting
audience: SDR, BDR, AE
skills-referenced:
  - skills/02-account-intelligence/intent-signal-aggregator/SKILL.md
  - skills/02-account-intelligence/signal-to-action-prioritiser/SKILL.md
  - skills/01-find-buyers/buying-trigger-research/SKILL.md
  - skills/03-run-the-pipeline/personalised-outreach-planner/SKILL.md
status: implemented
---

# Playbook: High-Intent Prospecting

## Overview

High-intent prospecting focuses your time on accounts that are showing active buying signals right now: a funding round, a new executive hire, a job posting that indicates a relevant initiative, a product launch, or a competitor displacement. These accounts are worth prioritising because the timing is right — but signals must be verified and the outreach must be grounded in evidence, not assumptions.

## When to use

- You have a list of tracked accounts and want to find the ones most likely to buy now
- A monitoring tool, alert, or colleague has surfaced a signal event
- You want to prioritise your week's outreach around timing rather than volume

## When NOT to use

- You have no account brief or ICP criteria defined yet (build those first)
- You're doing pure cold outbound with no signal data (use Outbound Prospecting playbook)
- The signal is more than 30 days old without any follow-through

## Preparation checklist

- [ ] ICP criteria defined and documented
- [ ] Target account list available (even if rough)
- [ ] Signal sources configured or manually reviewed (news, LinkedIn, job boards)
- [ ] Account brief template ready
- [ ] Outreach draft reviewed and approved before any send

---

## Step-by-step guide

### Step 1: Identify the signal
Use the Buying-Trigger Research skill or review your configured signal feed. For each signal, record:
- Event type (hiring, funding, product launch, etc.)
- Source URL and access date
- Confidence level (high / medium / low)
- Staleness (how recent?)

### Step 2: Verify and score relevance
Not every signal is worth acting on. Score it:
- Does it indicate a problem your product solves?
- Is it from a decision-maker-level change or a junior hire?
- Is it in a buying window (e.g., new budget year, post-funding)?

Discard low-relevance or unverifiable signals. Do not act on rumours.

### Step 3: Build or refresh the account brief
If you don't have a current brief, run the Account Brief Builder skill. Focus on:
- Confirmed company facts (size, sector, recent news)
- Likely buyer committee roles
- Known or inferred pain areas

### Step 4: Choose your angle
Use the Signal-to-Action Prioritiser to connect the signal to a relevant message angle. The angle must:
- Reference something verifiable (not "I heard you might be looking for…")
- Be relevant to the signal (not a generic product pitch)
- Respect what you do and don't know

### Step 5: Draft and review outreach
Use the Personalised Outreach Planner and First-Touch Draft skills. Review the draft yourself before sending. Check:
- Does it reference the signal correctly?
- Does it make a claim you can back up?
- Is the ask clear and low-friction?

### Step 6: Send (with your judgment applied)
Send the approved message. Log the signal and outreach in your tracker.

---

## Key skills to invoke

- `skills/02-account-intelligence/intent-signal-aggregator/SKILL.md`
- `skills/02-account-intelligence/signal-to-action-prioritiser/SKILL.md`
- `skills/01-find-buyers/buying-trigger-research/SKILL.md`
- `skills/03-run-the-pipeline/personalised-outreach-planner/SKILL.md`
- `skills/03-run-the-pipeline/first-touch-draft/SKILL.md`

---

## Common mistakes

1. **Acting on stale signals.** A funding round from 6 months ago is cold. Verify recency before referencing it.
2. **Over-personalising with guesswork.** "I saw you're probably looking to expand your team" when you only saw one job ad is an inference, not a fact. Label it as such or don't say it.
3. **Confusing signal with intent.** A job ad for a data engineer doesn't mean they're buying your product. It means they might have a relevant problem. Stay curious, not assumptive.
4. **Sending before reviewing.** The Outreach Agent drafts; you review. Never skip this step.
5. **Chasing every signal.** Quality beats volume. Three well-researched, signal-grounded outreach messages beat twenty generic ones.

---

## Example scenario

**Northlight Technologies** (fictional logistics software, 200 employees) announces a new VP of Operations on LinkedIn and simultaneously posts 3 data engineering roles.

Signal assessment: high confidence (public announcements), highly relevant (VP hire + tech build-out signals active initiative), fresh (last week).

Angle: New VP is likely establishing their team and priorities. Data engineering hires suggest a data infrastructure project. Acme Corp (fictional) helps logistics companies consolidate operational data.

First touch to VP Operations: references their recent start, acknowledges the team build-out, asks about data infrastructure priorities. Short, specific, no product dump.

---

## Success indicators

- Response rate from high-intent accounts measurably higher than cold baseline (track and compare)
- Meetings booked reference the signal as the reason for engaging
- Disqualification happens faster (signals surface poor fit quickly)
