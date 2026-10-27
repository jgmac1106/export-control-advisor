# Evidence request and mapping guide

These are analytical request templates, not a regulatory checklist or automatic
control-to-law equivalence. Select only topics relevant to the requested documents
and actual deployment. Verify applicable requirements through SOURCES.md.

| Topic | Candidate exports/records | Document targets | Review limitation |
|---|---|---|---|
| Identity and authorization | Role/group assignments, access reviews, Conditional Access configuration, relevant sign-in events | Access policy, personnel procedure, TCP, SSP | Account membership does not establish export eligibility or legal release authorization |
| Cloud sharing and handling | Sharing configuration, relevant audit events, approved recipient/release records | Handling procedure, TCP, cloud SSP sections | Configuration and successful/blocked events support different claims |
| Endpoints | Inventory, configuration/compliance results, patch and protection records | Asset register, endpoint procedure, SSP | Missing or stale devices may invalidate population claims |
| VDI | Host pools, session hosts, effective policies, redirection settings, client scope, session events | VDI procedure, diagrams, TCP, SSP | Host-pool defaults alone do not establish effective endpoint behavior |
| Single print station | Station/printer inventory, effective restrictions, print/maintenance records, physical handling procedure | Print procedure, physical policy, boundary/SSP | Logs do not prove authorized paper collection or disposal |
| Engineering and OT | Approved firewall exports, zone diagrams, asset lists, transfer approvals, maintenance/vendor-access records | Engineering/OT procedures, TCP, SSP | Segment names do not prove enforced isolation; never probe OT automatically |
| Hybrid identity/VPN | Directory/sync configuration, VPN rules and logs, privileged access records | Identity, remote access, recovery, SSP | Confirm cloud/on-prem dependencies and administrative paths |
| Commercial M365/file share | Exact service description, authorization scope, integration/configuration exports, access/transfer logs | Supplier review, handling, boundary/SSP | FedRAMP status alone does not establish export authorization or absence of local copies |
| Governance | Approved policies, responsibilities, training completion, audit/corrective-action records | Program policy, document register | Approval establishes governance, not universal execution |
| Export decisions | Classification determinations, authorization/proviso records, screening and release approvals | Classification, screening, release and records procedures | Human export-official review remains necessary for unresolved legal determinations |

For DEP-07 emphasize cloud-hosted VDI, client admission, redirection, identity,
monitoring, and recovery. For DEP-08 add the complete single-station printing path.
For DEP-09 include local engineering and OT zones, transfers, support, and safety
constraints. Apply the corresponding topics for other catalog patterns.

Example finding (synthetic): A host-pool export shows printer redirection disabled
at that layer. Map it to the VDI procedure's configuration statement with the exact
object/property locator. Mark effective end-to-end printing restrictions as not
assessed until applicable policies, client paths, and corroborating tests are reviewed.
