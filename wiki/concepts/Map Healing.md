---
type: concept
---

# Map Healing

Map Healing is the practice of proactively detecting, classifying, and fixing errors in digital map data — particularly road network errors that cause navigation problems.

*Source: raw/scans/MEDS Overview.pdf*

## Overview

Rather than relying solely on user reports or manual map audits, Map Healing uses real-world driver behaviour signals (e.g. [[Route Divergence]]) to automatically surface map errors. Detected errors are then fed into provider pipelines to apply corrections.

## Categories of Map Errors

Based on [[MEDS]] detector coverage:

| Error type | Description |
|---|---|
| Missing roads | A real road exists but is absent from the map |
| Invalid turn restrictions | A restriction in the map that drivers consistently ignore |
| Invalid permanent barriers | A barrier in the map that drivers drive through |
| Missing one-way restrictions | A one-way road not flagged as one-way |
| Missing turn restrictions | A turn drivers avoid but the map allows |
| Missing blockpassage | A fully blocked road not marked as blocked |
| Missing segments | No road segment near a popular PUDO |

## Uber's Implementation

Uber implements Map Healing via [[MEDS]] (Map Error Detection System), which uses GPS trace analysis against [[UMM]] (Uber Map Model) to detect errors and feed them into provider (e.g. [[TomTom]]) fix pipelines via [[Auto-Graduation]].

## Related

- [[MEDS]] — Uber's Map Healing platform
- [[Route Divergence]] — primary input signal
- [[Auto-Graduation]] — automated fix application
- [[UMM]] — the map model being healed
