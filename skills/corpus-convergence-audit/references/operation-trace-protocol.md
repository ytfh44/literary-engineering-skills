# Operation Trace Protocol

## Annotation rules

1. Use only the shared operation vocabulary (see the skill's core text).
   If a move fits no operation, either it is not an operation (a passage
   feature) or the vocabulary needs a new member — propose it with a
   definition and a corpus example before using it.
2. One operation per narrative move; a sentence can contain one.
   SENSORY_ANOMALY and ATTENTION_SHIFT in the same sentence are two moves
   if the anomaly and the redirect are separately recoverable.
3. Annotate at passage granularity (a paragraph or a beat), not per word.
4. When unsure between two operations, pick the one whose *effect on the
   reader* is primary: OBJECT_HANDOFF is about where the reader looks,
   EVENTIFY_PROPERTY is about what happens instead of a static property.
5. Mark MOTIF_RETURN only when the element had a prior occurrence and the
   repetition changes work state (the repetition rule from
   `literary-strategy-controller`).

## Measures

**Operation n-grams.** For each trace, slide a window of n operations
(n = 2..4). Count identical sequences across the corpus; report the top
sequences by coverage (fraction of passages containing them).

**Transition matrix.** Count, for each ordered pair (A, B), how often B
follows A. Highlight pairs with high conditional probability that are not
mandated by genre.

**Opening/closure distributions.** Classify first and last operations of
each passage (SENSORY_ANOMALY opener vs. BOUNDED_EVIDENCE opener;
OPEN_END vs. explicit closure). A corpus that opens the same way and
closes the same way has a template-shaped rhythm even when words differ.

**Eventification rate.** EVENTIFY_PROPERTY operations per passage, or the
ratio of eventified properties to direct state labels (see
`narrator-intervention-abstraction-control`).

**Abstraction/evidence alternation.** The sequence of labels vs. bounded
evidence moves; a strict alternation (label, evidence, label, evidence)
is itself a rhythm worth reporting.

## Reporting shape

Report skeletons as:

```text
SKELETON-1 (coverage 14/20): SENSORY_ANOMALY -> ATTENTION_SHIFT ->
EVENTIFY_PROPERTY -> OPEN_END
  A: <span from text A>
  B: <span from text B>
```

Then the transition-matrix highlights and the distributions. Never append
a quality verdict without the work's needs on the table.
