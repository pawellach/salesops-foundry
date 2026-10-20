---
name: Next-Best-Action Planner
description: Rank the most valuable next actions across accounts and opportunities by value, confidence, effort, and risk.
group: "03 — Run the Pipeline"
version: "1.0"
status: implemented
---

# Next-Best-Action Planner

## Purpose
Given a set of accounts or opportunities, recommend the specific next action for each, ranked by expected value, confidence of outcome, effort required, and risk of inaction. Help the seller focus time on the highest-leverage moves.

## When NOT to use
- When only one account or opportunity is being reviewed (use Opportunity Risk Review instead).
- When the seller has not supplied any account or deal context.
- As an automated action executor — this skill plans; humans act.

## Required inputs
- List of accounts or opportunities to consider (minimum 3; maximum 20 per run for quality).
- For each: current stage, last activity date, deal size or potential, and any known risks or blockers.

## Optional inputs
- Risk reviews for each opportunity (from Skill 29).
- Signals for each account (from Skill 19).
- Seller's available time this week (e.g., "10 hours of selling time").

## Step-by-step procedure

1. **Score each account/opportunity** on four dimensions (1–3 scale each):
   - **Value:** Deal size × stage probability. 3 = high value; 1 = low value.
   - **Confidence:** How likely is a positive outcome from the next action? 3 = high; 1 = low.
   - **Effort:** How much seller time does the best next action require? 3 = low effort; 1 = high effort.
   - **Risk of inaction:** What happens if this account is ignored for 5 business days? 3 = high urgency; 1 = low urgency.
2. **Calculate a priority score** for each: Value + Confidence + Effort + Risk of Inaction (max = 12).
3. **Identify the specific next action** for each account. Be concrete: not "follow up" but "send Touch 2 email using Series B angle on Tue 22 Oct."
4. **Rank by priority score.** Top 3 are the recommended focus for this selling period.
5. **Flag accounts to deprioritise.** Any account with no activity for >30 days and priority score ≤5 should be flagged for deprioritisation review.
6. **Produce priority action list.**

## Output contract

```markdown
## Next-Best-Action Plan
Seller: [Name] | Period: Week of 2026-10-20
Accounts reviewed: 5

### Priority actions

| Rank | Account | Priority Score | Next action | Deadline |
|---|---|---|---|---|
| 1 | Northlight Technologies | 10 | Send Touch 2 email (Series B angle) | Tue 22 Oct |
| 2 | Meridian Logistics | 9 | Book economic buyer intro call | Wed 23 Oct |
| 3 | Acme Corp | 8 | Send mutual action plan draft | Thu 24 Oct |

### Full scoring

| Account | Value | Confidence | Effort | Urgency | Score |
|---|---|---|---|---|---|
| Northlight Technologies | 3 | 2 | 3 | 2 | 10 |
| Meridian Logistics | 3 | 3 | 2 | 1 | 9 |
| Acme Corp | 2 | 2 | 3 | 1 | 8 |
| Tanaka Industries | 2 | 1 | 2 | 1 | 6 |
| Birchwood Ltd | 1 | 1 | 2 | 1 | 5 |

### Deprioritisation flags
- Birchwood Ltd: last activity 35 days ago; score 5 — recommend pausing active outreach.
```

## Evidence and citation rules
- Priority scores must trace to stated facts (deal size, last activity date, known blockers).
- Do not inflate confidence scores to favour accounts the seller likes.

## Confidence/uncertainty handling
- Label scores as estimates when deal size or stage probability is unknown.
- If data is too thin to score reliably, note it and use defaults with a flag.

## Safety, privacy, and compliance constraints
- Do not take any outreach action based on this plan.
- Deprioritisation is a recommendation; the seller decides.

## Human approval requirements
**This skill produces a prioritised action plan. No action is taken autonomously.** The seller reviews the ranked list, decides which actions to pursue, and executes them.

## Failure modes and fallback behaviour
- **Fewer than 3 accounts supplied:** Run the plan but note it is most useful with ≥5 accounts.
- **Missing data:** Use lowest score for missing dimensions and flag.

## Acceptance criteria
- Each account has a priority score with component dimensions.
- Top 3 actions are specific and time-bound.
- Deprioritisation flags are explicit.
- No action taken autonomously.

## Evaluation cases

**Case 1 — Mixed portfolio.**
Input: 5 accounts at different stages with varying deal sizes and last activity dates.
Expected: Ranked priority list; top 3 with specific next actions and dates; deprioritisation flag for any account with score ≤5 and >30 days inactive.

**Case 2 — All accounts under-documented.**
Input: 5 accounts with minimal data.
Expected: Scoring uses defaults; output flags that scores are low-confidence; recommends enriching account data before acting.

## Related skills
- [Opportunity Risk Review](/skills/03-run-the-pipeline/opportunity-risk-review/SKILL.md) — inputs for scoring.
- [Pipeline Stage Recommendation](/skills/03-run-the-pipeline/pipeline-stage-recommendation/SKILL.md) — stage data for scoring.
- [Weekly Pipeline Report](/skills/05-sales-enablement/weekly-pipeline-report/SKILL.md) — uses this output.
