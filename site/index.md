---
layout: home
title: SalesOps Foundry
---

# SalesOps Foundry

**A modular, human-governed AI operating system for modern sales teams.**

> ⚠️ **Status: MVP in development.** Skills are implemented and documented. Evaluation iterations are in progress. See the [Roadmap](/roadmap) for what is implemented vs. planned.

---

## The problem

Small sales teams work without a dedicated sales-operations function. They have access to powerful AI models but no structured, safe, maintainable way to apply them across the full sales lifecycle — from ICP definition and account research through outreach, discovery, deal progression, and forecasting.

Most "AI sales" prompts are monolithic, untested, and unsafe for autonomous execution. SalesOps Foundry is different.

---

## What SalesOps Foundry gives you

- **72 skills** covering the full sales lifecycle across 7 groups
- **11 agent definitions** with defined roles, tools, and approval gates
- **8 end-to-end workflows** from account selection to weekly pipeline review
- **9 playbooks** for SDRs, AEs, managers, and founders
- **Human-governed by design** — no autonomous emails, CRM writes, or bulk outreach
- **Evidence-based** — every researched claim carries a source, date, and confidence label

---

## Who it's for

| Role | Key workflows |
|---|---|
| **SDR / BDR** | ICP Builder, Fit Scoring, Signal Monitor, First-Touch Draft |
| **Account Executive** | Discovery Call Plan, Qualification Mapper, Demo Storyline, Mutual Action Plan |
| **Sales Manager** | Pipeline Hygiene Audit, Forecast Challenge, Win/Loss Review |
| **Founder** | End-to-end: research → outreach → discovery → pipeline |
| **RevOps / Enablement** | Metrics Dictionary, CRM Field Mapping, Experiment Designer |

---

## Quick start

```bash
git clone https://github.com/pawellach/salesops-foundry.git
cd salesops-foundry
python scripts/validate_structure.py
```

Then in Claude Code:
```
Use skills/01-find-buyers/icp-builder/SKILL.md
```

See [Getting Started](/getting-started) for the full setup guide.

---

## Disclaimer

This is a toolkit, not a guarantee of sales results. All outputs require human review before external use. AI-generated messages must be approved before sending.
