---
type: system
---

# Localization Layer

TomTom system owned by the Places team (also referred to as "Orbis Places VS") that processes and aggregates traffic sign data before serving it to downstream consumers such as the Guidance / Capybaras team.

## Role in sign processing

The Localization Layer (Places) receives raw or semi-processed sign observations and produces an aggregated view of traffic signs. Downstream teams (e.g. Guidance / Capybaras — [[Tomasz Gajewski]]) receive pre-aggregated data from this layer and therefore do not directly work with raw [[Seen-Sector Counts]].

As of 2026-04-30, [[Kyumars Sheykh Esmaili]] noted that if observed angles prove useful downstream, the Localization Layer team ([[Jan Callewaert]], [[Blazej Stokwisz]]) would be the ones to expose that data.

## Key contacts

- [[Jan Callewaert]] — Orbis Places VS
- [[Blazej Stokwisz]] — Places team
- [[Kyumars Sheykh Esmaili]] — Orbis/Guidance/Goldenapples (cross-functional stakeholder)

## Related

- [[Sign-to-Road Matching]] — downstream process consuming Localization Layer output
- [[Seen-Sector Counts]] — parameter potentially useful to expose via this layer
- [[Sign Orientation]] — heading data also processed here

*Source: `raw/slack/2026-05-08-sign-orientation-vs-observed-angles-for-sign-to-road-matching.md`*
