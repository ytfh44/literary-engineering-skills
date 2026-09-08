---
name: knowledge-consequence-audit
description: Use when a cross-chapter audit must test whether new knowledge, an institutional record, or a noticed trace crosses a threshold and changes actionable state, permission, relationship cost, or an irreversible consequence; distinguish state-changing consequence from mere knowledge timing, and preserve intentional non-action or open lines.
license: Apache-2.0
---

# Knowledge Consequence Audit

## Use when

Use this skill for a bounded, read-only audit across chapters or chapter
transitions. The question is not merely who knows what, but whether a cue,
new knowledge, or institutional record **crosses a threshold** and changes any
of the following:

- what someone can now do, refuse, authorize, expose, hide, or observe;
- what a rule, institution, document, seal, receipt, list, or witness now
  permits or forbids;
- what a relationship now costs to preserve, deny, or renegotiate;
- whether a consequence has become irreversible, publicly visible, or harder
  to undo.

It is appropriate when a chapter introduces a report, archive entry, payment
trace, diagnosis, notice, filing, accusation, sealed object, or witnessed fact,
and later chapters appear to treat it as either changed or unchanged.

## Do not use when

Do not use this as a demand that every fact produce action, that every record
be opened, or that every setup be closed. Do not force a character to act just
because the reader can see a consequence. Do not use it for:

- a single-scene question whose only issue is who knows what when; use
  `knowledge-boundaries`;
- pure plot order, scene placement, or open commitments in a bounded window;
  use `narrative-architecture`;
- choosing the next move across many existing revisions; use
  `literary-strategy-controller`;
- a controlled A/B comparison of one local edit; use
  `counterfactual-revision`;
- explaining a stable motive, habit, or residual impulse; use
  `character-motive`;
- dream, omen, hallucination, or symbol unless the text gives it a concrete
  carrier that changes permission, record status, observation access, cost, or
  consequence;
- a line that explicitly makes non-action, refusal, ritual continuation, or
  suspended judgment its subject;
- a debt, promise, or institutional line that the text has visibly paid, or
  intentionally leaves open as part of its design.

A repeated record, sealing, filing, or return to ordinary life is not by itself
a defect. It may be the point: the world records something while people keep
living, or the record may be visible only to the reader. Test what changes,
what does not, and whether the non-change is represented as a choice, a cost,
an inability, or an intentionally open state.

## Core test

**Did the new knowledge or record cross a textual threshold, and can I name
the before/after difference in permission, observation status, relationship
cost, or consequence without inventing an action?**

A threshold is crossed only when the supplied evidence supports a state delta.
A fact becoming known is not sufficient. The audit must identify at least one
of these observable changes, or explicitly report that none is established:

1. **Action permission** — an act becomes available, unavailable, authorized,
   prohibited, or newly dangerous.
2. **Observation status** — a person or institution can now see, verify,
   classify, retrieve, witness, or deny something that was previously hidden,
   unverified, or inaccessible.
3. **Relationship cost** — contact, silence, loyalty, accusation, debt,
   concealment, or repair now carries a changed price for a named relation.
4. **Consequence status** — a result is now public, documented, bodily,
   legal, financial, social, or otherwise harder to reverse.

If the only difference is that the reader can connect two chapters, record
that as reader-side assembly, not as a character-side threshold crossing.

## Scope

Name the exact chapters, transition, or bounded chapter window before reading
for consequence. Keep four layers separate:

- **fact layer** — what the text gives as an event, object, statement, record,
  trace, or observable absence;
- **belief layer** — what a character, institution, narrator, or reader takes
  that fact to mean; mark suspicion and misbelief separately;
- **state layer** — what action, observation, permission, cost, or consequence
  is now available or blocked;
- **design layer** — whether repetition, silence, delay, sealing, or ordinary
  continuation is visibly paid, intentionally open, or not decided by the
  supplied evidence.

Do not turn these layers into one universal causal chain. A record may change
institutional permission without changing a character's belief. A character
may know the fact but lack access to the action. A reader may splice two
chapters into a pattern no participant can see. Preserve all three positions.

## Inputs: evidence ledger

For every candidate cue, fill the following fields. Use `unknown` rather than
silently completing a gap.

```text
cue:
  exact chapter / scene / paragraph anchor and the concrete carrier
  (heard line, object, mark, file, seal, receipt, witness, bodily trace, etc.)

fact:
  what is directly supported; quote or tightly paraphrase the anchor

knower / misbeliever:
  named person, institution, narrator, and/or reader
  fact / belief / suspicion / misbelief; acquisition point if supported

record:
  record type, holder, visibility, access route, verification status,
  seal/filing/erasure state, and whether its status is directly stated

before state:
  action permission, observation status, relationship cost, and consequence
  status immediately before the cue; use unknown for unsupported fields

after state:
  the same four fields after the cue or later anchor; name the smallest
  supported delta, or say no established delta

consequence anchor:
  later concrete event, refusal, payment, exposure, changed access, bodily
  effect, institutional response, or explicit non-response that bears on the
  proposed delta

unknowns:
  missing access, timing, authority, motive, record status, or later payment
  that prevents a stronger claim
```

