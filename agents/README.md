# Agents

Each agent has a defined role, scope, set of allowed skills and tools, and a list of prohibited actions.

## Agent roster

| Agent | File | Role |
|---|---|---|
| Orchestrator | `orchestrator.md` | Sales Chief of Staff — decomposes requests, tracks state, routes to specialists |
| Research Agent | `research-agent.md` | Finds and summarises permitted, relevant sources |
| Account Intelligence | `account-intelligence-agent.md` | Account briefs, fit assessments, buyer hypotheses |
| Prospecting Agent | `prospecting-agent.md` | Account lists, prioritisation, contact research plans |
| Signal Monitor | `signal-monitor-agent.md` | Normalises signals, scores relevance and freshness |
| Outreach Agent | `outreach-agent.md` | Drafts messages and sequences — never sends autonomously |
| Discovery & Deal Coach | `discovery-agent.md` | Call plans, qualification notes, demo storylines |
| Pipeline Analyst | `pipeline-analyst-agent.md` | Pipeline analysis, gap detection, reports |
| Sales Enablement | `sales-enablement-agent.md` | Playbooks, training assets, onboarding |
| Evaluator / Red-Team | `evaluator-agent.md` | Independent testing against rubrics and adversarial inputs |
| Safety & Privacy Reviewer | `safety-reviewer-agent.md` | Data minimisation, injection defence, approval-gate compliance |

## Collaboration protocol

All agents report results to the Orchestrator. Agents do not communicate directly with each other. Each delegated task specifies: objective, inputs, trusted/untrusted data boundaries, expected output path and format, acceptance criteria, and prohibited actions.

See [docs/ARCHITECTURE.md](../docs/ARCHITECTURE.md) for the full collaboration model.
