# Project Charter — SalesOps Foundry

**Version:** 1.0  
**Date:** 2026-10-20  
**Owner:** Project sponsor (Paweł Łach)  
**Execution agent:** Hakken  
**Status:** Approved for execution

---

## 1. Mission

Design, build, test, review, and publish a complete AI-enabled sales operating system that helps a small sales team perform the work of a much larger, well-coordinated team.

SalesOps Foundry is a **repository-first toolkit**: a collection of reusable skills, agent definitions, playbooks, workflows, templates, evaluation cases, and operating guidance, structured for autonomous and multi-agent execution while keeping consequential external actions under human approval.

---

## 2. Problem statement

Small sales teams and founder-led businesses operate without a sales operations function. They have access to powerful AI models but no structured, safe, maintainable way to direct them across the full sales lifecycle — from ICP definition and account research through outreach, discovery, deal progression, forecasting, and continuous improvement. Existing "AI sales" prompts are typically monolithic, untested, and unsafe for autonomous execution.

---

## 3. Target users

| Role | Primary pain | Key workflows |
|---|---|---|
| Sales Development Representative (SDR/BDR) | Finding and prioritising prospects, writing first-touch outreach | Groups 1, 2, 3 |
| Account Executive (AE) | Discovery prep, demo planning, deal progression, negotiation | Groups 3, 4 |
| Sales Manager / Team Lead | Pipeline reviews, coaching, forecasting | Group 5 |
| Founder doing early sales | All of the above with minimal support | Groups 1–5 |
| RevOps / Enablement | Templates, trackers, metrics, experiment design | Group 6 |

---

## 4. Success definition

The project is complete when all 18 acceptance criteria in `docs/ACCEPTANCE_CRITERIA.md` are satisfied, including:
- A complete, navigable, documented repository with ≥48 substantive skills
- Three independent review-and-improvement iterations recorded
- Security, privacy, hallucination, and prompt-injection risks assessed
- A professional README, contribution guide, governance docs, and roadmap
- Private GitHub repository created, committed, and pushed
- Draft email to Maciek Oksiuta saved and awaiting owner approval

---

## 5. Scope matrix

### Must (MVP)
- Core repository structure, conventions, and discovery mechanism
- 72-skill catalogue (Groups 1–7), all substantive and testable
- 11 agent definitions with collaboration protocol
- 8 end-to-end workflows
- 9 playbooks
- 7 planning/architecture docs
- Templates (10), schemas (4), fictional examples (3 scenarios)
- Evaluation rubric, 12 golden tests, 8 adversarial cases, 3 E2E scenarios
- Security and privacy docs, threat model
- README, CONTRIBUTING, SECURITY, CHANGELOG, ROADMAP
- Validation scripts (Python)
- GitHub Pages site draft in `site/`
- Private GitHub repository

### Should (Release 1 polish)
- Full prompt-libraries directory (7 categories)
- Integration adapters README
- More evaluation regression cases

### Could (Release 2)
- CRM adapter implementations (Salesforce, HubSpot)
- Research-source adapters (LinkedIn Sales Navigator, Apollo)
- Human approval queue implementation
- CI test automation via GitHub Actions

### Won't (MVP)
- Domain purchase or external hosting beyond GitHub Pages
- Bulk outreach or contact-scraping tools
- Live CRM writes without explicit configuration
- Multi-tenant or SaaS packaging

---

## 6. Key constraints

- No real customer, prospect, or personal data in the repository
- No external communications sent autonomously
- Repository starts private; owner approves any public release
- No paid services, API keys, or credentials in code or Markdown
- Compatible with Claude Code's SKILL.md convention

---

## 7. Stakeholders

| Person | Role |
|---|---|
| Paweł Łach | Owner, final approver |
| Hakken | Execution agent, author |
| Maciek Oksiuta | Intended first external reader (email draft, pending approval) |
