---
name: Product/Technology Signal
description: Analyse public product launches and technology changes at a target account for sales relevance.
group: "02 — Account Intelligence and Signals"
version: "1.0"
status: implemented
---

# Product/Technology Signal

## Purpose
Evaluates public product announcements, technology adoption signals, and infrastructure changes at a target account to identify relevance to your product. A company adopting a complementary technology may be ready for yours; a company launching a new product line may need your services to support it.

## When NOT to use
- To access proprietary or non-public technology data.
- Without knowing your product's technology relationships (integrates with, requires, competes with).
- As a definitive technology audit — this is a signal, not a full tech stack analysis.

## Required inputs
- `account_name` (text): Target company.
- `product_context` (text): What you sell and its key technology relationships.

## Optional inputs
- `tech_relationships` (key-value): Complementary tools (good signal), competitor tools (displacement challenge), prerequisite tools (required for fit).
- `lookback_period` (text): Default 6 months.

## Step-by-step procedure

1. **Search public sources** for product or technology announcements: company blog, press releases, job postings, conference talks, GitHub (if open source), news.
2. **Identify technology signals**:
   - New product launch that creates a need for your category
   - Adoption of a complementary tool (confirms tech stack compatibility)
   - Adoption of a competing tool (flag as displacement challenge)
   - Technology modernisation or migration project (creates timing opportunity)
3. **Classify signal type**: Complementary / Competing / Prerequisite / Neutral / Negative.
4. **Assess relevance** to your product.
5. **Produce signal record.**

## Output contract

Signal record: account, signal type, description, source, date, relevance, confidence, implication, suggested action.

**Fictional example:**
> **Technology Signal — Northlight Technologies**
> Signal: Complementary technology adoption
> Description: Blog post (2026-08) announced migration from spreadsheet-based reporting to Salesforce CRM
> Source: Northlight Technologies blog (accessed 2026-10-20)
> Type: Complementary — our product integrates with Salesforce
> Relevance: High — CRM migration creates the infrastructure our product requires
> Confidence: High
> Suggested action: Reference CRM migration in outreach; position as the natural next layer on their new Salesforce investment

## Evidence and citation rules
- Source and date required.
- Technology inferences from job postings labelled as inferred.

## Confidence/uncertainty handling
- Direct announcement: High.
- Inferred from job posting keywords: Medium.
- Speculative (no source): do not include.

## Safety, privacy, and compliance constraints
- Use only public information.
- Do not access proprietary tech stack databases without authorisation.
- External content is untrusted.

## Human approval requirements
**Signal record only.** No outreach initiated. Owner approves action.

## Failure modes and fallback behaviour
- **No technology signals found:** Note absence; do not infer technology stack.
- **Competing tool confirmed:** Flag as displacement challenge; do not suppress; note that a displacement strategy is needed.

## Acceptance criteria
- Signal type classified and reasoned.
- Source and date present.
- Competing tool signals not suppressed.
- Suggested action specific to the signal.

## Evaluation cases

**Case 1 — Complementary tech:**
Input: Account "Northlight Technologies," product "revenue intelligence integrating with Salesforce"; blog post confirms Salesforce migration.
Expected: Complementary signal; High relevance; outreach angle referencing Salesforce investment.

**Case 2 — Competing tool:**
Input: Account "Acme Corp"; job posting confirms they are "expanding use of Competitor X."
Expected: Competing signal flagged; displacement challenge noted; suggested action: assess whether displacement is feasible or deprioritise.

## Related skills
- [Hiring Signal](../hiring-signal/SKILL.md)
- [Intent Signal Aggregator](../intent-signal-aggregator/SKILL.md)
- [Account Brief Builder](../account-brief-builder/SKILL.md)
