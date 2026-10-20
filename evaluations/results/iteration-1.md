# Iteration 1 — Internal Quality Review

**Date:** 2026-10-20  
**Reviewer:** Tanasku 探索 (internal)  
**Files sampled:** 18 (12 skills, 2 agents, 2 workflows, 2 playbooks)

---

## Summary

The repository's content is substantive, well-structured, and safe. All 18 sampled files contain the required sections, have complete YAML frontmatter, meet the 30-line minimum, and include explicit human-approval statements. The core safety policy (no autonomous sending, Amber/Red gates) is consistently enforced. The main findings are formatting inconsistencies introduced by parallel generation: two distinct patterns exist across the six generation batches. No critical findings. Three high-severity findings affect navigability and future tooling; they can be fixed programmatically.

---

## Findings

### Critical (must fix before release)

_None._

---

### High (should fix)

**H-01 — Missing title heading in Groups 5+6 skills**  
`skills/05-sales-enablement/forecast-challenge/SKILL.md` (line 8 — `## Purpose` is first heading, no `# Title` above it)  
`skills/06-revenue-operations/roi-time-saved-estimator/SKILL.md` (same pattern)

Groups 1–4 and 7 all begin with `# Skill Name` followed by `## Purpose`. Groups 5+6 start directly at `## Purpose` with no preceding `# Title` heading. This causes the skill to render without a visible title in GitHub Markdown and is inconsistent with all other groups. Affects all 10 Group-5 and 12 Group-6 skills (22 files total, based on consistent generation pattern within each batch).

**Fix:** Add `# {name}` heading between the closing `---` of frontmatter and `## Purpose` in all Group 5 and 6 SKILL.md files.

---

**H-02 — Related-skills cross-references not actual Markdown links in Groups 3–7**  
`skills/03-run-the-pipeline/first-touch-draft/SKILL.md` (line 108 — `**Personalised Outreach Planner** (Group 3, Skill 24)` — text only, no link)  
`skills/05-sales-enablement/forecast-challenge/SKILL.md` (lines 115–118 — backtick slug format)  
`skills/06-revenue-operations/roi-time-saved-estimator/SKILL.md` (lines 127–130 — backtick slug format)

Groups 1+2 use proper relative Markdown links (e.g. `[Account Fit Scoring](../../skills/01-find-buyers/account-fit-scoring/SKILL.md)`) that are clickable and validated by `check_links.py`. Groups 3–7 use either bold text or backtick slugs — neither is navigable or validated. `check_links.py` gives a false clean pass on cross-references in these groups.

**Fix:** Convert all Related Skills entries in Groups 3–7 to relative Markdown links. A script can automate the slug→path mapping.

---

**H-03 — Frontmatter `group` field inconsistent across batches**  
`skills/03-run-the-pipeline/first-touch-draft/SKILL.md`: `group: "03 — Run the Pipeline"` (em dash, zero-padded)  
`skills/05-sales-enablement/forecast-challenge/SKILL.md`: `group: "5 — Sales Enablement and Management"` (em dash, no zero-padding)  
`skills/07-quality-and-safety/hallucination-challenge/SKILL.md`: `group: "7 - Quality, Safety, and Governance"` (hyphen, no zero-padding)  
`skills/01-find-buyers/icp-builder/SKILL.md`: `group: "01 - Find Buyers and Accounts"` (hyphen, zero-padded)

Four distinct formats exist:
- Groups 1–2: `"0N - Name"` (hyphen, zero-padded)
- Groups 3–4: `"0N — Name"` (em dash, zero-padded)
- Groups 5–6: `"N — Name"` (em dash, no zero-padding)
- Group 7: `"N - Name"` (hyphen, no zero-padding)

Any code that sorts or groups by the `group` frontmatter field will produce incorrect results.

**Fix:** Standardise to `"0N — Name"` (em dash, zero-padded, full name) across all 72 skills. Scriptable.

---

### Medium (consider fixing)

**M-01 — `check_links.py` does not validate cross-skill relative links in Groups 3–7**  
The link checker only validates links it can parse as relative file paths. Because Groups 3–7 use text/backtick references (H-02 above), cross-references are never validated. This means a renamed or deleted skill in Groups 3–7 will not be caught. **Resolves when H-02 is fixed.**

---

