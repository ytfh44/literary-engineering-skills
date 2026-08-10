---
name: counterfactual-revision
description: Use when the user wants to know which local change actually improves or harms a passage, compare two revisions, test a suspected relation word or verb, or revise by controlled one-variable interventions rather than wholesale rewriting.
license: Apache-2.0
---

# Counterfactual Revision

## Use when

The question is causal: **which change made the effect?**

## Do not use when

Do not use this as the first pass when the failure mechanism is still unknown. Route or diagnose first. For evaluating many outputs or a skill itself, use `literary-evals`.

## Core rule

**Change one variable. If five things change, the comparison teaches nothing.**

## Standard interventions

- delete one relation marker;
- replace one predicate;
- swap subject/object or active/passive focus;
- switch a deictic direction such as 来/去;
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

## Read next

- [minimal-interventions.md](references/minimal-interventions.md) for choosing the smallest variable.
- [deletion-tests.md](references/deletion-tests.md) for relation/explanation ablation.
- [viewpoint-swaps.md](references/viewpoint-swaps.md) for observer and deictic changes.

## Return shape

Return **hypothesis -> A/B -> changed variable -> observed consequence -> verdict**. Keep the rest of the prose fixed enough that the verdict is legible.
