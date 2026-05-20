---
type: concept
---

# Route Divergence

A **route divergence** event occurs when a driver's actual GPS path deviates from the route that the navigation system suggested. Route divergences are the primary signal used by [[MEDS]] to detect map errors.

*Source: raw/scans/MEDS Overview.pdf*

## Definition

At a given road segment (the **divergence segment**), the driver turns onto a different segment (the **traversed segment**) instead of continuing on the **suggested segment**.

## Key Fields

| Field | Description |
|---|---|
| `divergence-location` | lat/lng of where the divergence occurred |
| `divergence-segment` | segment ID where the route was abandoned |
| `suggested-segment` | segment ID the navigation said to take |
| `traversed-segment` | segment ID the driver actually took |
| `timestamp` | when the divergence occurred |
| `trip-metadata` | additional trip context |

## Pipeline

```
Raw Driver Traces
    → [[MapMatching]]
    → [[PTMMT]]          (segment sequence)
                              ↘
                         Divergence Calculator ← Navigation Route Suggestions
                              ↓
                     RouteDivergences Dataset
```

## Usage in Detectors

Route divergence data is the core input for several [[MEDS]] detectors:

| Detector | How divergences are used |
|---|---|
| [[GeoCatch]] | Aggregated by `[divergence_segment + traversed_segment]` to find missing roads |
| OneWay | Aggregated on suggested segment to detect wrong-way suggestions |
| TurnRestriction | Identifies transitions with high suggestions but low traversals |
| Blocked Road | Segments suggested but never traversed in either direction |

## Related

- [[MEDS]] — system that processes route divergences
- [[Map Healing]] — broader domain
- [[MapMatching]] — produces the matched GPS trace
- [[PTMMT]] — creates segment sequence from matched trace
