# Follow-up Email Prompt

**Purpose:** Draft a follow-up email that adds value rather than just repeating the first message.

**Inputs:**
- `{{prospect_name}}` — first name
- `{{company_name}}` — their company
- `{{prior_message_summary}}` — brief summary of what you sent before
- `{{value_add}}` — something new to offer (insight, resource, question, relevant news)
- `{{ask}}` — the ask (same as before, or a lighter version)

---

## Prompt template

```
Write a follow-up email to {{prospect_name}} at {{company_name}}.

Context:
- Prior message: {{prior_message_summary}}
- They have not responded
- New value to add: {{value_add}}
- Ask: {{ask}}

Rules:
- 2–3 sentences maximum
- Do not repeat the previous message
- Add something new: an observation, a question, a relevant resource, or a different angle
- Don't apologise for following up
- Don't guilt-trip or pressure
- Keep the ask equal to or lighter than the previous one

Format:
[email body only — no subject line needed for a reply thread]
```

---

## Usage notes

- A good follow-up adds value; a bad one just says "just following up."
- Three touches is a reasonable default; more requires evidence that it works for your audience.
- After three touches with no response, use the break-up email template.
