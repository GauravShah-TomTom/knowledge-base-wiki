---
type: concept
---

# Vector Index

A search index that stores dense vector embeddings (numerical representations of text meaning) alongside traditional keyword (B2S) indexes, enabling semantic similarity search — retrieving results by meaning rather than exact keyword match.

## Usage in Team Wiki

The [[Team Wiki]] platform builds a combined B2S + vector index in [[Azure AI Search]]. Embeddings are generated via [[Azure OpenAI]] and updated incrementally each time a PR is merged to `main`. Both the Chat UI and [[MCP]] server query this index to retrieve relevant wiki pages.

*Source: raw/scans/ChatGPT Image May 19_ 2026_ 10_18_11 AM.png*
