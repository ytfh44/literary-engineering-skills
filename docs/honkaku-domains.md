# Honkaku Domains: Models, Meanings, and the Collapse Condition

This note records the formal reading behind `fair-play-mystery-audit` and
`narrative-necessity-audit`. It is not loaded by either skill, not part of the
skill catalog, and not a prerequisite for using them. Its only job is to keep
the theory inspectable while the skills stay operational.

The examples are original Chinese fragments, written to instantiate one
domain each; they are illustrations, not verdicts about any real work.

## Notation

Fix disjoint finite atom sets `P_H` (story-world facts) and `P_G` (discourse
configuration). Let `Ω = H × G` be the joint interpretation space, and let
`ω*` be the designated true interpretation. For a text with evidence

- `E_s ⊆ L_H` (event evidence),
- `E_f ⊆ L_G` (configuration evidence),
- `R_0` (public interpretation rules),
- `C` (the propositions declared true), `C_nar ⊆ C ∩ L_G` (the core
  narrative-mechanism propositions), `γ = ∧C_nar`,
- `A` (the pre-designated anomalies),

write `Ω_s = ⟦R_0 ∪ E_s⟧`, `Ω_f = ⟦E_f⟧`, `Ω* = Ω_s ∩ Ω_f`, and
`K_a = Cyl_a(⟦E_s ∪ E_f⟧)` for `a ∈ A` (the evidence with `a` projected out).
A minimal joint explanation for `a` is a non-empty `Θ ⊆ C_nar` and a background
`β ∈ L_{-a}` such that `K_a ⊆ ⟦β⟧`, `R_0 ∪ {β, θ_Θ}` is satisfiable, entails
`a`, and stops entailing `a` when any one member of `Θ` is removed.

The four postulates:

- **F** (public justification): `ω* ∈ Ω*` and `Ω* ⊆ ⟦γ⟧`.
- **P** (source provenance): every claim in the viable explanation has a
  traceable, licensed, accessible source; a triggered misdirection had a
  surface-viable source at the time.
- **R** (reverse joint explanation): every anomaly has a minimal joint
  explanation.
- **M** (whole-form necessity): `Ω_s ⊄ ⟦γ⟧` — event evidence alone does not
  determine the mechanism.

For this note, **the frame condition is `ω* ∈ Ω*`**: the declared truth is
itself among the states the public evidence allows. It is a structural
assumption of the model, not a fifth postulate. Under this frame, F is
equivalent to its justification half, written **F′**: `Ω* ⊆ ⟦γ⟧`. The note
says explicitly when a result depends on this frame.

## Single negation: four inhabited domains

Each of the four single negations is satisfiable, and each has a witness with
non-empty `Ω*`. The models below use `P_H = {a}`, `P_G = {m, f}`,
`C = C_nar = {m}`, `A = {a}`, and all sources legitimate unless stated.

| Domain | `R_0` | `E_s` | `E_f` | `Ω*` | fails |
| --- | --- | --- | --- | --- | --- |
| ¬F′ | `m → a` | `{a}` | `{f}` | 2 | F′ |
| ¬P | `f → m, m → a` | `{a}` | `{f}` | 1 | P |
| ¬R | `f → m` | `{a}` | `{f}` | 1 | R |
| ¬M | `a → m, f → m, m → a` | `{a}` | `{f}` | 1 | M |

In each row the other three postulates hold.

### ¬F′ — the unearned truth

The evidence leaves more than one mechanism standing, and the text declares one
of them true. Meaning: the solution is announced, not established. The reader
can see the answer working only because the text says so.

> 他死在书房。侦探宣布凶手是管家，理由是"只有管家有动机"——而全文没有一处证据指向管家。

### ¬P — the sourceless claim

The text declares a mechanism whose supporting claim has no trace, no licensed
channel, or no access path. Meaning: information arrives without a provenance;
a lie is not automatically a violation, but "someone knows" is not a channel.

> 她收到一封信，没有邮戳，没有笔迹，也没有人看见投递；信里写着只有死者和凶手知道的事。

### ¬R — the unexplained anomaly

A pre-designated anomaly has no minimal joint explanation, or the explanation
survives the deletion of every one of its parts. Meaning: the trick is named,
not explained; the anomaly is resolved by assertion.

> 门从里面锁着。答案说"是一种机关"，却没有一处交代机关如何工作。

### ¬M — the over-determined story

Event evidence alone already determines the whole mechanism. Meaning: the
telling is decoration; the reader has nothing to infer, because the facts
already say everything.

> 第一章就把凶手、动机、手法全部写明。剩下的九章反复回忆、插叙、推迟揭示，但读者需要的信息已在第一页。

## The collapse: ¬F′ ∧ ¬M

Under the frame `ω* ∈ Ω*`, the pair is unsatisfiable.

**Proof.** ¬M gives `Ω_s ⊆ ⟦γ⟧`. Since `Ω* = Ω_s ∩ Ω_f`, also
`Ω* ⊆ ⟦γ⟧`, which is F′. Hence ¬F′ and ¬M cannot both hold. ∎

