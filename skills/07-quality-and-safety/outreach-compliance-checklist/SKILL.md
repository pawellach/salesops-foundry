---
name: Outreach Compliance Checklist
description: Flag jurisdiction, consent, opt-out, frequency, and channel questions for human review before any outreach is sent.
group: "07 — Quality, Safety, and Governance"
version: "1.0"
status: implemented
---

# Outreach Compliance Checklist

## Purpose
Produce a human-review checklist for proposed sales outreach. This skill does not give legal advice; it surfaces the questions a sales practitioner and their legal/compliance team should answer before sending. It covers email, LinkedIn, phone, and other channels, and highlights jurisdiction-specific triggers.

## When NOT to use
- As a substitute for legal advice.
- After outreach has already been sent — use for pre-send review only.
- For internal communications (no external recipient).

## Required inputs
- `outreach_draft`: the message(s) to be sent (email, LinkedIn, call script, etc.)
- `channel`: "email" | "linkedin" | "phone" | "sms" | "other"
- `recipient_context`: what is known about the recipient (role, company, country/jurisdiction if known)

## Optional inputs
- `sequence_details`: if part of a sequence, describe the number of touches, intervals, and stop conditions
- `opt_out_mechanism`: how the recipient can opt out (reply with "unsubscribe", link, phone number, etc.)

## Step-by-step procedure
1. Identify the recipient's likely jurisdiction from context (country, state).
2. Apply the jurisdiction-specific question set (see below).
3. Check the outreach content for the universal checklist items.
4. Check sequence parameters if provided.
5. Produce the checklist — each item marked CONFIRMED, UNKNOWN, or FLAG.
6. If any item is flagged UNKNOWN for a high-risk jurisdiction (EU, California, Canada), escalate overall to REQUIRES LEGAL REVIEW.

### Universal checklist items
- Recipient is a business contact, not a consumer (B2B vs B2C distinction)
- Outreach is relevant to the recipient's professional role
- No deceptive sender identity (reply-to matches sender)
- Clear identification of who is sending (company name present)
- Opt-out mechanism present and functional
- No manipulative, coercive, or discriminatory language
- AI-generated content has been reviewed by a human before sending

### Jurisdiction-specific triggers
- **EU (GDPR):** Lawful basis for processing contact data identified?
- **Germany (BDSG + UWG):** Prior consent for cold email to individuals?
- **California (CCPA + CAN-SPAM):** CCPA consumer rights notice applicable?
- **Canada (CASL):** Express or implied consent for commercial electronic message?
- **UK (UK GDPR + PECR):** Legitimate interest assessment documented?
- **Australia (Spam Act 2003):** Inferred consent from business context?

## Output contract
```markdown
## Outreach Compliance Checklist

**Channel:** <channel>
**Recipient jurisdiction:** <country/unknown>
**Date:** <YYYY-MM-DD>

### Universal checks
| # | Check | Status | Notes |
|---|---|---|---|
| 1 | B2B contact (not consumer) | CONFIRMED / UNKNOWN / FLAG | |
| 2 | Relevant to professional role | CONFIRMED / UNKNOWN / FLAG | |
| 3 | No deceptive sender identity | CONFIRMED / FLAG | |
| 4 | Company name present | CONFIRMED / FLAG | |
| 5 | Opt-out mechanism present | CONFIRMED / FLAG | Opt-out: reply "unsubscribe" |
| 6 | No manipulative/coercive language | CONFIRMED / FLAG | |
| 7 | Human-reviewed AI content | FLAG | Awaiting review |

### Jurisdiction-specific checks
<jurisdiction-specific table>

### Sequence checks (if applicable)
- Touch limit: <N> messages — CONFIRM this is within internal policy
- Stop conditions: <stated conditions>
- Minimum interval: <N> days

### Overall status: PROCEED / REVIEW REQUIRED / REQUIRES LEGAL REVIEW

### Next steps for human reviewer
1. Confirm opt-out mechanism is functional.
2. ...
```

## Evidence and citation rules
- Base jurisdiction identification on supplied context only; do not assume jurisdiction without evidence.
- State clearly: "This checklist is a prompt for human and legal review, not legal advice."

## Confidence/uncertainty handling
- Unknown jurisdiction defaults to EU-level caution (most restrictive common framework).
- State: "Where jurisdiction is unknown, EU-level checks are applied as a conservative default."

## Safety, privacy, and compliance constraints
- This skill must never produce a "COMPLIANT — SAFE TO SEND" verdict. It produces review prompts only.
- Do not store recipient personal data in the output report beyond what is necessary to identify the context.

## Human approval requirements
- **Sending the outreach always requires human approval.** This skill is a pre-approval checklist, not a send gate.
- REQUIRES LEGAL REVIEW outputs must not proceed to send without legal/compliance sign-off.

## Failure modes
- **Jurisdiction missed:** If country is not supplied or guessed incorrectly, relevant jurisdiction checks are not applied.
- **Sequence evasion:** A human may interpret REVIEW REQUIRED as conditional approval. The report must clearly state that approval belongs to the human reviewer.

## Acceptance criteria
- All universal checks are assessed.
- Jurisdiction-specific checks are applied when jurisdiction is known or inferable.
- No "safe to send" verdict is produced.
- Opt-out mechanism is assessed.

## Evaluation cases

### Case 1 — EU recipient, no opt-out
**Input:** Email draft to a named individual at a German company. No opt-out link. No prior relationship context.
**Expected:** FLAG on opt-out mechanism; FLAG on GDPR lawful basis; overall REQUIRES LEGAL REVIEW.

### Case 2 — B2B US recipient, opt-out present
**Input:** Email to VP Sales at a US company (no California address), opt-out present, company name in signature.
**Expected:** Most checks CONFIRMED; FLAG on "Human-reviewed AI content" (awaiting review); overall REVIEW REQUIRED (not automatically proceed).

## Related skills
- Privacy and Data-Minimisation Review (Skill 68)
- Human Approval Gate (Skill 70)
- Follow-up Sequence Builder (Skill 26)
