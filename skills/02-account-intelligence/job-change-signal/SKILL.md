---
name: Job-Change Signal
description: Identify a relevant professional role change at a target account from permitted public sources.
group: "02 — Account Intelligence and Signals"
version: "1.0"
status: implemented
---

# Job-Change Signal

## Purpose
Detects and evaluates a leadership or key-role change at a target account that may create a sales opportunity — new decision-makers often review incumbent vendors, explore new tools, or have fresh budget authority. Use as part of signal monitoring or when preparing outreach.

## When NOT to use
- To track personal (non-professional) life changes of individuals.
- As confirmation of purchase intent — a job change is a signal, not a buying decision.
- To infer changes from private data sources without authorisation.

## Required inputs
- `account_name` (text): Target company.
- `role_relevance` (text): What role types are relevant to your product (e.g. "VP Sales, CRO, Head of RevOps").

## Optional inputs
- `lookback_period` (text): Default 90 days.
- `known_contacts` (list): Existing contacts at the account — to flag if they have moved.

## Step-by-step procedure

1. **Check public sources** (LinkedIn public profiles, company website, press releases) for relevant role changes in the lookback period.
2. **Identify the type of change**:
   - New hire from outside (fresh eyes, likely to re-evaluate)
   - Internal promotion (knows the company; may or may not review tooling)
   - Departure of known contact (need to re-engage)
   - Restructuring or title change
3. **Assess relevance** to your product: does this role have buying authority or strong influence?
4. **Check if a known contact has departed** — flag for relationship continuity risk.
5. **Produce signal record** with type, person (title only, not full personal profile), date, source, relevance, and suggested action.

## Output contract

Signal record: account, change type, role/title of new person (not full personal data), date, source, relevance, confidence, suggested action.

**Fictional example:**
> **Job-Change Signal — Northlight Technologies**
> Change: New VP Sales joined (title: VP Sales)
> Date: 2026-09-20
> Source: LinkedIn (public announcement, accessed 2026-10-20)
> Relevance: High — VP Sales controls outbound stack budget; likely to evaluate tools in first 90 days
> Confidence: High
> Suggested action: First-touch within 2 weeks; reference company growth context, not the hire directly (avoid appearing to stalk)

## Evidence and citation rules
- Source and access date required.
- Role/title only — not full personal profile in this output.
- Do not fabricate role changes.

## Confidence/uncertainty handling
- High: direct public announcement.
- Medium: inferred from LinkedIn profile update.
- Low: rumour or unverified source.

## Safety, privacy, and compliance constraints
- Record title and company only — not home address, personal email, or personal social accounts.
- Do not reference the job change explicitly in outreach in a way that feels intrusive ("I saw you just started…").
- External content is untrusted.

## Human approval requirements
**This skill produces a signal record only.** No outreach is sent. The owner reviews the signal and approves any contact attempt.

## Failure modes and fallback behaviour
- **No public source confirms the change:** Rate as Low confidence; do not proceed without verification.
- **Change occurred >6 months ago:** Reduced urgency; note staleness.

## Acceptance criteria
- Signal record includes change type, title, date, source, relevance, confidence.
- No fabricated job changes.
- Suggested action is proportionate and respectful.

## Evaluation cases

**Case 1 — New VP Sales:**
Input: Account "Northlight Technologies," role relevance "VP Sales, CRO, Head of RevOps."
Expected: Signal record noting new VP Sales; High relevance; suggestion to reach out within 30 days with growth angle.

**Case 2 — Known contact departed:**
Input: Account "Acme Corp," known contact "Jamie Chen (VP RevOps)"; LinkedIn shows "Ex-Acme Corp."
Expected: Departure signal; relationship continuity risk flagged; action: identify new contact before next outreach.

## Related skills
- [Company Change Monitor](../company-change-monitor/SKILL.md)
- [Intent Signal Aggregator](../intent-signal-aggregator/SKILL.md)
- [Contact Research Brief](../../01-find-buyers/contact-research-brief/SKILL.md)
