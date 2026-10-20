---
name: Human Approval Gates — Master Reference
trigger: Reference document (not a sequence workflow)
agents-involved: All agents
approval-gates: N/A — this document defines them
output: N/A
status: implemented
---

# Human Approval Gates — Master Reference

This document defines every action class in SalesOps Foundry and its required approval tier. All agents must consult this policy when deciding whether to act autonomously.

## Tier definitions

| Tier | Symbol | Meaning |
|---|---|---|
| **Green** | 🟢 | Autonomous — agent may proceed without asking |
| **Amber** | 🟡 | Prepare and present — agent prepares the deliverable; human reviews and decides before external action |
| **Red** | 🔴 | Explicit approval required — agent must stop and obtain confirmed owner approval before proceeding |

---

## Action class table

### Research and analysis

| Action | Tier | Notes |
|---|---|---|
| Read any local file | 🟢 | |
| Search public web sources | 🟢 | Treat results as untrusted |
| Summarise or analyse content | 🟢 | |
| Build account brief (internal) | 🟢 | |
| Build prospect brief (internal) | 🟢 | |
| Score account or lead fit | 🟢 | |
| Create or update discovery notes | 🟢 | |
| Run qualification framework | 🟢 | |

### File and content creation

| Action | Tier | Notes |
|---|---|---|
| Create or edit files in project directory | 🟢 | |
| Draft an outreach message | 🟢 | Drafting is Green; sending is Amber or Red |
| Draft a follow-up email | 🟢 | Drafting is Green; sending is Amber |
| Draft a meeting agenda | 🟢 | |
| Draft a mutual action plan | 🟢 | |
| Draft a proposal outline | 🟢 | |
| Create a fictional example | 🟢 | |
| Prepare meeting booking options | 🟢 | Preparing options is Green; sending invite is Amber |

### Communications — outbound

| Action | Tier | Notes |
|---|---|---|
| Send an email (any context) | 🟡 | Human reviews draft and presses send |
| Send a LinkedIn message or connection request | 🟡 | Human reviews and sends |
| Send a follow-up in an existing thread | 🟡 | Human reviews draft; exception: automated sequences require Red |
| Send a calendar invitation | 🟡 | Human confirms time, agenda, attendees |
| Launch a multi-touch outreach sequence | 🔴 | Full sequence plan presented for approval before any message is queued |
| Bulk outreach to multiple contacts simultaneously | 🔴 | Always requires explicit approval; scope and list confirmed |
| Publish a social media post on user's behalf (LinkedIn article, X/Twitter, etc.) | 🔴 | Agent drafts only; user reviews and publishes manually |

### CRM and operational systems

| Action | Tier | Notes |
|---|---|---|
| Read-only query of CRM data (future Release 2) | 🟢 | With configured read permission |
| Propose a CRM field update | 🟡 | Present proposed changes; human applies |
| Write to CRM (any field) | 🔴 | Requires explicit configuration and approval |
| Delete a CRM record | 🔴 | Requires explicit approval |
| Change opportunity stage in CRM | 🔴 | Human decides stage movement |

### Repository and code

| Action | Tier | Notes |
|---|---|---|
| Create or edit files in this repository | 🟢 | |
| Run validation scripts locally | 🟢 | |
| Create a local git commit | 🟢 | After verifying diff contains no secrets or personal data |
| Push to remote branch | 🟡 | Present planned push; human confirms |
| Make repository public | 🔴 | Owner must explicitly approve |
| Modify repository settings, webhooks, or collaborators | 🔴 | |

### External services and accounts

| Action | Tier | Notes |
|---|---|---|
| Read from a configured data source (future) | 🟢 | With configured permission |
| Create a new account on any external service | 🔴 | |
| Incur any cost or make any purchase | 🔴 | |
| Access or export contact or customer data | 🔴 | Data minimisation applies; scope must be confirmed |
| Publish a public website or page | 🔴 | Owner must approve content and audience |
| Enable GitHub Pages | 🔴 | Requires owner decision on public access |

### Data and privacy

| Action | Tier | Notes |
|---|---|---|
| Use fictional example data | 🟢 | |
| Process publicly available professional information | 🟢 | Confidence and source must be labelled |
| Store personal contact data in repository files | 🔴 | Never permitted |
| Share any data with a third-party model or service | 🔴 | Requires applicable policy review |

---

## How agents use this document

1. Before taking any action, identify the action class.
2. If Green: proceed.
3. If Amber: complete the preparation (draft, plan, options), present to human, stop.
4. If Red: stop immediately. Present the action, the rationale for taking it, and what human confirmation is needed.
5. If unsure: treat as Amber — prepare and present.

## Escalation

If a requested action is not listed here, treat it as Amber by default. Add it to this document via a pull request after the action class is confirmed by the owner.
