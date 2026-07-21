# Adversarial Review — Foundations: Logic & Set Theory

Reviewed: `data/territories/foundations.json` (25 concepts) against `data/spine.json` (foundations spine: set, function, equivalence-relation, axiom, cardinality).
Date: 2026-07-21. Reviewer: adversarial subagent.

**Verdict: solid territory overall — accurate glosses, real resources, sensible DAG — with 1 severe error and a handful of moderate/minor gaps.**

---

## SEVERE

### S1. Peano Axioms intuition_gloss makes a false categoricity claim
`peano-axioms` intuition_gloss: "Five simple rules ... that **completely capture** what the counting numbers are."

Two problems:
1. **Mathematically wrong in context.** The formal_gloss commits to *first-order* PA ("first-order PA is the standard formal theory of arithmetic"). First-order PA does **not** completely capture N — it has nonstandard models (compactness / Löwenheim–Skolem), and it is incomplete by Gödel. Only the second-order induction axiom gives categoricity. The gloss directly contradicts the map's own `godel-incompleteness` and `model-theory` entries ("the same axioms often describe wildly different universes"). A learner who takes both glosses at face value gets a contradiction.
2. **Internal miscount.** "Five simple rules — zero exists, every number has a successor, and induction" enumerates three things while claiming five.

Suggested fix: soften to something like "a short list of rules — zero, successor, and the induction domino principle — that pin down how counting works" and drop the "completely capture"/"five" claims, or explicitly note the first-order vs second-order caveat in the formal_gloss.

---

## MODERATE

### M1. Missing major concept: Cantor–Schröder–Bernstein theorem
The workhorse for comparing cardinalities (injections both ways ⇒ bijection) appears in every transition-to-proof and set theory course (Book of Proof ch. 13, Enderton, Halmos) and is load-bearing for `cardinality` and `countability` arguments. Not present as a concept, aka, or cross-link anywhere in the territory.

### M2. Compactness and Löwenheim–Skolem theorems absent
`model-theory` names only soundness/completeness. Compactness and Löwenheim–Skolem are the other two pillar theorems of first-order logic (Princeton Companion IV.24 treats them as such), and Löwenheim–Skolem is exactly what makes the "wildly different universes" claim in the model-theory gloss true. Minimum fix: add both to `model-theory`'s aka list and formal_gloss; a serious map arguably wants them as a concept.

### M3. Gap between cardinality (L4) and Continuum Hypothesis (L7): no cardinal numbers / aleph hierarchy
`continuum-hypothesis` speaks of "no cardinal lies strictly between |N| and |R|", and `ordinals` cross-links `cardinality`, but there is no concept for cardinal numbers as objects (alephs, cardinal arithmetic, 2^ℵ₀). Ordinals got a full entry; their cardinal twin did not. CH is hard to state precisely without it.

---

## MINOR

### m1. Same-level prereqs (level ties) — inconsistent with a level-encodes-progression reading
If `level` is meant to order study, prereqs should sit strictly lower. Ties found:
- `countability` (L4) → `cardinality` (L4)
- `peano-axioms` (L4) → `first-order-logic` (L4)
- `decidability` (L5) → `diagonalization` (L5)
- `axiom-of-choice` (L6) → `zfc` (L6)
- `ordinals` (L6) → `zfc` (L6)
- `recursive-definition` (L3) → `induction` (L3, spine)

No cycles, and no level is *wildly* off standard curricula — but the ties should either be resolved or the level semantics documented as "band, not strict order."

### m2. Extraneous prereq: `subset-and-power-set` requires `set-operations`
Subsets and power sets need only `set`; union/intersection are not used in their definition, and most texts (including the cited Book of Proof ch. 1) introduce subsets before or alongside operations. Harmless but noise in the DAG.

### m3. Alias collisions across concepts
- "Boolean logic" is an aka of **both** `propositional-logic` and `boolean-algebra`. Any alias-based lookup resolves ambiguously. Recommend removing it from `propositional-logic`.
- "Well-ordering theorem" is an aka of `axiom-of-choice` while a separate `well-ordering` concept exists. Technically defensible (the theorem is an AC-equivalent, the concept is the order property) but a search for "well-ordering" now hits two nodes; consider a disambiguating note.
- "Zorn's lemma" as a mere aka of `axiom-of-choice` under-serves it (it's the form working mathematicians actually use), but acceptable for map granularity.

### m4. Lean resource link is imprecise
`peano-axioms` cites "The Natural Number Game (Lean)" at `https://adam.math.hhu.de/` — that URL is the Lean game-server hub, not the NNG itself. Deep link would be `https://adam.math.hhu.de/#/g/leanprover-community/nng4`. (The same URL under `type-theory` is labeled generically "Lean game server", which is fine.)

---

## Checks that PASSED

- **Resource spot-checks (WebFetch, 3 URLs):** all genuine and correctly titled.
  - `https://richardhammack.github.io/BookOfProof/` — real; official Book of Proof site (3rd ed., free PDF). Used by 3 concepts.
  - `https://www.youtube.com/watch?v=OxGsU8oIWjY` — real; title confirmed "How An Infinite Hotel Ran Out Of Room" (Veritasium).
  - `https://www.youtube.com/watch?v=elvOZm0d4H0` — real; title confirmed "Infinity is bigger than you think" (Numberphile).
  - SEP slugs (`logic-classical`, `russell-paradox`, `set-theory`, `axiom-choice`, `continuum-hypothesis`, `model-theory`, `goedel-incompleteness`, `turing-machine`, `type-theory`, `category-theory`) all match real SEP entries.
- **Glosses:** with the exception of S1, intuition_glosses are genuinely image-first (bags, catalogs, dominoes, chessboards, bottomless descents) and formal_glosses are accurate — including the subtle ones (AC "independent of ZF", Gödel "consistent, effectively axiomatized, extending basic arithmetic", countable = "injects into N", Kuratowski pairs, Rosser-safe incompleteness phrasing).
- **No duplicate concepts.** `well-ordering` vs `ordinals`, `propositional-logic` vs `boolean-algebra`, `decidability` vs spine `algorithm` are all legitimately distinct with correct cross-links.
- **Key prereq edges are right:** diagonalization → {CH, Gödel, decidability}; Russell's paradox → {ZFC, type-theory}; formal-system → {model-theory, Gödel, decidability}. Matches the standard dependency narrative.
- **`category-theory` placement** (contested with algebra) is already self-flagged in its `sources` field per house rules — no action.

---

## Summary

| Severity | Count |
|---|---|
| Severe | 1 (S1) |
| Moderate | 3 (M1–M3) |
| Minor | 4 (m1–m4) |
| **Total** | **8** |
