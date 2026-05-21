---
type: system
---

# CoreDB

CoreDB is the core map database that stores road IDs and maneuver IDs used during restriction verification.

[[Veritas]] queries CoreDB to look up road IDs and maneuver IDs for each lead. If a road ID or maneuver ID is not found (or has been removed from CoreDB since the lead was created), Veritas previously silently skipped the lead. As of story 5950, these leads now receive an explicit fallout status instead of being silently dropped.

CoreDB can throw runtime exceptions (e.g., branch ID lookup failures), which are caught and handled by Veritas's exception handling.

*Source: `raw/notes/Sprint grooming_ Quality improvement - PC restrictions.docx` — sprint grooming meeting 2026-05-12*
