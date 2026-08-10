# Literary Engineering Skills

A portable Agent Skills pack for fiction diagnosis, revision, generation, and evaluation.

The pack treats literary effects as mechanisms: event structure, viewpoint, attention, metaphor selection, relation language, voice, motive, and information pressure. It does not prescribe one “literary” surface style.

Core rule: **preserve the cause of the effect; do not imitate the decoration.**

The four language-named skills (`chinese-event-geometry`, `japanese-viewpoint-engineering`, `english-motion-engineering`, `french-motion-engineering`) name traditions where a technique is especially dense or easy to expose. They are not language gates. Each contains a transfer procedure for carrying the underlying operation into another language through that language's native resources.

## Layout

All sixteen skills live in the `skills/` container: `skills/<name>/SKILL.md`. Each skill is a directory with `SKILL.md`; detailed material sits in `references/`; optional measurement tools sit in `scripts/`. This follows Agent Skills progressive disclosure: metadata first, instructions on activation, resources on demand.

The `skills/` container matches the discovery layout used by the open skills CLI (`npx skills add <owner>/literary-engineering-skills` auto-discovers all sixteen; flat `skills/<name>/SKILL.md` is the canonical one-level layout).

## Use

Install or copy the sixteen skill directories (under `skills/`) into a skills-compatible agent's skill directory. Start with `literary-style-router` when the failure is unclear; invoke a domain skill directly when the mechanism is already known.

Scripts are optional. They count and compare; they do not grade prose.

## Validation

```bash
python tests/validate_pack.py .
python tests/test_scripts.py
```

Prompt-trigger accuracy cannot be checked statically; run it with the host agent:

```bash
python tests/run_trigger_battery.py gen judge_input.json
# hand judge_input.json to a fresh agent: route each id to one of the 16 skill
# names, "NONE", or "ASK" (see the literary-evals skill for the procedure)
python tests/run_trigger_battery.py score judge_output.json
```

If `skills-ref` is installed, also run `skills-ref validate` on each skill directory.

## License

Original text and scripts are Apache-2.0. Short classical/public-domain examples are identified where useful.

## Format references

The package targets the open Agent Skills format documented at:

- <https://agentskills.io/home>
- <https://agentskills.io/specification>
- <https://agentskills.io/skill-creation/best-practices>
- <https://agentskills.io/skill-creation/optimizing-descriptions>
- <https://agentskills.io/skill-creation/using-scripts>

See `MANIFEST.md` for package counts and eval coverage.
