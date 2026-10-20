---
name: Warm-Path Mapping
description: Identify a potential introduction path to a target contact using only verified, supplied context — no fabrication of connections.
group: "03 — Run the Pipeline"
version: "1.0"
status: implemented
---

# Warm-Path Mapping

## Purpose
Given a target account and contact, identify whether a warm introduction path exists using only information the seller has explicitly supplied. Produce a ranked list of potential introduction paths with confidence and notes on how to pursue each.

## When NOT to use
- When no connection context has been supplied (do not invent relationships).
- When the purpose is to circumvent a contact's explicit opt-out or do-not-contact preference.
- As a substitute for building a genuine relationship.

## Required inputs
- Target account name and target contact name/role.
- Seller's supplied connection context: past colleagues, mutual LinkedIn connections (if exported and supplied), customer references, event attendees, investor/advisor relationships, or any other verifiable connections the seller has described.

## Optional inputs
- Account Brief for the target (from Skill 11).
- Prior interaction history with the account (if any).

## Step-by-step procedure

1. **List supplied connection context.** Extract every named connection, shared affiliation, or mutual relationship from the supplied materials. Do not add connections that are not in the supplied data.
2. **Map connections to the target.** For each supplied connection, assess whether it plausibly links to the target contact or their organisation. Rate each link: Direct (shared employer, confirmed mutual, direct referral), Indirect (shared event, alumni network, investor overlap), or Speculative (possible but unverified).
3. **Rank paths.** Order by: (1) Direct links, (2) Indirect links, (3) Speculative. Within each tier, prefer paths where the connector is likely to respond positively based on supplied context.
4. **Draft path notes.** For each ranked path, describe: who the connector is, what the connection is based on, what to say when asking for an introduction, and any risk (e.g., the connector also sells to this account).
5. **Flag gaps.** If no warm path exists in the supplied data, say so clearly rather than fabricating one.

## Output contract

```markdown
## Warm-Path Map — Northlight Technologies / Sarah Okafor (CTO)
Date: YYYY-MM-DD

**Paths found:** 2 Direct, 1 Indirect
**Recommendation:** Pursue Path 1 first.

### Path 1 — Direct (High confidence)
**Connector:** James Webb (ex-colleague, now VP Eng at Meridian Logistics)
**Basis:** Seller noted James worked with Sarah at a previous employer (supplied context: "James and Sarah both worked at CloudBase Inc. 2019–2022").
**Suggested ask:** "James, I know you worked with Sarah at CloudBase — would you be willing to make a quick intro?"
**Risk:** None noted.

### Path 2 — Indirect (Medium confidence)
**Connector:** Shared SaaS Growth Summit 2025 attendance
**Basis:** Both seller and Sarah listed as attendees in supplied event export.
**Suggested approach:** Mention shared event as a light opener; not a referral path.

### Gaps
- No confirmed mutual LinkedIn connections supplied.
```

## Evidence and citation rules
- Every named connection must trace back to the supplied context. State the source for each.
- If the connection is inferred (e.g., "they may know each other from their industry"), label it Speculative and note the inference.

## Confidence/uncertainty handling
- Direct: based on a confirmed, named mutual relationship explicitly supplied.
- Indirect: based on a shared context (event, alumni network) that plausibly creates familiarity.
- Speculative: based on inference without confirmed overlap.
- Never upgrade a Speculative path to Indirect to make the output look better.

## Safety, privacy, and compliance constraints
- Do not aggregate personal data beyond what is needed to identify a plausible path.
- Do not suggest approaches that misrepresent the nature of the connection.
- Do not use paths that exploit personal relationships in ways the connector has not agreed to.
- If the target has previously requested no contact, stop and flag rather than finding an alternative path.

## Human approval requirements
**No introduction request is sent without human review.** This skill produces a path map only. The seller decides whether to pursue any path and reaches out themselves. No message is drafted or sent autonomously.

## Failure modes and fallback behaviour
- **No connection context supplied:** Return "No warm paths found in supplied data — cold outreach or event-based approach recommended."
- **Supplied context is vague:** List what was supplied, note it is insufficient to identify a specific connector, and ask for more detail.
- **Target has a do-not-contact flag:** Surface the flag immediately and stop.

## Acceptance criteria
- Every path traces to a named, supplied connection.
- Confidence tiers are assigned and defined.
- Output clearly states when no path exists rather than fabricating one.
- No introduction message is sent.

## Evaluation cases

**Case 1 — Direct path found.**
Input: Target = Sarah Okafor (CTO, Northlight). Supplied context: "My colleague James Webb worked with Sarah at CloudBase Inc."
Expected: Path 1 = Direct, traces to James Webb and CloudBase context; suggested ask drafted.

**Case 2 — No connection data supplied.**
Input: Target = random contact; no connection context provided.
Expected: Output = "No warm paths found in supplied data." No invented connections.

## Related skills
- [Account Brief Builder](/skills/02-account-intelligence/account-brief-builder/SKILL.md) — provides account context that may reveal shared affiliations.
- [Personalised Outreach Planner](/skills/03-run-the-pipeline/personalised-outreach-planner/SKILL.md) — next step after identifying the outreach angle.
- [Contact Research Brief](/skills/01-find-buyers/contact-research-brief/SKILL.md) — research on the target contact.
