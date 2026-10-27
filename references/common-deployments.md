# Common deployment patterns

Use these patterns to tailor export-control documentation in either workflow.
Classification: reusable architecture templates and supporting analysis. These are
proposed reference designs, not regulatory authority, validated company deployments,
or compliance determinations. Catalog reviewed: 2026-10-27.

## Contents

- [Selection and common intake](#selection-and-common-intake)
- [Pattern index](#pattern-index)
- [DEP-01: GCC High full cloud](#dep-01-gcc-high-full-cloud)
- [DEP-03: GCC High hybrid enclave](#dep-03-gcc-high-hybrid-enclave)
- [DEP-04: GCC High cloud with on-premises printers](#dep-04-gcc-high-cloud-with-on-premises-printers)
- [DEP-05: Commercial M365 with FedRAMP file sharing](#dep-05-commercial-m365-with-fedramp-file-sharing)
- [DEP-06: Commercial M365 with FedRAMP file sharing and printing](#dep-06-commercial-m365-with-fedramp-file-sharing-and-printing)
- [DEP-07: GCC High full-cloud VDI with zero-trust controls](#dep-07-gcc-high-full-cloud-vdi-with-zero-trust-controls)
- [DEP-08: GCC High VDI enclave with one print station](#dep-08-gcc-high-vdi-enclave-with-one-print-station)
- [DEP-09: GCC High VDI enclave with engineering and OT segments](#dep-09-gcc-high-vdi-enclave-with-engineering-and-ot-segments)
- [Shared overlays](#shared-overlays)
- [Documentation and evidence outputs](#documentation-and-evidence-outputs)
- [Technical references and currency](#technical-references-and-currency)

## Selection and common intake

Select the nearest pattern or combination after shared intake. Record departures
instead of forcing a company into a reference design. Confirm:

- Actual versus proposed architecture; service names, cloud environment, tenant,
  regions, licenses, identity authority, support model, and feature availability.
- Data categories and determinations: CUI, ITAR technical data, EAR technology or
  software, and other business information. Do not treat these as interchangeable.
- Users, administrators, service accounts, vendors, locations, remote access,
  eligibility determinations, and authorization conditions governing each release.
- Creation, receipt, processing, storage, transfer, backup, logging, recovery, and
  disposal flows, including caches, synchronization, print spools, and hard copies.
- Devices and services that handle information or protect the environment; proposed
  exclusions and their rationale. Evaluate export-program and cybersecurity scopes
  separately. Do not derive CMMC asset categories from these pattern names.
- Existing policy, TCP, SSP, diagram, procedure, and evidence identifiers and versions.

Treat cloud branding, FedRAMP status, VDI, segmentation, and zero trust as inputs to
analysis; none independently establishes export authorization or compliance.
Evaluate plaintext access, encryption, key custody, provider support, locations,
and release conditions for the actual service and activity.

## Pattern index

| ID | Deployment | Distinguishing boundary |
|---|---|---|
| DEP-01 | GCC High full cloud | Managed endpoints and cloud workloads; no local servers, printing, or OT assumed |
| DEP-03 | GCC High enclave with AD, Entra Connect, VPN, and segmented OT | Hybrid identity, remote-access gateway, and IT/OT boundaries |
| DEP-04 | GCC High full cloud with on-premises printers | Cloud and endpoints plus printer, spool, and physical handling paths |
| DEP-05 | Commercial M365 with a FedRAMP file-sharing service | Separate designated controlled-information repository and commercial collaboration |
| DEP-06 | Commercial M365 with a FedRAMP file-sharing service and printer | DEP-05 plus local print processing and paper handling |
| DEP-07 | GCC High full-cloud VDI with zero-trust controls | Cloud-hosted desktops, applications, storage, and management; client devices evaluated explicitly |
| DEP-08 | GCC High VDI enclave with one print station in scope | VDI boundary plus one designated station and its complete print path |
| DEP-09 | GCC High VDI enclave with segmented engineering workstations and segmented OT | VDI, local engineering, and OT zones explicitly in scope |

The three additions are DEP-07 through DEP-09. The GCC/Global Secure Access
pattern has been removed from this catalog at the user’s direction; DEP-02 is retired.

## DEP-01: GCC High full cloud

**Boundary:** Managed user and administrative endpoints access selected Microsoft
365 GCC High workloads and any separately identified cloud services. Full cloud
describes workload placement; it does not eliminate endpoint responsibilities.

**Confirm:** Which workloads process controlled information? Are local application
caches, offline files, synchronization, mobile access, external sharing, and guest
accounts allowed? What identity, device management, backup, logging, and support
services are actually deployed? Add a printer or OT overlay if either exists.

**Document focus:** Cloud and endpoint access, handling and release approval,
external collaboration, administrative access, incident response, recovery, and
data-flow/SSP descriptions. Record effective endpoint and sharing configurations.

## DEP-03: GCC High hybrid enclave

**Boundary:** Microsoft 365 GCC High with on-premises Active Directory, Microsoft
Entra Connect, VPN access, local resources, and segmented OT. Map identity and
administration dependencies across the cloud, IT, and OT boundaries.

**Confirm:** Authoritative directory, synchronization scope and direction,
authentication method, privileged accounts, synchronization-server protection,
VPN users/devices/routes, vendor connections, and recovery dependencies. Verify
supported government-cloud identity configurations before describing implementation.

**Document focus:** Identity lifecycle, synchronization administration, privileged
access, VPN authorization and monitoring, network segmentation, recovery, and OT
transfer/maintenance procedures. Include identity infrastructure in scope analysis.

## DEP-04: GCC High cloud with on-premises printers

**Boundary:** DEP-01 plus identified printers and any print servers, workstations,
connectors, spool storage, network paths, and paper handling areas.

**Confirm:** Direct printing versus a print service; printer storage, multifunction
scan/email features, administrative interfaces, remote maintenance, and output
collection. A cloud workload can still create local copies through printing.

**Document focus:** Apply the print overlay, revise physical/electronic flow diagrams
and asset records, and reconcile cloud-only SSP descriptions with local processing.

## DEP-05: Commercial M365 with FedRAMP file sharing

**Boundary:** Commercial Microsoft 365 for designated business uses plus a separate
file-sharing service proposed for controlled information. Record the exact offering
and authorization boundary, not merely the vendor name or a FedRAMP marketing claim.

**Confirm:** Applicable contractual requirements, current authorization status and
scope, export conditions, personnel/support access, key handling, endpoint clients,
local copies, previews, search indexes, logs, backup, and integrations. Determine
whether content or sensitive metadata enters commercial email, Teams, Office,
browser caches, synchronization folders, or notification messages.

**Document focus:** Approved repository and transfer rules, collaboration/release
approvals, commercial-service usage boundaries, endpoint handling, supplier review,
and boundary diagrams. Record allowed versus blocked integration paths. A designated
file share does not automatically keep controlled information out of M365.

## DEP-06: Commercial M365 with FedRAMP file sharing and printing

**Boundary:** DEP-05 plus an identified printer and its workstation/server, spool,
network, maintenance, and paper paths. Do not assume encryption at the file-sharing
service protects decrypted local print processing.

**Confirm:** How files reach the print application, who authorizes printing, which
local copies remain, and whether output can be sent to another printer or service.

**Document focus:** DEP-05 documentation plus the print overlay, local handling,
physical access, maintenance, and disposal procedures; update affected SSP statements.

## DEP-07: GCC High full-cloud VDI with zero-trust controls

**Boundary:** Microsoft 365 GCC High plus a separately identified government-cloud
VDI service, such as Azure Virtual Desktop in Azure Government, subject to current
service/configuration verification. Host desktops, applications, profiles, data,
and management in identified cloud services. Include cloud-hosted identity services
if required. This pattern assumes no on-premises workload servers, printing, or OT.

GCC High names the Microsoft 365 environment; it does not identify the VDI product.
Record control plane, session-host region, identity tenant, storage, management,
monitoring, and supported client separately. Do not assume public-cloud feature parity.

**Confirm:** Identity/join model, supported tenant combinations, licensing, approved
clients, device posture, administrative paths, cloud networking, recovery, and
session/profile persistence. Evaluate accessing endpoints even if local file
transfer is disabled. Resolve any dependency on local AD as a design departure.

**Document focus:** Apply the VDI/zero-trust overlay; document conditional access,
least privilege, segmentation, device security, session controls, approved release
paths, monitoring, and response. Label each safeguard proposed or implemented.
Use T02 and T04 for technical questions, checking government-cloud applicability.

## DEP-08: GCC High VDI enclave with one print station

**Boundary:** A GCC High/verified government-cloud VDI enclave plus exactly one
designated print station in scope. Include the attached or networked printer,
drivers, queues/spools, any server/connector, network path, operators, maintenance,
and physical output handling. Other corporate services may exist outside the
enclave; document each permitted interface and evaluate scope dependencies.

**Confirm:** Station identifier and location; authorized users; print path from VDI;
effective redirection settings; how the single-station restriction is enforced;
local retention and cleanup; printer storage; support and disposal arrangements.
Do not equate one station with one asset or assume ordinary printer redirection
restricts printing to that station. Verify effective policy and client behavior (T03).

**Document focus:** VDI and print overlays, approved printing/release procedure,
physical handling, exception review, asset/data-flow records, and revised SSP/TCP
boundaries. Propose blocking alternative print paths and test enforcement before
describing that restriction as implemented.

## DEP-09: GCC High VDI enclave with engineering and OT segments

**Boundary:** A GCC High/verified government-cloud VDI enclave, segmented engineering
workstations, and segmented OT, all explicitly in scope. Represent VDI, engineering,
and OT as distinct zones with controlled interfaces. Add transfer or jump services
only where the actual or proposed design requires them.

**Confirm:** Engineering workstation inventory, CAD/CAM applications, local
processing/storage, license servers, approved VDI-to-engineering transfers,
engineering-to-OT programs/files, equipment interfaces, removable media, vendor
maintenance, and OT safety/availability constraints. Identify what information each
OT device receives, processes, or retains and justify its applicable asset category.

**Document focus:** VDI and OT overlays, engineering endpoint administration,
controlled transfer and release approvals, removable media, network rules,
maintenance, recovery, and incident response. Include engineering and OT assets
in diagrams and scope records; do not imply VDI contains all processing or that
segmentation alone excludes local equipment from scope. Evaluate printing separately.

## Shared overlays

### VDI and zero trust

Record identity verification and MFA, device admission rules, least-privilege
administration, session isolation, network access, patching, image management,
monitoring, and response as explicit design decisions. Determine available controls
for the selected government-cloud service and clients rather than inferring them
from a zero-trust label.

Review clipboard, drives, file transfer, printers, USB, camera/audio, browser
downloads, screenshots, local caches, session recordings, and support access.
Record each allowed path, restriction, rationale, enforcement point, and evidence.
Do not claim screen capture or photography is impossible. Address residual exposure
through appropriate device, personnel, and physical handling measures.

### Printing and paper

Trace source application to spool, station/server/connector, printer storage, paper,
collection, use, storage, reproduction, transport, and destruction. Identify access,
release authorization, markings, secure collection, maintenance, and disposal.
Derive retention and review frequencies from applicable sources or documented company
choices. Assess scan-to-email/cloud and technician access when present.

### Engineering and OT

Record zones, permitted sources/destinations/protocols, authentication, transfer
approval, monitoring, vendor access, removable media, and emergency maintenance.
Consider firmware, backups, job/program files, drawings, logs, and diagnostic uploads.
Use operations-approved validation for safety-sensitive equipment. Do not recommend
disruptive scanning or patching as an automatic documentation step. Keep compensating
safeguards and unresolved constraints explicit; segmentation is not an air gap.

## Documentation and evidence outputs

For either workflow, incorporate the following into the existing registers where
practical rather than creating duplicate documents:

| Output | Capture |
|---|---|
| Deployment profile | Pattern IDs, deviations, owner, actual/proposed status, service/tenant/region details, verification date |
| Boundary and flow record | Assets, zones, administrators, support paths, data lifecycle, scope rationale and unresolved interfaces |
| Document impact | Policy/TCP/procedure/SSP/diagram sections; retain, cross-reference, revise, create, not applicable, or clarify |
| Access and release rules | Authorized roles and recipients, applicable conditions, permitted paths, approval and record requirements |
| Governance evidence | Approved scope decisions, policies, procedures, diagrams, and responsibility assignments |
| Operating evidence | Relevant configuration exports, effective policy checks, access reviews, logs, transfer/print records, and recovery results |
| Open decisions | Missing facts, unsupported assumptions, source questions, owner, drafting impact, and implementation action |

In Workflow 1, use the profile to tailor the new document set. In Workflow 2, compare
it with the existing 800-171 documents and canonical SSP before revising affected
sections. Preserve confirmed implementation and distinguish proposed changes.
Do not copy company-specific architecture or evidence into this reusable catalog
without explicit authorization.

## Technical references and currency

These are primary vendor technical references, classified as vendor explanations,
not export-control regulations. Reviewed 2026-10-27 for the limited topics below;
recheck exact service support during engagement. Other configurations in this
catalog remain proposed until separately verified.

| ID | Reference | Use and limitation |
|---|---|---|
| T02 | [Microsoft: Apply Zero Trust principles to Azure Virtual Desktop](https://learn.microsoft.com/en-us/security/zero-trust/azure-infrastructure-avd) | Design topics; verify each feature in the selected government environment |
| T03 | [Microsoft: Configure printer redirection](https://learn.microsoft.com/en-us/azure/virtual-desktop/redirection-configure-printers) | Policy layers and effective redirection; does not establish a single-station restriction |
| T04 | [Microsoft: Azure Virtual Desktop with Intune](https://learn.microsoft.com/en-us/intune/solutions/azure-virtual-desktop) | Management and cloud compatibility, including unsupported public/sovereign cross-cloud enrollment |

Use the regulatory and agency sources in SOURCES.md for legal/program obligations.
For each engagement, record current technical source URLs, access dates, applicable
configuration, unresolved dependencies, and evidence supporting implementation.
