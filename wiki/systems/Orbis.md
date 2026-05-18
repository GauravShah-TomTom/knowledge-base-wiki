---
type: system
---

# Orbis

Orbis is a map data platform and delivery layer used in TomTom's [[Lanes]] pipeline and [[HD Basemap]] workflow.

## Roles

- **Lane connectivity data source**: Orbis provides lane connectivity data that can conflict with [[Genesis]], causing invalid lane connectivity errors (rule 51068 — see [[problems/Rule 51068 Invalid Lane Connectivity]]).
- **Basemap layer**: The "Orbis layer" is the delivery format where [[HD Basemap]] releases are published. After [[Leg Boosting|leg boosting]] is applied, the corrected junction models appear in the Orbis layer. The most recent Orbis basemap can be browsed via [[Map Content Portal]].

## Related

- [[Genesis]] — counterpart data / QA system
- [[HD Basemap]] — basemap product delivered via Orbis
- [[Map Content Portal]] — release catalogue
- [[Leg Boosting]] — pipeline whose output appears in the Orbis layer

## Improvement requests from FMO review

The DEU-01 [[concepts/FMO|FMO]] violation review identified several areas where Orbis improvements are requested:
- Provide lane count indication on intermediate road elements in large junctions (rule 50329).
- Ensure Lane Direction Category is reflected in connectivity generation (rule 53887).
- Incorporate maneuvers, DTFR, and general restrictions when creating lane connectivities (rule 51068).
- Improve lane connectivity for bidirectional road scenarios (rules 50263, 51085).

*Sources: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`, `raw/slack/adas-hd-basemap-lanes-general/2026-05-13 18_20_40 - reply - 2026-05-14 09_44_31.md`, `raw/confluence/Lanes FMO-- violation review.md`*
