# Automation project intake and acceptance-planning worksheet

**Status: editorial draft; not published.** Intended for an industrial buyer preparing a system-integration RFQ. This worksheet structures discovery. It is not a design, risk assessment, safety validation, standards-compliance statement or acceptance certificate. A responsible project engineer must define and approve requirements for the actual site.

## 1. Define the problem

| Buyer input | Record for the RFQ |
|---|---|
| Process step and current condition | What happens today? What event or constraint starts the project? |
| Desired outcome | Which observable task should the system perform? |
| Scope boundary | What is explicitly included? What adjacent equipment, building work, utilities or production areas are excluded? |
| Current baseline | Which production records, cycle observations, defect categories or sample records establish today's condition? Who owns those records? |
| Operating pattern | Planned shift pattern, batch size, product variants, changeovers and known peak conditions |
| Site and jurisdiction | Installation location, site owner and the parties responsible for site rules and approvals |

Do not promise an improvement percentage before the buyer supplies comparable baseline data and both parties agree how to measure it.

## 2. Describe the item, material or workpiece

Attach controlled drawings, photographs, sample data or product references where authorized. Record revision and owner for each attachment.

- Part/material/product identifiers and revision
- Dimensions, tolerances, mass, orientation, surface or contamination constraints that matter to handling or measurement
- Variant count and how the active variant is identified
- Approved substitutes, if any; otherwise write “none without written approval”
- Sample quantity, ownership, return/disposal method and shipping responsibility
- Known changes expected during the project

For bulk material or sampling, identify the material condition, flow point, sampling interval, sample mass or volume, sample identification, contamination controls and downstream laboratory interface. The customer's process owner and qualified engineering team must set the required values.

## 3. Map inputs, outputs and interfaces

For each interface, name the system/party that owns it and attach the current version of its specification.

| Interface | Buyer to specify | Owner / evidence |
|---|---|---|
| Physical | Line layout, access, mounting, handoff positions, existing equipment and site constraints | Drawing revision / site owner |
| Controls and data | Signals, state model, data fields, event timing, network/security boundary, time source and ownership | Interface control document / IT-OT owner |
| Materials and samples | Infeed, outfeed, reject path, labels, containers and replenishment | Process owner / sample records |
| Utilities | Available services and connection limits | Site engineering records |
| Operations | Recipe/variant selection, user roles, changeover, restart and manual mode | Operations owner |
| Maintenance | Access, service clearances, consumables, spares, diagnostics and training | Maintenance owner |

Do not assume a named protocol, brand or cybersecurity requirement until the customer verifies it.

## 4. Plan failure handling and safe operation

The project team should identify normal operation, foreseeable disturbances and the system's behavior in each condition. Examples for discussion include a missing or misoriented part, blocked path, sensor disagreement, communication loss, power interruption, full sample container, rejected inspection, invalid recipe and restart after a stop.

For each condition, decide who may reset or recover the system, what evidence is recorded, what product is quarantined, what manual work is permitted, and who can authorize return to production. The qualified project team must separately perform any required site-specific hazard analysis and determine applicable safety requirements. This worksheet does not replace that work.

## 5. Make acceptance observable

Agree acceptance methods before design freeze. Use a matrix such as:

| Requirement | Test setup and sample | Pass condition | Evidence captured | Approver |
|---|---|---|---|---|
| Functional sequence | Defined recipe, variant and normal-condition sample | Buyer-specified observable state sequence | Test record with revisions and timestamps | Named role |
| Throughput/cycle | Agreed operating window and method of measurement | Buyer-specified value and tolerance | Raw time series and calculation method | Named role |
| Inspection/sampling | Agreed reference material, sampling/measurement method and comparison owner | Buyer-specified detection/representativeness criteria | Raw results, exceptions and calibration references where applicable | Named role |
| Interfaces | Agreed signals, data fields and failure cases | Each agreed state and error response behaves as specified | Interface test log | Named role |
| Recovery | Agreed controlled fault and restart procedure | Safe, documented recovery and required material disposition | Witnessed recovery record | Named role |
| Documentation/training | Agreed deliverable list and audience | Buyer confirms receipt and review status | Document register and attendance record | Named role |

Specify whether each test occurs at the supplier, at the site, or both; who supplies samples; the witness list; retest limits; and how an open issue is accepted, corrected or deferred. Do not describe a worksheet or factory test as regulatory certification.

## 6. Attachments to prepare

1. Current process/layout drawing with revision date.
2. Product/material specification and authorized sample information.
3. Existing control/data interface description and a named IT/OT contact.
4. Site access, utilities and operating constraints.
5. Requirements-to-test matrix with owners and approval roles.
6. An open-issues register, including unresolved values and decision dates.

## Reader next step

Before requesting a quotation, fill the unknown values with the people who own production, engineering, IT/OT, safety, quality and site approval. Then send the same controlled revision to every bidder.

## Publication gate

Before hosting on `xiaodu.tech`, an authorized automation engineer must review technical accuracy and safety boundaries. The company must confirm that the scope descriptions match currently offered services. A bylined media submission additionally needs an identified, consenting human author and any reviewer credentials the publisher requires. The current Automation.com contribution rules were read on 2026-10-25; this draft is not yet a submission.
