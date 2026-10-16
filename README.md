# export-control-advisor
Copy the following into `README.md`:

````markdown
# Export Control Policy Advisor

An AI skill for creating and adapting company-specific export-control policies, plans, procedures, and supporting documentation.

Export Control Policy Advisor helps organizations translate their business activities, regulatory obligations, and existing safeguards into practical documentation for the **International Traffic in Arms Regulations (ITAR)** and **Export Administration Regulations (EAR)**.

The skill supports two workflows:

1. **Create a new export-control documentation set.**
2. **Adapt an existing NIST SP 800-171 documentation set for export control.**

It also supports targeted revisions to individual documents.

## Who this is for

- Defense contractors and suppliers
- Manufacturers and engineering firms
- Software and cloud-service providers
- Export compliance officers and consultants
- IT and security teams maintaining NIST SP 800-171 documentation

The skill scales its recommendations to the organization’s activities, size, systems, and risks. A small company may need an integrated manual; a larger organization may need separate policies, plans, and procedures.

## What it produces

Depending on the request, outputs may include:

- Export Control Policy
- Supporting plans and operating procedures
- Technology Control Plan, where applicable
- Document register and responsibility assignments
- Source-to-document traceability matrix
- NIST SP 800-171 adaptation matrix
- Targeted System Security Plan revisions
- Change summaries
- Open-decision and implementation-action lists
- Supporting forms, acknowledgments, and record templates

Outputs distinguish established practices, proposed changes, and unresolved decisions. New or revised documents are marked as drafts for company approval unless a different status is established.

## The two workflows

### 1. Create a new documentation set

Use this workflow when an organization needs a new export-control program or lacks a usable documentation baseline.

The skill:

1. Establishes the organization’s scope and known regulatory applicability.
2. Examines relevant export-control risks.
3. Defines the documents, owners, and supporting records needed.
4. Drafts the governing policy.
5. Develops applicable plans, procedures, and forms.
6. Checks source traceability and consistency.
7. Identifies remaining approvals and implementation actions.

### 2. Adapt an existing NIST SP 800-171 documentation set

Use this workflow when approved policies, plans, procedures, and a System Security Plan (SSP) already provide a foundation.

The skill:

1. Identifies canonical documents, versions, approvals, and owners.
2. Maps existing provisions to relevant export-control topics.
3. Identifies export-specific gaps and additions.
4. Assigns a treatment to each topic: retain, cross-reference, revise, create, not applicable, or clarify.
5. Revises existing documents and creates missing components.
6. Reconciles affected SSP descriptions with confirmed implementation facts.
7. Produces a change summary and remaining action list.

The bundled adaptation crosswalk addresses **NIST SP 800-171 Revision 2**. Mappings to other revisions require separate validation.

## Getting started

Clone or download this repository:

```bash
git clone https://github.com/jgmac1106/export-control-advisor.git
```

Use the complete repository with an AI environment that supports skills or can read local instructions and reference files. Follow that environment’s skill-loading instructions and point it to [`SKILL.md`](SKILL.md).

Keep the `references` directory with the skill. The instructions route drafting tasks to those materials.

Where explicit skill invocation is supported, use:

```text
Use $export-control-advisor to draft an export-control policy
or adapt my existing NIST SP 800-171 documentation.
```

Cloning the repository alone does not activate the skill in every AI environment.

## Example requests

### Start a new program

> Use Export Control Policy Advisor to develop an export-control documentation set for a small engineering company. Review the company information I provide, identify material unanswered questions, and propose the necessary documents before drafting.

### Adapt existing documentation

> Use Export Control Policy Advisor to adapt our approved NIST SP 800-171 Rev. 2 policies, plans, procedures, and SSP for export control. Preserve our document structure and terminology. Identify what can be retained, what needs revision, and what new documentation is needed.

### Review a cloud-service workflow

> We provide cloud-based analysis of customer technical data. Review our described data flows, processing, support access, and existing safeguards. Identify the facts and decisions needed to draft an export-control policy.

