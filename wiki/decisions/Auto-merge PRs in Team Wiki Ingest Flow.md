---
type: decision
---

# Auto-merge PRs in Team Wiki Ingest Flow

The [[Team Wiki]] GitHub Action ingest flow creates pull requests that auto-merge by default, without requiring manual review approval for every ingest run.

## Rationale

Wiki ingest runs are high-frequency, automated, and low-risk — the content comes from internal raw files already vetted by the team. Requiring manual PR approval for each ingest run would create friction and slow down knowledge capture. Conflicts and contradictions are detected programmatically and surface as `⚠️ CONFLICT` blocks rather than blocking the merge.

## Related decisions

- [[Use Azure AI Search for Team Wiki Indexing]] — the merged PR triggers an automatic reindex

*Source: raw/scans/ChatGPT Image May 19_ 2026_ 10_18_11 AM.png*
