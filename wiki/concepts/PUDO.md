---
type: concept
---

# PUDO — Pick-Up / Drop-Off Location

A **PUDO** (Pick-Up/Drop-Off location) is a geographic point where drivers pick up or drop off riders. Popular PUDOs are used by [[MEDS]]'s SegErr Detectors as reference points to identify missing road segments.

*Source: raw/scans/MEDS Overview.pdf*

## Usage in Map Error Detection

The SegErr (Segment Error) detector within [[MEDS]] uses PUDOs as follows:

1. Load popular PUDOs (high-frequency pick-up or drop-off points)
2. Find the closest road segment in [[UMM]] to each PUDO
3. If the distance exceeds **50 metres** → flag as a potential missing segment

This catches cases where the map has no road near a place where many trips start or end — indicating a missing road segment in [[UMM]].

## Related

- [[MEDS]] — uses PUDO data in the SegErr detector
- [[UMM]] — the map model checked for nearby segments
- [[Map Healing]] — broader domain
