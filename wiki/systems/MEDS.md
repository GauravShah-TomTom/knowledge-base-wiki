---
type: system
---

# MEDS — Map Error Detection System

MEDS is Uber's **Map Healing** platform that proactively detects, classifies, and fixes errors in the map data used for navigation and routing.

*Source: raw/scans/MEDS Overview.pdf*

## Objective

Automatically detect map problems before drivers or riders experience them, and feed verified detections into map-fix pipelines (e.g. [[TomTom]] edit workflows).

## Inputs / Signals

MEDS consumes four data sources:

| Signal | Description |
|---|---|
| **Route Divergences** | Events where a driver's actual path deviates from the navigation suggestion — see [[Route Divergence]] |
| **Segment Traversals** | Count of how many times each directed road segment was suggested vs. actually traversed |
| **Transition Traversals** | Count of how many times each 3-segment transition (From → Via → To) was suggested vs. traversed |
| **[[UMM]]** | The Uber Map Model — structured representation of road network entities |

## Architecture

```
transition traversals  ──┐
segment traversals     ──┼──▶  Detectors  ──▶  MIT Reporting
Route Divergences      ──┤
UMM                    ──┘
```

Route divergence pipeline: Raw Driver Traces → [[MapMatching]] → [[PTMMT]] → Divergence Calculator ← Navigation Route Suggestions → RouteDivergences Dataset

## Detectors

### 1. GeoCatch → Missing Roads

Detects roads present in reality that are absent from the map.

**Algorithm:**
1. Aggregate route-divergences by composite key `[divergence_segment + traversed_segment]`
2. Filter only records where segments do **not** share a junction
3. Filter out records with < 12 trips
4. Filter out records where divergence and traversed segments are topologically connected within 3 hops

**Output:** From Segment, To Segment

See also: [[GeoCatch]]

---

### 2. TurnPermitted → Invalid Turn Restrictions

Detects turn restrictions in the map that drivers consistently ignore (restriction is wrong).

**Algorithm:**
1. Fetch all non-conditional turn restriction maneuvers; filter out those co-located with barriers
2. Join with transition traversals; apply thresholds:
   - Restricted transition traversals ≥ 21
   - Restricted transition traversals ≥ 5% of first segment traffic
3. Filter out by map spec / provider rules:
   - Steering angle < 60° (sharp turn)
   - Implicit turns (`mnrFeatureType = 21031`)
   - Calculated turns (`mnrFeatureType = 2101`)
   - U-turns in US and Brazil

**Output:** Invalid Maneuver ID

---

### 3. IPBP → Invalid Permanent Barriers

Detects permanent barriers that drivers are driving through (barrier is wrong).

**Algorithm:**
1. Fetch all permanent barrier road furnitures
2. Aggregate 3-segment transition traversals on blocked segments
3. Threshold: actual traversals ≥ 20; filter out U-turns for barrier leads

**Output:** Invalid Barrier ID

---

### 4. OneWay → Missing OneWay Restrictions

Detects segments without a one-way flag that should have one.

**Algorithm:**
1. Aggregate route divergences on suggested segment
2. Join with segment traversals
3. Thresholds:
   - Problematic direction: suggestions ≥ 10 AND traversal% ≤ 15%
   - Opposite direction: traversals ≥ 10 AND traversal% ≥ 80%
4. Exclude: PARKING_ROAD, WALKWAY, CONNECTOR (add private roads)

**Output:** Segment ID

---

### 5. TurnRestriction → Missing Turn Restrictions

Detects turns that should be restricted but aren't (drivers avoid them, taking an alternative).

**All thresholds must pass:**
- Problematic transition suggestions ≥ 20
- Problematic transition traversal rate ≤ 20% (actual/suggested)
- Alternative transition traversal rate ≥ 80%
- Alternative transition traversal count ≥ 100

**Output:** Pre-Divergence segment, Divergence segment, Suggested segment

---

### 6. Blocked Road Detector → Missing Blockpassage

Detects segments that should have a full road blockage.

**Algorithm:**
1. Aggregate route divergences on suggested segment
2. Both directions must be blocked: suggestions ≥ 10 AND traversals = 0
3. Exclude: PARKING_ROAD, WALKWAY, CONNECTOR

**Output:** Segment ID

---

### 7. SegErr Detectors → Missing Segments

Detects map segments missing near popular [[PUDO]] locations.

**Algorithm:**
1. Load popular PUDOs
2. Find closest segment to each PUDO
3. If distance > 50 metres → produce detection

**Output:** PUDO location, Closest Segment ID

---

## Auto-Graduation

MEDS detections feed into an [[Auto-Graduation]] pipeline that automatically applies fixes to the map via provider pipelines (e.g. TomTom):

| Detector | Internal OPS accuracy | TomTom pipeline action | Pipeline yield | Applied fixes/week |
|---|---|---|---|---|
| MissingRoad | 75% | AddSegment | 43% | ~600 |
| TurnPermitted | 80% | DeleteTurnRestriction | 15% | ~1,200 |
| MissingOneWay | 50–70% | MakeRoadOneWay | 13% | ~150 |
| TurnRestriction | ~50% | AddTurnRestriction | 5% | ~50 |
| InvalidPermanentBlockPassage | 80% | DeleteBarrier | TBD | TBD |

*Pipeline yield* = the fraction of MEDS detections that result in a fix being applied by the TomTom pipeline.

## Related

- [[UMM]] — underlying map model
- [[GeoCatch]] — missing road detector component
- [[MapMatching]] — upstream GPS-to-road-network matching
- [[PTMMT]] — probabilistic map matching tool used in route divergence pipeline
- [[Route Divergence]] — primary signal
- [[Auto-Graduation]] — automated fix application
- [[PUDO]] — pick-up/drop-off locations used by SegErr detector
