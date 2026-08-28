# Literary Engineering Skills

A portable Agent Skills pack for fiction diagnosis, revision, generation, and evaluation.

The pack treats literary effects as mechanisms: event structure, viewpoint, attention, metaphor selection, relation language, voice, motive, and information pressure. It does not prescribe one “literary” surface style.

Core rule: **preserve the cause of the effect; do not imitate the decoration.**

## v2 taxonomy: four conceptual layers

The 22 skills are organized by **how deep in the language they load**. The
shallower the carrier, the more reliable the audit rule; the deeper, the
more the rule degrades into an analysis frame. The layers are conceptual —
every skill still lives flat under `skills/` so discovery keeps working.
See `LAYERS.md` for the canonical map, the rule-strength gradient, and the
shared operation vocabulary.

- **I. Language carriers (10)** — `relation-scaffolding`,
  `property-and-adjective-engineering`, `naming-and-address-engineering`,
  `metaphor-audit`, `predicate-licensing-and-personification`,
  `verb-event-engineering`, `chinese-derived-event-geometry`,
  `english-derived-motion-packaging`, `french-derived-motion-packaging`,
  `adverb-particle-viewpoint-engineering`.
- **II. Composition / discourse (4)** — `camera-attention-engineering`,
  `sentence-pressure`, `dialogue-voice`,
  `narrator-intervention-abstraction-control`.
- **III. Character / world (3)** — `character-motive`,
  `knowledge-boundaries`, `social-naming-relation-maps`.
- **IV. Method / eval (5)** — `counterfactual-revision`,
  `literary-style-router`, `literary-evals`, `corpus-convergence-audit`,
  `literary-strategy-controller`.

The three language-derived skills (`chinese-derived-event-geometry`,
`english-derived-motion-packaging`, `french-derived-motion-packaging`) name
traditions where a technique is especially dense or easy to expose. They are
not language gates: each contains a transfer procedure plus a **transfer
residue** record of what cannot survive the move. The Japanese viewpoint
tradition lives as references under
`adverb-particle-viewpoint-engineering`.

Start with `literary-style-router` when the failure is unclear; invoke a
domain skill directly when the mechanism is already known. For multi-fix
sessions, consult `literary-strategy-controller` before stacking local
optima into a house style.

## Layout

All twenty-two skills live in the `skills/` container:
`skills/<name>/SKILL.md`. Each skill is a directory with `SKILL.md`;
detailed material sits in `references/`; optional measurement tools sit in
`scripts/`. This follows Agent Skills progressive disclosure: metadata
first, instructions on activation, resources on demand.

The `skills/` container matches the discovery layout used by the open
skills CLI (`npx skills add <owner>/literary-engineering-skills`
auto-discovers all twenty-two; flat `skills/<name>/SKILL.md` is the
canonical one-level layout).

## Use

Install or copy the twenty-two skill directories (under `skills/`) into a
skills-compatible agent's skill directory. Start with
`literary-style-router` when the failure is unclear; invoke a domain skill
directly when the mechanism is already known.

Scripts are optional. They count and compare; they do not grade prose.

## Validation

```bash
python tests/validate_pack.py .
python tests/test_scripts.py
python tests/test_trigger_battery.py
python tests/run_regression.py
```

Prompt-trigger accuracy cannot be checked statically; run it with the host
agent as a controlled experiment:

```bash
python tests/run_trigger_battery.py gen judge_input.json \
  --map scoring_map.json --seed 42
# hand only judge_input.json to fresh agent(s): route each opaque id to one
# of the 22 skill names, "NONE", or "ASK"; keep scoring_map.json private.
# Split the prompts across several judges if desired, then merge their JSON:
python tests/run_trigger_battery.py score --map scoring_map.json \
  judge_output_a.json judge_output_b.json
```

The seed makes the opaque-id assignment and prompt order reproducible. The
scorer validates that every expected id appears exactly once, that no unknown
ids or invalid routes are present, and only then computes trigger metrics.

For quality-case A/B experiments (with-skill vs. no-skill on the same
prompt), use the `quality_cases` fixtures in `tests/eval_cases.yaml` and
grade mechanism identification, not polish.

If `skills-ref` is installed, also run `skills-ref validate` on each skill
directory.

## License

Original text and scripts are Apache-2.0. Short classical/public-domain
examples are identified where useful.

## Format references

The package targets the open Agent Skills format documented at:

- <https://agentskills.io/home>
- <https://agentskills.io/specification>
- <https://agentskills.io/skill-creation/best-practices>
- <https://agentskills.io/skill-creation/optimizing-descriptions>
- <https://agentskills.io/skill-creation/using-scripts>

See `MANIFEST.md` for package counts and eval coverage.
