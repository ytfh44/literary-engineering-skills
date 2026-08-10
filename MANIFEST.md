# Package Manifest

This pack contains **16 Agent Skills** in the `skills/` container, **55 focused reference manuals**, and **4 optional measurement scripts**.

## Top-level skills

1. `literary-style-router`
2. `anti-ai-prose`
3. `relation-language-audit`
4. `metaphor-engineering`
5. `verb-engineering-core`
6. `chinese-event-geometry`
7. `japanese-viewpoint-engineering`
8. `english-motion-engineering`
9. `french-motion-engineering`
10. `camera-attention-engineering`
11. `sensory-specificity`
12. `dialogue-voice-integrity`
13. `character-motive-engineering`
14. `counterfactual-revision`
15. `sentence-pressure-and-rhythm`
16. `literary-evals`

The language-named skills are source-tradition modules. They identify places where a mechanism is especially dense or teachable; they do not reserve the technique for that language.

## Optional scripts

- `skills/relation-language-audit/scripts/zh_style_scan.py`
- `skills/relation-language-audit/scripts/concordance.py`
- `skills/counterfactual-revision/scripts/revision_diff.py`
- `skills/literary-evals/scripts/phrase_recurrence.py`

Scripts expose inspectable counts and diffs. None emits an AI-probability or literary-quality score.

## Evals

`tests/eval_cases.yaml` contains, for every skill:

- at least 8 should-trigger prompts;
- at least 8 near-miss should-not-trigger prompts;
- at least 4 ambiguous prompts;
- at least 2 output-quality cases.

`tests/run_regression.py` validates fixture coverage and package invariants.

`tests/run_trigger_battery.py` packages the host-agent trigger eval: `gen` emits judge input (descriptions + fixtures), `score` grades the judge's routing against `eval_cases.yaml`. Actual prompt-trigger accuracy must be executed by the host agent/model that will use the skills.
