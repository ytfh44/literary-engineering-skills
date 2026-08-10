---
name: corpus-convergence-audit
description: Use when many outputs, chapters, or corpus samples use different words but feel like the same writer — the same narrative operation skeleton under different vocabulary; use to detect operation-level convergence (sensory anomaly then mundane motive, object handoff, deleted explanation, motif return) that surface n-grams cannot catch; also for abstraction/evidence alternation rhythm and eventification rate across outputs.
license: Apache-2.0
---

# Corpus Convergence Audit

## Use when

The corpus has no repeated phrases, yet every piece reads as the same
author. The template is not lexical — it is operational: the same sequence
of narrative moves under different words. Surface recurrence (see
`literary-evals` phrase_recurrence) cannot see it; this skill traces the
operations.

## Do not use when

Do not treat convergence as a defect by default: a stable operation
skeleton can be a deliberate house style, a genre convention, or a single
author's signature. The audit reports the skeleton; the question of whether
it is a template is answered by the work's needs, not by the audit alone.

## Core test

**Strip the words. Does the operation sequence repeat?**

Two texts with zero shared vocabulary can share an operation skeleton:
SENSORY_ANOMALY -> ATTENTION_SHIFT -> EVENTIFY_PROPERTY -> DELETE_RELATION.
That skeleton is what convergence means.

## Operation vocabulary

Annotate each passage as a sequence of operations (shared with
`literary-strategy-controller`):

```text
SENSORY_ANOMALY      a sensory fact breaks the expected field
ATTENTION_SHIFT      the reader's look is redirected
EVENTIFY_PROPERTY    a static property becomes an event consequence
OBJECT_HANDOFF       one object passes attention to another
DELETE_RELATION      an explicit edge removed, event order carries it
BOUNDED_EVIDENCE     evidence with a bounded inference range replaces a label
MOTIF_RETURN         a repeated element that changes work state
OPEN_END             closure withheld
```

Keep the vocabulary small. If an operation does not appear in at least a
few passages, it is a passage feature, not an operation.

## Workflow

1. Select the corpus: outputs of one skill run, chapters of one work, or
   samples from one author.
2. Annotate each passage as an operation trace (one line per passage).
3. Compute the measures:
   - **operation n-grams** — repeated sequences of 2-4 operations;
   - **transition matrix** — which operation follows which;
   - **opening strategy distribution** — how passages start;
   - **closure strategy distribution** — how passages end;
   - **attention-path distribution** — continuous vs. hard-cut vs.
     withheld-anchor;
   - **eventification rate** — how often properties become events;
   - **abstraction/evidence alternation** — the rhythm between labels and
     bounded evidence.
4. Rank repeated skeletons by coverage: what fraction of the corpus shares
   the most common 3-operation sequence?
5. Report the skeleton with example spans from two different texts that
   share it.

## Minimal pair

Text A:

> 雪落下来，声音被吸走了。他站在门口，忽然觉得门缝里渗进来的风
> 是活的。他没有关门。 (SENSORY_ANOMALY -> ATTENTION_SHIFT ->
> EVENTIFY_PROPERTY -> OPEN_END)

Text B:

> 灯光在雾里化开，像被水泡过的字。她低头看自己的影子，影子被路灯
> 拉得很长，长到台阶下面。她没开灯。 (SENSORY_ANOMALY ->
> ATTENTION_SHIFT -> EVENTIFY_PROPERTY -> OPEN_END)

No shared words. Same skeleton. If the corpus is full of these, the
template is operational, and no vocabulary audit will find it.

## Counterexamples

- A genre with mandatory moves (mystery: clue -> misdirection -> reveal)
  will show high convergence by design; the audit's job is to distinguish
  genre skeleton from author-level tic.
- A deliberate motif structure (the same opening image across chapters)
  is MOTIF_RETURN, not convergence; the repeated operation changes the
  work state.
- One author writing a suite of thematically linked stories may share an
  operation skeleton as their signature; convergence is a fact, not a
  verdict.

## Rule strength

**Method — measurement, not grading.** The audit produces distributions
and skeletons, never a quality score. Convergence is reported with
coverage numbers and example spans; whether the skeleton is a strength or
a template is decided by the work's needs, usually with
`literary-strategy-controller`.

## Read next

- [operation-trace-protocol.md](references/operation-trace-protocol.md)
  for annotation rules and the transition-matrix recipe.
- See `literary-strategy-controller` for the state side: which operations
  are already saturated in the current document.

## Return shape

Return **operation traces -> top skeletons with coverage -> transition
matrix highlights -> example spans from two texts -> verdict (signature,
genre, or template) with reasons**. Do not report surface n-grams as
convergence evidence.