A cue is not a threshold merely because it is emphatic, repeated, official,
or emotionally charged. “封存” is a record state; it becomes a consequence
only if the text shows who cannot retrieve it, who can rely on its existence,
or what cost follows from leaving it sealed.

## Workflow

1. **Bound the chapter window.** Name the transition and the audit question.
2. **Collect cues without interpreting them.** Mark the exact carrier and
   chapter anchor. Include records, absences, continued routine, and explicit
   refusals when they are part of the evidence.
3. **Map fact to holder.** Separate fact, belief, suspicion, and misbelief.
   This is where `knowledge-boundaries` may be needed; do not call an
   information asymmetry a consequence by itself.
4. **Snapshot the before state.** For each relevant person or institution,
   record action permissions and observation status first; then record
   relationship cost and consequence status. If the text does not establish
   one, write `unknown`.
5. **Test the carrier's threshold.** Ask whether the cue changes a rule,
   access route, witness position, social price, or reversibility. A record
   can cross a threshold for an institution while remaining inert for a
   character.
6. **Locate the after anchor.** Find the smallest later passage that shows a
   changed permission, observation, cost, consequence, or deliberate
   non-change. If none exists, report the threshold as unproven, not broken.
7. **Build the state ledger.** Use the return shape below. Keep parallel
   implementations separate: an interpersonal realization and an official
   filing may be two routes to one state, or they may conflict.
8. **Audit blocking points.** Name what prevents the implied transition:
   unavailable access, wrong belief, absent authority, sealed record, cost of
   disclosure, competing institution, timing gap, or simply no evidence.
9. **Check return flow and double implementation.** A later scene may return
   to an earlier cue and alter its force. Note whether the return adds a new
   permission/cost, merely repeats the same state, or creates a conflict
   between two implementations (for example, a receipt says “paid” while a
   person still demands payment). Do not resolve the conflict unless the text
   does.
10. **Run a reversible minimum A/B only if requested or needed to isolate the
    diagnosis.** Keep facts and wording fixed as far as possible. A: preserve
    the cue and remove the proposed threshold marker. B: preserve the cue and
    add the smallest concrete state anchor. Compare what permission,
    observation, cost, or consequence becomes legible; do not rewrite the
    chapter globally.
11. **Apply stop conditions.** Stop when the supplied evidence cannot
    distinguish a state delta from reader assembly, when the line is visibly
    paid or intentionally open, or when a proposed repair would require
    changing motive, knowledge timing, and event order at once. Return the
    unresolved alternatives and the missing anchor.

## State ledger and output fields

Use this compact chain for each cue or cue-cluster:

```text
fact
  -> belief / suspicion / misbelief
  -> available action or observation
  -> cost (relationship / institutional / bodily / financial / public)
  -> next state ledger
```

The `next state ledger` must name only what the next anchor supports:

```text
state id:
  holders:
  record status:
  action permission: available | blocked | altered | unknown
  observation status: visible | verifiable | hidden | inaccessible | unknown
  relationship cost: named change or unknown
  consequence: reversible | harder to reverse | irreversible | none shown | unknown
  anchor:
  confidence note: evidence / competing reading / gap
```

Also return, for each candidate transition:

- **blocking point** — the concrete missing or resisting link;
- **return flow** — whether a later chapter reactivates the earlier cue and
  changes its state;
- **double implementation conflict** — whether two carriers implement the
  same supposed transition differently, with both readings preserved;
- **reversible minimum A/B** — only if a local intervention was actually run;
- **stop condition reached** — the reason to stop rather than escalate into a
  global rewrite.

## Evidence contract

Every diagnosis must be executable by another reader using the supplied novel
passages:

1. Quote or locate the cue and consequence anchors by chapter and local
   position.
2. State whether each claim is **observed**, **supported inference**, or
   **unknown**.
3. Name the holder whose state changes. Do not substitute the reader's
   inference for a character's action permission.
4. Show `before` and `after` fields side by side. A claimed threshold without
   a state difference is only a hypothesis.
5. Distinguish a record's existence, visibility, authority, and use. “有记录”
   does not imply “有人能取用”或“制度会执行”。
6. Distinguish visible payment from reader assembly across chapters. If the
   reader connects a receipt in Chapter 2 to silence in Chapter 7 but no
   participant acts on that connection, label it `reader splice`.
7. Preserve competing readings when the same cue can support both a changed
   state and intentional non-change.
8. Do not upgrade repetition, ordinary routine, sealing, or non-action into a
   fault without a concrete lost permission, missing observation, unpaid cost,
   or contradiction in the text.

## Minimal pair

### Visible threshold versus reader splice

A:

> 第二章，档案员把“失踪”盖章归档。第七章，妹妹拿着复印件去领回
> 工资，窗口说：“系统里已经结案，不能再改。”

B:

> 第二章，档案员把“失踪”盖章归档。第七章，妹妹仍照常上班，读者把
> 归档和她的沉默拼在一起，但没有窗口、对话或行为显示她知道归档结果。

A gives a visible threshold: the record changes institutional permission and
creates a concrete cost. B gives a reader splice only. The audit must not
invent the sister's knowledge or call her continued routine a failed payoff.

