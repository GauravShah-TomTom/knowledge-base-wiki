---
type: decision
date: 2026-04-30
---

# Sign Matching Parameter Choices by Team

## Context

[[Ian Atkinson]] raised a cross-team question on 2026-04-28: which parameters — [[Sign Orientation]] (heading) or [[Seen-Sector Counts]] (observation direction buckets) — are most useful for [[Sign-to-Road Matching]]?

This page records the informal decisions each team had made as of 2026-04-30.

## Decisions by team

### Speeds team (Kenan Ozturk, Tomasz Raciborowski, Piotr Strzelecki)
- **Use heading only.** Sign orientation is used directly for sign→road matching in speed-limit generation.
- Observed angles not used. Open to exploring in future, particularly for parallel-road / slip-road disambiguation.

### Map matching (Gaurav Shah)
- **Use both**, with different depths: heading is applied with a threshold; `seen_count` max value per cluster is also used. `not_seen` count has not been used yet.

### ML training (Pim Arendsen)
- **Neither used currently** for ML training data.

### Guidance / Capybaras (Tomasz Gajewski)
- **Heading used; sector counts not used.** The team receives pre-aggregated sign data from [[Localization Layer]] (Places team), so sector-level data is not available to them directly. If sector counts were to be used, the [[Localization Layer]] would need to expose them.

## Related

- [[Sign Orientation]] — heading parameter
- [[Seen-Sector Counts]] — observation-direction parameter
- [[Sign-to-Road Matching]] — process using these parameters
- [[Sign Duplication at Junctions]] — problem motivating this review
- [[Ian Atkinson]], [[Kenan Ozturk]], [[Tomasz Raciborowski]], [[Piotr Strzelecki]], [[Gaurav Shah]], [[Pim Arendsen]], [[Tomasz Gajewski]]

*Source: `raw/slack/2026-05-08-sign-orientation-vs-observed-angles-for-sign-to-road-matching.md`*
