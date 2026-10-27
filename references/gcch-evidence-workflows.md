# GCC High tenant evidence collection: next implementation phase

Status: implementation plan, not deployed connectors or a verified service design.
Start with the export-based agent and its schema. This plan introduces no live
credentials, jobs, network changes, tenant access, or data transfers.

## Required environment decisions

Establish tenant/cloud IDs, approved host/runtime and repository, selected deployment,
source systems, exact government endpoints/API versions, allowed permissions,
retention, evidence period, collection cadence, owners, and AI processing boundary.
Verify current official documentation for each service/API/feature and the selected
Security Copilot or ChatGPT integration before implementing it. Do not infer
Security Copilot support from Microsoft 365 Copilot or Copilot Studio availability.
Do not infer approved AI processing from GCC High source-system location.

## Workflow A: approved tenant collectors

1. Run approved queries under a tenant-controlled identity with the minimum needed
   read permissions. Separate source read rights from evidence-store write rights.
2. Use fixed, versioned collection definitions with explicit assets, fields, time
   windows, filters, pagination, retry/backoff, and record-count checks. Prefer
   allowlisted queries; do not execute arbitrary model-generated shell or API calls.
3. Record request identifiers, retrieval times, source windows, endpoint/API versions,
   permissions used, errors, truncation, and partial results. Redact credentials.
4. Write originals and collector provenance to approved tenant storage. Hash the
   artifacts and generate the common evidence manifest. Preserve failed runs.
5. Run inventory and review; compare against the prior run for drift without
   equating every configuration change to a compliance failure.
6. Route findings to an internal reviewer. Retain approvals and activity logs.
   Scheduling and notification destinations require explicit tenant configuration.

## Workflow B: Security Copilot adapter

After verifying support in the exact environment, expose narrowly scoped approved
collector/query actions through supported plugins and an agent manifest. The agent
requests a collection, reads authorized results, and drafts evidence mappings.
Keep query execution and storage deterministic and auditable. Source changes,
remediation, permission edits, and external notifications are outside collection
scope. If the integration is unsupported, continue with approved exports.

## Workflow C: ChatGPT adapter

After verifying workspace and data-handling suitability, expose approved read-only
result tools through an authorized app/MCP service. Prefer evidence metadata and
approved excerpts when full source content is unnecessary. Authenticate each user,
enforce tenant/engagement isolation at the service, and audit reads. Never rely on
model instructions alone for access control. Do not put credentials in the skill.
The same collector API can later support an API-hosted orchestrator; a ChatGPT skill
alone is not a continuously running collector.

## Deployment gate and pilot

Build one collector against an agreed source using synthetic fixtures first.
Validate permission boundaries, government endpoint selection, pagination, throttling,
expired credentials, interrupted runs, clock/window handling, duplicate records,
source integrity, and prevention of cross-tenant reads. Then pilot a limited
approved scope and reconcile results with an administrator's independent export.
Only describe a collector as live after this tenant-specific validation.

Next deliverables: approved source/permission matrix; collector implementation;
manifest adapter; tenant storage and run logging; optional AI connector; scheduling
configuration; operator runbook and pilot results. The current release implements
the export inventory and review layer only.
