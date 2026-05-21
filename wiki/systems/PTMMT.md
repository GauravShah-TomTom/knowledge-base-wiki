---
type: system
stub: true
---

# PTMMT

*Source: raw/scans/MEDS Overview.pdf*

PTMMT is an internal Uber system that takes map-matched driver traces and produces a **segment sequence** — the sequence of road segments actually traversed by a driver. This sequence is compared against the Navigation Route Suggestions segment sequence by the Divergence Calculator to produce [[Route Divergence]] events consumed by [[MEDS]].

The acronym is not expanded in available sources.

## Role in MEDS pipeline

```
Raw Driver Traces → MapMatching → PTMMT → segment sequence
                                                    ↓
Navigation Route Suggestions → segment sequence → Divergence Calculator
```
