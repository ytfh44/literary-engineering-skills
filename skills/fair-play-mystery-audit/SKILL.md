---
name: fair-play-mystery-audit
description: Use when a mystery's solution feels unearned or unfair — the reveal rests on evidence the text never planted, a clue appears with no traceable source, a character knows what they had no access to, a misdirection was never viable before the reveal, or an ambiguity is declared resolved. 症状：读者会觉得作者作弊、这条线索凭空出现、这个真相没法从前面推出来、我想让读者误判但没有可成立的假说、结尾两种读法却宣布了一种。
license: Apache-2.0
---

# Fair-Play Mystery Audit

## Use when

The solution has been announced, or is about to be, and the doubt is not
"is it surprising?" but "is it earned?" Typical symptoms:

- 读者会觉得作者作弊 — the reveal works only because the text withheld the means.
- 这条线索凭空出现 — a load-bearing fact has no earlier trace.
- 这个真相没法从前面推出来 — the announced answer is not derivable from the page.
- 角色知道了他不可能知道的事 — the claim has no access path, or no channel the text licensed.
- 我想让读者误判，但那个假说在当时根本站不住 — the misdirection was dead on arrival.
- 结尾两种读法都活着，我却宣布了一种 — ambiguity is closed by authorial assertion.
- 有个假说没被揭穿，读者却以为它已经死了 — an open reading is treated as debunked.

## Do not use when

- The question is only who knows what: use `knowledge-boundaries`.
- The question is scene order, reveal timing, or obligation state: use
  `narrative-architecture` or `macro-narrative-architecture`. This skill
  judges the solution's legitimacy, not its placement.
- The question is dialogue register or voice: use `dialogue-voice`.
- The task is a one-variable A/B edit: use `counterfactual-revision`.
- The work deliberately refuses a solution (open weird tale, gothic fragment):
  fairness is not its contract.

Do not demand that every clue be explicit. A fair solution can rest on a
trace the text never labels as a clue. Do not turn this into a quota or a
demand that the reader guess the exact answer.

## Core test

**Cover the reveal. Could a reader, using only what the page put there before
the reveal, have built this answer — and can every load-bearing claim in it be
traced to a source the text licensed?**

Both halves are required: derivability and provenance. A solution can be
derivable but sourceless, or sourced but not derivable.

## Where it bites

| Bridge | What the check is about |
| --- | --- |
| 来源段 — a clue, testimony, document, or memory enters | trace, license, access |
| 误导段 — the false lead is set up | viability at the time, surface source |
| 揭示段 — the answer is announced | derivability from prior evidence |
| 收束段 — the final state is declared | ambiguity, open hypotheses |

For each bridge, ask what it had to put on the page for the later claim to be
legitimate — not whether the bridge is well written.

## Checks

### 1. Derivable before the reveal

Which prior beats entail the announced answer? If the only support is the
reveal itself, the solution is circular.

Repairs: move one supporting beat earlier; make the inferential chain explicit
once; delete a claim only the reveal can support; reduce the answer to the part
the text does support.

### 2. Legitimate source

Does every load-bearing claim have (a) a trace in the text, (b) a channel the
text's rules allow, and (c) access in the state where it is used?

A lie, forgery, or false memory is not automatically a source violation: the
content can be false while the channel is legitimate. "Someone knows it" is
not a channel; the text must show how the information reached them.

Repairs: add a short trace scene; give an access route (saw it, heard it from a
licensed source, inferred from an object); reclassify the claim as a surface
source rather than a true one; if no channel exists, remove the claim.

### 3. Viable misdirection

At the moment the reader is meant to believe the false lead, was it possible
under the then-available evidence? And does the final truth contradict it?

Repairs: add the evidence that made the false lead plausible then; give the
false lead a real source; if it was already excluded, move it earlier or change
what the reader knew at that point.

### 4. Bounded ambiguity

If two readings both survive the final evidence, is either declared true? If
yes, the text is closing an ambiguity it has not closed.

Repairs: keep both readings open and do not declare; remove the support for one
reading before the declaration; make the declaration a character's claim rather
than the text's verdict.

### 5. Open hypotheses stay open

Is an unresolved hypothesis treated as "already debunked"? A hypothesis not
eliminated by evidence is not a dead lead.

Repairs: mark it open; give the character who holds it a reason; do not let the
narration say "the theory was disproved" without the disproof on the page.

### 6. Second source under a single discredited source

If the only source for a claim is discredited or denied access, does the claim
survive? If not, the solution depends on a single point of failure.

Repairs: add an independent second source; or make the claim conditional on the
discredited source and let the solution lose it honestly.

## Operations

- **plant** — put the trace in an earlier bridge.
- **license** — establish the channel by rule or custom before using it.
- **grant access** — make the character's route visible at the moment of use.
- **surface** — keep a false source real while the final truth contradicts it.
- **withhold declaration** — leave the ambiguity to the reader.
- **drop** — remove a claim the text cannot support.

## Minimal pair

Baseline:
> 他烧了信。

Candidate:
> 他烧了信。三章前，只有她看见了落款。

The comparison asks whether the second sentence supplies a trace and an access
route — not whether it makes the scene better. If it only repeats that the
letter existed, fairness has not changed.

## Counterexamples

- A gothic or weird tale whose knowledge is deliberately sourceless; fairness is not its contract.
- An unreliable narrator whose lie has a legitimate channel: the content is false, the provenance valid.
- A clue the text never labels but makes inferable; explicit labeling is not required.
- A misdirection built on a real document; the source can be legitimate while the interpretation is wrong.
- A deliberate open ending that refuses to declare either reading.
- A solution the reader could not guess but could verify in retrospect; guessing is not the bar.

## Rule strength

**Witness-based audit, medium-high.** It checks trace, license, access, and
whether the final declaration matches what survived. It does not prescribe clue
counts, does not ban coincidence, and does not require the reader to guess. The
verdict can be "fair but unguessable" or "guessable but unfair".

## Return shape

Return, for each announced claim:

1. claim;
2. supporting beats;
3. source: trace / license / access, each present, missing, or unknown;
4. misdirection: viable then? contradicted now? source real?;
5. ambiguity: closed or open;
6. one concrete repair, or "no repair needed".

## Read next

- [Knowledge boundaries](../knowledge-boundaries/SKILL.md)
- [Narrative architecture](../narrative-architecture/SKILL.md)
- [Counterfactual revision](../counterfactual-revision/SKILL.md)
