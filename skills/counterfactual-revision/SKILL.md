---
name: counterfactual-revision
description: Use when the user wants to know which local change actually improves or harms a passage, compare two revisions, test a suspected relation word, adjective, name, verb, or particle, or revise by controlled one-variable interventions rather than wholesale rewriting; this is the pack's shared experiment protocol — every layer has a canonical intervention.
license: Apache-2.0
---

# Counterfactual Revision

## Use when

The question is causal: **which change made the effect?**

## Do not use when

Do not use this as the first pass when the failure mechanism is still unknown. Route or diagnose first. For evaluating many outputs or a skill itself, use `literary-evals`.

## Core rule

**Change one variable. If five things change, the comparison teaches nothing.**

## Shared protocol

This is the pack's experiment method, not one technique among many. Every
layer has a canonical intervention — the smallest change that isolates that
layer's variable:

| Layer | Canonical intervention |
| --- | --- |
| relation | delete one relation marker (只删“因此”) |
| property | delete one affective adjective (只删“阴冷”) |
| naming | swap one name (父亲 → 那个男人) |
| figurative | delete the metaphor while keeping literal facts |
| verb/event | replace one predicate (杀 → 毙) |
| adverb/particle | swap one particle (又 → 才) |
| discourse | move one boundary (split/join, reveal order, conclusion timing) |
| character | change one knowledge or motive input, freeze the rest |

Any skill in this pack that proposes a change should be able to state its
canonical intervention. If a change cannot be stated as one variable, it
is not yet a tested claim.

## Standard interventions

- delete one relation marker;
- replace one predicate;
- swap subject/object or active/passive focus;
- switch a deictic direction such as 来/去;
- swap one particle (又/才/也/竟);
- remove the explanatory sentence after a scene;
- remove a metaphor while keeping literal facts;
- move the observer before or after the reveal;
- change clause order only.

## Workflow

1. State the suspected mechanism.
2. Freeze every unrelated variable: facts, tense, viewpoint person, register, length when possible.
3. Produce A/B with one controlled change.
4. Compare predictions: agency, inference, viewpoint, information timing, voice.
5. If no relevant prediction changes, the intervention did not isolate the cause.
6. Only then perform a full revision, if requested.

## Minimal pair

A: `他把钥匙还给她。这意味着两人的关系结束了。`

B: `他把钥匙还给她。`

The intervention deletes only the explanatory relation. If later context still makes the breakup unmistakable, the second sentence was redundant; if not, the test reveals missing evidence rather than proving explanation is bad.

## Counterexamples

- When fixing a continuity error that affects tense, subject, and event order together, one-variable editing may be impossible; repair correctness first.
- When the user asks for “three radically different versions,” controlled ablation is not the requested output, though it can still explain differences afterward.

## Script

`scripts/revision_diff.py` compares versions and reports inspectable textual differences. Use it for long passages; never treat its counts as a quality score.

## Rule strength

**Protocol — applies to every layer.** The one-variable discipline is
universal; the variable inventory is layer-specific (see the table above).
When variables cannot be isolated (multi-axis continuity repairs), say so
and repair correctness first; the protocol's first rule is honesty about
what could not be controlled.

## Read next

- [minimal-interventions.md](references/minimal-interventions.md) for choosing the smallest variable.
- [deletion-tests.md](references/deletion-tests.md) for relation/explanation ablation.
- [viewpoint-swaps.md](references/viewpoint-swaps.md) for observer and deictic changes.

## Return shape

Return **hypothesis -> A/B -> changed variable -> observed consequence -> verdict**. Keep the rest of the prose fixed enough that the verdict is legible.