### Revise one document

> Revise our Access Control Plan to address applicable export-control responsibilities. Preserve confirmed implementation details and identify proposed controls separately. Provide a change summary and source mapping.

## Information to provide

Start with the information already available:

- Company activities, products, and services
- Known jurisdiction and classification determinations
- Customers, suppliers, operating locations, and international activities
- Personnel, visitor, administrator, and support access
- System boundaries, cloud services, and information flows
- Relevant authorizations, conditions, and contractual requirements
- Existing policies, plans, procedures, SSP, and diagrams
- Canonical document versions and approval status
- Requested deliverables and intended audience

The skill should ask only material unanswered questions and continue drafting unaffected sections while other decisions remain open.

## Repository contents

| Path | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | Core instructions, intake, workflow routing, drafting rules, and required outputs |
| [`agents/openai.yaml`](agents/openai.yaml) | Interface metadata and suggested starting prompt |
| [`references/SOURCES.md`](references/SOURCES.md) | Source inventory, classifications, provenance, dates, and limitations |
| [`references/intake.md`](references/intake.md) | Intake questions and fact-handling guidance |
| [`references/output-review.md`](references/output-review.md) | Output schemas and completion review |
| [`references/sources/`](references/sources/) | Source documents and searchable extracts |
| [`assets/icon.svg`](assets/icon.svg) | Skill icon |

## Source collection

The collection distinguishes regulatory references from guidance, templates, analysis, and vendor explanations.

| Source group | Intended use |
|---|---|
| 22 CFR Part 120 | Foundational ITAR provisions and definitions |
| 15 CFR Part 730 | Foundational EAR information and navigation |
| DDTC Compliance Program Guidelines | ITAR program structure and drafting guidance |
| DDTC ITAR Risk Matrix | Risk identification and program tailoring |
| BIS Export Compliance Guidelines | EAR program structure, audit guidance, and templates |
| NIST SP 800-171 export-control crosswalk | Adaptation of existing cybersecurity documentation |
| DCSA sample TCP and NISPOM cross-reference workbook | Conditional support for applicable industrial-security work |
| Microsoft ITAR cloud article | Supplemental implementation context requiring verification |
| Older DDTC compliance guidance | Historical comparison |

See the [source register](references/SOURCES.md) for exact editions, dates, filenames, and usage limitations.

Bundled documents are dated reference copies. They do not represent the complete ITAR or EAR. The skill directs the agent to verify applicable requirements against current official sources and consult additional provisions as needed.

Searchable extracts support retrieval. Original documents should be consulted when tables, formatting, or OCR could affect interpretation.

## Drafting principles

- Ground documents in the organization’s actual activities and confirmed facts.
- Distinguish legal obligations, authorization conditions, contract requirements, agency recommendations, and company choices.
- Preserve useful existing documentation and avoid unnecessary duplication.
- Keep ITAR, EAR, CUI, cybersecurity, and NISPOM applicability distinct.
- Recognize approved policies as evidence of documented governance while evaluating operational implementation separately.
- Never invent classifications, licenses, approvals, personnel eligibility, or implemented safeguards.
- Keep proposed changes separate from current SSP implementation statements.
- Treat vendor claims and analytical crosswalks as inputs requiring validation.

## Contributing

Useful contributions include corrected citations, updated primary sources, improved workflow instructions, and realistic examples using public or synthetic information.

For source updates, identify the issuing authority, publication or effective date, official URL, and affected references. Preserve the distinction between regulatory requirements and recommended practices.

## Limitations

This skill provides drafting and decision support. It does not issue legal opinions, government approvals, export authorizations, or certifications. Completed documentation does not by itself establish compliance or prove that controls operate.

Unresolved legal and authorization questions should be directed to the organization’s responsible export official or qualified counsel.

## License

Original project material is provided under the [MIT License](LICENSE).

Bundled third-party and government source materials retain their respective legal status and applicable terms. Their inclusion does not imply endorsement by an agency or vendor or relicense those materials under MIT.
````
