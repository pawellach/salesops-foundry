# Changelog

All notable changes to SalesOps Foundry are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

---

## [0.1.5] — 2026-10-31

### Added
- `scripts/build_q.py`: converts all 72 SKILL.md files to Amazon Q Desktop compatible format with auto-generated `trigger_phrases`, `tools`, and `depends_on` frontmatter fields; output to `dist/q-skills/`
- `docs/AMAZON_Q_GUIDE.md`: installation and usage guide for Amazon Q Desktop integration
- `skills/00-integrations/salesforce-write-back/SKILL.md`: helper skill to push structured skill output to Salesforce via sf CLI, with mandatory confirmation step before any DML

---

## [0.1.0] — 2026-10-31

First public release.

### Added
- Initial project structure, 7 planning docs, validation scripts, CI workflows (Phase 0–2)
- 72-skill catalogue across 7 groups — 83 files with complete frontmatter (Phase 3)
- 11 agent definitions including Orchestrator, Outreach Agent, and Safety Reviewer (Phase 3)
- 8 end-to-end workflows including master human-approval-gates reference (Phase 3)
- 9 sales playbooks covering SDR, AE, manager, and founder-led scenarios (Phase 3)
- 26 prompt-library files across 7 categories (Phase 3)
- 10 output templates, 4 JSON schemas, 3 fictional scenario examples (Phase 3)
- Evaluation rubric (12 dimensions), 12 golden tests, 8 adversarial cases, 3 E2E scenarios (Phase 3)
- GitHub Pages site draft: 8 pages in `site/` (Phase 3)
- docs: MODEL_STRATEGY, SECURITY_AND_PRIVACY, INSTALLATION, OPERATING_GUIDE, ROADMAP (Phase 3)

### Fixed
- H-01: Added `# Title` heading to 22 Group 5+6 skills (Phase 4)
- H-02: Converted Related Skills text/backtick references to relative links in 44 skills (Phase 4)
- H-03: Standardised `group` frontmatter field to `"0N — Name"` format across 72 skills (Phase 4)
- M-01 (adversarial): First-Touch Draft — explicit prompt-injection trust-boundary note (Phase 5)
- M-02 (adversarial): human-approval-gates — added social media posting row (Red tier) (Phase 5)
- L-04: Account Brief Builder — moved inference labelling instruction to Steps 4–5 (Phase 5)
- M-01 (usability): discovery-to-demo workflow — explicit prerequisite link to Discovery Call playbook (Phase 6)
