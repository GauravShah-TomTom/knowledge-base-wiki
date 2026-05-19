---
type: system
---

# Azure AI Search

Microsoft Azure's cloud search service used by the [[Team Wiki]] platform to host keyword (B2S) and vector indexes over wiki Markdown pages. Supports hybrid search (keyword + semantic vector similarity).

## Usage in Team Wiki

- Indexed incrementally on pull request merge via a GitHub Action (`wiki-aoai-index`)
- Reindexes automatically on push to `main` — no manual re-index step required
- Backs both the [[Team Wiki]] Chat UI and [[MCP]] server retrieval

## Related systems

- [[Team Wiki]] — the platform that writes to this index
- [[Azure OpenAI]] — provides embeddings and reasoning over search results
- [[Azure Blob]] — upstream file storage

*Source: raw/scans/ChatGPT Image May 19_ 2026_ 10_18_11 AM.png*
