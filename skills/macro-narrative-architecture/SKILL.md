---
name: macro-narrative-architecture
description: Use when a literary request concerns the architecture of a whole novel, volume, or ordered multi-thread sequence — trace main lines, side lines, intercalary chapters, returns, crossings, chapter-to-chapter switches, and the lifecycle of commitments; inspect knowledge, rhythm, and retrieval load without requiring convergence or closure. Do not use for a paragraph, scene, or bounded 3–5-scene window.
license: Apache-2.0
---

# Macro Narrative Architecture

## Use when

The supplied material is a whole novel, one volume, or a long ordered sequence of
chapters/beats with more than one active thread. The question concerns how the
work moves across that order:

- where a main line, side line, or intercalary chapter enters and exits;
- where a line returns after absence, crosses another line, or remains parallel;
- what a chapter switch carries forward as knowledge, rhythm, or retrieval work;
- how a request, warning, debt, vow, object, or other commitment changes state
  across chapters;
- whether the ending leaves lines open, separate, or deliberately unclosed.

Use it even when the user says “plot structure,” “chapter architecture,” “parallel
threads,” “回收,” or “这一卷怎么分配线索,” provided the evidence is chapter-scale.
This skill observes the macro arrangement first; it does not rewrite the novel.

## Do not use when

Do not use this skill for:

- one sentence, paragraph, scene, or a bounded 3–5-scene window; use
  `narrative-architecture`;
- deciding who knows a fact, when a character learns it, or whether a disclosure
  leaks; use `knowledge-boundaries`;
- sequencing several local revisions, tracking accumulated edits, or choosing the
  next marginal revision across a document; use `literary-strategy-controller`;
- testing whether one local change caused an effect; use
  `counterfactual-revision`;
- a general plot summary with no structural question;
- rewriting, filling gaps, inventing payoffs, or declaring an open line defective.

Do not infer a whole-book architecture from a local excerpt. If chapter order,
thread identity, or commitment evidence is absent, mark the field `unknown` and
narrow the claim.

## Core test

**Can I trace at least two anchored thread/commitment events in the supplied
chapter order, and show what changes at each entry, exit, return, or crossing?**

A valid observation names the chapter/beat anchor, quotes or locates the evidence,
and separates observation from inference. If it cannot do that, return `unknown`
or `out of scope`, not a global diagnosis.

## Scope

Work over the user's supplied whole work, volume, or ordered chapter set. Preserve
three orders separately:

- **chapter order** — the order in which the text presents chapters or inserts;
- **story order** — the order of events, only when the text supports it;
- **thread order** — each line's own entrances, absences, returns, and crossings.

Never collapse an inserted chapter into a main-line chapter merely because it shares
time, place, or a character. Treat `插章`, `回流`, and `交叉` as observations to
verify, not as defects or required stages.

## Inputs

Request or construct these records from the supplied text. Missing fields remain
`unknown`; do not backfill them from genre expectations or a synopsis.

### 1. Ordered chapter/beat anchors

```text
chapter_id: C01
order: 1
beat_id: C01-b2
location: chapter 1, paragraph 4 / page 8
anchor: 小满收到一封未寄出的信
textual evidence: “……”
thread candidates: T-main, T-father-letter
```

An anchor must be findable again. A chapter title alone is not evidence of a
thread event; pair it with a beat, sentence, page, or supplied locator.

### 2. Thread table

```text
thread_id | working label | first anchored entry | known participants | notes
T-main   | 小满返乡      | C01-b1              | 小满               | label is provisional
T-bridge | 桥的传说      | C02-b1              | unknown            | relation to T-main: unknown
```

Labels are handles for tracking, not claims about thematic importance. Use
`unknown` for an unanchored origin, identity, or relation.

### 3. Commitment table

```text
commitment_id: K03
kind: request / warning / debt / vow / object / constraint
introduced_at: C01-b2
holder_or_issuer: unknown
wording_or_event: “三天后在桥边见。”
textual evidence: exact sentence or locator
```

Record only forward-facing conditions that the text actually establishes. A
reader's hope, a genre convention, or an analyst's preferred payoff is not a
commitment until anchored.

## Workflow

1. **Declare the scope and evidence limit.** List the included chapters/volume and
   say whether beats, page locators, or full text are available.
2. **Normalize the order without normalizing the story.** Number chapters and
   inserts as presented (`C02`, `C02-insert`, `C03`); preserve titled and untitled
   intercalaries. Note any missing chapter or uncertain order as `unknown`.
