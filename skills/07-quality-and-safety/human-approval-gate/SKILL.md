---
name: Human Approval Gate
description: Classify a proposed agent action by risk tier and generate an approval request for human review before the action proceeds.
group: "07 — Quality, Safety, and Governance"
version: "1.0"
status: implemented
---

# Human Approval Gate

## Purpose
Before any consequential external action is taken, classify it by risk tier, summarise what will happen, list what can't be undone, and present it to the human for approval or rejection. This skill is the enforcement mechanism for the human-governance principle of SalesOps Foundry.

## When NOT to use
- For read-only local operations (reading files, local analysis, draft creation).
- When the human has already given explicit approval for this exact action in the current session.

## Required inputs
- `action_description`: a precise description of the proposed action (what will be sent/written/published/created, to whom, on which platform)
- `agent`: which agent is requesting the action
- `skill_context`: which skill or workflow triggered this request

## Optional inputs
- `reversibility`: "reversible" | "partially reversible" | "irreversible" — provide if known
- `urgency`: "low" | "medium" | "high" — affects how the approval request is framed
- `draft_content`: the content that will be acted upon (email body, CRM update, etc.)

## Step-by-step procedure
1. Classify the action into a risk tier:
   - **Green:** No external effect (local reads, draft creation, analysis). Gate not required.
   - **Amber:** Reversible external effect (booking a meeting slot, creating a draft CRM note for review). Gate recommended.
   - **Red:** Consequential or irreversible (sending email, posting to LinkedIn, writing to CRM, publishing a page, making a repo public).
2. For Red actions, produce the full approval request (see Output contract).
3. For Amber actions, produce a shorter "proceed or review" prompt.
4. For Green actions, return immediately with "No gate required for this action class."
5. Record the action, its classification, and the outcome (approved/rejected/pending) in the session log.

## Output contract
```markdown
## Human Approval Request

**Action:** <precise description>
**Requested by:** <agent name>
**Risk tier:** GREEN / AMBER / RED
**Reversibility:** <reversible / partially reversible / irreversible>
**Urgency:** <low / medium / high>

### What will happen if approved
<One paragraph describing the exact action and its immediate effects>

### What cannot be undone
<List of irreversible effects, or "None — fully reversible" if applicable>

### Draft content (if applicable)
<The email / message / CRM update that will be sent or written>

### Decision
- [ ] APPROVE — proceed with the action as described
- [ ] REJECT — do not proceed
- [ ] MODIFY — modify the draft (provide instructions below)

**Reviewer:** ___________________  
**Decision date:** ___________________  
**Notes:** ___________________
```

## Evidence and citation rules
- The action description must be specific — not "send an outreach email" but "send the email below to james.okafor@northlight-tech.com from pawel@acme.com."
- Draft content must be shown in full, not summarised.

## Confidence/uncertainty handling
- If the reversibility of an action is uncertain, classify it as irreversible.
- If the action class is borderline between Amber and Red, classify as Red.

## Safety, privacy, and compliance constraints
- A Red action must never proceed without an explicit APPROVE decision recorded.
- This gate applies to ALL agents, including the Orchestrator.
- Bulk or scheduled actions require a separate approval record for each batch.

## Human approval requirements
- **This skill is itself the approval mechanism.** It does not require additional approval to run.
- The output record must be saved and acknowledged by the human before any Red action proceeds.

## Failure modes
- **Gate bypass:** An agent may attempt to proceed without invoking this gate. The Safety Reviewer (Skill 11 agent) audits for this pattern.
- **Vague action descriptions:** An approval given for a vague description does not constitute approval for a specific consequential action. Descriptions must be specific.

## Acceptance criteria
- Every Red action produces a complete approval request with draft content shown in full.
- The approval/rejection outcome is recorded.
- No Red action proceeds without a recorded APPROVE decision.

## Evaluation cases

### Case 1 — Email send request
**Input:** Outreach Agent requests approval to send a first-touch email to "James Okafor, VP Sales, Northlight Technologies."
**Expected:** RED tier; full approval request produced; draft email shown in full; irreversible noted (email cannot be unsent once delivered).

### Case 2 — Local draft creation
**Input:** Outreach Agent requests to create a draft email file locally.
**Expected:** GREEN tier; "No gate required for this action class" returned immediately.

## Related skills
- Outreach Compliance Checklist (Skill 69)
- Prompt-Injection Defence Review (Skill 67)
- Privacy and Data-Minimisation Review (Skill 68)
