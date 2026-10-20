---
name: Privacy and Data-Minimisation Review
description: Review a skill, workflow, or document for unnecessary personal and customer data, and recommend what to remove or anonymise.
group: "07 — Quality, Safety, and Governance"
version: "1.0"
status: implemented
---

# Privacy and Data-Minimisation Review

## Purpose
Identify personal data and customer data that is present without clear justification, and recommend data-minimisation actions. Applies to skill files, workflow definitions, example documents, test fixtures, and output reports. This is not a legal compliance assessment — it is a practical data-hygiene check.

## When NOT to use
- As a substitute for legal advice on GDPR, CCPA, or other privacy law.
- On data that the user has explicitly reviewed and approved for the purpose at hand.

## Required inputs
- `target`: the document, skill file, or data file to review
- `purpose`: the stated purpose of the document (e.g. "account brief for internal use", "test fixture", "outreach draft")

## Optional inputs
- `jurisdiction_hints`: relevant jurisdictions for the data subject (e.g. "EU", "California") — triggers additional flag categories
- `data_categories`: specific data types the reviewer is most concerned about (e.g. "email addresses", "direct phone numbers", "health data")

## Step-by-step procedure
1. Identify all personal data present: names, email addresses, phone numbers, job titles linked to a named individual, location data, financial data, health data, LinkedIn/social URLs of individuals.
2. For each piece of personal data, assess:
   a. Is this data necessary for the stated purpose?
   b. Is the data subject a real individual (higher risk) or a clearly fictional person?
   c. Is the data sourced from a public professional profile (lower risk) or from private/sensitive sources (higher risk)?
3. Flag data that fails the necessity test.
4. For test fixtures and examples: flag any real person's data — all examples must use fictional identities.
5. Produce the review report with specific, actionable recommendations.

## Output contract
```markdown
## Privacy and Data-Minimisation Review

**Target:** <file or document name>
**Purpose:** <stated purpose>
**Review date:** <YYYY-MM-DD>

### Personal data found
| # | Data item | Type | Necessary? | Risk level | Recommendation |
|---|---|---|---|---|---|
| 1 | "sarah.chen@northlight.com" | Email | No — purpose is analysis only | MEDIUM | Remove or replace with fictional address |
| 2 | "James Okafor, VP Sales" | Name + title | Yes — buyer committee mapping | LOW | Retain, ensure sourced from public profile |

### Summary
- Items to remove: <N>
- Items to anonymise: <N>
- Items acceptable: <N>
- **Overall verdict:** PASS / REMEDIATE

### Recommendations
1. Replace all real email addresses in test fixtures with @example.com addresses.
2. ...
```

## Evidence and citation rules
- Each flagged item must name the exact data and its location (line, section, field name).
- Necessity assessments must reference the stated purpose.

## Confidence/uncertainty handling
- This review checks data presence and apparent necessity, not lawfulness under specific privacy laws.
- State: "This is a data-hygiene review, not a legal compliance assessment."

## Safety, privacy, and compliance constraints
- Do not reproduce personal data from the target in the report beyond short excerpts needed to identify the finding.
- Handle review outputs as sensitively as the data they reference.

## Human approval requirements
- No external actions. This skill produces a local review report.
- REMEDIATE-rated outputs must have personal data addressed before use in external communications or public repository commits.

## Failure modes
- **Missed implicit identifiers:** A skill may use data combinations (company + role + hire date) that are uniquely identifying without containing an obvious PII field.
- **Fictional-looking real data:** Real names that happen to sound fictional will not be automatically flagged.

## Acceptance criteria
- All obvious personal data types (name, email, phone, social URL) are identified.
- Each item has a necessity assessment and recommendation.
- No real individual's data is present in test fixtures or example files.

## Evaluation cases

### Case 1 — Test fixture with real email
**Input:** An example file containing: `Contact: james.okafor@northlight-tech.com, +44 7700 900123`
**Expected:** Both items flagged; email and phone not necessary for a fictional example; recommend replace with fictional data.

### Case 2 — Account brief with public professional data
**Input:** Account brief referencing: `"CEO: Daniel Park (LinkedIn: linkedin.com/in/danielpark-northlight)"` — sourced from public LinkedIn.
**Expected:** Name and title acceptable for account brief purpose; LinkedIn URL flagged as unnecessary (title is sufficient); PASS with minor recommendation.

## Related skills
- Source and Citation Auditor (Skill 65)
- Outreach Compliance Checklist (Skill 69)
- Prompt-Injection Defence Review (Skill 67)