3. **Anchor thread events.** For each chapter, record which thread is entered,
   active, exited, returned to, crossed with another, or not evidenced. Keep a
   provisional label where identity is uncertain.
4. **Build the thread × chapter matrix.** Put one compact evidence anchor in each
   non-empty cell. An empty cell means “not evidenced in supplied material,” not
   “thread absent from the fictional world.”
5. **Read switches as loads.** At every boundary, record the departing and entering
   thread and the observable carryover:
   - **knowledge load** — facts, questions, or commitments left active across the
     switch; do not decide who knows what;
   - **rhythm load** — an observable change in duration, intensity, density, or
     pause created by the sequence; do not label it good or bad;
   - **retrieval load** — a prior anchor the text asks the reader to recover when a
     line returns; if no textual cue supports recovery, mark `unknown`.
6. **Trace commitments longitudinally.** At each later anchor, classify only what
   the text supports: `paid`, `transformed`, `open`, or `unknown`. A refusal to
   return, an explicit abandonment, and an open ending remain evidence about the
   work's state; they are not automatic defects.
7. **List competing architectural readings.** For each uncertain return, crossing,
   or commitment state, give the strongest supported reading, a live alternative,
   the anchors supporting each, and what the text does not settle.
8. **Name one reversible next experiment.** Propose an outline-level test such as
   bracketing one insert, temporarily swapping one chapter boundary, or marking a
   return cue. State what relation the test would observe and what would count as
   no meaningful change. Do not perform a rewrite. If actual A/B prose is wanted,
   hand off to `counterfactual-revision`.
9. **Stop when the evidence boundary is reached.** Do not extrapolate beyond the
   supplied chapters or convert an unresolved state into a verdict.

## Thread × chapter matrix

Use this report view rather than a hidden graph:

```text
             C01                 C02-insert             C03                 C04
T-main       enter: C01-b1       —                      return: C03-b1       cross: C04-b3
T-bridge     —                   enter/active: C02-b1   active: C03-b2       exit: C04-b1

Cell note: [anchor] -> [observed status] -> [inference, if any]
```

Allowed status words are descriptive: `enter`, `active`, `exit`, `return`,
`cross`, `intercalary`, `not evidenced`, `unknown`. Do not use the matrix to
rank lines, calculate coverage, or imply that every line should appear in every
chapter.

## Switch and load register

For each chapter boundary, return:

```text
boundary: C02-insert -> C03
leaving thread: T-bridge (anchor C02-b1)
entering thread: T-main (anchor C03-b1)
knowledge load: K03 remains named / holder unknown
rhythm load: short insert followed by a long waiting scene (observed)
retrieval load: C01-b2 is echoed by “那封信” at C03-b1
alternative: C03 may begin a new cycle rather than return to T-main
unknown: whether the echo is intended as reader recall or character recall
```

“Load” names work created by the ordering. It is not a measurement of reader
performance and does not authorize adding reminders.

## Commitment lifecycle

Return one row per anchored commitment, retaining its history:

```text
id   introduced       carried through     later anchor   state        evidence
K03  C01-b2           C02-insert,C03       C04-b3         transformed  “见面” becomes “留下钥匙”
K04  C02-b1            C03                  end            open         text explicitly declines the promised reunion
K05  C03-b2            C04                  —              unknown      later status not supplied
```

- **paid**: the text enacts, answers, or materially resolves the established
  condition; quote the paying anchor.
- **transformed**: the condition changes object, terms, bearer, or consequence;
  show both the old and new anchors.
- **open**: the text leaves it active, suspended, refused, or deliberately
  unanswered; say which textual signal supports that description.
- **unknown**: the supplied evidence cannot determine its later state.

`open` is a state, not a quality judgment. An explicitly refused recovery can be
structurally deliberate. Do not rename it `failed payoff` unless the user asks for
a separate evaluative argument and supplies evidence for that argument.

## Evidence contract

Every claim in the report must be executable by another reader:

```text
claim: T-main returns in C03
anchor(s): C01-b1, C03-b1
locator: chapter/beat or page
quoted evidence: exact words or a faithful short excerpt
observation: C03 resumes the named waiting action
inference: likely return to T-main
alternative: C03 may reuse the motif without resuming the thread
unknown: thread identity is not explicitly named in C03
```

Use these rules:

1. No anchor, no confident relation.
2. Every matrix cell and lifecycle row points to a locator.
3. Keep `observed`, `inferred`, and `unknown` visibly separate.
4. When two readings survive, show both; do not average them into one verdict.
5. If the user supplied only a synopsis, label synopsis-level claims and do not
   present them as textual proof.
