# Integrations

**Status: Planned for Release 2.**

This directory will contain optional adapter modules for connecting SalesOps Foundry to external systems. All integrations are opt-in, configuration-based, and require explicit owner approval before any data is read or written.

## Planned adapters

### CRM adapters (`crm-adapters/`)
- Salesforce (read-only account/opportunity data)
- HubSpot (read-only contact/deal data)
- Generic CSV export format

### Research-source adapters (`research-sources/`)
- LinkedIn Sales Navigator (requires authorised access)
- Apollo.io (requires API key, configured by user)
- Public web search (via configured search API)

### Notification adapters (`notification-adapters/`)
- Slack (draft messages for human approval, never send autonomously)
- Email (draft messages for human approval, never send autonomously)

## MVP approach

For MVP, all skills accept plain-text file inputs (Markdown, CSV, JSON, YAML). No API credentials are required. Supply data by copying it into the appropriate template.

## Security note

Integration adapters will store credentials in environment variables only, never in Markdown, YAML, logs, or commits. See `docs/SECURITY_AND_PRIVACY.md`.