Meaning: a solution cannot be simultaneously *unjustified* and *already
determined by the events*. If the facts already fix the mechanism, the
declaration is redundant; if the declaration is not justified, the facts did
not fix it. Requiring both removes every coherent interpretation.

> 开头三页写死了全部事件与凶手；结尾又让侦探宣布一个从未被证据支持的动机。读者既不需要读，也无法相信。

**Without the frame, the pair is satisfiable.** Take
`R_0 = {a → f, a → m, m → a}`, `E_s = {a}`, `E_f = {¬f}`,
`C = C_nar = {m}`. Then `Ω_s = {(1,1,1)}`, `Ω* = ∅`, so F fails on its
first conjunct while `Ω_s ⊆ ⟦m⟧` makes M fail. This shows why the collapse
statement must name the frame: "the truth is evidence-compatible" is part of the
model, not of the negated F.

## Other double negations: inhabited, not collapsed

The claim "any two negations collapse" is false. Under the same frame, every
pair except `{¬F′, ¬M}` has a model with `Ω* ≠ ∅`:

| Domain | model sketch | `Ω*` | also fails |
| --- | --- | --- | --- |
| ¬F′ ∧ ¬P | the ¬F′ model, with `Trace` false | 2 | F′ , P |
| ¬F′ ∧ ¬R | `R_0 = ∅`, `E_s = {a}`, `E_f = {f}` | 2 | F′ , R |
| ¬P ∧ ¬R | the ¬R model, with `Trace` false | 1 | P, R |
| ¬P ∧ ¬M | `R_0 = {a → m}`, `Trace` false | 1 | P, M, R |
| ¬R ∧ ¬M | `R_0 = {a → m}` | 1 | R, M |

Each row has `ω* ∈ Ω*`, so it is a genuine double-negation domain, not a
degenerate one. A row may fail a third postulate; that does not collapse it.

Literal meanings:

- **¬F′ ∧ ¬P** — an unjustified truth with no legitimate source: legend or
  hearsay promoted to solution.
  > 小镇传说湖底有钟声。没有人听见过，也没有人知道传说从哪来；故事最后把它当作真相宣布。
- **¬F′ ∧ ¬R** — an unjustified answer and an unexplained anomaly: an open
  weird tale that nonetheless declares a solution.
  > 桌上多了一只不属于任何人的手套。没有人解释它，也没有证据支持任何解释；叙述者最后说"也许吧"。
- **¬P ∧ ¬R** — a sourceless claim about an unexplained anomaly: an
  unverifiable machine, a rumor with no witness.
  > 据说地下室有一台机器会自己启动。唯一提到它的人已经失忆，机器也从未被描述过。
- **¬P ∧ ¬M** — a bare assertion the events already imply: the text tells you
  the answer without provenance and without a puzzle.
  > 叙述者第一句就断言"是弟弟干的"，没有来源，也没有任何事件让读者需要这个断言。
- **¬R ∧ ¬M** — a mechanical puzzle: the facts give the answer, the trick is
  never explained.
  > 事件本身把谁做了什么写完了；读者只想知道手法，而手法从头到尾没有解释。

Any negation set containing both ¬F′ and ¬M is unsatisfiable (it contains the
collapsing pair); any set not containing both has a model, by extending one of
the rows above.

**Correction to the broad claim.** "Negating any two postulates collapses the
domain" is false: the unique collapsing pair is `{F′, M}`. The intuition that
"two or more negations collapse" is right only when the pair includes exactly
this pair. Moreover, `Ω* = ∅` is a *different* failure: it can occur under
¬F′ alone when the evidence is inconsistent, so "empty Ω*" is not equivalent to
the collapse of the domain.

## The three limits, as literary meanings

- **Event-layer openness (limit 1).** A well-formed story may leave the
  mechanism open; that is the default, not a missing piece. Do not force an
  explanation to fill it.
- **Background relativity (limit 2).** The same anomaly can be minimally
  explained from different backgrounds. "The explanation" is relative to the
  background allowed; a stronger background makes more explanations redundant,
  a weaker one makes more mechanisms necessary.
- **Source substitution and truth gaps (limit 3).** If two readings survive the
  final evidence, an unresolved hypothesis is not a debunked one. A source can
  be replaced only if a second legitimate channel exists; otherwise the claim
  is a single point of failure.

These are relative results inside finite classical propositional semantics.
They are not Gödelian incompleteness, Tarski undefinability, or algorithmic
undecidability in literary costume. Once a text is annotated with `R_0`, `E`,
`C`, `A`, and the source relations, the questions above are decidable; the
correctness of the annotation, and the literary value of the choices, are not
guaranteed by the logic.

## Scope

This note is descriptive. It does not grade prose, does not prescribe how many
clues or mechanisms a story should have, and does not claim that every
well-formed mystery instantiates all four postulates. Its use is to keep the
domain boundaries visible when someone asks why the two audit skills are split
the way they are.
