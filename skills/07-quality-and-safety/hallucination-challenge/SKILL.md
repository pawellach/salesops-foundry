---
name: Hallucination Challenge
description: Adversarially search a sales document or skill output for invented facts, dates, people, metrics, and claims that cannot be verified from supplied sources.
group: "07 — Quality, Safety, and Governance"
version: "1.0"
status: implemented
---

# Hallucination Challenge

## Purpose
Actively challenge a document or AI-generated output for hallucinated content: facts that sound plausible but are invented. This skill goes beyond citation checking (Skill 65) — it probes whether the content contains claims that contradict supplied sources, are internally inconsistent, or are the typical failure modes of language models (fabricated names, round-number statistics, invented quotes, false product capabilities).

## When NOT to use
- As a substitute for ground-truth verification against live data.
- On documents the user has personally written and stands behind — use Source and Citation Auditor (Skill 65) instead.
- When the document is explicitly a draft and the user has not yet sourced it.

## Required inputs
- `document`: the text to challenge
- `sources`: the source material the document was generated from (if any)

## Optional inputs
- `focus_areas`: specific claim types to prioritise (e.g. "statistics", "named individuals", "product features", "dates")
- `document_type`: "account brief" | "outreach email" | "discovery notes" | "pipeline summary" | "skill output"

## Step-by-step procedure
1. Read the document and sources.
2. Identify every factual claim not directly traceable to the provided sources.
3. For each such claim, apply the hallucination heuristics:
   - **Named individuals:** Is this person real and in the role claimed? Is there source evidence?
   - **Round-number metrics:** Suspiciously round numbers (e.g. "saves 40% of time") without context are high-risk.
   - **Quotes:** Any attributed quote not in the sources is a fabrication candidate.
   - **Dates:** Check for plausibility — future dates claimed as past, dates that don't match supplied context.
   - **Product/feature claims:** Claims about a product's capabilities that go beyond what the sources say.
   - **Internal inconsistency:** The same fact stated differently in two places.
4. Rate each finding: LIKELY HALLUCINATION / POSSIBLE HALLUCINATION / UNVERIFIABLE / CONSISTENT WITH SOURCES.
5. Produce the challenge report.

## Output contract
```markdown
## Hallucination Challenge Report

**Document type:** <type>
**Challenge date:** <YYYY-MM-DD>
**Source material provided:** Yes/No

### Findings
| # | Claim | Finding | Explanation |
|---|---|---|---|
| 1 | "CEO Sarah Chen joined in 2023" | UNVERIFIABLE | No source mentions Sarah Chen or her start date |
| 2 | "Saves 40% of sales rep time" | LIKELY HALLUCINATION | Round-number metric with no study or source cited |

### Summary
- Likely hallucinations: <N>
- Possible hallucinations: <N>
- Unverifiable claims: <N>
- Consistent with sources: <N>
- **Recommendation:** PASS / REVISE / REJECT
```

## Evidence and citation rules
- Every finding must explain why it is suspicious, not just assert it.
- Findings rated CONSISTENT WITH SOURCES must cite which source.
- Do not fabricate "correct" information to replace a suspected hallucination — mark it and flag for human verification.

## Confidence/uncertainty handling
- State clearly: "This challenge identifies suspicious claims; it does not verify ground truth."
- UNVERIFIABLE ≠ false. It means the claim cannot be confirmed from provided sources.

## Safety, privacy, and compliance constraints
- Do not reproduce personal data from the document in the report unless essential to identify the finding.
- If the document contains an invented person's personal details (fabricated email, phone, etc.), flag as HIGH RISK privacy issue.

## Human approval requirements
- No external actions required. This skill produces a local report.
- REJECT-rated documents must not be used in any external communication until reviewed and corrected by a human.

## Failure modes
- **False positives:** Real facts with no source in the provided material will be flagged as UNVERIFIABLE. This is expected — the reviewer resolves them.
- **Source coverage gap:** If no sources are provided, nearly all claims will be UNVERIFIABLE, reducing the report's value.

## Acceptance criteria
- All material claims in the document are assessed.
- At least one of the four finding categories is applied to each claim.
- The overall PASS/REVISE/REJECT recommendation is present.

## Evaluation cases

### Case 1 — Fabricated quote
**Input:** Account brief containing: `"According to their CTO Mark Davies, 'We're actively evaluating new vendors.'"` — no source material mentions Mark Davies.
**Expected:** LIKELY HALLUCINATION — fabricated attributed quote; not in any supplied source.

### Case 2 — Round-number claim
**Input:** Outreach email: `"Teams using tools like ours report 45% faster ramp time for new reps."`
**Expected:** POSSIBLE HALLUCINATION — round metric, no study cited; recommend removing or sourcing.

## Related skills
- Source and Citation Auditor (Skill 65)
- Privacy and Data-Minimisation Review (Skill 68)
- Regression Evaluator (Skill 72)
