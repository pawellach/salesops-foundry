# Operating Guide — SalesOps Foundry

**Version:** 1.0

---

## Using skills directly

Skills are the atomic unit of the toolkit. Each skill in `skills/` has a `SKILL.md` file describing what it does, what inputs it needs, and what it produces.

**Basic usage in Claude Code:**

```
Use skills/02-account-intelligence/account-brief-builder/SKILL.md.
Input: [paste your account data here]
```

**What to provide:**
- Follow the "Required inputs" section in the skill file exactly.
- If an input is optional, you can omit it — the skill will note the gap in its output.
- Never paste real personal contact data (email addresses, phone numbers).

---

## Running workflows

Workflows in `workflows/` chain multiple agents and skills across an end-to-end process.

**Example:**

```
Use workflows/account-to-meeting.md for Northlight Technologies.
Here is the account brief: [paste account brief]
```

Workflows include human approval gates. When the workflow reaches an Amber or Red tier action (such as a prepared outreach draft), it will pause and ask for your approval before proceeding.

---

## Working with the Orchestrator

For complex multi-step tasks, use the Orchestrator agent:

```
Use agents/orchestrator.md.
Goal: Research and prioritise 5 accounts from this list, then prepare outreach drafts for the top 2.
Input: [paste account list]
```

The Orchestrator will:
1. Decompose the task into sub-tasks
2. Assign each to the appropriate specialist agent
3. Pause at approval gates
4. Consolidate results

---

## Understanding approval gates

Every action that has an external effect (sending a message, writing to a CRM, publishing content) requires human approval. The system will never send a message without your explicit OK.

When you see output labelled **DRAFT — human approval required before sending**, you must:
1. Read the draft carefully
2. Verify all claims are accurate
3. Make any edits needed
4. Explicitly tell the agent "Approved — send" or save the draft to a Human Approval Record

See `templates/human-approval-record.md` for the approval record format.

---

## Customising for your team

1. **Update the ICP:** Run `skills/01-find-buyers/icp-builder/SKILL.md` with your actual hypothesis and save the output as your team's ICP document.
2. **Adjust templates:** Copy any template from `templates/` and edit the fields for your context.
3. **Add skills:** Follow `CONTRIBUTING.md` to add a skill specific to your sales process.
4. **Configure the model:** See `docs/MODEL_STRATEGY.md` to adjust model routing for cost or capability.

---

## Adding new skills

See `CONTRIBUTING.md` for full instructions. The short version:
1. Create `skills/NN-group-name/your-skill-name/SKILL.md`
2. Add YAML frontmatter: `name`, `description`, `group`, `version`, `status`
3. Follow the 16-field specification from `docs/REQUIREMENTS.md` §FR-1.2
4. Run `python scripts/validate_frontmatter.py` to verify

---

## Evaluating outputs

After running a skill or workflow, evaluate the output using `evaluations/rubric.md`. Score the 12 dimensions and record the result in `evaluations/results/`.

This helps you track quality over time and identify skills that need improvement.

---

## What the toolkit will not do

- Send emails, LinkedIn messages, or other communications without your approval
- Write to any CRM without explicit configuration and approval
- Guarantee sales results — outputs are starting points, not certainties
- Replace your judgment about a specific deal or prospect
