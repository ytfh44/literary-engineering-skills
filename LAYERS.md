# LAYERS — the v2 taxonomy

This pack organizes literary mechanisms by **how deep in the language they
load**: the shallower the carrier, the more reliable the audit rule; the
deeper, the more the rule degrades into an analysis frame. This file is the
canonical map. The four layers are conceptual — every skill still lives flat
under `skills/` so the discovery contract (`npx skills add
<owner>/literary-engineering-skills`) keeps working.

**One line for the whole pack:** a literary effect is produced by a specific
language layer; engineering asks *which layer carries this effect now, and
why that layer*.

## Rule strength gradient

```text
relation layer        strong audit rules      frequency -> alarm, concordance -> inspection, deletion -> counterfactual
property layer        functional tests        classify the adjective's job before touching it
naming layer          framing comparison      who names, what identity is activated, what changes
figurative layer      role/domain tests       audit first; "no metaphor needed" is a verdict
verb/event layer      event decomposition     predicate commitments, role assignment
adverb/particle layer minimal-pair laboratory  change one particle, read the reader's stance
```

Downward: fewer blacklists, fewer universal preferences, fewer automatic
rewrites, more counterexamples, more language-specific reference, more
contextual comparison. Shallow linguistic claims produce silly rules at
depth; the gradient is the guard against that.

## I. Language carriers

1. `relation-scaffolding` — explicit connectors, relational constructions,
   relation content words. The layer's question: **must this edge be stated?**
   Distinguishes event-link overmarking (beginner-human: 然后…然后…) from
   concept-link overmarking (first-generation AI: 并非A而是B, 不仅而且,
   因此可以看出 — expository relation-marking leaking into fiction).
2. `property-and-adjective-engineering` — adjectives as property assignment:
   discriminative, state-bearing, evaluative, affective. Never "delete
   adjectives"; classify the job, then test the loss.
3. `naming-and-address-engineering` — the same referent reclassified by each
   naming act (狗/野狗/那畜生/阿黄). Who names, what they know, which identity
   is activated.
4. `metaphor-audit` — audit before generation. Ten utility axes; a metaphor
   that only repeats "dark/cold/sad" spends too much. "No metaphor here" is a
   complete verdict.
5. `predicate-licensing-and-personification` — a noun temporarily licensed to
   carry a predicate its class usually cannot (风追着他). Nominal
   reclassification + predicate licensing; reader recovery cost is the test.
6. `verb-event-engineering` — the predicate cuts the event into structure:
   agency, patienthood, causation, control, intention, duration, path,
   result, responsibility, experiencer. "Strong verb" upgrades are a
   dangerous rule; decompose before replacing.
7. `chinese-derived-event-geometry` — source tradition: serial action,
   direction, result, coercion, role reassignment.
8. `english-derived-motion-packaging` — source tradition: manner + path
   packing in the clause.
9. `french-derived-motion-packaging` — source tradition: path/manner/
   appearance hierarchy.
10. `adverb-particle-viewpoint-engineering` — particles, adverbs, clitics,
    aspect markers: they do not change the event, they change how the event
    is understood, presupposed, attended to, and located (又/才/也/竟/还,
    ふと/ちらり/じっと). Minimal-pair laboratory; lowest rule strength.
    Carries the Japanese viewpoint tradition as
    `references/japanese-viewpoint/`.

Language-named skills are **source traditions, not territories**. Each one
exposes a mechanism where it is cheap to see, then abstracts it for transfer
and records what does not survive.

## II. Composition / discourse

 1. `camera-attention-engineering` — reader access: reveal, occlusion,
    attention handoff, scale, spatial continuity — and first-class
    discontinuity (jump, misbind, retroactive anchor, false continuity,
    parallel field, withheld anchor).
 2. `sentence-pressure` — two tracks: semantic pressure (when information
    arrives, withholds, revises, resolves) and kinetic/prosodic pressure
    (how the sentence moves in the mouth, ear, and working memory).
 3. `dialogue-voice` — a character voice is a cross-layer profile: preferred
    names, address terms, hedges, particles, sentence endings, relation
    markers, habitual metaphors, verb commitment, ellipsis, repair.
 4. `narrator-intervention-abstraction-control` — how directly the narrator
    names states, summarizes, concludes, and settles meaning; the evidence
    policy that lets inference stay bounded. Absorbs the former anti-ai-prose
    register work and sensory-specificity evidence work.

## III. Character / world

 1. `character-motive` — partially coherent generation: durable motives plus
    habits, physiology, scripts, beliefs, misbeliefs, role performance,
    imitation, unresolved conflicts, path dependence, context, and a residual
    that is not explained by default. Labels are observations, not
    parameters.
 2. `knowledge-boundaries` — what each character knows, when they learned it,
    what they misbelieve; asymmetry between character, narrator, and reader
    (dramatic irony as a managed resource).
 3. `social-naming-relation-maps` — the global map: naming consistency across
    the work, relation arcs encoded in address terms (李叔 → 老李 → 李建国).
    Local act in #3; global structure here.

## IV. Method / eval

 1. `counterfactual-revision` — the shared experiment protocol: one variable,
    frozen background, A/B, verdict. Every layer has its canonical
    intervention (delete 因此 / delete 阴冷 / 父亲→那个男人 / 杀→毙 / 又→才).
 2. `literary-evals` — trigger batteries, minimal pairs, counterexamples,
    adversarial cases, transfer cases, regression for all 22 skills.
 3. `corpus-convergence-audit` — operation-level convergence: different
    words, same operation skeleton. Operation n-grams, transition matrix,
    opening/closure strategy distribution, eventification rate.
 4. `literary-style-router` — two-stage diagnosis: which layer, then which
    mechanism. Symptoms are search prompts, not diagnoses.
 5. `literary-strategy-controller` — state-aware strategy selection: track
    the document state, compute marginal utility, adapt. Never randomize;
    every local optimum repeated six times is a house style.

## Shared operation vocabulary

Used by `corpus-convergence-audit` and `literary-strategy-controller` to
annotate what a revision did, independent of surface words:

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

Repetition rule: **repetition must change the work state.** The same
operation twice in a row may be a motif; the same operation six times in a
row is a template.

## Anti-patterns (rejected pedagogy)

No verb-upgrade drills, no add-a-metaphor-by-rule, no delete-all-adjectives,
no delete-all-然后, no "show, don't tell" as a law, no five-senses-per-
paragraph, no mechanical long-short alternation, no contrast-for-depth.
Local form is never a quality proxy. Ask what the effect needs first, then
which carrier is cheapest, then whether the surface should change at all.

## Dissolution ledger

- `anti-ai-prose` → relation-scaffolding (concept-link theory) +
  narrator-intervention-abstraction-control (register, explanation,
  false depth).
- `sensory-specificity` → narrator-intervention-abstraction-control
  (evidence policy).
- `japanese-viewpoint-engineering` → adverb-particle-viewpoint-engineering
  (references/japanese-viewpoint/).
