---
type: system
---

# MEDS — Map Error Detection System

*Source: raw/scans/MEDS Overview.pdf*

MEDS is Uber's internal platform for proactively detecting, classifying, and fixing map data errors ("Map Healing"). It ingests driver trace signals, compares them against the current map model ([[UMM]]), and surfaces discrepancies to a set of specialized detector modules. Detections feed into [[MIT Reporting]] and an [[Auto-Graduation]] pipeline that automatically applies fixes via the TomTom map provider.

## Objective

Proactively detect, classify, and fix map problems before they impact rider or driver experience.

## Input Signals

| Signal | Description |
|---|---|
| Route Divergences | Points where the driver's actual path diverges from the navigation suggestion — see [[Route Divergence]] |
| Segment Traversals | Per-directed-segment counts of suggestions vs. actual traversals — see [[Segment Traversal]] |
| Transition Traversals | Per-3-segment-turn counts of suggestions vs. actual traversals — see [[Transition Traversal]] |
| UMM | The [[UMM]] (Uber Map Model) — segments, junctions, maneuvers, road furniture |

## Architecture

```
transition traversals ──→ MissingRoad Detector (GeoCatch) ──┐
segment traversals    ──→ TurnRestriction Detector          ──┼──→ MIT Reporting
Route Divergences     ──→ [other detectors...]              ──┤
UMM                   ──→ OneWay Detector                   ──┘
                                                              └──→ Auto-Graduation → TomTom
```

## Detectors

### 1. GeoCatch — Missing Roads

Detects roads that exist on the ground but are absent from the map.

**Algorithm:**
1. Aggregate route-divergences by composite key `[divergence_segment + traversed_segment]`
2. Filter records where segments do not share a junction
3. Filter out records with fewer than 12 trips
4. Filter out records where divergence and traversed segments are topologically connected within 3 hops

**Output:** From Segment, To Segment

### 2. TurnPermitted — Invalid Turn Restrictions

Detects turn restrictions in the map that drivers are actually ignoring.

**Algorithm:**
1. Fetch all non-conditional turn restriction maneuvers; filter out those co-located with barriers
2. Join with transition traversals; apply thresholds:
   - Restricted transition traversals ≥ 21
   - Restricted transition traversals ≥ 5% of first segment traffic
3. Filter based on map specification:
   - Exclude sharp turns (steering angle < 60°)
   - Exclude implicit turns (mnrFeatureType = 21031)
   - Exclude calculated turns (mnrFeatureType = 2101)
   - Exclude U-turns in US and Brazil

**Output:** Invalid Maneuver ID

### 3. IPBP — Invalid Permanent Barriers

Detects permanent barrier road furniture that drivers are driving through.

**Algorithm:**
1. Fetch all permanent barrier road furnitures
2. Join with 3-segment transition traversal data; sum actual traversals per barrier segment
3. Threshold: actual traversals ≥ 20 (filter out U-turns for barrier leads)

**Output:** Invalid Barrier ID

### 4. OneWay — Missing OneWay Restrictions

Detects bidirectional segments that should be one-way in the map.

**Algorithm:**
1. Aggregate route divergences on suggested segment
2. Join with segment traversals
3. Apply thresholds:
   - Problematic direction: Suggestions ≥ 10 AND traversal% ≤ 15%
   - Opposite direction: Traversals ≥ 10 AND traversal% ≥ 80%
4. Exclude road types: PARKING_ROAD, WALKWAY, CONNECTOR, private roads

**Output:** Segment ID

### 5. TurnRestriction — Missing Turn Restrictions

Detects turns that drivers consistently avoid, indicating a physical restriction absent from the map.

**Algorithm — all thresholds must pass:**
- Problematic transition suggestions ≥ 20
- Problematic transition traversal rate ≤ 20% (actual/suggested)
- Alternative transition traversal rate ≥ 80%
- Alternative transition traversal count ≥ 100

**Output:** Pre-Divergence segment, Divergence segment, Suggested segment

### 6. Blocked Road Detector — Missing Blockpassage

Detects segments with zero traversals in both directions despite navigation suggesting them.

**Algorithm:**
1. Aggregate route divergences on suggested segment
2. Both directions: Suggestions ≥ 10 AND traversals = 0
3. Exclude: PARKING_ROAD, WALKWAY, CONNECTOR

**Output:** Segment ID

### 7. SegErr — Missing Segments

Detects popular [[PUDO]] locations that are too far from any mapped road segment.

**Algorithm:**
1. Load popular PUDOs
2. Find closest segments
3. If distance > 50 meters → produce detection

**Output:** PUDO location, Closest Segment ID

## Auto-Graduation Pipeline

Detector outputs feed the [[Auto-Graduation]] pipeline, which applies fixes via TomTom:

| Detector | TomTom operation | Internal accuracy | Pipeline yield | Applied fixes/week |
|---|---|---|---|---|
| MissingRoad (GeoCatch) | AddSegment | 75% | 43% | 600 |
| TurnPermitted | DeleteTurnRestriction | 80% | 15% | 1,200 |
| MissingOneWay | MakeRoadOneWay | 50–70% | 13% | 150 |
| TurnRestriction | AddTurnRestriction | ~50% | 5% | 50 |
| InvalidPermanentBlockPassage (IPBP) | DeleteBarrier | 80% | TBD | TBD |

## Related

- [[UMM]] — underlying map data model
- [[Route Divergence]] — primary input signal
- [[Segment Traversal]] — segment-level signal
- [[Transition Traversal]] — turn-level signal
- [[Map Matching]] — produces the traversal signals
- [[Auto-Graduation]] — automated fix application
- [[MIT Reporting]] — reporting destination
- [[PUDO]] — used by SegErr detector
- [[Map Healing]] — the broader map quality initiative
