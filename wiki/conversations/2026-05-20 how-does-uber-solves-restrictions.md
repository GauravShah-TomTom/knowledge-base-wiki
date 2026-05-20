---
type: conversation
title: "How does uber solves restrictions?"
posted_by: "72a9f352-c246-4124-8ba0-be189031ee5b"
posted_at: "2026-05-20T08:46:18.806Z"
posted_via: "wiki_feedback_up"
citations:
  - "wiki/systems/Veritas.md"
  - "wiki/systems/UMM.md"
---
# How does uber solves restrictions?

## Question

How does uber solves restrictions?

## Answer

Short answer: Uber represents turn/traffic restrictions in the Uber Map Model (UMM) and verifies proposed restriction “leads” through the Veritas pipeline, which checks them against CoreDB and drives downstream workflow routing.

How it works (high level)
- **Modeling** — UMM stores road geometry and maneuver entities (directed segments, junctions, maneuvers, provider tags, maneuver feature types) that represent turn restrictions and allowed movements.
- **Lead ingestion** — Restriction leads (maneuver-type leads like “can-left” or “no-left”) are submitted via the Uber ACI Service and queued for processing.
- **Pre‑processing** — BFrost runs to mark leads as non‑overlapping; only after BFrost completes are leads picked up by Veritas.
- **Verification (Veritas)** — Veritas looks up road IDs and maneuver IDs in CoreDB, runs verification logic (including SDO and LLM-based implicit/restriction checks), and sets a `verification_result` status on each lead.
- **Statuses & fallout** — Results include `VERIFIED`, `NOT_VERIFIED`, and a new `FALLOUT_MISSING_FEATURE` for missing road/maneuver features (replacing silent skips).
- **Output & routing** — Veritas emits an XML transition record (all fields must be non‑empty) that Camunda BPMN/DMN scripts consume to drive downstream workflow routing.

Operational notes
- The Veritas workflow is triggered manually at first, then scheduled (Mondays) through Airflow.
- The XML output format is strict: empty fields cause runtime failures, so all transition metadata fields must be populated.

## Citations

- [[wiki/systems/Veritas]]
- [[wiki/systems/UMM]]
