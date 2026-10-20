---
layout: page
title: Safety and Privacy
---

# Safety and Privacy

SalesOps Foundry is designed to be safe by default. Here is how that works in practice.

---

## Human approval gates

Every consequential external action requires human approval before execution.

| Tier | Examples | What happens |
|---|---|---|
| **Green** | File reads, draft creation, internal analysis, local commits | Agent proceeds autonomously |
| **Amber** | Outreach drafts, CRM field mapping proposals, meeting booking options | Agent prepares and presents; you review and approve |
| **Red** | Sending email/LinkedIn, publishing the repo, writing to CRM, bulk outreach | Agent stops and explicitly asks for your confirmation |

**You will never receive a bill for a mass email you didn't approve.**

---

## Privacy principles

- **Data minimisation:** Skills collect only what is needed for the specific task.
- **Fictional test data:** All examples and evaluation fixtures use invented companies and contacts.
- **No personal data in the repository:** Real customer names, email addresses, and phone numbers must never be committed.
- **Source separation:** External content (web pages, documents, CRM notes) is treated as untrusted. Agents do not follow instructions embedded in source material.

---

## Prompt injection defence

External content may contain hidden instructions designed to redirect agent behaviour. SalesOps Foundry addresses this by:
- Labelling all source material as UNTRUSTED at the point of ingestion
- Separating source text from agent instructions
- Including a dedicated Skill 67 (Prompt-Injection Defence Review) to test for injection vulnerabilities

---

## Evidence and uncertainty

Every researched claim in a skill output must include:
- A named source
- A source date
- A confidence level (high/medium/low/unverified)

Claims are labelled as: **fact** (sourced), **inference** (derived), **assumption** (untested), or **recommendation** (advised action).

Skills will not fill in fields they cannot source. When evidence is insufficient, the correct output is to stop and ask.

---

## What this toolkit will not do

- Send any message without your explicit approval
- Fabricate contact details, company metrics, or analyst quotes
- Follow instructions embedded in untrusted source material
- Write to any CRM without explicit opt-in configuration
- Guarantee sales results — all outputs are starting points for human judgment

---

## Disclaimer

> This toolkit is a decision-support tool. AI-generated sales actions require human review before external use. Compliance with applicable laws (GDPR, CAN-SPAM, CASL) is the user's responsibility. Outreach compliance skill outputs are prompts for qualified human review, not legal advice.
