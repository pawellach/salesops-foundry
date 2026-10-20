# Requirements — SalesOps Foundry

**Version:** 1.0  
**Date:** 2026-10-20

---

## Functional requirements

### FR-1: Skill library
- FR-1.1: The repository must contain ≥48 skills covering the full sales lifecycle.
- FR-1.2: Each skill must follow the standard specification (brief §8): name/purpose, inputs, outputs, procedure, evidence rules, safety constraints, human-approval requirements, failure modes, acceptance criteria, evaluation cases, and related skills.
- FR-1.3: Skills must be discoverable by Claude Code's SKILL.md convention (named directory + `SKILL.md` file with YAML frontmatter).
- FR-1.4: Skills must not claim to guarantee sales outcomes.

### FR-2: Agent definitions
- FR-2.1: The repository must define ≥10 specialist agents and 1 orchestrator.
- FR-2.2: Each agent must specify its objective, inputs, outputs, accepted tools, prohibited actions, and escalation conditions.
- FR-2.3: The orchestrator must define how it decomposes requests, tracks state, validates dependencies, and requests human approval at defined gates.

### FR-3: Workflows
- FR-3.1: At least 8 end-to-end workflows must be documented.
- FR-3.2: Each workflow must name the trigger, agents involved, approval gates, and expected output.
- FR-3.3: A `human-approval-gates.md` workflow must enumerate every action class and its approval requirement.

### FR-4: Evaluation
- FR-4.1: An evaluation rubric with 12 scored dimensions (0–5) must exist.
- FR-4.2: At least 12 golden test cases, 8 adversarial/safety cases, and 3 end-to-end fictional scenarios must be defined.
- FR-4.3: Test fixtures must use synthetic data only.
- FR-4.4: Review results for all three iterations must be recorded in `evaluations/results/`.

### FR-5: Safety and privacy
- FR-5.1: A threat model covering prompt injection, data leakage, over-permissioned tools, false claims, accidental publication, and unauthorised outreach must be documented.
- FR-5.2: Every skill must include an explicit human-approval requirement statement.
- FR-5.3: No skill may send email, post to social media, write to CRM, or take other consequential external actions without a defined approval gate.

### FR-6: Documentation
- FR-6.1: README must explain purpose, audience, quick-start, and repository navigation.
- FR-6.2: CONTRIBUTING must explain how to add or improve skills.
- FR-6.3: ROADMAP must distinguish implemented, planned, and deferred items.
- FR-6.4: GitHub Pages site draft must cover: landing, getting started, skills catalogue, agent architecture, workflows, safety, and roadmap.

### FR-7: Repository hygiene
- FR-7.1: `.gitignore` must cover Python, Node.js, OS artefacts, `.env`, and secrets.
- FR-7.2: No secrets, credentials, API keys, or personal contact data may appear in any committed file.
- FR-7.3: Validation scripts must check directory structure, YAML frontmatter, and internal links.

---

## Non-functional requirements

### NFR-1: Modifiability
- Any skill can be updated independently without breaking others.
- Adding a new skill requires only creating a new directory; no central registry update required.

### NFR-2: Portability
- Skill files are plain Markdown with YAML frontmatter. They are readable on any platform.
- No runtime-specific binary or proprietary format.

### NFR-3: CRM-agnostic MVP
- All skills accept plain-text inputs (Markdown, CSV, JSON, YAML). No CRM API credentials required for MVP.

### NFR-4: Lightweight setup
- A user with Git and Claude Code installed can start using the toolkit within 10 minutes.
- No build step required to use skills.

### NFR-5: Evidence standards
- Researched claims must be labelled with source, date, and confidence level.
- Skills must distinguish facts from inferences and assumptions.

### NFR-6: Measurable evaluation
- Evaluation rubric scores must have explicit 0–5 definitions, not just labels.
- Release gate: no critical safety failures; no fabricated material facts in golden tests; all mandatory output fields present; all approval gates respected; overall average ≥4.0 on core workflows.
