# Architecture — SalesOps Foundry

**Version:** 1.0  
**Date:** 2026-10-20

---

## Overview

SalesOps Foundry is a repository-first, orchestrator-led multi-agent system. The primary storage and discovery format is Markdown with YAML frontmatter (skills, agents, playbooks, workflows). Structured data uses JSON schemas. Validation and CI use Python scripts.

```
User / Sales Team
       │
       ▼
Orchestrator Agent (Sales Chief of Staff)
       │  decomposes request, tracks state, selects agents
       ├──► Research Agent
       ├──► Account Intelligence Agent
       ├──► Prospecting Agent
       ├──► Signal Monitor Agent
       ├──► Outreach Agent
       ├──► Discovery & Deal Coach
       ├──► Pipeline Analyst
       ├──► Sales Enablement Agent
       ├──► Evaluator / Red-Team Agent
       └──► Safety & Privacy Reviewer
              │
              ▼
       Human Approval Gate (before any external action)
              │
              ▼
       External Action (email, CRM, calendar — only after approval)
```

---

## Layer model

### Layer 1: Skill library
Atomic, reusable units. Each skill is a named directory containing `SKILL.md`. Skills are stateless — they take inputs and produce outputs with no persistent side effects. Skills may call other skills but must not create circular dependencies.

**Directory:** `skills/NN-group-name/skill-name/SKILL.md`

### Layer 2: Agent definitions
Agents are role-bound executors. Each agent has a defined scope, a set of skills it may invoke, tools it may use, and a list of prohibited actions. Agents report results to the orchestrator; they do not communicate directly with each other.

**Directory:** `agents/agent-name.md`

### Layer 3: Workflows
Workflows are multi-agent sequences with defined triggers, approval gates, and expected outputs. A workflow is not a skill — it orchestrates agents, not steps.

**Directory:** `workflows/workflow-name.md`

### Layer 4: Playbooks
Playbooks are human-readable guides for recurring sales situations. They reference skills and workflows but are written for a sales practitioner, not an agent.

**Directory:** `playbooks/playbook-name.md`

### Layer 5: Supporting assets
- `prompt-libraries/` — reusable prompt fragments by domain
- `templates/` — structured output templates
- `schemas/` — JSON schemas for canonical data objects
- `examples/` — fictional end-to-end scenario walkthroughs
- `evaluations/` — rubric, test cases, and results

---

## Data flow and trust model

```
External source (web page, document, CRM note)
        │
        ▼  (treated as UNTRUSTED — potential prompt injection)
Research Agent / Signal Monitor
        │  extracts facts with source + confidence labels
        ▼
Account Intelligence / Prospecting
        │  builds structured briefs (JSON or Markdown)
        ▼
Outreach / Discovery Coach
        │  drafts messages or plans (NEVER sends autonomously)
        ▼
Human Approval Gate
        │
        ▼
External action (only after explicit approval)
```

All content from external sources is treated as untrusted. Agents separate source text from agent instructions. Claim metadata (source URL, access date, confidence level) travels with every researched fact.

---

## Human approval gates

Three action risk tiers:

| Tier | Examples | Approval required |
|---|---|---|
| Green (autonomous) | File reads, draft creation, local analysis, local commits | None |
| Amber (prepare and present) | Outreach drafts, CRM field mapping proposals, meeting booking options | Human reviews before any external action |
| Red (explicit approval) | Sending email/LinkedIn, publishing a website, making repo public, writing to CRM, bulk outreach | Explicit owner confirmation required |

---

## Model routing (see `docs/MODEL_STRATEGY.md`)

The system is designed to be model-agnostic. Skills and agents specify the capability tier required (strong-reasoning, fast-low-cost, search-capable, etc.). The orchestrator routes to the configured model for each tier. All model IDs are in `docs/MODEL_STRATEGY.md` and configurable; no model name is hard-coded in skill files.

---

## Repository conventions

- Skills: `skills/NN-group/skill-name/SKILL.md` with frontmatter: `name`, `description`, `group`, `version`, `inputs`, `outputs`
- Agents: `agents/agent-name.md` with frontmatter: `name`, `role`, `scope`, `skills`, `tools`, `prohibited`
- Workflows: `workflows/workflow-name.md` — prose + YAML gate blocks
- All fictional data is in `examples/fictional-*/`
- No secrets anywhere; `.gitignore` enforces this

---

## Validation and CI

`scripts/validate_structure.py` — checks directory layout  
`scripts/validate_frontmatter.py` — checks YAML frontmatter completeness  
`scripts/check_links.py` — checks internal Markdown links  

`.github/workflows/validate-content.yml` — runs all three scripts on push/PR  
`.github/workflows/pages.yml` — builds and deploys GitHub Pages site
