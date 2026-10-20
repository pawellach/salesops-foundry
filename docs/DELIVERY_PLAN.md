# Delivery Plan — SalesOps Foundry

**Version:** 1.0  
**Date:** 2026-10-20  
**Executor:** Tanasku 探索

---

## Phase overview

| Phase | Name | Effort estimate | Gate |
|---|---|---|---|
| 0 | Environment and safety check | 30 min | Safe local path confirmed |
| 1 | Research and planning docs | 45 min | Planning docs complete |
| 2 | Skeleton and conventions | 25 min | Structure validates |
| 3 | MVP implementation | 90–120 min (parallel) | All content created |
| 4 | Iteration 1: internal quality review | 30 min | Findings recorded |
| 5 | Iteration 2: adversarial review | 30 min | Findings recorded |
| 6 | Iteration 3: user-value pass | 30 min | 3 scenarios walked |
| 7 | Release readiness | 20 min | No unresolved Critical/High |
| 8 | GitHub publication | 15 min | Private repo created |
| 9 | Final handover | 20 min | Maciek email draft saved |

**Total estimated wall time:** ~5 hours (with parallel Phase 3 agents)

---

## Phase 3 workstreams (parallel)

Phase 3 fans out to 6 parallel implementation agents:

| Agent | Scope | Output |
|---|---|---|
| Skills-A | Group 1 (Find Buyers, skills 1–10) + Group 2 (Signals, skills 11–20) | 20 skill files |
| Skills-B | Group 3 (Pipeline, skills 21–30) + Group 4 (Discovery/Deals, skills 31–42) | 22 skill files |
| Skills-C | Group 5 (Enablement, skills 43–52) + Group 6 (RevOps, skills 53–64) | 22 skill files |
| Skills-D | Group 7 (Quality/Safety, skills 65–72) + all 11 agent definitions | 8 + 11 files |
| Content-E | Workflows (8) + Playbooks (9) + Prompt-libraries (7 categories) | 24+ files |
| Content-F | Templates (10) + Schemas (4) + Examples (3 scenarios) + Evaluations | 25+ files |

After all agents complete, a controlled integration step checks for conflicts, validates frontmatter, and commits.

---

## Definition of done (per phase)

**Phase 0:** Git and gh CLI confirmed; project directory created without touching neighbours; git user config set.

**Phase 1:** All 7 docs in `docs/` exist and have substantive content; DECISIONS.md records ADR-001 (name change); scope matrix complete.

**Phase 2:** All top-level directories created; README.md, CLAUDE.md, LICENSE, .gitignore exist; validate_structure.py passes.

**Phase 3:** All 72 skill files exist with complete frontmatter; all 11 agent files exist; all 8 workflows exist; all 9 playbooks exist; 3 fictional examples exist; evaluation rubric and ≥12 test cases exist.

**Phase 4:** `evaluations/results/iteration-1.md` exists with findings; all critical findings fixed.

**Phase 5:** `evaluations/results/iteration-2.md` exists with adversarial findings; all critical/high fixed.

**Phase 6:** `evaluations/results/iteration-3.md` exists; 3 scenario walkthroughs recorded.

**Phase 7:** validate_structure + validate_frontmatter + check_links all pass; no secrets in `git status`; README, CHANGELOG, ROADMAP current.

**Phase 8:** Private repo exists on GitHub; visibility verified as private; branch pushed.

**Phase 9:** `docs/OUTREACH_DRAFT_MACIEK_OKSIUTA.md` exists, clearly marked DRAFT awaiting approval; final report delivered.

---

## Risk summary

See `docs/RISK_REGISTER.md` for full details. Top risks:
1. GitHub Pages not available on private free-plan repo (mitigated: site draft in `site/`)
2. Parallel agent file conflicts (mitigated: exclusive domains per agent, no concurrent writes to same file)
3. Skill count vs quality trade-off (mitigated: brief §7 allows combining overlapping skills)
