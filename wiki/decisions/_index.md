---
type: index
date: 2026-05-21 08:24:06
---
# Decisions - index
[[wiki/index|← Index]]

Why decisions were taken, on what basis, by whom, and when.

- [[wiki/decisions/auto-graduation-tomtom-pipeline|Decision: Use TomTom Pipeline for Automated Map Fix Application]] — *Source: raw/scans/MEDS Overview.pdf*
- [[wiki/decisions/veritas-fallout-status-generic|Decision: Use Generic Fallout Status for CoreDB Lookup Failures in Veritas]] — [[Veritas]] needs to set an explicit status for leads that are currently skipped silently when a road ID or maneuver ID is not found in [[CoreDB]] (see [[problems/Veritas Silent Lead Skipping]]).
- [[wiki/decisions/veritas-uber-production-manual-first|Decision: Run Veritas Uber ACI in Production Manually Before Scheduling]] — The [[projects/Uber ACI Flow]] production deployment (story 6011) will introduce [[Veritas]] processing of Uber restriction leads into the live environment.
- [[wiki/decisions/veritas-xml-omit-empty-fields|Decision: Omit Empty Fields from Veritas XML Metadata Output]] — [[Veritas]] emits XML with transition metadata.