### Repeated record, sealing, and ordinary life

A:

> 他把收据封进铁盒。下一章仍照常买菜；再下一章，债主拿同一编号的
> 收据来拒绝他的申辩。

The repeated sealing and routine are not automatically inert: the later use
shows an observation and relationship-cost change, while the seal limits the
holder's immediate action.

B:

> 他把收据封进铁盒。下一章仍照常买菜。小说明确说他决定不再追究，
> 因为继续过日子本身就是他的选择。

Here non-action is an explicit theme or state. Do not “repair” it by adding a
confrontation or making the record force action.

### One-variable A/B

A: `她看到医院记录，却仍能自由进入病房。`

B: `她看到医院记录；门禁随后拒绝了她。`

The changed variable is the concrete permission anchor, not the fact of seeing.
If later text never establishes who changed the door permission, report the
institutional transition as unknown rather than assigning motive.

## Counterexamples

- A catalogue, exposition paragraph, or bureaucratic list may display
  knowledge without changing action permission; that is pure knowledge
  presentation unless a later anchor establishes a state delta.
- A dream may forecast a later event, but forecast is not a record or
  permission change unless the waking text gives it a concrete institutional,
  relational, or observational carrier.
- A character may know a danger and choose not to act. If the text explicitly
  makes the refusal, ritual, or daily continuation the subject, preserve it.
- A debt or promise may be visibly paid: the demanded amount is transferred,
  the apology is accepted, the file is closed, or the work intentionally
  leaves it open. Do not reopen it merely to create a later consequence.
- A seal, archive, or official notation may be decorative world texture. It
  matters only to the extent that authority, access, witness, cost, or
  reversibility is anchored.
- Two chapters may intentionally require the reader to connect separate facts
  while characters remain unable or unwilling to connect them. Report the
  reader's assembly and the character's unchanged state separately.
- The same record may be implemented twice on purpose: once as an official
  fact and once as a private wound. Do not collapse the institutional and
  interpersonal paths into one transition.

## Rule strength

**Low — evidence-bound audit, not a closure rule.** The reliable operations
are cue collection, before/after state snapshots, authority and access checks,
consequence anchoring, blockage naming, and reversible local comparison. No
requirement says that knowledge must cause action, records must be opened,
foreshadowing must close, or non-action must be explained. A valid result may
be “no threshold established,” “reader splice only,” “two competing
implementations,” or “intentionally open.”

## Ownership boundaries

- `knowledge-boundaries` owns who knows what, when they know it, how belief or
  misbelief is formed, and reader/character information asymmetry. This skill
  imports that map only to test whether a state-changing threshold follows.
- `narrative-architecture` owns bounded temporal, causal, and obligation
  relations between anchors. This skill asks the narrower question of whether
  a knowledge or record cue changes permission, observation, cost, or
  consequence.
- `literary-strategy-controller` owns document-wide revision sequencing and
  marginal choice among multiple edits. This skill may supply one local audit
  ledger; it does not manage a whole revision campaign.
- `counterfactual-revision` owns controlled A/B interventions. This skill
  specifies the consequence hypothesis and smallest state anchor, then hands
  any actual edit comparison to that protocol.
- `character-motive` owns durable motive, habits, beliefs, role performance,
  and residual behavior. This skill must not explain a blocked transition by
  inventing a motive.

When boundaries overlap, report both layers: “she knows the filing” belongs to
`knowledge-boundaries`; “the filing blocks her claim at the counter” belongs
here. If the supplied evidence cannot separate them, preserve the overlap and
mark the state delta unknown.

## Return shape

Return the following, in order:

1. **Scope** — chapters, transition, and question.
2. **Cue table** — cue, fact, knower/misbeliever, record, and anchors.
3. **Before/after ledger** — action permission, observation status,
   relationship cost, consequence status, with unknowns explicit.
4. **State chain** — `fact -> belief/suspicion -> available action -> cost ->
   next state ledger`.
5. **Threshold verdict** — crossed, not established, reader splice only,
   intentionally unchanged/open, or competing readings.
6. **Blocking points** — access, authority, belief, cost, timing, or missing
   anchor.
7. **Return flow / double implementation conflict** — later reactivation and
   unresolved collisions.
8. **Reversible minimum A/B** — only when run; state the one changed variable
   and observed consequence.
9. **Stop condition** — why the audit stops without forcing closure or action.
10. **Read next** — the adjacent skill that owns the remaining question.

## Read next

- [knowledge-boundaries](../knowledge-boundaries/SKILL.md) for fact holders,
  knowledge timing, suspicion, and misbelief.
- [narrative-architecture](../narrative-architecture/SKILL.md) for anchor
  relations, open commitments, and bounded cross-scene structure.
- [counterfactual-revision](../counterfactual-revision/SKILL.md) for a
  one-variable A/B intervention.
- [literary-strategy-controller](../literary-strategy-controller/SKILL.md)
  when several local audits or edits must be sequenced across a work.
- [character-motive](../character-motive/SKILL.md) when the unresolved issue is
  why a character chooses, refuses, or repeats rather than what the new record
  changes.
