---
type: concept
---

# MapMatching

MapMatching is the process of aligning raw GPS driver traces to a road network, producing a sequence of road segments that best explains the observed positions. It is a prerequisite step in the [[Route Divergence]] pipeline used by [[MEDS]].

## Role in MEDS

Raw driver GPS traces are noisy and position-only. MapMatching converts them into a structured segment sequence on the [[UMM]] road graph. The matched sequence is then handed to [[PTMMT]] to produce the canonical traversed-segment sequence, which is compared against Navigation Route Suggestions by the Divergence Calculator.

## Related

- [[Route Divergence]] — downstream consumer of map-matched traces
- [[PTMMT]] — converts map-matched output into a segment sequence
- [[MEDS]] — overall system that uses map matching as a data source
- [[UMM]] — the road network graph used for matching

*Source: `raw/scans/MEDS Overview.pdf`*
