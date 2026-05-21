---
type: concept
---

# Route Divergence

*Source: raw/scans/MEDS Overview.pdf*

A Route Divergence is a signal produced when a driver's actual path (as determined by [[Map Matching]] of GPS traces) deviates from the route that navigation suggested. Divergences are the primary input signal for [[MEDS]] and indicate potential map data errors.

## How it is computed

```
Raw Driver Traces → MapMatching → PTMMT → actual segment sequence
                                                    ↓
Navigation Route Suggestions → suggested segment sequence → Divergence Calculator
                                                                        ↓
                                                             RouteDivergences Dataset
```

The Divergence Calculator compares the two segment sequences and records the point and segments where they first differ.

## Output fields

| Field | Description |
|---|---|
| divergence-location | lat/lng coordinate where divergence occurs |
| divergence-segment | the map segment where the suggested path was abandoned |
| suggested-segment | the segment navigation suggested the driver take |
| traversed-segment | the segment the driver actually took |
| timestamp | when the divergence occurred |
| trip-metadata | associated trip information |

## Visual representation

- **Blue** = Divergence segment (where navigation said to go)
- **Red** = Suggested segment
- **Green** = Traversed segment (where driver actually went)

## Usage in MEDS detectors

- **GeoCatch** — aggregates divergences by `[divergence_segment + traversed_segment]` to find missing roads
- **OneWay** — aggregates divergences on suggested segment to find one-way errors
- **TurnRestriction** — aggregates divergences to find missing turn restrictions
- **Blocked Road** — aggregates divergences to find missing blockpassage attributes

## Related

- [[MEDS]] — consumer of route divergence data
- [[Map Matching]] — produces the actual traversal data
- [[PTMMT]] — processes traces into segment sequences
- [[Segment Traversal]] — aggregated view of segment-level traversals
