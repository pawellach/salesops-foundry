# Trade-off Analysis Prompt

**Purpose:** Analyse the trade-offs between deal variables to find a durable agreement.

**Inputs:**
- `{{prospect_ask}}` — what the prospect is asking for
- `{{your_priorities}}` — what matters most to you (e.g., annual contract value, payment terms, close date)
- `{{available_variables}}` — what you can trade (e.g., price, term length, scope, implementation timing)

---

## Prompt template

```
Analyse the trade-offs for the following negotiation situation.

Prospect's ask: {{prospect_ask}}
Your priorities: {{your_priorities}}
Available variables: {{available_variables}}

For each variable, assess:
1. **Cost to you** of moving on this variable (Low / Medium / High)
2. **Value to the prospect** of this variable (Low / Medium / High — based on what you know)
3. **Trade-off quality** (High-value-to-them + Low-cost-to-you = good trade; reverse = avoid)
4. **Suggested trade** (if you move on X, ask for Y in return)

Then recommend:
- **The best trade** (highest prospect value for lowest cost to you)
- **The trade to avoid** (highest cost to you for lowest prospect value)
- **One suggested opening offer** (combines your priorities with a genuine benefit to the prospect)

Rules:
- Do not fabricate information about the prospect's priorities
- Label all assessments of prospect value as [Assumption] unless confirmed in discovery
- Do not recommend trades that exceed your approval authority
```

---

## Usage notes

- The trade-off quality analysis is most reliable when the prospect's priorities were confirmed in discovery.
- [Assumption] labels indicate where you're guessing — verify if possible before the negotiation.
