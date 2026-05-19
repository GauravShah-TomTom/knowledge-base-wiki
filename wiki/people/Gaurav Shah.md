---
type: person
---

# Gaurav Shah

Engineer on the [[Lanes]] project. Assigned stories:
- Route 5832 — implement post-processing task to add lanes at intersections (including lane count and lane connectivity based on road class). As of 2026-05-19 sprint planning: checking if road element is part of a normal intersection, applying lane count/connectivity for VR roads, and extending JSON metadata with rule ID for transaction tracing.
- End-to-end H3 tile parallel processing design — moving orchestration to [[Airflow]], making [[Lanes Automator]] node pool auto-scalable, and calling [[Transaction Manager]] REST API once per H3 tile.

Gaurav proposed the idea of using separate Iris projects per rule ID for targeted editor QA, and also contributed to the decision to use the priority field in [[Iris]] instead. He also described the planned [[Airflow]] orchestration for parallel [[H3 Tiles|H3 tile]] processing.

In the 2026-05-19 sprint planning, Gaurav clarified the lane connectivity defaulting approach: the pipeline should *supplement* HD data (fill missing connectivity) rather than ignore it entirely. He also noted the team should start with T-junctions and handle dual-carriageway and other complex cases in follow-up stories.

Active in the `#adas-hd-basemap-lanes-general` Slack channel. Raised a question (2026-05-13) about why junctions in the [[HD Basemap]] are so large (~57 meters wide) and why entire roundabouts are modelled as a single junction. The QA system [[Genesis]] flags these because the roads are classified as intermediate roads and lack lane count. Coordinated with [[Jose Martinez Teira]] to check whether the junction at 54.2898788, 10.4342199 had already been processed by the [[Leg Boosting|leg boosting]] pipeline.

*Sources: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`, `raw/transcripts/converted/2026-05-19 Lanes_Sprint_Planning.md`, `raw/slack/adas-hd-basemap-lanes-general/2026-05-13 18_20_40 - reply - 2026-05-14 09_44_31.md`*
