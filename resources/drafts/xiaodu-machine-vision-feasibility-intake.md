# Machine-vision feasibility intake sheet

**For:** buyers evaluating an in-line inspection, measurement, OCR, code-reading, positioning or robot-guidance project with Xiaodu.
**Status:** draft for technical review; not published and not yet cleared for editorial outreach.
**Scope:** this sheet collects the evidence needed for an initial feasibility discussion. It is not a performance guarantee, a final specification, or an acceptance standard.

Xiaodu's public machine-vision scope includes 2D/3D vision, in-line inspection and decision, and inspection-data traceability. The existing project-delivery page already covers general requirements, interfaces, cycle time, FAT/SAT and acceptance. This draft narrows that general project intake to the image-formation and decision-quality questions that can make or break a vision application. [Machine Vision & Inspection](https://xiaodu.tech/en/solutions/machine-vision/)

## 1. State the decision the system must make

- Part/product and process step:
- What must be detected, read, measured, located or guided:
- What should happen when the system says **pass**, **fail** or **uncertain**:
- Is the task inspection, measurement, OCR/barcode reading, presence/absence, positioning, or robot guidance?
- What is the current manual or automated method, and what specific problem should change?

Avoid starting with a camera model or an AI method. Describe the production decision and the consequence of a wrong decision first.

## 2. Describe the part and its variation

- Material, color, finish and surface reflectivity:
- Size range, orientation and pose variation:
- Expected good-part variation:
- Known defect types or borderline examples:
- Do parts move, rotate, overlap, vibrate, deform or change temperature?
- Can the same part be presented consistently, or does the system need to tolerate variation?

For an initial review, use representative, non-confidential images or samples where possible. Include ordinary variation and difficult borderline cases; a few ideal images are not enough to characterize the task.

## 3. Record the image geometry and scene

- Required field of view and smallest feature that must be resolved:
- Approximate camera-to-part working distance and available mounting space:
- Camera view: top, side, oblique, multiple views, or not yet known:
- Part presentation and expected position repeatability:
- Background, nearby surfaces and reflections:
- Ambient light, changing sunlight, dust, moisture, oil, heat or washdown exposure:
- Is strobed or controlled illumination possible?

These are inputs for a feasibility review, not fixed recommendations. If dimensions are not known, provide a drawing with a scale or a clear photo with one measured reference dimension.

## 4. Define throughput and decision timing

- Target cycle time / parts per minute:
- Maximum time available for image capture and decision:
- Is the line continuous, indexed or manually triggered?
- What should the line do if the camera, network or PLC signal is unavailable?
- Must the image or decision be retained for traceability? If yes, for how long and under whose policy?

## 5. Define how performance will be measured

Do not use a single phrase such as “high accuracy” as the acceptance criterion. Ask the process owner to define the cost and treatment of each outcome.

| Measure to agree | Project-specific definition |
|---|---|
| False accept / escape | Which defect or out-of-tolerance condition must never be passed? What is the allowed escape rate and how will it be measured? |
| False reject | How many good parts may be rejected for review or rework? How is a reject disposition handled? |
| Measurement | Which dimensions, units, tolerances, reference method and repeatability study apply? |
| OCR / code read | Which formats, print-quality range, missing/duplicate codes and read-rate denominator apply? |
| Positioning / robot guidance | Coordinate frame, calibration method, allowable pose error and recovery path |
| Test set | Who supplies representative samples, labels ground truth and approves the test set? |
| Change control | What happens after a part, supplier, finish, lighting, lens, camera or software revision changes? |

The project owner and integrator must agree the metric, sample selection, test conditions and pass/fail rule before design freeze. A threshold cannot be inferred from a marketing claim or selected without representative samples and process context.

## 6. Map the controls and traceability boundary

- PLC / robot / line-control platform and available communication interface:
- Required outputs: pass/fail, measured value, code, position, image or event record:
- Handshake, time-out and retry behavior:
- Required alarm and operator-recovery behavior:
- Network, storage and cybersecurity constraints:
- Image retention, access permissions and deletion policy:

List only interfaces that are actually required. Confirm the controller, protocol, timing and ownership with the responsible controls engineer.

## 7. Prepare an initial evidence pack

1. A short process video showing normal operation and cycle timing.
2. Representative good and problem examples, labeled with the intended decision.
3. A drawing or photo showing part size, view, distance and mounting constraints.
4. Current cycle target and the downstream action for pass / fail / uncertain.
5. A list of controller, robot and traceability interfaces, if known.
6. The proposed acceptance measures and who owns approval.

Redact customer names, personal information, serial numbers and confidential drawings unless you are authorized to share them. Do not send sensitive files before the recipient, purpose and secure transfer route are agreed.

## 8. Initial feasibility outcome

A first review should return one of these outcomes, with the missing evidence stated:

- **Ready for concept review:** task, samples, timing and decision owner are clear enough to discuss an architecture.
- **Needs sample or process clarification:** the task may be feasible, but an important input is missing or unrepresentative.
- **Needs site / interface review:** mounting, lighting, line timing or control integration cannot be judged remotely.
- **Not yet scoped:** the required result or responsibility boundary is not measurable.

No outcome on this sheet promises a production result. Final design and acceptance criteria require project-specific engineering review, representative testing and customer approval.

## Editorial QA before publication

- Confirm with an engineer that each field reflects Xiaodu's actual project-intake practice.
- Compare against the existing project checklist and machine-vision page; remove repeated general intake fields unless they serve the vision-specific decision.
- Add one simple, original diagram only if it clarifies the relationship between sample variation, image capture, decision threshold and line response.
- Link to the existing machine-vision solution and contact route; state that project scope and availability are confirmed case by case.
- Do not add customer logos, sample images, performance statistics, certifications or product brands without evidence and permission.
- Publish only after a technical owner signs off; then verify the live URL, canonical, sitemap inclusion and contact CTA before using it in outreach.
