# Skills

Each skill is a named directory containing a `SKILL.md` file. Skills are organised into 7 groups covering the full sales lifecycle.

## Groups

| Group | What it covers | Skills |
|---|---|---|
| [1. Find Buyers and Accounts](01-find-buyers/) | Define your ICP, score accounts, map buying committees, spot purchase triggers | 1–10 |
| [2. Account Intelligence and Signals](02-account-intelligence/) | Research any account, aggregate signals, decide when to act | 11–20 |
| [3. Run the Pipeline](03-run-the-pipeline/) | Triage leads, plan and draft outreach, manage stage and risk | 21–30 |
| [4. Discovery, Demos, and Deal Progression](04-discovery-and-deals/) | Prepare calls, handle objections, build demos, close with a mutual plan | 31–42 |
| [5. Sales Enablement and Management](05-sales-enablement/) | Coach reps, review deals, audit pipeline, challenge forecasts | 43–52 |
| [6. Templates, Trackers, and RevOps](06-revenue-operations/) | Outreach templates, CRM field mapping, metrics definitions, ROI estimation | 53–64 |
| [7. Quality, Safety, and Governance](07-quality-and-safety/) | Catch hallucinations, enforce human approval gates, verify AI output | 65–72 |

## Using a skill

Reference the skill file directly in your agent session:

```
Use skills/01-find-buyers/icp-builder/SKILL.md
```

Or reference it from a workflow that chains multiple skills.

## Adding a skill

See [CONTRIBUTING.md](../CONTRIBUTING.md) and the skill specification in [docs/REQUIREMENTS.md](../docs/REQUIREMENTS.md) §FR-1.2.
