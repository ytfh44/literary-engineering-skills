---
name: anti-ai-prose
description: Use when fiction, narration, interior monologue, or dialogue sounds like a staff report, therapy summary, retrospective memo, generic self-help post, automatic “growth” statement, or authorial explanation that settles meaning before the scene earns it.
license: Apache-2.0
---

# Anti-AI Prose

## Use when

The prose feels non-human because it explains relationships, growth, motives, or significance in a register no present speaker or perceiver would naturally use.

## Do not use when

Do not punish explicit relations in essays, law, technical writing, or a character whose job and situation genuinely call for them. For count-heavy relation scaffolds, use `relation-language-audit`.

## Core test

**Swap the nouns. Would the sentence still fit a quarterly review, therapy recap, or generic life-advice post?**

If yes, inspect it. The sentence may be replacing an event with an administrative summary of the event.

## Workflow

1. Mark the smallest sentence that sounds externally summarized.
2. Ask who owns it: character, narrator, institution, or nobody in particular.
3. Underline abstract relation or development claims: “realized,” “meant,” “relationship,” “growth,” “new stage,” “in a sense.”
4. Recover the scene fact those claims summarize.
5. Keep the abstract sentence only if it adds information unavailable from the scene or belongs to the speaker's authentic register.
6. Otherwise delete it or replace it with the event that made the relation legible.

## Hard rules

- There is no blacklist. “意识到” can be exact; “看见” can be dead.
- Do not replace an abstraction with a body-language cliché.
- Do not turn every conclusion into mystery. Sometimes the narrator should conclude.
- Do not confuse intelligence with institutional diction.
- Preserve deliberate essayistic or comic bureaucratic voice.

## Minimal pair

> 她把钥匙放回桌上。她意识到，他们的关系已经发生了变化。
>
> 她把钥匙放回桌上。这次没有拿走。

The second version does not become “more human” by using concrete nouns. It stops charging the narrator to explain a relation the altered action can carry.

## Counterexamples

- “他意识到煤气没关。” Keep it: the realization is an event with immediate informational content.
- A management consultant narrating a deliberately comic breakup as “关系进入维护期.” Keep it if the register is the joke and belongs to the character.

## Read next

- Read [corporate-register.md](references/corporate-register.md) when the prose sounds like HR, project management, or a postmortem.
- Read [explanatory-overreach.md](references/explanatory-overreach.md) when the narrator repeatedly states what a scene “means.”
- Read [false-depth.md](references/false-depth.md) when balanced clauses or abstract reversals simulate profundity.

## Return shape

For analysis, return **span -> foreign register -> scene fact -> keep/delete/rewrite reason**.

For revision, change only the sentences whose ownership or explanatory load fails. Do not sand the whole passage into neutral prose.
