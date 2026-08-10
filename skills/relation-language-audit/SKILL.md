---
name: relation-language-audit
description: Use when fiction repeatedly states causation, contrast, implication, relationship, process, state, level, dimension, or other links that the event order may already supply; also use when the user wants a frequency/context audit of Chinese function words or relation-heavy content words.
license: Apache-2.0
compatibility: Optional Python script uses jieba for Chinese token/POS measurements; manual analysis works without it.
---

# Relation Language Audit

## Use when

The prose keeps naming how facts relate instead of letting syntax, event order, or juxtaposition carry part of the relation.

## Do not use when

Do not optimize fiction toward a low conjunction count. Logical argument, legal prose, technical exposition, and deliberately analytic narrators often need explicit relations.

## Core test

**Delete the relation marker. If the facts and the intended inference survive unchanged, the marker may be paying rent only as explanation.**

Frequency is an alarm, not a verdict.

## Workflow

1. Mark function words, relation constructions, and relation-heavy nouns/verbs.
2. Group by job: cause, contrast, simultaneity, implication, state/process naming, metadiscourse.
3. Inspect local concordance, not raw count.
4. For each candidate, delete or demote the marker mentally.
5. Keep it if it changes logic, timing, scope, emphasis, or voice.
6. Remove or recast it if event order already makes the same relation unavoidable.
7. Re-read for accidental ambiguity. Compression is not a virtue if the causal graph breaks.

## Candidates, not banned words

Chinese prose often deserves inspection around forms such as `因此`, `然而`, `于是`, `从而`, `同时`, `意味着`, `体现`, `关系`, `状态`, `过程`, `层面`, `维度`, `某种`, `似乎`, `并非……而是……`.

A necessary “因此” is cheaper than two sentences that force the reader to reconstruct a non-obvious proof.

## Minimal pair

> 他没带伞，因此淋湿了。

> 他没带伞。到办公室时，袖口还在滴水。

In ordinary scene prose, the second sentence carries cause through event order. In an argument about causes of absenteeism, `因此` may be exactly right.

## Counterexamples

- “若阀门关闭，因此压力上升” in a technical derivation: relation marking is the content; do not strip it for literary sparsity.
- “他似乎睡着了。” when viewpoint uncertainty matters: `似乎` changes epistemic scope and must survive.

## Scripts

- `scripts/zh_style_scan.py` — candidate counts, normalized rates, repeated scaffolds. Never returns an “AI score.”
- `scripts/concordance.py` — literal/regex concordance with local context.

Use scripts only when the passage is long enough that memory-based counting becomes unreliable.

## Read next

- [chinese-function-words.md](references/chinese-function-words.md) for candidate classes and retention tests.
- [relational-nouns-and-verbs.md](references/relational-nouns-and-verbs.md) for content words that summarize links.
- [relation-constructions.md](references/relation-constructions.md) for clause-level scaffolds.

## Return shape

Report candidate spans in three buckets: **keep**, **compress**, **rewrite the event**. Give one local reason per span; do not dump a blacklist.
