---
name: property-and-adjective-engineering
description: Use when adjectives feel decorative, piled up, or wrong in a way that is hard to name; use when a property is assigned by an adjective (or adverb, or attributive noun) and the question is what job the property does; classify before deleting or replacing — discriminative, state-bearing, evaluative, or affective adjectives fail and pay differently.
license: Apache-2.0
---

# Property and Adjective Engineering

## Use when

A modifier assigns a property to an object. The engineering question is what
the property is **for** in this sentence — before any decision to keep,
delete, or replace it.

## Do not use when

Do not treat adjectives as excess weight to be removed. "删掉后事实没变"
is not a verdict, because several adjective functions do not add facts by
design. Do not run adjective reduction as a batch pass over a passage.

## Core test

**Classify the adjective's function first; then ask what deleting it
loses.**

If the loss is reference, the adjective was doing identification. If the
loss is state, it was reporting the world. If the loss is judgment, it was
evaluation. If the loss is atmosphere, it was affect. The four losses are
not the same loss, and only one of them is a fact-loss.

## Function classes

1. **Discriminative** — narrows the referent set: 红门, 左边那间小屋,
   高个子男人. Deleting it may break reference: which door, which man?
2. **State-bearing** — reports a current condition: 湿衣服, 冷水, 破窗.
   Deleting it removes a fact about the world.
3. **Evaluative** — presses a narrator's or character's judgment into a
   property: 可怜的人, 讨厌的声音, 荒唐的决定. Deleting it removes the
   judge, not the object.
4. **Affective** — changes the emotional field without adding much objective
   fact: 阴冷的房间, 惨白的灯, 懒洋洋的下午. Deleting it removes a
   temperature of perception.

## Workflow

1. Mark every modifier in the span.
2. Classify each by function class; when a modifier is ambiguous, test both
   classes.
3. For each, ask: **who needs this property, for what decision or
   inference?**
4. Test deletion: what exactly disappears — referent, fact, judgment, or
   affect?
5. Check redundancy: is the same loss already carried by another mechanism
   (event, verb, camera, dialogue)?
6. Keep, trim, or replace by what the loss is — not by adjective count.

## Minimal pair

> 他走进阴冷的房间。
>
> 他走进房间，暖气片是凉的。

The first is affective: the room's cold is a felt atmosphere. The second
eventifies the same property through a state-bearing fact. Neither is
better by rule; the question is whether the scene needs the room's cold as
a perception (affective) or as a checkable condition (state).

> 那个高个子男人把钥匙放回桌上。
>
> 那个男人把钥匙放回桌上。

If "高个子" separates him from the other men in the room, deletion breaks
reference. If no other man exists, the discriminative load is zero and the
adjective is decoration — trimmed for that reason, not because adjectives
are bad.

## Counterexamples

- 他很累 may be exact after a long action sequence; adding drooping eyelids
  dilutes it (state-bearing label beats a cliché inventory of evidence).
- A deliberately judgmental narrator ("这个荒唐的决定") — the evaluative
  load is the narrator's position; do not neutralize it.
- An affective adjective can be load-bearing when it is the only carrier of
  the scene's temperature ("惨白的灯" in a hospital waiting room).

## Rule strength

**Functional tests.** No adjective blacklist, no ratio targets, no
"concrete beats abstract" rule. The reliable operation is classification
plus deletion-loss accounting. Classifiers may disagree at the margins
(evaluative vs. affective); when they do, test both losses and pick the one
the scene actually pays.

## Read next

- [function-class-tests.md](references/function-class-tests.md) for the
  per-class test battery and the redundancy check.

## Return shape

Report per modifier: **class -> who needs it -> deletion loss -> keep/trim/
replace reason**. If a replacement is proposed, state which class the
replacement belongs to and what it adds.
