# Contributing to SalesOps Foundry

Thank you for your interest in improving SalesOps Foundry.

## How to contribute

### Adding a new skill

1. Create a new directory under the appropriate group: `skills/NN-group-name/your-skill-name/`
2. Add a `SKILL.md` file following the standard specification in `docs/REQUIREMENTS.md` §FR-1.2.
3. Include at least two evaluation cases in the skill file.
4. Run `python scripts/validate_frontmatter.py` to check your frontmatter.
5. Update the skills catalogue in `site/skills-catalog.md`.
6. Open a pull request with a description of what the skill does and why it adds value.

### Improving an existing skill

1. Make your changes in the skill's `SKILL.md` file.
2. Update the `version` field in the frontmatter and add an entry to the skill's own change log section.
3. Add or update at least one evaluation case that covers your change.
4. Run `python scripts/validate_frontmatter.py` and `python scripts/check_links.py`.
5. Open a pull request.

### Reporting issues

Open a GitHub issue with:
- The skill or component name
- The problem you observed
- Steps to reproduce
- What you expected to happen

### Security issues

Do not open public issues for security vulnerabilities. See `SECURITY.md`.

## Standards

- All examples must use fictional data (see `docs/DECISIONS.md` ADR-008).
- No credentials, API keys, or personal data in any file.
- Skills must include an explicit human-approval requirement statement.
- Keep skill procedures actionable and testable — not just a description.

## Governance

This project is currently owner-led. Significant changes to scope, architecture, or safety policy require owner approval. See `docs/DECISIONS.md` for the ADR log.
