# Coaching 1:1 Prep Prompt

**Purpose:** Prepare an evidence-based agenda for a sales coaching 1:1.

**Inputs:**
- `{{rep_name}}` — the rep's name
- `{{pipeline_summary}}` — brief summary of their current pipeline
- `{{recent_activity}}` — recent calls, emails, or deal updates (as notes)
- `{{prior_coaching_focus}}` — what you worked on last time

---

## Prompt template

```
Prepare a coaching 1:1 agenda for {{rep_name}}.

Pipeline summary: {{pipeline_summary}}
Recent activity: {{recent_activity}}
Prior coaching focus: {{prior_coaching_focus}}

Generate:
1. **Pipeline review questions** (2–3): evidence-seeking questions about specific deals — not "how is X going?" but "what evidence do you have that the CFO is aware of this?"
2. **Pattern observation** (1): one pattern you see across their deals that is worth discussing (positive or developmental)
3. **Coaching focus for this session** (1 only): the single most valuable skill or behaviour to work on, based on evidence from their pipeline and activity
4. **One specific example** to anchor the coaching conversation (a specific deal or call moment)
5. **Suggested action** for the rep to take before the next 1:1

Rules:
- All observations must be grounded in the provided pipeline/activity data
- Do not invent deal details or coaching points not supported by the input
- One coaching focus only — not a list
- Frame developmental observations constructively, not punitively
```

---

## Usage notes

- The one-coaching-focus rule is intentional — covering everything means improving nothing.
- Review the output against your own knowledge of the rep before using it.
- The rep's self-assessment (ask them at the start of the 1:1) often surfaces more useful information than a prepared agenda.
