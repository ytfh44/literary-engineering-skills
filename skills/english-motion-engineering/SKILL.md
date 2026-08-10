---
name: english-motion-engineering
description: Use when manner, path, particles, prepositions, reveal, or field-of-view motion should be packed tightly into a clause. Especially useful for English, but designed to export the manner/path decomposition to any language without forcing English phrasal-verb syntax.
license: Apache-2.0
---

# English-Derived Motion Engineering

## Use when

English often makes **manner + path** cheap: the verb can carry how something moves while a particle or preposition carries where it goes. Treat that as a reusable diagnostic, not an English-only trick.

## Do not use when

Do not replace every neutral motion verb with a manner verb. Do not calque English particles into languages that naturally put path in the main verb or separate manner.

## Core test

**If manner and path both matter, ask where each can live most cheaply. If one does not matter, do not encode it.**

## Workflow

1. Split the event into **manner**, **path**, **source/goal**, and **result**.
2. Decide which component is narratively load-bearing.
3. In English, test a manner-rich verb plus a light path carrier.
4. Check whether the clause still reads as the character's/narrator's register rather than a thesaurus choice.
5. For reveals, distinguish literal object motion from the observer's field-of-view change.
6. If writing another language, repack the same decomposition with its native verbs and adjuncts. See **Transfer**.

## Working operations

- **pack manner** — `stumble`, `creep`, `drift`, `lunge`, `shuffle` when manner predicts something;
- **satellite path** — `in`, `out`, `up`, `down`, `across`, `past`, `through` when natural;
- **field entry** — `come into view`, `swing into view`, `loom`, `emerge`;
- **gaze motion** — `glance up`, `peer into`, `look past`;
- **unpack** — separate manner from path when a packed verb would overcommit.

## Minimal pair

> He went out of the room unsteadily.

> He stumbled out of the room.

The second is cheaper only if unstable gait matters. If “out of the room” is the sole event, `left the room` may be better than either.

## Counterexamples

- `walked` can be exact where `stalked`, `strode`, or `ambled` would invent attitude.
- `The ridge swung into view` is useful only when the apparent motion follows observer movement; otherwise it may falsify the scene.

## Transfer

The reusable object is the decomposition, not the phrasal verb. Reduce `stumbled out` to two coordinates: unstable manner + outward path. A French sentence may put path in `sortir` and manner in `en trébuchant`; Chinese may combine a manner/action verb with趋向; Japanese may spread the same event across a predicate chain. If another language needs more machinery to mimic English packing than to state the event naturally, unpack it. Compression is local to a grammar.

**Transfer the operation, not the costume.**

## Read next

- [manner-verbs.md](references/manner-verbs.md) for deciding when manner belongs in the verb.
- [satellites-and-path.md](references/satellites-and-path.md) for path packaging.
- [entering-the-field-of-view.md](references/entering-the-field-of-view.md) for apparent motion and reveal.

## Return shape

Return **manner -> path -> English packaging or target-language packaging -> overcommitment risk**. Do not praise a packed clause merely for being shorter.
