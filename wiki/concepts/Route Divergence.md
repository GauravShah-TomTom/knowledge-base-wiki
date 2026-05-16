---
type: concept
---

# Route Divergence

A route divergence is an event where a driver traverses a different road segment than the one suggested by the navigation system. Route divergences are the primary input signal to [[MEDS]] (Map Error Detection System) — when many drivers diverge at the same location in the same way, it indicates the map data is likely wrong at that point.

## How It Is Produced

1. **Raw Driver Traces** are ingested and processed by **MapMatching**, which aligns GPS positions to road segments.
2. **[[PTMMT]]** converts the map-matched trace into a *segment sequence* representing the path actually taken.
3. The **Navigation Route Suggestions** system provides an independent *segment sequence* representing the intended route.
4. The **Divergence Calculator** compares the two sequences and emits a divergence record wherever they diverge.
5. Divergence records are stored in the **RouteDivergences Dataset**.

## Output Fields

| Field | Description |
|---|---|
| `divergence-location` | Lat/lng where the driver left the suggested route |
| `divergence-segment` | The segment suggested by navigation at the point of divergence |
| `suggested-segment` | The segment navigation wanted the driver to use |
| `traversed-segment` | The segment the driver actually used |
| `timestamp` | When the event occurred |
| `trip-metadata` | Trip context (vehicle type, city, etc.) |

## Usage in MEDS Detectors

Different detectors use route divergence data differently:

- **[[GeoCatch]]** — groups by `divergence_segment + traversed_segment` to find missing roads
- **OneWay Detector** — groups by `suggested_segment` to detect wrong one-way markings
- **TurnRestriction Detector** — compares problematic vs. alternative transitions
- **Blocked Road Detector** — finds segments suggested but never traversed (suggestions ≥ 10, traversals = 0)

## Related

- [[MEDS]] — system that consumes route divergences for map error detection
- [[PTMMT]] — produces the traversed segment sequence
- [[UMM]] — map topology against which divergences are compared
- [[Map Healing]] — the goal that route divergence detection serves
- [[GeoCatch]] — the missing-roads detector driven by route divergences

*Source: `raw/scans/MEDS Overview.pdf`*
