# Demo Storyline Prompt

**Purpose:** Build a demo narrative that connects product capabilities to the prospect's confirmed needs.

**Inputs:**
- `{{company_name}}` — the prospect's company
- `{{confirmed_pains}}` — the specific pains confirmed in discovery (not hypotheses)
- `{{product_capabilities}}` — the capabilities you plan to demonstrate
- `{{prospect_success_criteria}}` — what they said a good solution looks like

---

## Prompt template

```
Build a demo storyline for {{company_name}}.

Confirmed pains from discovery:
{{confirmed_pains}}

Prospect's success criteria:
{{prospect_success_criteria}}

Product capabilities to demonstrate:
{{product_capabilities}}

Structure the demo storyline as:
1. **Opening frame** (2–3 sentences): Acknowledge what you heard in discovery. Connect their situation to what you're about to show. No product intro yet.
2. **Core sequence** (3–5 steps): Map each capability to a specific confirmed pain. For each: [Pain → Capability → "What this means for you"]
3. **Closing frame**: Connect to their success criteria. Propose a natural next step.

Rules:
- Ground every capability demonstration in a confirmed pain — not a hypothetical one
- Do not include capabilities that don't connect to their stated needs
- Avoid superlatives and product hype
- The sequence should feel like a story, not a feature checklist
```

---

## Usage notes

- Only include capabilities that map to confirmed pains. If you're including something "just in case they care about it," remove it.
- The opening frame is the most important part — it signals you listened.
- Review the output against your actual discovery notes before using it.
