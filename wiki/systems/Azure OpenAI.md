---
type: system
---

# Azure OpenAI

Microsoft Azure's managed OpenAI service, used by the [[Team Wiki]] platform as the reasoning gateway. Powers the Chat UI's answer generation and produces embeddings ingested into [[Azure AI Search]].

## Usage in Team Wiki

- Acts as the language model backend for the [[Team Wiki]] Chat UI
- Provides vector embeddings for the B2S + vector index in [[Azure AI Search]]

## Related systems

- [[Team Wiki]] — the platform that calls this service
- [[Azure AI Search]] — consumes embeddings produced via Azure OpenAI

*Source: raw/scans/ChatGPT Image May 19_ 2026_ 10_18_11 AM.png*
