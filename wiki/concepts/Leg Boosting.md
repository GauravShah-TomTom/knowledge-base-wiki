---
type: concept
---

# Leg Boosting

A production pipeline stage in the [[HD Basemap]] workflow that corrects junction models by adding missing road legs. Without leg boosting, junctions can appear artificially large (e.g. ~57 m wide) or entire roundabouts collapse into a single junction node, because one or more approach legs are absent from the raw automation output.

As of May 2026, leg-boosted regions are not being delivered at scale; most raw automation output has not passed through this pipeline. The fix is visible in the [[Orbis]] layer once applied.

See also: [[problems/Large Junctions Missing Lane Count]], [[HD Basemap]], [[Jose Martinez Teira]].

*Source: `raw/slack/adas-hd-basemap-lanes-general/2026-05-13 18_20_40 - reply - 2026-05-14 09_44_31.md`*
