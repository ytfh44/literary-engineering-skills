# Controlled Experiments Record

Three experiments are recorded. Experiment 1 was rerun on the current
27-skill pack (2026-11-18). Experiment 2 is the 2026-08-10 quality A/B from
the 22-skill era, kept as a historical result and not rerun. Experiment 3
covers only the two skills added in this revision (4 quality cases).

Static tests validate structure. These experiments measure what static tests
cannot: trigger routing with fresh judges, and skill effect with and without
guidance.

## Experiment 1 — trigger battery (27 skills, one round, six fresh judges)

**Design.** 574 routing prompts from `tests/eval_cases.yaml`: 234
should-trigger (ST), 226 should-not-trigger (SN), 114 ambiguous (unscored).
Prompt ids were replaced with opaque ids by
`tests/run_trigger_battery.py gen --map scoring_map.json --seed 42`; the
private map never entered the judge slices. Six fresh-context agents each
received one slice (96/96/96/96/96/94 prompts) plus only the 27 skill
descriptions. Judges were instructed to route by mechanism, never by id, and
not to open fixtures, the scoring map, or other slices. All 574 ids were
routed exactly once; `score` validated completeness, duplicates, unknown ids,
and invalid routes before computing any metric. One round only: descriptions
were not patched after seeing the result, so the measurement is not tuned to
this run.

**Results.**

| Metric | Result |
| --- | --- |
| should_trigger | **214/234 (91.5%)** |
| should_not_trigger | **221/226 (97.8%)** |
| ambiguous | 114 routed, not scored |

The two new skills in this battery:

| Skill | ST | SN |
| --- | --- | --- |
| `fair-play-mystery-audit` | 8/8 | 8/8 |
| `narrative-necessity-audit` | 7/8 | 8/8 |

**ST misses (20).** Every miss routed to another skill name; none were NONE
or ASK. The pattern is boundary double-attribution:

| Expected → chosen | Count |
| --- | --- |
| `verb-event-engineering` → `chinese-derived-event-geometry` / `predicate-licensing` | 1 + 1 |
| `chinese-derived-event-geometry` → `predicate-licensing` / `verb-event-engineering` | 1 + 1 |
| `sentence-pressure` → `chinese-derived-event-geometry` / `literary-strategy-controller` / `english-derived-motion-packaging` | 1 + 1 + 1 |
| `social-naming-relation-maps` → `naming-and-address-engineering` | 2 |
| `naming-and-address-engineering` → `social-naming-relation-maps` | 1 |
| `counterfactual-revision` → `narrative-necessity-audit` / `metaphor-audit` | 1 + 1 |
| `narrator-intervention` → `narrative-necessity-audit` / `chinese-derived-event-geometry` | 1 + 1 |
| `narrative-necessity-audit` → `fair-play-mystery-audit` | 1 |
| other single cross-routes (english→verb, dialogue→relation, adverb→camera, property→metaphor, strategy→predicate) | 5 |

The new boundary is visible: the one `narrative-necessity-audit` miss
("那封伪造的信到底排除了哪个整体可能性？还是只是装饰？") is routed to
`fair-play-mystery-audit`, a legitimate surface overlap between provenance
and configuration evidence. The naming pair still misses in both directions
(1 + 2), so the boundary remains symmetric.

**SN hits (5).** All five are self-routes:

| Skill | Prompt |
| --- | --- |
| `relation-scaffolding` | 写一个没有关系词的诗。 |
| `narrator-intervention-abstraction-control` | 解释"意识到煤气没关"是否自然。 |
| `narrative-architecture` | 给这段加一个伏笔并直接重写。 |
| `macro-narrative-architecture` | 把整部小说直接重写成三幕。 |
| `knowledge-consequence-audit` | 统计记录、封存出现了多少次。 |

The last three are rewrite/count requests that the skills' own Do-not-use
sections exclude; they are recorded as fixture-boundary hits, not patched
after the run.

**Comparison with the previous Experiment 1 (22 skills, 3 rounds).** The old
run converged at 91.2% ST / 99.5% SN; the current single round is 91.5% ST /
97.8% SN. The ST rate is stable; the SN rate is 1.7 points lower on a
different, larger fixture set (226 SN prompts vs 186). The two runs are not
directly comparable: different skill set, different fixtures, one round
instead of three.

