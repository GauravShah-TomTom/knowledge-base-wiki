---
type: problem
status: active
---

# Sign Duplication at Junctions

## Problem

At road junctions, the same physical traffic sign may be visible from multiple driving directions. Eagle probe vehicles from different approach angles each record an observation of the same sign, leading to **duplicate sign entries** in the dataset. These duplicates distort downstream systems that rely on sign-to-road matching (e.g. speed limit derivation).

Raised by [[Ian Atkinson]] on 2026-04-28.

## Contributing factors

- [[Sign Orientation]] (heading) alone is insufficient to distinguish whether two observations at similar angles are genuinely the same sign seen from different directions or two distinct signs.
- [[Seen-Sector Counts]] could help by indicating from which sectors an observation cluster was seen, but adoption across teams is limited (as of 2026-04-30).

## Investigation

[[Ian Atkinson]] is assessing whether additional messages in the newest [[Eagle]] firmware can improve sign bearing and help resolve duplicates.

## Related

- [[Sign Orientation]] — current primary matching parameter
- [[Seen-Sector Counts]] — potential additional signal
- [[Sign-to-Road Matching]] — the process affected by duplicates
- [[FCD Cluster API]] — exposes the relevant cluster properties

*Source: `raw/slack/2026-05-08-sign-orientation-vs-observed-angles-for-sign-to-road-matching.md`*
