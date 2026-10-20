# Options Framing Prompt

**Purpose:** Frame three negotiation scenarios before a commercial conversation.

**Inputs:**
- `{{deal_context}}` — what the prospect has asked for or objected to
- `{{your_constraints}}` — your walk-away conditions and approval thresholds
- `{{tradeable_variables}}` — variables you can move on (price, term, scope, support, timing)

---

## Prompt template

```
Prepare three negotiation scenarios for the following deal situation.

Deal context: {{deal_context}}
Your constraints: {{your_constraints}}
Variables you can trade on: {{tradeable_variables}}

For each scenario, specify:
- **Name**: Optimal / Acceptable / Last Resort
- **Price or commercial terms**: [specific]
- **Other variables**: [what changes in scope, term, support, or timing]
- **Rationale**: why this scenario works for both sides
- **What you get**: what you receive in return for any concession
- **Risk**: what's the risk of accepting this scenario

Rules:
- All scenarios must be within your stated constraints
- Each concession must be paired with something you receive
- Do not create a scenario that requires approval you don't have
- Label the walk-away condition explicitly: "If the prospect pushes beyond Last Resort, the correct response is [X]."
```

---

## Usage notes

- Review all three scenarios with your manager before the negotiation if the deal is significant.
- Know your walk-away before the meeting, not during it.
- The "optimal" scenario should be genuinely good for both sides — not just maximally good for you.
