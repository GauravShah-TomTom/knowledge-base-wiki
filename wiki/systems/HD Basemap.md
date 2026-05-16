---
type: system
---

# HD Basemap

[[TomTom]]'s HD (high-definition) map basemap product, containing detailed road geometry, lane models, and junction topology. Output is published via the [[Map Content Portal]] and is available as a layer in [[Orbis]].

## Versioning

Releases are versioned numerically (e.g. `26070.001`). Release 26070.001 was checked in May 2026 via the [[Map Content Portal]] at catalog release ID `167528030`.

## Known issues

- **Large junctions / roundabout modelling**: Some junctions are modelled as very wide (~57 m) or entire roundabouts are collapsed into a single junction node. This happens when a road leg is absent from the raw automation output. The [[Leg Boosting|leg boosting]] production pipeline fixes missing legs, but leg-boosted regions are not yet being delivered at scale (as of May 2026). See [[problems/Large Junctions Missing Lane Count]].
- The [[Genesis]] QA system flags intermediate roads inside such large junctions for missing lane count.

## Related

- [[Orbis]] — data layer / delivery format
- [[Map Content Portal]] — release catalogue
- [[Leg Boosting]] — pipeline fixing missing junction legs
- [[Genesis]] — QA system that validates basemap output

*Source: `raw/slack/adas-hd-basemap-lanes-general/2026-05-13 18_20_40 - reply - 2026-05-14 09_44_31.md`*
