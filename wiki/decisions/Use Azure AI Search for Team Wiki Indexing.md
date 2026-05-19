---
type: decision
---

# Use Azure AI Search for Team Wiki Indexing

The [[Team Wiki]] platform uses [[Azure AI Search]] as its search and vector index backend, with automatic reindexing triggered on every push to `main` via the `wiki-aoai-index` GitHub Action.

## Rationale

Azure AI Search provides managed hybrid search (keyword + semantic vector) with no infrastructure to run. The automatic reindex-on-push pattern means the search index stays current with the wiki without any manual intervention after an ingest run.

## Related decisions

- [[Auto-merge PRs in Team Wiki Ingest Flow]] — merged PRs trigger the reindex
- [[Use Azure OpenAI as Team Wiki Reasoning Gateway]] — embeddings for vector search come from Azure OpenAI

*Source: raw/scans/ChatGPT Image May 19_ 2026_ 10_18_11 AM.png*
