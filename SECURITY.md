# Security Policy

## Scope

This document covers the SalesOps Foundry toolkit repository. For the full threat model, see `docs/SECURITY_AND_PRIVACY.md`.

## Supported versions

| Version | Supported |
|---|---|
| Unreleased (main branch) | Yes |

## Reporting a vulnerability

If you discover a security issue — including a prompt-injection vector, a skill that bypasses human approval, a data-leakage path, or a dependency vulnerability — please **do not** open a public GitHub issue.

Instead:
1. Open a private GitHub security advisory (Repository → Security → Advisories → New advisory), or
2. Email the project owner directly (contact details in the README).

Please include:
- A description of the vulnerability
- Steps to reproduce
- The potential impact
- Any suggested mitigations

You will receive a response within 7 days. We aim to disclose resolved vulnerabilities publicly within 90 days of the report.

## Key security principles

- No credentials, API keys, tokens, or secrets may be committed to this repository.
- All examples use fictional data. Do not add real customer, prospect, or personal contact information.
- External content (web pages, documents, CRM notes) must be treated as untrusted by all skills.
- Every skill that could take an external action must include a human approval gate.
- See `docs/SECURITY_AND_PRIVACY.md` for the full threat model.
