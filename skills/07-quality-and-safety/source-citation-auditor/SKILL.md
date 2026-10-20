---
name: Source and Citation Auditor
description: Check whether material claims in a sales document or skill output have traceable evidence, and flag unsupported assertions.
group: "07 — Quality, Safety, and Governance"
version: "1.0"
status: implemented
---

# Source and Citation Auditor

## Purpose
Verify that every material claim in a sales document, account brief, or skill output is supported by a cited source. Flag claims that are stated as fact but have no traceable evidence — including statistics, company facts, funding figures, headcount, product capabilities, and buyer intent.

## When NOT to use
- For stylistic or tone review (use Sales Call Coach instead).
- For checking whether a claim is *true* — this skill checks whether it is *evidenced*, not verified against ground truth.
- On internal strategy documents where the author owns all assertions.

## Required inputs
- `document`: the text to audit (account brief, outreach draft, pipeline note, skill output, etc.)
- `context`: what kind of document it is (e.g. "account brief", "first-touch email draft")

## Optional inputs
- `source_list`: a list of sources the author believes they used (URLs, document names, access dates)
- `strictness`: "light" (flag only statistics and strong factual claims) | "full" (flag all material claims)

## Step-by-step procedure
1. Read the document and identify every sentence that asserts a fact about an external entity (company, person, market, product, competitor).
2. For each assertion, categorise it as: (a) sourced with citation, (b) sourced but citation incomplete, (c) unsourced, (d) explicitly marked as inference/hypothesis.
3. Apply the strictness level: in "light" mode flag categories (c) only for statistics, funding, headcount, and product claims. In "full" mode flag all category (c) assertions.
4. For each flagged item, note: the claim text, its category, and a recommended action (add source / mark as inference / remove).
5. Produce the audit report in the Output contract format.
6. If >30% of material claims are unsourced, escalate the overall rating to HIGH RISK.

## Output contract
```markdown
## Source and Citation Audit

**Document type:** <context>
**Audit date:** <YYYY-MM-DD>
**Strictness:** <light|full>
**Overall rating:** LOW / MEDIUM / HIGH RISK

### Unsourced material claims
| # | Claim (excerpt) | Category | Recommended action |
|---|---|---|---|
| 1 | "Northlight grew 40% YoY" | Unsourced statistic | Add source or remove |

### Incomplete citations
| # | Claim | What is missing |
|---|---|---|

### Well-sourced claims: <N>
### Explicitly marked inferences: <N>
```

## Evidence and citation rules
- A claim is "sourced" only if a URL, document name, or named public record is present and plausibly supports the claim.
- Access dates are not required to pass, but their absence should be noted for time-sensitive claims.
- A claim marked "[inference]" or "[hypothesis]" is exempt from the unsourced flag.

## Confidence/uncertainty handling
- This skill can only assess whether a citation exists, not whether the citation is accurate.
- State explicitly: "This audit checks citation presence, not factual accuracy."

## Safety, privacy, and compliance constraints
- Do not reproduce large excerpts of audited content in the report if it contains personal data.
- If the document contains personal contact data (names, emails, phone numbers) without clear business justification, note it as a privacy concern.

## Human approval requirements
- No external actions. This skill produces a local audit report only.
- No approval required to run the audit.
- Remediation of HIGH RISK documents requires human review before the document is used externally.

## Failure modes
- **False negatives:** The auditor may miss a fabricated claim that sounds plausible. Pair with Hallucination Challenge (Skill 66).
- **Over-flagging:** Commonly known facts (e.g. "Salesforce is a CRM") may not need citations. Use judgment.
- **Missing source list:** Without a source list, the audit can only identify absence of citations, not verify that claimed sources exist.

## Acceptance criteria
- All material factual claims are categorised.
- The overall risk rating is present and calculated correctly.
- No personal data is reproduced unnecessarily in the report.

## Evaluation cases

### Case 1 — Basic unsourced statistic
**Input:** "Northlight Technologies grew its ARR by 60% last quarter and is expanding into the DACH region." (no sources)
**Expected:** One unsourced statistic (60% ARR growth) flagged; DACH expansion flagged if strictness=full; overall MEDIUM RISK.

### Case 2 — Well-cited brief
**Input:** Account brief with 5 claims, each followed by `[Source: Northlight press release, 2026-09-01]`.
**Expected:** All 5 claims pass; no unsourced flags; overall LOW RISK.

## Related skills
- Hallucination Challenge (Skill 66)
- Privacy and Data-Minimisation Review (Skill 68)
- Account Brief Builder (Skill 11)
