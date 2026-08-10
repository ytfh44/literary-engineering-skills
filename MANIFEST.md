# Package Manifest

This pack contains **22 Agent Skills** in the `skills/` container (v2
taxonomy: four conceptual layers, flat directory layout), **65 focused
reference manuals**, and **4 optional measurement scripts**.

## Layer I — Language carriers

1. `relation-scaffolding`
2. `property-and-adjective-engineering`
3. `naming-and-address-engineering`
4. `metaphor-audit`
5. `predicate-licensing-and-personification`
6. `verb-event-engineering`
7. `chinese-derived-event-geometry`
8. `english-derived-motion-packaging`
9. `french-derived-motion-packaging`
10. `adverb-particle-viewpoint-engineering`

The three language-derived skills are source-tradition modules: they
identify places where a mechanism is especially dense or teachable, and
each records a transfer-residue report (what survives, what is added by the
target carrier, what is irrecoverable). The Japanese viewpoint tradition is
carried as references under `adverb-particle-viewpoint-engineering`.

## Layer II — Composition / discourse

 1. `camera-attention-engineering`
 2. `sentence-pressure`
 3. `dialogue-voice`
 4. `narrator-intervention-abstraction-control`

## Layer III — Character / world

 1. `character-motive`
 2. `knowledge-boundaries`
 3. `social-naming-relation-maps`

## Layer IV — Method / eval

 1. `counterfactual-revision`
 2. `literary-style-router`
 3. `literary-evals`
 4. `corpus-convergence-audit`
 5. `literary-strategy-controller`

## Rule-strength gradient

Relation layer runs strong audit rules; property layer runs functional
tests; naming layer runs framing comparison; figurative layer runs
role/domain tests; verb/event layer runs event decomposition; the
adverb/particle layer runs minimal-pair laboratories with the lowest rule
strength. See `LAYERS.md` for the full table and the shared operation
vocabulary.

## Optional scripts

- `skills/relation-scaffolding/scripts/zh_style_scan.py`
- `skills/relation-scaffolding/scripts/concordance.py`
- `skills/counterfactual-revision/scripts/revision_diff.py`
- `skills/literary-evals/scripts/phrase_recurrence.py`

Scripts expose inspectable counts and diffs. None emits an
AI-probability or literary-quality score.

## Evals

`tests/eval_cases.yaml` (v2) contains, for every one of the 22 skills:

- at least 8 should-trigger prompts;
- at least 8 near-miss should-not-trigger prompts;
- at least 4 ambiguous prompts;
- at least 2 output-quality cases (fail/pass pairs for controlled A/B
  experiments).

`tests/run_regression.py` validates fixture coverage and package
invariants.

`tests/run_trigger_battery.py` packages the host-agent trigger eval:
`gen` emits judge input (descriptions + fixtures), `score` grades the
judge's routing against `eval_cases.yaml`. Actual prompt-trigger accuracy
must be executed by the host agent/model that will use the skills —
preferably as a controlled experiment with fresh-context judges, not by
static inspection.
