# GCC High tenant evidence collection: next implementation phase

Status: implementation plan, not deployed connectors or a verified service design.
Start with the export-based agent and its schema. This plan introduces no live
credentials, jobs, network changes, tenant access, or data transfers.

## Contents

- [Current availability](#current-security-copilot-availability)
- [Environment decisions](#required-environment-decisions)
- [Tenant collectors](#workflow-a-approved-tenant-collectors)
- [Microsoft 365 Copilot direction](#microsoft-365-copilot-direction)
- [ChatGPT adapter](#workflow-c-chatgpt-adapter)
- [Pilot and deployment](#deployment-gate-and-pilot)
- [Technical sources](#technical-source-register)

## Current Security Copilot availability

Checked 2026-10-27: Microsoft states that Security Copilot is not designed for US
government clouds, including GCC High and Azure Government [SC01]. Consequently,
this guide does not provide an executable Security Copilot deployment inside a
GCC High tenant. Microsoft 365 Copilot and Copilot Studio are separate products;
their availability does not change this restriction.

Continue with Workflow A using individually verified government-service APIs or
administrator exports and an approved tenant-controlled runtime. Keep collection,
storage, and review inside approved environments. Do not build a Security Copilot
workflow for government clouds or bridge a commercial instance to GCC High data.
The AI direction for this project is Microsoft 365 Copilot, a separate product.

## Required environment decisions

Establish tenant/cloud IDs, approved host/runtime and repository, selected deployment,
source systems, exact government endpoints/API versions, allowed permissions,
retention, evidence period, collection cadence, owners, and AI processing boundary.
Verify current official documentation for each service/API/feature and the selected
Microsoft 365 Copilot integration before implementing it. Do not infer
specific agent, connector, or automation support from product availability alone.
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

## Microsoft 365 Copilot direction

Focus subsequent AI workflow design on Microsoft 365 Copilot in GCC High. Verify
its exact tenant capabilities, supported agents and connectors, permissions, and
approved data-handling boundary before writing deployment instructions. Keep
collection through approved exports or tenant-local collectors separate from
Copilot-assisted evidence organization and review. Do not assume Microsoft 365
Copilot can directly query every security API or run unattended collectors.

This section records project direction only; no Microsoft 365 Copilot agent or
connector has been configured. Do not substitute Security Copilot setup steps.

## Workflow C: ChatGPT adapter

Deferred alternative; Microsoft 365 Copilot is the current project focus.

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

## Technical source register

Classification: primary vendor documentation; checked 2026-10-27. Recheck current
service availability before implementation. Product support is not export authorization.

- SC01: [Get started with Security Copilot](https://learn.microsoft.com/en-us/copilot/security/get-started-security-copilot) — Microsoft states that Security Copilot is not designed for US government clouds, including GCC, GCC High, DoD, and Azure Government. Do not use it for the government-cloud workflow.
