---
type: conversation
title: "How does uber finds error in turn restriction?"
posted_by: "72a9f352-c246-4124-8ba0-be189031ee5b"
posted_at: "2026-05-21T04:50:38.293Z"
posted_via: "wiki_feedback_up"
citations:
  - "wiki/systems/MEDS.md"
  - "wiki/concepts/Map Healing.md"
  - "wiki/projects/Map Healing.md"
  - "wiki/concepts/Transition Traversal.md"
  - "wiki/concepts/Route Divergence.md"
  - "wiki/concepts/Map Matching.md"
  - "wiki/concepts/Auto-Graduation.md"
  - "wiki/problems/Map Data Quality Issues.md"
---
# How does uber finds error in turn restriction?

## Question

How does uber finds error in turn restriction?

## Answer

Uber detects turn-restriction errors as part of its MEDS map‑healing pipeline using driver behavior signals (primarily transition traversals and route divergences). There are two complementary detectors:

- **TurnPermitted — detects invalid (present but ignored) turn restrictions** — Finds turn restriction maneuvers in the map that drivers are actually making.
  - Inputs: non‑conditional turn restriction maneuvers joined with 3‑segment transition traversal counts.
  - Filters: exclude restrictions co‑located with barriers and exclude certain map‑specified turn types (sharp turns with steering angle < 60°, implicit or calculated turns, and U‑turns in US/Brazil).
  - Thresholds: reported only when the restricted transition has ≥ 21 actual traversals and those traversals are ≥ 5% of the originating segment’s traffic.
  - Action: output invalid maneuver IDs (used to delete the erroneous restriction via the auto‑fix pipeline).

- **TurnRestriction — detects missing (physically enforced but absent) turn restrictions** — Finds suggested turns drivers consistently avoid, implying a real restriction is missing from the map.
  - Inputs: aggregated route divergences and transition traversal data comparing the problematic (suggested) transition to alternative transitions drivers take.
  - All thresholds must pass:
    - Problematic transition suggestions ≥ 20
    - Problematic transition traversal rate ≤ 20% (actual/suggested)
    - Alternative transition traversal rate ≥ 80%
    - Alternative transition traversal count ≥ 100
  - Output: the pre‑divergence, divergence, and suggested segments (used to add a turn restriction via the auto‑fix pipeline).

In short: MEDS uses transition‑level traversal and divergence statistics, applies detector‑specific filters and numeric thresholds, and then either flags an existing restriction as invalid or proposes adding a missing restriction.

## Citations

- [[wiki/systems/MEDS]]
- [[wiki/concepts/Map Healing]]
- [[wiki/projects/Map Healing]]
- [[wiki/concepts/Transition Traversal]]
- [[wiki/concepts/Route Divergence]]
- [[wiki/concepts/Map Matching]]
- [[wiki/concepts/Auto-Graduation]]
- [[wiki/problems/Map Data Quality Issues]]
