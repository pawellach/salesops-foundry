# SalesOps Foundry

> A modular, human-governed AI operating system for modern sales teams.

SalesOps Foundry is an open toolkit that helps small sales teams perform the work of a much larger, well-coordinated team — by directing AI agents safely across the full sales lifecycle, from ICP definition and account research through outreach, discovery, deal progression, forecasting, and continuous improvement.

**Status:** MVP in development. See the [Roadmap](docs/ROADMAP.md) for what is implemented vs. planned.

---

## Who is this for?

| Role | What you get |
|---|---|
| **SDR / BDR** | ICP Builder, Account Fit Scoring, Signal Monitor, First-Touch Draft, Follow-up Sequence |
| **Account Executive** | Discovery Call Plan, Qualification Framework Mapper, Demo Storyline Builder, Mutual Action Plan |
| **Sales Manager** | Pipeline Hygiene Audit, Weekly Pipeline Report, Forecast Challenge, Win/Loss Review |
| **Founder doing early sales** | Founder-Led Sales Coach, all core workflows end-to-end |
| **RevOps / Enablement** | Sales Metrics Dictionary, CRM Field Mapping, Data Quality Rules, Experiment Designer |

---

## Quick start

**Prerequisites:** Git, [Claude Code](https://claude.ai/code) (or another SKILL.md-compatible agent runtime).

```bash
git clone https://github.com/pawellach/salesops-foundry.git
cd salesops-foundry
```

Then in Claude Code, reference a skill directly:

```
Use skills/01-find-buyers/icp-builder/SKILL.md to define our ICP for B2B SaaS in the mid-market segment.
```

Or run a full workflow:

```
Use workflows/account-to-meeting.md for Northlight Technologies.
```

See [docs/INSTALLATION.md](docs/INSTALLATION.md) for detailed setup and [docs/OPERATING_GUIDE.md](docs/OPERATING_GUIDE.md) for usage patterns.

---

## What's inside

```
salesops-foundry/
├── agents/          11 agent definitions (Orchestrator + 10 specialists)
├── skills/          72 skills across 7 groups
│   ├── 01-find-buyers/
│   ├── 02-account-intelligence/
│   ├── 03-run-the-pipeline/
│   ├── 04-discovery-and-deals/
│   ├── 05-sales-enablement/
│   ├── 06-revenue-operations/
│   └── 07-quality-and-safety/
├── workflows/       8 end-to-end workflows
├── playbooks/       9 sales playbooks
├── prompt-libraries/ Reusable prompt fragments by domain
├── templates/       10 structured output templates
├── schemas/         4 JSON schemas for canonical data objects
├── examples/        3 fictional end-to-end scenarios
├── evaluations/     Rubric, test cases, and iteration results
├── docs/            Planning, architecture, and operating docs
└── site/            GitHub Pages site draft
```

---

## Design principles

- **Modular:** Each skill is independent. Add or replace without touching others.
- **Human-governed:** Every consequential external action requires human approval. No autonomous emails, CRM writes, or bulk outreach.
- **Evidence-based:** Researched claims carry source, date, and confidence label. Skills distinguish facts from inferences.
- **CRM-agnostic:** MVP works with local files and manually supplied inputs. CRM integrations are planned for a later release.
- **Safe by default:** External content is treated as untrusted. Prompt injection is addressed explicitly.

---

## Disclaimer

This is a toolkit, not a sales performance guarantee. All metrics (conversion rates, time saved, reply rates) are hypotheses to validate against your own baseline. AI-generated sales actions require human review before sending.

---

## License

MIT. See [LICENSE](LICENSE).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Security

See [SECURITY.md](SECURITY.md) and [docs/SECURITY_AND_PRIVACY.md](docs/SECURITY_AND_PRIVACY.md).

---

*Built by [Hakken](https://hakken.ai) — AI agent, with Paweł Łach.*
