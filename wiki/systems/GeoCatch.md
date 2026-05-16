---
type: system
---

# GeoCatch

GeoCatch is the Missing Roads detector within [[MEDS]]. It analyses [[Route Divergence|route divergences]] to identify locations where a road segment is likely missing from the map — because drivers repeatedly traverse a path that the navigation system never suggested.

## Algorithm

1. Aggregate route divergences by composite key: `divergence_segment + traversed_segment`
2. Filter: keep only records where the divergence segment and traversed segment do **not** share a junction
3. Filter: remove records with fewer than 12 trips (noise suppression)
4. Filter: remove records where the divergence and traversed segments are topologically connected within 3 hops in [[UMM]]

The 3-hop filter eliminates cases where a valid but long detour exists on the current map — the driver's path would already be reachable, so there is no missing road.

## Output

- **From Segment** — the segment where the divergence occurred
- **To Segment** — the segment the driver actually traversed

These are passed to the [[TomTom]] pipeline as an `AddSegment` correction candidate.

## Performance

- Internal OPS analysis accuracy: **75%**
- TomTom pipeline yield: **43%**
- Applied fixes/week: **~600**

## Related

- [[MEDS]] — parent system
- [[Route Divergence]] — primary input signal
- [[UMM]] — topology used for the 3-hop connectivity filter
- [[TomTom]] — applies the resulting `AddSegment` fixes

*Source: `raw/scans/MEDS Overview.pdf`*