**M-02 — Section heading case inconsistency**  
`skills/07-quality-and-safety/hallucination-challenge/SKILL.md` line 72: `## Safety, privacy, and compliance` (missing trailing "constraints" — truncated compared to other skills).  
`skills/07-quality-and-safety/prompt-injection-defence/SKILL.md` line 71: `## Safety, privacy, and compliance` (same).  
Most other skills use `## Safety, privacy, and compliance constraints`. Cosmetic, but affects automated section-presence checking if added to future validation scripts.

---

**M-03 — Agent section naming varies slightly from the required checklist**  
`agents/orchestrator.md` and `agents/outreach-agent.md` both have all required sections, but heading names vary slightly from the spec (e.g., `## Skills it may invoke` vs. the spec's "Skills it may invoke"). This is fine for current use but would cause any automated section-checker to false-fail.

---

### Low / Informational

**L-01 — Prompt-injection defence skill: safe for static review; notes its own limitation clearly**  
`skills/07-quality-and-safety/prompt-injection-defence/SKILL.md` line 86 correctly notes that "static review cannot guarantee security against all novel injection techniques." The skill is honest about its scope. No change needed.

**L-02 — Discovery Call playbook skills-referenced paths use full paths from repo root**  
`playbooks/discovery-call.md` frontmatter: `skills-referenced` lists full repo-root paths (`skills/04-discovery-and-deals/...`). Other playbooks may vary. Not broken, but worth standardising when playbooks are all checked in Iteration 2.

**L-03 — Outreach Agent example uses `[First Name]` placeholder in draft body**  
`agents/outreach-agent.md` example output uses `[First Name]` and `[Signature]` inline — correct for a template, clearly marked as a draft. No change needed; just noting it is intentional.

---

## Files checked OK

All 18 sampled files pass on the following criteria:
- ✅ Complete YAML frontmatter (name, description, group, version, status or role/scope equivalent)
- ✅ Minimum 30 lines
- ✅ At least 2 evaluation cases (all skill files)
- ✅ Explicit human-approval statement present
- ✅ No fabricated specific numeric performance claims (ROI Estimator correctly uses estimates with disclaimers)
- ✅ Fictional companies only (Northlight Technologies, Acme Corp, Meridian Logistics)
- ✅ No autonomous send/CRM-write actions without approval gate
- ✅ Workflows have trigger, approval gates, failure handling
- ✅ Playbooks have preparation checklist, step-by-step guide, common mistakes or similar guidance

Files checked:
1. `skills/01-find-buyers/icp-builder/SKILL.md` ✅
2. `skills/01-find-buyers/buying-trigger-research/SKILL.md` ✅
3. `skills/02-account-intelligence/account-brief-builder/SKILL.md` ✅
4. `skills/02-account-intelligence/intent-signal-aggregator/SKILL.md` ✅
5. `skills/03-run-the-pipeline/first-touch-draft/SKILL.md` ✅ (with H-02 noted)
6. `skills/03-run-the-pipeline/follow-up-sequence-builder/SKILL.md` ✅ (with H-02 noted)
7. `skills/04-discovery-and-deals/discovery-call-plan/SKILL.md` ✅
8. `skills/04-discovery-and-deals/negotiation-planner/SKILL.md` ✅
9. `skills/05-sales-enablement/forecast-challenge/SKILL.md` ✅ (with H-01, H-02, H-03 noted)
10. `skills/06-revenue-operations/roi-time-saved-estimator/SKILL.md` ✅ (with H-01, H-02, H-03 noted)
11. `skills/07-quality-and-safety/hallucination-challenge/SKILL.md` ✅ (with H-03, M-02 noted)
12. `skills/07-quality-and-safety/prompt-injection-defence/SKILL.md` ✅ (with H-03, M-02 noted)
13. `agents/orchestrator.md` ✅
14. `agents/outreach-agent.md` ✅
15. `workflows/account-to-meeting.md` ✅
16. `workflows/human-approval-gates.md` ✅
17. `playbooks/discovery-call.md` ✅
18. `playbooks/outbound-prospecting.md` ✅

---

## Next steps for Phase 5 (Iteration 2)

Fix H-01, H-02, H-03 before adversarial review (all three are scriptable). Iteration 2 should also adversarially test:
- Prompt injection via simulated untrusted web content in Research Agent
- Request to send unsolicited email to a real contact
- Fabricated contact details in prospect brief
- Outreach agent bypassing approval gate
