# SalesOps Foundry — Agent Instructions

This file governs agent behaviour when working in this repository.

## Project overview

SalesOps Foundry is a modular, human-governed AI operating system for modern sales teams. It contains skills, agent definitions, workflows, playbooks, templates, schemas, examples, and evaluation fixtures.

## Autonomy and approval policy

### Autonomous (no approval needed)
- Reading any file in this repository
- Creating or editing files in this repository (skills, docs, examples, etc.)
- Running validation scripts locally
- Creating local commits after verifying the diff

### Approval required (stop and ask)
- Sending any email, Slack message, or other external communication
- Making the GitHub repository public
- Writing to any CRM or operational system
- Creating, modifying, or deleting GitHub repository settings
- Pushing to remote branches (unless explicitly instructed)
- Any action that incurs costs or purchases

## Conventions

### Skill files
Location: `skills/NN-group-name/skill-name/SKILL.md`  
Required frontmatter fields: `name`, `description`, `group`, `version`, `status`

### Agent files
Location: `agents/agent-name.md`  
Required frontmatter: `name`, `role`, `scope`

### Data safety
- All example data must be fictional (see `docs/DECISIONS.md` ADR-008)
- Never commit real customer, prospect, or personal contact information
- Never commit secrets, API keys, or credentials

### Testing
After any change to skill files, run:
```bash
python scripts/validate_frontmatter.py
python scripts/check_links.py
```

## Repository structure

See `docs/ARCHITECTURE.md` for the full layer model and data-flow diagram.

## Decision log

All architecture decisions are in `docs/DECISIONS.md`. Record any new decisions there.
