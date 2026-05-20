---
type: system
---

# GeoCatch

GeoCatch is the **Missing Roads** detector component within [[MEDS]]. It identifies road segments that exist in reality (as evidenced by driver GPS traces) but are absent from the map.

*Source: raw/scans/MEDS Overview.pdf*

## Algorithm

1. Aggregate [[Route Divergence]] events by composite key `[divergence_segment + traversed_segment]`
2. Retain only records where the two segments do **not** share a junction (genuine topological gap)
3. Filter out records with fewer than 12 trips (noise reduction)
4. Filter out records where the divergence and traversed segments are topologically connected within 3 hops (already connected via another path)

## Output

- **From Segment** — the segment where the driver diverged from the suggested route
- **To Segment** — the segment the driver actually traversed

## Auto-Graduation

- Internal OPS analysis accuracy: **75%**
- TomTom pipeline action: `AddSegment`
- Pipeline yield: **43%**
- Applied fixes/week: ~**600**

## Related

- [[MEDS]] — parent system
- [[Route Divergence]] — input signal
- [[UMM]] — map model being corrected
