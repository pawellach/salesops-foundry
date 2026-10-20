# Roadmap — SalesOps Foundry

**Version:** 1.0  
**Date:** 2026-10-20

Items are labelled: ✅ Implemented | 🔄 In Progress | 📋 Planned | ⏳ Deferred

---

## MVP — Foundation

**Goal:** A complete, navigable, documented repository usable immediately by a sales practitioner with Claude Code.

| Item | Status | Value | Complexity | Completion condition |
|---|---|---|---|---|
| Core repository structure and conventions | ✅ | High | Low | validate_structure.py passes |
| 7 planning and architecture docs | ✅ | High | Medium | All docs present and substantive |
| Orchestrator and 10 specialist agent definitions | ✅ | High | Medium | All 11 agent files present with full spec |
| 72-skill catalogue across 7 groups | ✅ | High | High | All 72 skill files present, ≥30 lines, valid frontmatter |
| 8 end-to-end workflows | ✅ | High | Medium | All 8 workflow files present |
| 9 sales playbooks | ✅ | Medium | Medium | All 9 playbook files present |
| 10 templates | ✅ | Medium | Low | All 10 template files present |
| 4 JSON schemas | ✅ | Medium | Low | All 4 schemas valid JSON |
| 3 fictional end-to-end examples | ✅ | High | Medium | All 3 scenario dirs with full files |
| Evaluation rubric (12 dimensions) | ✅ | High | Medium | rubric.md present with all score definitions |
| 12 golden test cases | ✅ | High | Medium | All 12 files present with target scores |
| 8 adversarial/security test cases | ✅ | High | Medium | security-cases.md with all 8 cases |
| 3 quality review iterations | ✅ | High | High | Results in evaluations/results/ |
| Security and privacy docs + threat model | ✅ | High | Medium | SECURITY_AND_PRIVACY.md with 7 threats |
| README, CONTRIBUTING, CHANGELOG, ROADMAP | ✅ | High | Low | All root docs present |
| GitHub Pages site draft (7 pages) | ✅ | Medium | Medium | All site/ pages present |
| Private GitHub repository | 📋 | High | Low | Repo created, visibility verified private |

---

## Release 1 — Complete Sales Toolkit

**Goal:** Fully polished toolkit with all quality iteration results recorded, comprehensive prompt-libraries, and improved onboarding.

| Item | Status | Value | Complexity | Dependencies | Completion condition |
|---|---|---|---|---|---|
| Prompt-libraries directory (7 categories) | ✅ | Medium | Medium | Skill catalogue | All 7 prompt-library dirs with content |
| Full evaluation iteration results | 🔄 | High | High | All skills built | All 3 iteration reports in results/ |
| Model benchmark results | 📋 | Medium | Medium | Models available | model-benchmark.md in results/ |
| Improved onboarding examples | 📋 | Medium | Low | MVP complete | 2+ scenario walkthroughs per group |
| Integration README | ✅ | Low | Low | None | integrations/README.md present |
| CHANGELOG with version history | ✅ | Low | Low | MVP complete | CHANGELOG.md updated for 0.1.0 |

---

## Release 1.5 — Runtime Portability and Salesforce Skills

**Goal:** Make the toolkit usable beyond Claude Code, and add Salesforce-native skills for teams already on the platform. These two tracks run in parallel with Release 1 polish.

| Item | Status | Value | Complexity | Dependencies | Notes |
|---|---|---|---|---|---|
| Amazon Q adapter — skill format mapping | 📋 | High | Medium | R1 complete | Port SKILL.md convention to Amazon Q Builder format; generate equivalent skill definitions |
| Amazon Q runtime guide | 📋 | High | Low | Adapter complete | How to invoke skills from Amazon Q; differences from Claude Code |
| Amazon Q parity test | 📋 | Medium | Medium | Adapter + guide | Run golden test suite against Q; document any behaviour differences |
| Salesforce Account/Opportunity skill pack | 📋 | High | High | R1 complete | Skills that read Salesforce data (SOQL queries, opportunity fields) as input; CRM-aware variants of account brief, pipeline hygiene, forecast challenge |
| Salesforce admin onboarding guide | 📋 | Medium | Medium | SF skill pack | Permissions, Connected App setup, Named Credentials pattern |
| Salesforce write-back (manual approval queue) | ⏳ | High | High | SF skill pack stable | Update fields via approval gate only; no autonomous DML |

---

## Release 2 — Integrations

**Goal:** Optional connectors to external systems. All read-only first; writes only after explicit configuration and approval.

| Item | Status | Value | Complexity | Dependencies | Notes |
|---|---|---|---|---|---|
| Salesforce adapter (read-only) | ⏳ | High | High | R1 complete | Requires org credentials; owner to configure |
| HubSpot adapter (read-only) | ⏳ | Medium | High | R1 complete | Requires API key |
| LinkedIn Sales Navigator adapter | ⏳ | High | High | R1 complete | Requires authorised account |
| Apollo.io adapter | ⏳ | Medium | Medium | R1 complete | Requires API key |
| Human approval queue (Slack) | ⏳ | High | Medium | R1 complete | Draft messages for approval, never send autonomously |
| Calendar integration (prep only) | ⏳ | Low | Medium | R2 connectors | Booking suggestions only; no autonomous booking |
| CRM write access | ⏳ | Medium | High | Read adapters stable | Explicitly disabled until opt-in + approval |

---

## Release 3 — Operational Intelligence

**Goal:** Team-level reporting, controlled experiments, and continuous improvement loops.

| Item | Status | Value | Complexity | Dependencies | Notes |
|---|---|---|---|---|---|
| Team-level pipeline dashboard | ⏳ | High | High | R2 complete | Aggregated read-only reporting |
| Experiment tracking (A/B outreach) | ⏳ | Medium | Medium | R2 integrations | Uses experiment-card.md template |
| Configurable team playbooks | ⏳ | Medium | Medium | R1 complete | Playbooks parameterised by team context |
| Feedback loop for skill improvement | ⏳ | High | High | R3 | Proposes improvements; owner approves changes |
| Quality trend reporting | ⏳ | Medium | Medium | R2 integrations | Tracks rubric scores over time |

---

## Known limitations (current MVP)

- No live data connections — all inputs are supplied manually
- Skill evaluation is manual — no automated test runner yet
- Model routing is advisory — not programmatically enforced
- GitHub Pages requires repo to be public (free plan) — site draft is local until owner decides
