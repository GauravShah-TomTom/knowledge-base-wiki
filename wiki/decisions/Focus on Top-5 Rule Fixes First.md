---
type: decision
date: 2026-05-15
---

# Decision: Focus on Top-5 Rule Fixes First

## Context

The [[Lanes]] backlog contains many rule errors, but most have very low occurrence rates. The top 5 rules account for the majority of errors; the others are "very low" and considered impractical to fix now (they represent edge cases that may become relevant only when the pipeline exceeds ~90% accuracy).

## Decision

Focus the current sprint on fixing the top 5 rules only. After running those fixes, re-evaluate the remaining error distribution before deciding whether to tackle lower-frequency rules.

## Rationale

Diminishing returns: fixing rare errors at current accuracy levels is low-value. Re-assess the distribution after the top fixes reduce overall error rate first.

*Source: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`*
