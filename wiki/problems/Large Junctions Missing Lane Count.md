---
type: problem
---

# Large Junctions Missing Lane Count

## Summary

Junctions in [[HD Basemap]] raw automation output can be abnormally large (e.g. ~57 m wide), and entire roundabouts may be modelled as a single junction node. The roads inside these oversized junctions are classified as [[Intermediate Roads|intermediate roads]] and lack lane count data. [[Genesis]] QA flags these frequently, causing noise in QA reports.

## Root cause

Missing road legs in the raw automation output inflate junction boundaries. The [[Leg Boosting|leg boosting]] production pipeline corrects this, but it is not yet applied at scale (as of May 2026), so most published basemap releases still contain the raw, un-boosted junction models.

## Status (as of 2026-05-14)

- The specific junction at `54.2898788, 10.4342199` was confirmed to be correctly modelled in the most recent [[Orbis]] layer (leg already present).
- For other junctions, the fix depends on leg boosting reaching production scale.

## Affected systems

- [[HD Basemap]] — source of the large junction models
- [[Genesis]] — QA system raising the flags
- [[Orbis]] — delivery layer where fixed junctions appear

## Contacts

- [[Gaurav Shah]] — reported the issue
- [[Jose Martinez Teira]] — confirmed root cause and leg-boosting fix

*Source: `raw/slack/adas-hd-basemap-lanes-general/2026-05-13 18_20_40 - reply - 2026-05-14 09_44_31.md`*
