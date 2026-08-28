# Controlled Experiments Record

Real experiments run on the v2 pack (2026-08-10), executed by fresh-context
agents. Static tests validate structure; these experiments measure what
static tests cannot: trigger accuracy with real judges, and skill effect
with and without guidance.

## Experiment 1 — trigger battery (double-blind, 3 rounds)

**Design.** 474 prompts from `tests/eval_cases.yaml` (22 skills ×
should-trigger / should-not-trigger / ambiguous). Prompt ids were replaced
with opaque random ids (mapping kept separate) so judges could not route by
id prefix. Six fresh-context judges per round, each routing one slice of 79
prompts using only the 22 skill descriptions. Judges did not know the
expected answers; the mapping was joined only after scoring.

**Results.**

| Round | Description version | should_trigger | should_not_trigger |
| --- | --- | --- | --- |
| 1 | initial v2 | 176/194 (90.7%) | 185/186 (99.5%) |
| 2 | after 6 description patches | 176/194 (90.7%) | 185/186 (99.5%) |
| 3 | after ablation/eventification/deictic patches + 2 prompt rewrites | 177/194 (91.2%) | 185/186 (99.5%) |

**Convergence.** Three rounds with different judges converged at ~91% ST /
99.5% SN. Description patches did not change the total; the miss set
reshuffled between rounds. The remaining 17 ST misses are all
**boundary double-attributions**: each missed prompt's chosen route is a
legitimate trigger surface of an adjacent skill (metaphor ablation →
metaphor-audit, predicate coercion → predicate-licensing, eventify →
chinese-derived-event-geometry, walk/stride → verb-event-engineering,
particle epistemic scope → adverb-particle-viewpoint, 万葉集 visual field →
camera-attention, single-act naming ↔ global naming map). The naming pair
misses in both directions (2+2), confirming the boundary is symmetric, not
one-sided. This is a property of the taxonomy's adjacent borders, not a
description defect; further description edits reshuffle rather than reduce.

**Known limitation.** The eval schema requires exactly one target per
prompt; borderline cases that are legitimately two skills' trigger surface
count as misses. An "acceptable alternate" field would move the boundary
cases out of the miss column.

## Experiment 2 — quality-case A/B (double-blind grading)

**Design.** 48 quality cases (2 per skill). Each prompt answered twice:
control (no skill document) and treatment (relevant SKILL.md provided).
All 96 answers were pooled, shuffled, given opaque ids, and graded by two
fresh judges who did not know the condition; the mapping was joined after
grading. Grading rubric: does the answer identify the causal variable in
the pass_criteria (strict on mechanism).

**Result.** 96/96 PASS in both conditions — a ceiling effect. Eyeball
audit of matched pairs shows the control condition already identifies the
correct mechanism (e.g., manner/path decomposition, unplanned-attention
onset, bounded inference) without the skill document.

**Interpretation.** On mechanism-identification tasks, the base model
already performs at ceiling; the skill documents did not measurably change
identification. The skills' value is likely in execution discipline
(one-variable control, state tracking, layer attribution) and in routing —
which Experiment 1 measures — not in bare mechanism recognition. This
suggests the next eval generation should test **revision discipline**
(e.g., does the counterfactual protocol stop multi-variable rewrites? does
the controller veto a saturated operation?) rather than recognition.

## Reproducibility

- Generator: `python tests/run_trigger_battery.py gen judge_input.json
  --map scoring_map.json --seed 42` (descriptions + all fixture prompts).
- Blinding: opaque ids and prompt order are randomized per round with a fixed
  seed; the private mapping is kept out of the repo (gitignored).
- Judges: fresh-context agents, `isolated: true`, instructed to route by
  mechanism, never by id; every output validated (all ids present, routes
  within the 22 names + NONE + ASK).
- Grading: `python tests/run_trigger_battery.py score --map
  scoring_map.json judge_output_*.json`; duplicate, missing, unknown, or
  invalid routes fail validation before any metric is computed. Two fresh
  judges used a rubric from the per-case fail/pass criteria, with condition
  unknown; 96/96 verdicts.

Raw artifacts (slices, outputs, mappings, score reports) are gitignored by
design — the record above is the deliverable, and the fixture file
`tests/eval_cases.yaml` is the reproducible input.
