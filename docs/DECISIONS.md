# Architecture Decision Records (ADR Log)

## ADR-001: Project name — SalesOps Foundry (not RevenuePilot AI)

**Date:** 2026-10-20  
**Status:** Accepted  
**Decided by:** Tanasku 探索 (autonomous, per brief §5)

### Context

Brief §5 proposed "RevenuePilot AI" as the working name with slug `revenuepilot-ai-sales-os`. Brief required a collision check before finalising.

### Decision

Rename to **SalesOps Foundry** / slug `salesops-foundry`.

### Rationale

`gh search repos revenuepilot` returned 5+ public repositories, including one literally named "Multi-Agent To-B Sales Decision Agent" (September 2026). Using the same name would cause search confusion and positioning ambiguity for a professional sales leader audience. `gh search repos salesops-foundry` returned zero results.

Alternative "SalesOps Foundry" is:
- Clean on GitHub (zero collisions found as of 2026-10-20)
- Professional: "foundry" implies a manufacturing/crafting metaphor aligned with a toolkit framing
- Descriptive of the RevOps + sales execution scope
- Easily searchable and unambiguous

### Rejected alternatives

| Name | Reason rejected |
|---|---|
| RevenueCraft | 2 GitHub hits (RevenueCraft products, copy site) |
| Sales Agent Toolkit | Too generic; likely hundreds of informal uses |
| OpenRevenue OS | "Open" implies open-source license commitment not yet decided |

### Cost if wrong

One rename (directory, README, GitHub repo URL). Low cost; reversible before publication.

---

## ADR-002: Git user identity for this repository

**Date:** 2026-10-20  
**Status:** Accepted

Local git config set to `pawellach` / `pawel.lach@l2studio.pl` to match the authenticated GitHub account (`pawellach`) used for all private personal projects in `C:\Inne Projekty\`. Global config (`pawellach-symf`) is for Symfonia work.

---

## ADR-003: Repository visibility — private at creation, decision deferred to owner for publication

**Date:** 2026-10-20  
**Status:** Accepted

Repository will be created **private**. GitHub Pages on a private repo (free plan) is not available — the site draft will live in `site/` and be documented as "pending publication decision". Owner approves making the repo public and enabling Pages before any external link is shared with Maciek Oksiuta.

---

## ADR-004: MVP scope — 48 skills in Release 1, not all 72

**Date:** 2026-10-20  
**Status:** Accepted

Brief §7 targets "at least 48 substantive skills or skill modules" with a stretch of 60–72 "only if each has a distinct use case and tests." All 72 catalogue slots are defined; Groups 1–6 (skills 1–64) are fully implemented. Group 7 (Quality & Safety, skills 65–72) is delivered as the evaluation/safety layer woven through the others, with 8 dedicated skill files, reaching the full 72.

---

## ADR-005: CRM-agnostic first release with file-based inputs

**Date:** 2026-10-20  
**Status:** Accepted

Per brief §4: first release is CRM-agnostic. All skills accept inputs as Markdown, CSV, JSON, or YAML files. CRM adapters are planned for Release 2. No external API credentials required for MVP.

---

## ADR-006: License — MIT

**Date:** 2026-10-20  
**Status:** Accepted (provisional — owner to confirm before making repo public)

MIT is the least-restrictive option, appropriate for a toolkit intended to be shared with a sales leader. Owner to confirm before public release. If owner wants a non-commercial restriction, switch to CC BY-NC 4.0 for documentation and MIT for code (scripts). No action needed while the repo is private.

---

## ADR-007: Skill file format — Markdown with YAML frontmatter

**Date:** 2026-10-20  
**Status:** Accepted

Skills are stored as `SKILL.md` files inside named subdirectories under `skills/NN-group-name/skill-name/SKILL.md`. This follows Claude Code's native skill discovery convention and is compatible with other agent runtimes (format is plain Markdown with YAML frontmatter; a runtime-specific adapter can transform it). Confirmed against local Claude Code installation.

---

## ADR-008: Fictional data for all examples and test fixtures

**Date:** 2026-10-20  
**Status:** Accepted

All examples use clearly fictional companies (Acme Corp, Northlight Technologies, Meridian Logistics) and fictional contacts. No real customer, prospect, or personal data is used anywhere in the repository.
