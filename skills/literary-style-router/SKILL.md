---
name: literary-style-router
description: Use when a fiction-writing or revision request is broad, vague, or described only as “AI-like,” “flat,” “wooden,” “purple,” “not literary,” or “make it better,” and the actual failure mechanism has not yet been identified.
license: Apache-2.0
---

# Literary Style Router

## Use when

The complaint names a symptom, not a mechanism. Diagnose first; then load the smallest skill set that can act on the cause.

## Do not use when

Skip the router when the user already names a narrow operation: verb roles, metaphor ablation, Japanese viewpoint, dialogue register, clause pressure, or another domain covered by a dedicated skill.

## Core test

**Route by what the sentence is doing wrong, not by what the user calls the feeling.**

“AI-like,” “flat,” and “too literary” can each arise from several unrelated mechanisms. Treat them as search prompts, not diagnoses.

## Workflow

1. **Locate the failure.** Quote the smallest span that creates the complaint.
2. **Name one mechanism.** Prefer an event, viewpoint, relation, voice, metaphor, motive, or pressure diagnosis over an adjective.
3. **Choose one primary skill.** Add at most two secondary skills when they answer separate questions.
4. **Order the passes.** Repair structure before ornament. Typical order: event/viewpoint -> evidence/voice -> metaphor/rhythm.
5. **Recheck by intervention.** If the user asks for revision or validation, use `counterfactual-revision` or `literary-evals` after the primary fix.

## Routing map

| Symptom in the text | Primary destination |
|---|---|
| staff-report, therapy-summary, retrospective voice | `anti-ai-prose` |
| too many explicit causal/concessive/relationship links | `relation-language-audit` |
| image says nothing beyond “dark/cold/angry/sad” | `metaphor-engineering` |
| wrong agency, weak result, decorative synonym swap | `verb-engineering-core` |
| scene is seen in a poor order | `camera-attention-engineering` |
| emotion label replaces evidence | `sensory-specificity` |
| character suddenly speaks in the author's register | `dialogue-voice-integrity` |
| “contradictory traits” feel pasted together | `character-motive-engineering` |
| clause length changes but pressure does not | `sentence-pressure-and-rhythm` |
| source-language packaging itself matters | one language-named engineering skill |

For close collisions, read [routing-matrix.md](references/routing-matrix.md). For pass order, read [audit-order.md](references/audit-order.md).

## Hard rules

- Do not activate every plausible skill “for completeness.” Context is a budget.
- Do not rewrite while the diagnosis is still “it feels off.”
- Do not route “Chinese prose” automatically to `chinese-event-geometry`; language is context, not a failure.
- Do not route “make it vivid” automatically to metaphor. The missing mechanism may be a verb or camera move.
- Do not let the router become a prose critic. Its product is a route.

## Minimal pair

User: “这句很平，帮我修。”

- Weak route: `metaphor-engineering` because “flat” sounds like an image problem.
- Strong route: inspect first. If the sentence says “他很紧张,” choose `sensory-specificity`; if it says “他走进房间,” but agency/path matter, choose `verb-engineering-core`.

Only the diagnosis changed.

## Counterexamples

- “比较‘杀’和‘毙’怎样改变施受关系。” -> go straight to `verb-engineering-core`.
- “把这段法语里的 mouvement 路径和 manière 拆开分析。” -> go straight to `french-motion-engineering`.

## Return shape

When only routing is requested, return:

1. **Primary mechanism** — one sentence.
2. **Evidence** — the smallest span.
3. **Primary skill** — one name.
4. **Optional secondary skill(s)** — zero to two, each with one reason.

Do not add a full rewrite unless the user asks for one.
