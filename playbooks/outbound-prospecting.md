---
name: Outbound Prospecting
audience: SDR, BDR, AE
skills-referenced:
  - skills/01-find-buyers/icp-builder/SKILL.md
  - skills/01-find-buyers/account-fit-scoring/SKILL.md
  - skills/01-find-buyers/territory-planner/SKILL.md
  - skills/03-run-the-pipeline/personalised-outreach-planner/SKILL.md
  - skills/03-run-the-pipeline/follow-up-sequence-builder/SKILL.md
status: implemented
---

# Playbook: Outbound Prospecting

## Overview

Pure cold outbound starts with no existing relationship and no confirmed buying signal. The quality of your ICP definition, account research, and message personalisation determines whether this is a productive activity or noise. This playbook walks through building a small, high-quality outbound list and running a focused sequence.

## When to use

- Building pipeline from scratch in a territory
- No inbound leads available or insufficient inbound volume
- Targeting a specific segment where you have a hypothesis about need

## When NOT to use

- You haven't defined your ICP (do that first)
- You have a warm list or signal data (use High-Intent Prospecting playbook)
- You're about to send bulk untargeted outreach (this playbook is for focused, personalised sequences)

## Preparation checklist

- [ ] ICP criteria defined (firmographic, technographic, situational, exclusion)
- [ ] Negative ICP / disqualification criteria defined
- [ ] Territory or segment defined
- [ ] Research sources identified (public, authorised)
- [ ] Message reviewed and approved before send
- [ ] Sequence stop rules defined (max touches, opt-out response)

---

## Step-by-step guide

### Step 1: Define and validate your ICP
Use the ICP Builder skill to turn your hypothesis into explicit, testable criteria. Include exclusions — who is NOT a fit is as important as who is.

### Step 2: Build your account list
Use the Account Search Planner skill to define where and how to find accounts matching your ICP. Research account fit before adding to the list. Aim for quality over quantity: 20 well-researched accounts beat 200 unresearched ones.

### Step 3: Score and prioritise
Run Account Fit Scoring for each account. Use the Territory Planner to prioritise by fit, potential, and your capacity. Don't pursue every account equally — tiering is essential.

### Step 4: Research each account
For Tier 1 accounts, build an account brief. Know:
- What the company does
- Who the likely buyers are (role and function — not specific names unless verifiable)
- Any relevant context (recent news, product, growth signals)
- Why they might have the problem your product solves

### Step 5: Define your outreach angle
Each account should have a specific angle — not "we help companies like yours." Angles come from: company context, industry patterns, role-specific pain, or hypothesised situation.

### Step 6: Build a bounded sequence
Use the Follow-up Sequence Builder skill. Define:
- Number of touches (3–5 is typical; more requires evidence that it works for your audience)
- Channels (email, LinkedIn — respect platform norms)
- Cadence (spacing between touches)
- Stop rules (opt-out, reply, meeting booked)
- Value added per touch (not repetitions of the same message)

### Step 7: Review all messages before sending
Never let an agent send. Review every message. Check for accuracy, tone, and relevance.

---

## Key skills to invoke

- `skills/01-find-buyers/icp-builder/SKILL.md`
- `skills/01-find-buyers/account-fit-scoring/SKILL.md`
- `skills/01-find-buyers/account-search-planner/SKILL.md`
- `skills/01-find-buyers/negative-icp-disqualification/SKILL.md`
- `skills/01-find-buyers/territory-planner/SKILL.md`
- `skills/03-run-the-pipeline/personalised-outreach-planner/SKILL.md`
- `skills/03-run-the-pipeline/first-touch-draft/SKILL.md`
- `skills/03-run-the-pipeline/follow-up-sequence-builder/SKILL.md`

---

## Common mistakes

1. **Skipping ICP definition.** Sending to "companies" without criteria wastes everyone's time and damages your sender reputation.
2. **Confusing a contact list with an account list.** Start with accounts, not contacts. Then identify who within those accounts to reach.
3. **Sending the same message five times.** A sequence should add value at each touch, not repeat the same ask.
4. **Ignoring opt-out responses.** Immediately stop all outreach on opt-out. No exceptions.
5. **Measuring success only by reply rate.** Track meeting-to-sequence ratio and pipeline-to-sequence ratio. Reply rate alone can be gamed.

---

## Example scenario

**Scenario:** SDR at Acme Corp targeting logistics companies with 100–500 employees in Central Europe.

ICP: Logistics / freight companies, 100–500 employees, operational data challenges, no existing consolidated reporting tool, using legacy ERP.

Tier 1 list (5 accounts): Northlight Technologies, Meridian Logistics, etc. (all fictional).

Northlight angle: recent Series B + data engineering hires = active tech build-out. Pain hypothesis: fragmented operational data.

Sequence: 3 touches over 14 days. Touch 1: first-touch email (signal angle). Touch 2: LinkedIn connection + note (value-add: relevant content). Touch 3: break-up email (low friction, last ask).

---

## Success indicators

- Meeting booked rate per sequence started (establish baseline, improve from there)
- % of sequences reaching Touch 3 without response (measures list quality)
- Pipeline created from outbound sequences (the ultimate measure)
