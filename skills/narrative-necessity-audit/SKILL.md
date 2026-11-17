---
name: narrative-necessity-audit
description: Use when the narration or explanation feels gratuitous or incoherent — an anomaly is left unexplained, an explanation survives after any one mechanism is deleted, the explanation smuggles in the thing it explains, the raw events already determine the whole mechanism, or a passage adds nothing over direct telling. 症状：这个机关解释不通/解释是硬凑的、删掉一个设定也照样成立、直接讲事件也一样、读者不知道为什么要这么讲。
license: Apache-2.0
---

# Narrative Necessity Audit

## Use when

The doubt is "why is this here?" rather than "is this true?" Typical symptoms:

- 这个机关解释不通 — an anomaly has no explanation, or the explanation never reaches it.
- 解释是硬凑的 — mechanisms are piled up until the anomaly disappears.
- 删掉一个设定也照样成立 — the explanation has redundant parts; delete one and it still works.
- 解释偷用结论 — the background used to explain already contains the anomaly or its consequence.
- 直接讲事件也一样 — the narration adds nothing the raw events could not carry.
- 读者不知道为什么要这么讲 — the telling (who narrates, in what order, with what withheld) is decorative.

## Do not use when

- The question is scene order, reveal timing, or obligation state: use
  `narrative-architecture` or `macro-narrative-architecture`.
- The question is rhythm, clause load, or information timing inside a sentence:
  use `sentence-pressure`.
- The task is a one-variable A/B edit: use `counterfactual-revision`.
- The question is what a character knows: use `knowledge-boundaries`.
- The work is a lyric essay, a mood piece, or a deliberate fragment where
  explanation is not the contract: necessity is not the criterion.

Do not demand that every anomaly be explained. Deliberate open weirdness,
ritual repetition, and oral redundancy can be the point. Do not turn this into
a quota or a rule that all narration must be load-bearing.

## Core test

**Strip the narration to raw events. What still needs explaining, and what does
the telling add that the events cannot?**

Explanation: does an anomaly have a minimal set of mechanisms that jointly
reach it? Necessity: does the telling do work the events alone could not? A story
can explain everything and still be gratuitous; a story can be spare and still
necessary.

## Where it bites

| Bridge | What the check is about |
| --- | --- |
| 异常段 — something breaks the expected field | is it explained, or deliberately open? |
| 解释段 — a mechanism is offered | minimality, background, redundancy |
| 叙述配置段 — who narrates, order, reveal, framing | what the configuration adds |
| 转折段 — a turn changes what the reader can infer | configuration evidence vs event evidence |

## Checks

### 1. Minimal joint explanation

Which mechanisms together explain the anomaly, and does removing any one of
them break the explanation? If it survives with one removed, that one is not
load-bearing.

Repairs: delete the redundant mechanism; merge two mechanisms into one; or
accept that the anomaly needs no mechanism and mark it deliberate.

### 2. Background without the anomaly

Does the background used to explain the anomaly already contain the anomaly or
its consequence? The explanation must be supported by evidence with the anomaly
removed.

Repairs: rebuild the background from the evidence minus the abnormal fact; if it
cannot support the mechanism, the mechanism was smuggled in.

### 3. Redundancy when the mechanism is already proven

If the remaining evidence already proves the mechanism, is the explanation still
doing work? Then the mechanism was never the thing needing explanation.

Repairs: drop the explanation and let the proven mechanism stand; or move the
explanation to the part that is genuinely open.

### 4. Configuration evidence excludes a whole alternative

Does the configuration evidence — a document, a lie, an order, a viewpoint, a
withheld scene — rule out at least one whole-mechanism alternative that the
event facts alone would leave open?

Repairs: add one configuration fact that eliminates a complete alternative; or,
if no alternative is eliminated, remove the apparatus and tell the events
directly.

### 5. Event facts must not settle everything

If the raw events alone determine the whole mechanism, what is the telling for?
Then the discourse is decorative.

Repairs: change who narrates, what is withheld, or the order so that the telling
carries information the events do not; or accept that this is a plain narrative
and stop pretending it is a puzzle.

### 6. Openness is not a hole

Is the event layer simply open? That is the default condition, not a defect. Do
not invent an explanation to fill it, and do not treat an open mechanism as a
missing piece.

Repairs: none; record it as "open by design" or "no explanation required". If
the text promises a solution, that promise is a fairness question — see
`fair-play-mystery-audit`.

## Operations

- **name the anomaly** — make it one checkable fact.
- **add a mechanism** — only if a check shows a missing link.
- **delete a mechanism** — remove redundancy.
- **weaken the background** — stop smuggling the anomaly.
- **move configuration evidence** — make the telling carry a fact.
- **reconfigure the telling** — change who narrates, the order, or the reveal.
- **tell it directly** — drop the apparatus when it does no work.

## Minimal pair

Baseline:
> 门从里面锁着。

Candidate:
> 门从里面锁着；唯一的备用钥匙在第一章的抽屉里，只有管家知道。

The comparison asks whether the added mechanism is load-bearing — does the
anomaly survive without it, and can the background support it without already
containing the anomaly? It does not ask whether the added sentence is more
interesting.

## Counterexamples

- A horror scene whose unexplained noise is the effect; the absence of explanation is the point.
- A folk tale whose repetition is ritual, not filler.
- A police procedural where the event facts are the subject and the telling adds no puzzle.
- A narrator whose ignorance or unreliability is the subject; the withheld explanation is the mechanism.
- A deliberately open ending that does not promise a solution.
- A mechanism already proven by the events; the explanation is redundant, and that flatness can be intended.

## Rule strength

**Witness-based audit, medium.** It checks minimality, background support,
configuration exclusion, and what the telling adds. It does not demand
explanation, does not ban redundancy, and does not convert "open" into
"defect". The verdict can be "no explanation needed" or "the telling is the
explanation".

## Return shape

Return, for each anomaly and each major narration choice:

1. anomaly or choice;
2. mechanism set, with the delete-one result;
3. background used, and whether it contains the anomaly;
4. configuration evidence, and which whole alternative it excludes;
5. what the telling adds that the events cannot;
6. one concrete repair, or "no repair needed / deliberate".

## Read next

- [Narrative architecture](../narrative-architecture/SKILL.md)
- [Macro narrative architecture](../macro-narrative-architecture/SKILL.md)
- [Counterfactual revision](../counterfactual-revision/SKILL.md)
- [Fair-play mystery audit](../fair-play-mystery-audit/SKILL.md)
