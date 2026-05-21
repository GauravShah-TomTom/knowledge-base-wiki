---
type: system
---

# BFrost

BFrost is an upstream process in the [[projects/Uber ACI Flow]] pipeline that runs on a **Thursday schedule**. It identifies non-overlapping restriction leads and feeds them into the [[Camunda]] workflow for verification by [[Veritas]].

## Role in the pipeline

- Receives raw leads and marks them as non-overlapping before passing them to Veritas
- Only leads marked as non-overlapping by BFrost are picked up by Veritas
- For end-to-end testing (story 5947), [[Sunil Jaiswal]] mocked the BFrost step in a separate test project so Veritas could be tested independently without triggering a full BFrost run

## Deployment coordination

Production deployment of the Veritas–Uber integration must be coordinated with the BFrost team (Swapnil / Amog). The DMN placement and overall BPMN flow must be reviewed and agreed with them before merging to production.

*Source: `raw/notes/Sprint grooming_ Quality improvement - PC restrictions.docx` — sprint grooming meeting 2026-05-12*
