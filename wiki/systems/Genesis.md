---
type: system
---

# Genesis

Genesis is a QA and map data system used in the [[Lanes]] pipeline and the [[HD Basemap]] workflow.

## Roles

- **Lane connectivity QA**: Genesis can provide lane connectivity data that conflicts with [[Orbis]], causing invalid lane connectivity errors (rule 51068 — see [[problems/Rule 51068 Invalid Lane Connectivity]]).
- **Junction QA**: Genesis flags oversized junctions where interior [[Intermediate Roads|intermediate roads]] lack lane count data (see [[problems/Large Junctions Missing Lane Count]]). This occurs frequently in [[HD Basemap]] raw automation output.

## Related

- [[Orbis]] — counterpart data source / delivery layer
- [[HD Basemap]] — basemap product whose output Genesis validates
- [[Lanes]] — pipeline that uses Genesis data

*Sources: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`, `raw/slack/adas-hd-basemap-lanes-general/2026-05-13 18_20_40 - reply - 2026-05-14 09_44_31.md`*
