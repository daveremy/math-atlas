# Adversarial Review — Mathematical Practice

Reviewed: `data/territories/mathematical-practice.json` (24 concepts) against `data/spine.json` (spine contributes `proof`, `induction`, `proof-by-contradiction` to this territory). Cross-territory prereqs verified against `foundations.json`; overlap checked against `discrete-combinatorics.json`. Three resource URLs spot-checked live with WebFetch.

**Verdict: solid territory overall.** Coverage of proof techniques + Polya/Schoenfeld/Engel heuristics + practice meta-skills is well-sourced and internally consistent. 10 issues found: 2 severe, 3 moderate, 5 minor.

---

## Severe

### S1. `problem-reduction` — wrong-topic resource (verified live)
The resource "Reduction (mathematics) — Wikipedia" (`https://en.wikipedia.org/wiki/Reduction_(mathematics)`) is a real page but about the **wrong concept**: fetched content covers rewriting expressions into simpler form — fraction reduction, row reduction/Gaussian elimination, integration-by-parts reduction formulas, Guyan reduction. It does not cover reducing one *problem* to another, which is what this concept is. A learner clicking through lands on unrelated material.
**Fix:** replace with `https://en.wikipedia.org/wiki/Reduction_(complexity)` (the formal analogue already cited in `sources` via MSC 68Q) or drop it and keep the Polya link.

### S2. `extremal-principle` — wrong prereq `invariant`
The extremal principle does not depend on invariants in any curriculum. In Engel (the concept's own cited source) they are parallel, independent chapters (ch. 1 Invariance, ch. 3 Extremal Principle), both taught as entry-level olympiad techniques. Listing `invariant` as a prereq falsely gates this concept behind an unrelated one. The genuine dependencies are `proof-by-contradiction` (kept) and the well-ordering idea (already a cross_link).
**Fix:** remove `invariant` from prereqs; move it to `cross_links` if the pairing is worth keeping.

---

## Moderate

### M1. Missing concept: standard proof patterns for biconditionals / set equality / uniqueness
The territory covers direct, contrapositive, cases, constructive, plus spine's contradiction and induction — but omits the other half of every transition-to-proof course (including its own cited Hammack text, chs. 7–8, 10-adjacent): proving "iff" statements by two implications, proving set equality by double inclusion, and existence-and-uniqueness proofs. These are workhorse patterns a serious practice map should name, not fold silently into `direct-proof`.

### M2. Missing concept: strong induction / induction variants
`induction` sits in the spine under this territory, but the territory adds no entry for strong (complete) induction, well-ordering-based induction, or structural induction. Strong induction is a standard, separately-taught technique (Hammack ch. 10, Velleman) with a real conceptual delta (different inductive hypothesis). Nothing anywhere in the atlas appears to own it.

### M3. `proof-by-contrapositive` aka "Indirect proof" is misleading
In most texts "indirect proof" primarily denotes **proof by contradiction** (or is an umbrella for both). Attaching the alias exclusively to contrapositive will misroute searches and contradicts common usage. Fix: drop the alias or note it's shared with contradiction.

---

## Minor

### m1. `extremal-principle` level 4 reads one notch high
Consequence of S2's framing: it's an olympiad-entry technique on par with `invariant` (level 3). With the bogus `invariant` prereq removed, level 3 is more faithful; 4 is defensible only if levels track the well-ordering formalization. Not "wildly off," so minor.

### m2. `rigor-and-intuition` intuition_gloss contains jargon
"...your gut speaks fluent epsilon-delta" — intuition glosses are supposed to be image-first plain language; epsilon-delta is insider jargon, meaningless before analysis. The first clause ("fast intuition checked by slow rigor") stands fine alone.

### m3. `mathematical-definition` intuition_gloss is maxim-first, image-second
"The exact wording ... is the whole game" is advice, not an image. The contract-you-unfold metaphor in the second clause should lead.

### m4. `without-loss-of-generality` vs `exploiting-symmetry` overlap
WLOG is essentially the proof-writing face of exploiting symmetry (WLOG's own gloss says so). They're both standard named entries and cross-linked, so keeping both is acceptable — but glosses should explicitly delimit them (WLOG = the proof *move*; exploiting symmetry = the discovery *strategy*).

### m5. Missing cross_link to `pigeonhole-principle`
Pigeonhole (in discrete-combinatorics) is the third member of the classic olympiad trio with `invariant` and `extremal-principle` (Engel ch. 4 sits beside chs. 1 and 3), yet neither concept cross-links it. Add `pigeonhole-principle` to both concepts' cross_links.

---

## Checks that passed

- **Levels:** No wildly mis-leveled concepts. Transition-to-proof cluster at 2–3, heuristics at 1–3, meta/abstraction at 3–4, `proof-formalization` at 6 — all match standard curricula. Prereq levels are monotone (same-level prereqs like polya→working-backwards at level 1 are acceptable).
- **Cross-territory prereqs resolve:** `foundations:propositional-logic`, `foundations:first-order-logic`, `foundations:well-ordering` all exist in `foundations.json`; spine ids (`proof`, `induction`, `function`, `algorithm`, etc.) all resolve.
- **URLs spot-checked (3 live fetches):**
  - `https://richardhammack.github.io/BookOfProof/` — **real**, official Book of Proof 3rd-ed site with free PDF.
  - `https://link.springer.com/book/10.1007/b97682` — resolves (Springer bot-wall redirect); DOI is Engel, *Problem-Solving Strategies* — correct.
  - `https://en.wikipedia.org/wiki/Reduction_(mathematics)` — real page, wrong topic (→ S1).
  - Not fetched but recognized-genuine: Tao career-advice and writing-advice URLs, arXiv `math/9404236` (Thurston), `adam.math.hhu.de` (Lean game server), Knuth *Mathematical Writing* PDF at jmlr.csail.mit.edu.
- **No duplicates:** closest pair is WLOG/exploiting-symmetry (m4); no true duplicates. `specialization-small-cases` vs `estimation-sanity-checking` are properly distinct (conjecture-generation vs answer-validation).
- **Glosses:** no circular or factually wrong glosses found; formal glosses are accurate (contrapositive equivalence, counterexample definition, Schoenfeld attribution, Tao three-stages all check out).
- **Sources:** attributions are real and apt (Polya, Schoenfeld 1985, Engel chapter numbers correct, Lakatos, Nelsen, Cajori, Princeton Companion section numbers plausible).
