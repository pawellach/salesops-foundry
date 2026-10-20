# First-Touch Email Prompt

**Purpose:** Draft a personalised, signal-grounded first-touch email to a new prospect.

**Inputs:**
- `{{prospect_name}}` — first name
- `{{prospect_role}}` — their job title
- `{{company_name}}` — their company
- `{{signal_or_context}}` — the specific reason you're reaching out (funding, hire, job ad, news, referral)
- `{{pain_hypothesis}}` — the problem you think they have (based on research)
- `{{your_value_proposition}}` — what you do in one sentence
- `{{ask}}` — the low-friction ask (e.g., "Would a 20-minute call make sense?")

---

## Prompt template

```
Write a first-touch cold email to {{prospect_name}}, {{prospect_role}} at {{company_name}}.

Context:
- Signal / reason for outreach: {{signal_or_context}}
- Pain hypothesis: {{pain_hypothesis}}
- What we do: {{your_value_proposition}}
- Ask: {{ask}}

Rules:
- 3–4 sentences maximum (excluding subject line and sign-off)
- Open with the signal or context — not with "I" or a statement about your product
- Reference the pain hypothesis as a question or observation, not a fact ("I imagine..." or "Are you finding...")
- One clear, low-friction ask at the end
- No hype, no jargon, no claims you can't back up
- Do not fabricate information about the prospect or company
- Output: subject line + email body

Format:
Subject: [subject line]

[email body]
```

---

## Usage notes

- Review the output before sending. The signal reference and pain hypothesis must be accurate.
- If the output makes a claim you can't verify, remove or soften it.
- The subject line options can be tested — A/B test over 20+ sends to find what works for your audience.
