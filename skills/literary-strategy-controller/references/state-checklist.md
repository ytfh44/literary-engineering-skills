# State Checklist

## Fields and update rules

| Field | Definition | Update when |
| --- | --- | --- |
| relation density | explicit edges per unit text | after every DELETE_RELATION or added edge |
| direct naming density | states/meanings named outright per unit | after each label kept, added, or removed |
| eventification density | properties turned into event consequences | after each EVENTIFY_PROPERTY |
| explicit emotion density | direct emotion labels | after each label kept or replaced |
| metaphor function distribution | what metaphors do (voice/motif/semantic/comic), by count per function | after each metaphor kept, added, or removed |
| narrator intervention level | scene / near-scene / summary / verdict | when the narration moves on the dial |
| attention continuity | continuous / hard-cut / withheld-anchor | after each camera operation |
| hard-cut frequency | deliberate discontinuities per unit | after each cut |
| closure mode | open / settled | at each scene end |
| recent operation history | last N operations in order | after every operation |

Update the history immediately after each applied operation; recompute
densities when a new operation would push a density past what the document
has already established as its pattern.

## Reading the state

- **High density is a fact, not a verdict.** The document may be a litany
  by design. The controller reports; the design decides.
- **Density comparisons are within-document.** 0.3 relations per sentence
  means nothing alone; it means "the document has been using explicit
  edges steadily" only against its own baseline.
- **The history list is the decision input.** Saturation is judged on the
  recent window, not the whole document: the same operation in a new
  register or new context is not automatically saturated.

## The veto log

Keep a running log of vetoed or redirected operations:

```text
op: EVENTIFY_PROPERTY at §3        vetoed: saturation (5 in 700 chars)
op: DELETE_RELATION at §7          redirected: edge was load-bearing, kept
op: BOUNDED_EVIDENCE at §9         chosen: contrast +1, evidence run broken
```

The veto log is the controller's output of record. A revision session with
an empty veto log has not actually used state information.
