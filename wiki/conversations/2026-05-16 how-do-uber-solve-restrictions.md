---
type: conversation
title: "how do uber solve restrictions?"
posted_by: "72a9f352-c246-4124-8ba0-be189031ee5b"
posted_at: "2026-05-16T06:55:09.902Z"
posted_via: "wiki_feedback_up"
citations:
  - "wiki/systems/MEDS.md"
  - "wiki/systems/UMM.md"
  - "wiki/competition/TomTom.md"
  - "wiki/concepts/Map Healing.md"
  - "wiki/problems/Rule 51059 Lanes on Non-Payload Roads.md"
  - "wiki/concepts/PUDO.md"
  - "wiki/systems/GeoCatch.md"
  - "wiki/concepts/DTFR.md"
---
# how do uber solve restrictions?

## Question

how do uber solve restrictions?

## Answer

Short answer: Uber detects incorrect turn/one‑way restrictions by mining driver route divergences and traversal counts in MEDS, classifies them with specific detectors/thresholds, and then either reports them or auto‑graduates fixes into the TomTom fix pipeline (e.g., DeleteTurnRestriction, AddTurnRestriction, MakeRoadOneWay).

How it works (concise):

- **Signals used** — route divergences, segment traversals, transition (3‑segment) traversals, and the Uber Map Model (UMM) maneuvers/barrier data.
- **Detectors for restrictions**
  - **TurnPermitted** — finds invalid (erroneously restricted) turns. Key thresholds: restricted transitions ≥ 21 AND ≥ 5% of first‑segment traffic. Certain maneuver types are excluded via provider feature codes.
  - **TurnRestriction** — finds missing turn restrictions. All required: suggestions ≥ 20, traversal rate ≤ 20%, alternative (alt) rate ≥ 80%, alt count ≥ 100.
  - **OneWay** — finds missing one‑way markings by comparing suggested vs actual traversal proportions (problem direction suggestions ≥ 10 and traversal% ≤ 15%; opposite direction traversals ≥ 10 and traversal% ≥ 80%).
- **UMM role** — MEDS queries maneuvers, junction topology and barriers from the UMM to evaluate candidate restrictions and to filter known/implicit maneuver types.
- **From detection to fix** — detections are reported into MIT; high‑confidence detections are auto‑graduated to the TomTom pipeline which applies fixes like DeleteTurnRestriction, AddTurnRestriction, or MakeRoadOneWay.
- **Operational outcomes** — TurnPermitted has the highest throughput (≈1,200 delete‑restriction fixes/week) due to good internal accuracy; other detectors yield smaller weekly fix counts.

If you want, I can list the exact detector thresholds again or show which UMM feature codes are filtered.

## Citations

- [[wiki/systems/MEDS]]
- [[wiki/systems/UMM]]
- [[wiki/competition/TomTom]]
- [[wiki/concepts/Map Healing]]
- [[wiki/problems/Rule 51059 Lanes on Non-Payload Roads]]
- [[wiki/concepts/PUDO]]
- [[wiki/systems/GeoCatch]]
- [[wiki/concepts/DTFR]]
