# Acceptance Criteria — SalesOps Foundry

**Version:** 1.0  
**Date:** 2026-10-20

---

The project is complete only when all criteria below are satisfied. Status is updated as phases complete.

| # | Criterion | Status |
|---|---|---|
| AC-01 | Project concept, target users, scope, architecture, risks, and delivery plan documented in `docs/` | ✅ Done |
| AC-02 | A well-organised local project directory exists at `C:\Inne Projekty\salesops-foundry\` without touching neighbouring projects | ✅ Done |
| AC-03 | A private GitHub repository `pawellach/salesops-foundry` has been created and visibility verified | ✅ Done — visibility: PRIVATE |
| AC-04 | Repository contains ≥48 substantive skills with complete specification (inputs, outputs, procedure, evidence rules, safety, approval gates, evaluation cases) | ✅ Done — 72 skills |
| AC-05 | Skills are organised in the standard directory structure and discoverable via SKILL.md convention | ✅ Done — validate_frontmatter PASS |
| AC-06 | At least 11 specialist agent definitions exist with objectives, tools, and prohibited actions specified | ✅ Done — 11 agents |
| AC-07 | At least 8 end-to-end workflows exist with trigger, agents, approval gates, and expected output | ✅ Done — 8 workflows |
| AC-08 | At least 3 fictional end-to-end scenario examples exist and work without hidden context | ✅ Done — Phase 6 verified |
| AC-09 | Evaluation rubric (12 dimensions, 0–5) exists; ≥12 golden tests, ≥8 adversarial cases, 3 E2E scenarios defined | ✅ Done |
| AC-10 | Three independent review-and-improvement iterations completed and recorded in `evaluations/results/` | ✅ Done — Phases 4, 5, 6 |
| AC-11 | Security and privacy threat model documented; human approval policy enforced in all skills | ✅ Done — docs/SECURITY_AND_PRIVACY.md |
| AC-12 | Professional README with navigation, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, CHANGELOG, ROADMAP all exist | ✅ Done |
| AC-13 | GitHub Pages site draft in `site/` with ≥7 pages; deployed or blocker documented | ✅ Draft done (8 pages) — deployment pending public repo (ADR-003) |
| AC-14 | Validation scripts (structure, frontmatter, links) all pass with zero errors | ✅ Done — 203 files, 77 links, all PASS |
| AC-15 | No secrets, API keys, credentials, or real personal data committed | ✅ Done — secret scan clean |
| AC-16 | Repository committed and pushed to private GitHub repo | ✅ Done — https://github.com/pawellach/salesops-foundry |
| AC-17 | `docs/OUTREACH_DRAFT_MACIEK_OKSIUTA.md` exists, contains a draft email in Polish, is clearly marked DRAFT AWAITING OWNER APPROVAL, and has not been sent | ✅ Done — awaiting owner approval |
| AC-18 | Final handover report delivered with accurate counts, verified URLs, known limitations, and recommended next steps | ⬜ Pending Phase 9 |

---

## Release gate (Phase 7)

The following conditions must ALL be true before Phase 8 (GitHub publication):
- validate_structure.py: **PASS**
- validate_frontmatter.py: **PASS**
- check_links.py: **PASS**
- Iteration-3 report: **no unresolved Critical or High findings**
- `git grep -r "api_key\|password\|secret\|token" -- "*.md" "*.yml" "*.json"`: **zero matches in committed content**
- All 72 skills present and each ≥30 lines
- README renders correctly on GitHub (verified locally)
