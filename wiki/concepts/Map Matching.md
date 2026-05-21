---
type: concept
---

# Map Matching

*Source: raw/scans/MEDS Overview.pdf*

Map Matching is the process of taking raw GPS traces from a moving vehicle and aligning them to the road network in [[UMM]], producing a sequence of road segments that best represents the vehicle's actual path.

At Uber, map-matched driver traces are the foundation of the [[Route Divergence]] and [[Segment Traversal]] signals that power [[MEDS]] map error detection. The map matching pipeline outputs matched traces to [[PTMMT]], which converts them into segment sequences for comparison against navigation suggestions.

## Pipeline context

```
Raw Driver Traces → MapMatching → PTMMT → segment sequence → Divergence Calculator
```

## Related

- [[PTMMT]] — downstream consumer that converts matched traces to segment sequences
- [[Route Divergence]] — produced by comparing matched traces against navigation suggestions
- [[Segment Traversal]] — aggregated from map-matched paths
- [[MEDS]] — map error detection system that relies on these signals
