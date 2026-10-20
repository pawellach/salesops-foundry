---
layout: page
title: Agent Architecture
---

# Agent Architecture

SalesOps Foundry uses an orchestrator-led multi-agent architecture. All agents report to the Orchestrator; they do not communicate directly with each other.

---

## Agent roster

| Agent | Role | Key skills |
|---|---|---|
| **Orchestrator** | Sales Chief of Staff — decomposes requests, tracks state, routes to specialists, requests approval at gates | All (routing only) |
| **Research Agent** | Finds and summarises permitted, relevant sources with citation metadata | Groups 1, 2 |
| **Account Intelligence Agent** | Produces account briefs, fit assessments, and buyer hypotheses | Skills 3, 4, 11 |
| **Prospecting Agent** | Builds prioritised account lists and contact research plans | Skills 1, 2, 5, 8, 9 |
| **Signal Monitor Agent** | Normalises signals; scores relevance, freshness, confidence, and urgency | Skills 12–20 |
| **Outreach Agent** | Drafts contextual messages and sequences — never sends autonomously | Skills 24–27 |
| **Discovery & Deal Coach** | Builds call plans, qualification notes, demo storylines | Skills 31–42 |
| **Pipeline Analyst** | Analyses supplied pipeline data, identifies gaps, prepares reports | Skills 28, 29, 46–50 |
| **Sales Enablement Agent** | Turns approved knowledge into playbooks, templates, and training | Skills 43–45, 51–64 |
| **Evaluator / Red-Team Agent** | Tests outputs against rubrics and adversarial inputs independently | Skills 65–72 |
| **Safety & Privacy Reviewer** | Reviews data minimisation, injection defence, and approval-gate compliance | Skills 67–70 |

---

## Collaboration model

```
User request
    ↓
Orchestrator (decomposes, plans, tracks state)
    ↓ assigns bounded tasks with defined inputs/outputs
Specialist agents (work independently, report back)
    ↓ results consolidated by Orchestrator
Human approval gate (for any external action)
    ↓ after approval
External action (email draft sent, CRM updated)
```

Each delegated task specifies:
- Objective
- Inputs and trusted/untrusted data boundaries
- Expected output path and format
- Acceptance criteria
- Prohibited actions

---

## Model routing

See [docs/MODEL_STRATEGY.md](../docs/MODEL_STRATEGY.md) for the full routing policy. Summary:
- **Orchestration, adversarial review, release gates:** Strongest available model
- **Account briefs, discovery plans, outreach drafts:** Mid-tier reasoning model
- **Bulk classification, simple formatting:** Fast, low-cost model

All model assignments are configurable; no model name is hard-coded in skill files.

---

## Approval tiers

| Tier | Examples | Gate |
|---|---|---|
| Green | File reads, draft creation, local analysis | None |
| Amber | Outreach drafts, CRM field mapping proposals | Human reviews before external action |
| Red | Sending email, publishing repo, writing to CRM | Explicit owner confirmation |
