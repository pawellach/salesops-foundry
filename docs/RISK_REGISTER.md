# Risk Register — SalesOps Foundry

**Version:** 1.0  
**Date:** 2026-10-20

---

## Risk scoring

**Probability:** 1 (rare) – 5 (almost certain)  
**Impact:** 1 (negligible) – 5 (blocks completion or causes harm)  
**Score:** P × I

---

## Active risks

### R-01: GitHub Pages unavailable on free-plan private repo

| Field | Value |
|---|---|
| Probability | 4 |
| Impact | 2 |
| Score | 8 |
| Category | Technical / Platform |
| Mitigation | Site draft lives in `site/` directory and can be deployed when repo is made public or moved to a paid plan. Brief §8 explicitly notes this scenario. |
| Owner | Hakken |
| Status | Open — mitigated by design |

### R-02: Parallel agent file conflicts during Phase 3

| Field | Value |
|---|---|
| Probability | 3 |
| Impact | 3 |
| Score | 9 |
| Category | Execution |
| Mitigation | Each agent has an exclusive directory domain (skills groups, agents, content). Commit in agents prohibited; integration step runs after all agents complete and audits diff before committing. |
| Owner | Hakken |
| Status | Open — mitigated by domain partitioning |

### R-03: Skill quality vs. quantity trade-off

| Field | Value |
|---|---|
| Probability | 3 |
| Impact | 3 |
| Score | 9 |
| Category | Quality |
| Mitigation | Brief §7 explicitly permits combining overlapping candidates. All 72 catalogue slots are defined but overlapping slots will be merged. Quality gate: no skill file under 30 lines. |
| Owner | Hakken |
| Status | Open |

### R-04: Hallucinated facts in skill content

| Field | Value |
|---|---|
| Probability | 3 |
| Impact | 4 |
| Score | 12 |
| Category | Content quality / Safety |
| Mitigation | Skills reference methods and frameworks (MEDDICC, SPICED) by name only; they do not cite statistics or company facts. All claims are marked as guidance, not evidence. Adversarial review (Phase 5) explicitly tests for fabricated facts. |
| Owner | Hakken |
| Status | Open |

### R-05: Prompt injection via untrusted source text

| Field | Value |
|---|---|
| Probability | 2 |
| Impact | 5 |
| Score | 10 |
| Category | Security |
| Mitigation | Every skill that processes external content explicitly labels it as untrusted in the procedure. Prompt-injection defence skill (Skill 67) is a dedicated capability. Threat model in `docs/SECURITY_AND_PRIVACY.md`. |
| Owner | Hakken |
| Status | Open |

### R-06: Real personal data accidentally included in examples

| Field | Value |
|---|---|
| Probability | 2 |
| Impact | 4 |
| Score | 8 |
| Category | Privacy |
| Mitigation | All examples use clearly fictional companies and names (Acme Corp, Northlight Technologies, Meridian Logistics). ADR-008 mandates fictional-only test data. Pre-publish scan in Phase 7. |
| Owner | Hakken |
| Status | Open |

### R-07: Accidental public repo creation

| Field | Value |
|---|---|
| Probability | 1 |
| Impact | 5 |
| Score | 5 |
| Category | Security |
| Mitigation | `gh repo create --private` flag used. Visibility verified after creation. Owner must explicitly approve making public. |
| Owner | Hakken |
| Status | Open |

### R-08: Context compaction loses execution state mid-build

| Field | Value |
|---|---|
| Probability | 3 |
| Impact | 3 |
| Score | 9 |
| Category | Execution |
| Mitigation | Git commits at end of each phase. Files on disk are authoritative. Recovery: `git log` + `ls` to determine phase. |
| Owner | Hakken |
| Status | Open |

---

## Closed risks

_None at project start._
