---
name: Lead Routing Recommendation
description: Suggest lead ownership using transparent, configurable routing rules — never route autonomously.
group: "03 — Run the Pipeline"
version: "1.0"
status: implemented
---

# Lead Routing Recommendation

## Purpose
Apply a supplied set of routing rules to a triaged lead and produce a ranked recommendation for which salesperson, team, or queue should own the lead, with the reasoning made explicit.

## When NOT to use
- Before Lead Triage has been completed.
- When no routing rules have been defined (do not invent rules).
- When the recommended owner is unavailable and no fallback is defined in the rules.

## Required inputs
- Lead triage output (from **Lead Triage**, Skill 21).
- Routing rules document: criteria (territory, product line, role seniority, deal size, language, etc.) mapped to owners.

## Optional inputs
- Team capacity or availability data (if supplied, use to prefer available owners).
- Historical win-rate by owner segment (if supplied, note as a tiebreaker signal, not a hard rule).

## Step-by-step procedure

1. **Parse routing rules.** Extract all routing dimensions and their mappings from the supplied rules document.
2. **Match lead to rules.** For each routing dimension, evaluate whether the lead satisfies the criterion. Use only confirmed data from the triage output; treat Unconfirmed dimensions as non-matches.
3. **Identify primary owner.** The owner whose rules match the most confirmed dimensions is the primary recommendation. If multiple owners tie, list all and flag the tie.
4. **Identify fallback owner.** If the routing rules specify a fallback (e.g., round-robin queue, manager), name it.
5. **Explain the recommendation.** For each routing dimension used, state the criterion, the lead's data, and whether it matched.
6. **Flag exceptions.** If the lead matches an exclusion criterion, a special-handling flag, or no rule at all, escalate rather than assigning silently.
7. **Produce routing recommendation document.**

## Output contract

```markdown
## Routing Recommendation — [Company Name] / [Contact Name]
Date: YYYY-MM-DD

**Primary recommended owner:** [Name or Queue]
**Fallback:** [Name or Queue, or "Not defined"]
**Confidence:** High | Medium | Low

### Routing dimension matches
| Dimension | Criterion | Lead data | Match |
|---|---|---|---|
| Territory | EMEA | Company HQ: UK | Yes |
| Product line | Platform tier | Mentioned "enterprise integration" | Possible |
| Deal size | >£50k ACV | No data | No |

### Exceptions / flags
- Deal size unconfirmed — AE to qualify on first call.

### Routing rationale
Territory match is confirmed. Product line is possible based on form language. Deal size is unknown.
```

## Evidence and citation rules
- Routing decisions must cite the specific rule criterion and the specific lead data element that matched or did not match.
- Do not infer routing from the company name or contact title alone without a matching rule.

## Confidence/uncertainty handling
- Confidence = High when ≥2 dimensions are confirmed matches and no flags exist.
- Confidence = Medium when ≥1 confirmed match and ≤1 flag.
- Confidence = Low when primary match relies on Possible status or unconfirmed data.

## Safety, privacy, and compliance constraints
- Do not expose routing rules that contain salary, commission, or personal performance data in the output.
- Do not assign leads based on protected characteristics of the contact (nationality, gender, etc.).

## Human approval requirements
**No lead is routed without a human decision.** This skill produces a recommendation document only. The sales manager or ops team reviews and takes the actual routing action in the CRM or queue system.

## Failure modes and fallback behaviour
- **No matching rule:** Output "No rule match — escalate to manager" with a list of unmatched dimensions.
- **Routing rules document missing:** Return an error; do not invent rules.
- **Multiple equal matches:** List all candidates; do not arbitrarily select one.

## Acceptance criteria
- Recommendation names at least one owner or explicitly escalates.
- Every routing dimension in the rules is addressed in the output.
- Confidence level is stated and justified.
- No autonomous CRM update is made.

## Evaluation cases

**Case 1 — Clean single match.**
Input: Lead triage = Strong, EMEA territory, enterprise inquiry. Routing rules: EMEA → Alice Chen; SMB → Bob Müller.
Expected: Primary = Alice Chen; Confidence = High; one dimension match explained.

**Case 2 — No rule match.**
Input: Lead triage = Moderate, company in APAC. Routing rules cover only EMEA and North America.
Expected: Output = "No rule match — escalate to manager"; no owner named.

## Related skills
- [Lead Triage](/skills/03-run-the-pipeline/lead-triage/SKILL.md) — prerequisite.
- [Territory Planner](/skills/01-find-buyers/territory-planner/SKILL.md) — defines the territory structure used in routing rules.
- [Warm-Path Mapping](/skills/03-run-the-pipeline/warm-path-mapping/SKILL.md) — used after routing to find the best introduction path.