**Known limitations.**

- Single-label ground truth: borderline prompts that legitimately sit on two
  skills' trigger surfaces count as misses. The harness supports
  `primary/acceptable/forbidden` objects, but the fixtures still use plain
  strings, so this limitation remains.
- AM prompts are routed but not scored; the battery reports no ambiguity
  metric.
- SN has a floor: a judge that answers `NONE` to every SN prompt scores
  226/226 SN and 0/234 ST, so SN alone is not a quality measure.
- Blinding is instruction-based: judges share a filesystem with the fixtures
  and scoring map. They were told not to open them, and each reported
  reading only its slice; this is weaker than process isolation.

## Experiment 2 — quality-case A/B (22-skill era, historical)

**Design.** 48 quality cases (two per skill) from the 22-skill pack. Each
prompt was answered twice: control (no skill document) and treatment
(relevant `SKILL.md` provided). All 96 answers were pooled, shuffled, given
opaque ids, and graded by two fresh judges who did not know the condition;
the mapping was joined after grading. Rubric: does the answer identify the
causal variable in the pass criteria (strict on mechanism).

**Result.** 96/96 PASS in both conditions — a ceiling effect. Matched-pair
audit showed the control condition already identified the correct mechanism
(manner/path decomposition, unplanned-attention onset, bounded inference)
without the skill document.

**Status.** Not rerun. It predates the 25-skill and 27-skill packs; its 48
cases cover 22 skills, while the current fixture set has 58 quality cases
over 27 skills. The new skills are covered by Experiment 3 instead. The
ceiling interpretation stands as a historical finding: on
mechanism-identification tasks, the base model already performed at ceiling.
The next generation of evals should test **revision discipline** (does the
one-variable protocol stop multi-variable rewrites; does the strategy
controller veto a saturated operation) rather than bare recognition.

## Experiment 3 — quality A/B for the two new skills (4 cases)

**Design.** The four quality cases added to `tests/eval_cases.yaml` for
`fair-play-mystery-audit` and `narrative-necessity-audit` (two each). One
fresh agent answered all four prompts without any skill document (control);
one fresh agent answered all four with the relevant `SKILL.md` provided
(treatment). The eight answers were anonymized, shuffled, and given opaque
ids; two fresh graders applied each case's pass/fail criteria without
knowing the condition. Grading remained mechanism identification, the same
rubric family as Experiment 2. One grader failed before writing its file and
was replaced by a second fresh agent; the retry is recorded here.

**Results.** Per grader, PASS counts out of 4:

| Grader | Control | Treatment |
| --- | --- | --- |
| grader 1 | 2/4 | **4/4** |
| grader 2 | 3/4 | **4/4** |

Both graders failed the control answer to `fp2` ("我想在最后揭穿一个假说，
但它在第二章之后就没再被提过") and passed the treatment answer; both
passed `fp1` and `nn1` in both conditions; they disagreed on the control
answer to `nn2` (one PASS, one FAIL). Under an all-graders-must-pass rule:
control 2/4, treatment 4/4.

**Interpretation.** The treatment was not a pure ceiling: the two skills
produced a measurable lift on the "dropped hypothesis" case under both
graders, and on the "decorative narrator" case under one. Two of the four
cases were still ceiling (control already passed), so the effect is partial,
not universal. This is the first evidence in this repo that the new audit
skills change a graded outcome rather than only routing; the sample is four
cases and two graders, so it should not be generalized.

## Reproducibility

- Generator: `python tests/run_trigger_battery.py gen judge_input.json
  --map scoring_map.json --seed 42` (574 prompts, 27 descriptions).
- Slices: the public judge input was split into six files of
  96/96/96/96/96/94 prompts; each fresh judge received one slice only.
- Scoring: `python tests/run_trigger_battery.py score --map scoring_map.json
  judge_output_*.json`; duplicate, missing, unknown, and invalid routes fail
  validation before any metric is computed.
- Blind judging (Experiments 1 and 3): opaque ids, private mapping kept out
  of the repository; judges and graders instructed to ignore condition/id and
  to read only their assigned file.
- Raw artifacts (slices, judge outputs, mappings, grader files) were kept
  outside the repository and are not committed. The reproducible input is
  `tests/eval_cases.yaml`; the declared seed is 42.
