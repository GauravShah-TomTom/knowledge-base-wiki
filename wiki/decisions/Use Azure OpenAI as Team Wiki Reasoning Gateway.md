---
type: decision
---

# Use Azure OpenAI as Team Wiki Reasoning Gateway

The [[Team Wiki]] Chat UI and [[MCP]] server use [[Azure OpenAI]] as the language model backend for answer generation and embedding production.

## Rationale

Azure OpenAI provides enterprise-grade OpenAI models within an Azure tenant, keeping data within the organisation's cloud boundary and simplifying compliance. It integrates naturally with [[Azure AI Search]] for retrieval-augmented generation.

## Related decisions

- [[Use Azure AI Search for Team Wiki Indexing]] — retrieval layer that feeds context to Azure OpenAI
- [[Serve MCP from Team Wiki Next.js App]] — MCP server also routes queries through Azure OpenAI

*Source: raw/scans/ChatGPT Image May 19_ 2026_ 10_18_11 AM.png*