6. Do not use absence of evidence as evidence of absence unless the supplied text
   explicitly marks the absence.

## Minimal pair

**Baseline order:**

```text
C01：小满收到未寄出的信（T-main）
C02：插章讲桥的传说（T-bridge）
C03：回到小满在邮局等人（T-main）
```

**Candidate order:**

```text
C01：小满收到未寄出的信（T-main）
C03：小满在邮局等人（T-main）
C02：插章讲桥的传说（T-bridge）
```

Observe only the changed macro relation: in the baseline, C03 is a return after
an intercalary switch; in the candidate, the return occurs before the insert. Ask
which knowledge, rhythm, and retrieval loads move, and whether the bridge line's
relation to the waiting line becomes more or less ambiguous. Do not conclude that
either order is superior without further anchors. This is an outline experiment,
not a prose rewrite.

## Counterexamples

- Two lines may remain intentionally parallel and never converge; report the
  sustained separation and its evidence.
- A volume may contain independent short stories; do not force them into one
  thread system merely because they share a book.
- A local 3–5-scene window may suggest a return, but it is out of scope for a
  whole-book claim; route to `narrative-architecture`.
- A text may explicitly refuse to recover a promise or reunion; preserve that
  refusal as `open` or `transformed` where the evidence supports it.
- An intercalary chapter may alter rhythm or echo an image without belonging to
  either adjacent thread; keep `intercalary` and `unknown` available.
- A repeated name or object may be a motif rather than a thread crossing; do not
  merge identities without an anchor that links their functions.

## Non-goals and stop conditions

This skill does not:

- calculate coverage, closure rate, or edge counts;
- treat unrecovered material as a defect;
- require every promise to be paid;
- require threads to merge, mirror, or converge;
- infer reader psychology, character knowledge, or author intention without
  evidence;
- rewrite chapters, insert explanations, or prescribe a global rearrangement.

Stop when any of these conditions holds:

1. all supplied chapter/beat anchors have been placed in order and each unresolved
   field is marked `unknown`;
2. the requested thread or commitment has no additional anchor in the supplied
   material;
3. competing readings cannot be distinguished by the supplied evidence;
4. the report has named the smallest reversible experiment that could distinguish
   the live readings, without executing it.

## Ownership boundaries

- **`narrative-architecture`** owns paragraph, scene, and bounded 3–5-scene
  relations. This skill owns chapter-scale thread movement and whole-work order;
  it does not replace local analysis.
- **`knowledge-boundaries`** owns facts, beliefs, concealment, disclosure timing,
  and leak checks for characters, narrator, and reader. This skill records the
  structural load a switch carries, then hands knowledge-state questions over.
- **`literary-strategy-controller`** owns the state of a revision sequence and the
  marginal choice among multiple edits. This skill may expose a macro pattern but
  does not choose or sequence revisions.
- **`counterfactual-revision`** owns controlled A/B interventions and causal
  comparison. This skill names a reversible outline experiment; it does not
  execute the edit or claim that a rearrangement caused an effect.

If a question genuinely spans owners, state the overlap and report only the
cross-anchor evidence that remains observable.

## Rule strength

**Observation protocol, not a quality grade.** Prefer exact anchors, ordered
records, competing readings, and explicit unknowns. The valid result may be a
matrix with open cells, parallel lines, an unresolved commitment, or an ending
that stays open. No structural rule in this skill demands closure or convergence.

## Return shape

Return in this order:

1. **Scope and input sufficiency** — whole work/volume, chapter range, missing
   fields, and evidence limits.
2. **Thread × chapter matrix** — statuses plus locators.
3. **Entries, exits, returns, inserts, and crossings** — each with anchors.
4. **Switch/load register** — knowledge, rhythm, and retrieval loads; unknowns.
5. **Commitment ledger** — `paid`, `transformed`, `open`, or `unknown` with proof.
6. **Competing readings** — evidence for, against, and unsettled residue.
7. **Reversible next experiment** — one outline-level test, not a rewrite.
8. **Stop condition** — why the report stops at this evidence boundary.

## Read next

- [Narrative architecture](../narrative-architecture/SKILL.md)
- [Knowledge boundaries](../knowledge-boundaries/SKILL.md)
- [Literary strategy controller](../literary-strategy-controller/SKILL.md)
- [Counterfactual revision](../counterfactual-revision/SKILL.md)
