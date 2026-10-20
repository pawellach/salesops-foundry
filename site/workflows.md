---
layout: page
title: Workflows
---

# Workflows

8 end-to-end multi-agent workflows covering the full sales process.

---

## Account to Meeting

**Trigger:** A target account has been identified.  
**Agents:** Orchestrator → Research → Account Intelligence → Prospecting → Outreach  
**Output:** A prepared outreach draft for human approval and a call-ready account brief.  
**Approval gates:** Amber (outreach draft) — human approves before sending.

---

## Signal to Action

**Trigger:** A buying signal has been detected for a tracked account.  
**Agents:** Orchestrator → Signal Monitor → Account Intelligence → Outreach  
**Output:** A prioritised recommended action with supporting evidence, and an optional outreach draft.  
**Approval gates:** Amber (if outreach is recommended).

---

## Inbound Lead Triage

**Trigger:** A new inbound lead arrives via web form, email, or event.  
**Agents:** Orchestrator → Research → Account Intelligence → Pipeline Analyst  
**Output:** Lead classification (qualified/unqualified/needs-info), routing recommendation, and qualification questions draft.  
**Approval gates:** Green (classification is internal). Amber (if outreach is proposed).

---

## Discovery to Demo

**Trigger:** A discovery call has been completed and notes are available.  
**Agents:** Orchestrator → Discovery & Deal Coach → Pipeline Analyst  
**Output:** Structured discovery notes, qualification summary, and a demo plan.  
**Approval gates:** Green (all internal preparation).

---

## Demo to Follow-up

**Trigger:** A demo has been completed and notes are available.  
**Agents:** Orchestrator → Discovery & Deal Coach → Outreach Agent  
**Output:** Structured demo debrief, a follow-up email draft, and a Mutual Action Plan draft.  
**Approval gates:** Amber (follow-up email draft).

---

## Opportunity Review

**Trigger:** Weekly cadence or manager request.  
**Agents:** Orchestrator → Pipeline Analyst  
**Output:** Opportunity Review for a single deal with qualification gaps and recommended actions.  
**Approval gates:** Green (internal review).

---

## Weekly Pipeline Review

**Trigger:** Weekly (manager-initiated).  
**Agents:** Orchestrator → Pipeline Analyst → Safety & Privacy Reviewer  
**Output:** Weekly Pipeline Report, hygiene audit summary, and forecast challenge.  
**Approval gates:** Green (internal). Amber if any follow-up outreach is recommended.

---

## Human Approval Gates

**Not a workflow — a policy document.**  
**File:** `workflows/human-approval-gates.md`  
**Content:** Master list of every action class, its approval tier (Green/Amber/Red), and the required approval record format.
