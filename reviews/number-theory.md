# Adversarial Review — Number Theory Territory

Reviewed: `data/territories/number-theory.json` against `data/spine.json` and sibling territory files.
Date: 2026-07-21. Reviewer: adversarial pass (levels, prereqs, coverage, glosses, resources, duplication).

Verdict: solid skeleton and mostly excellent glosses, but the graph has **two level inversions**, **one dangling prereq id used twice**, a **pattern of fake book-resource URLs (3 confirmed 404s)**, a **circular definition** between the spine's `prime-number` and FTA, and a **whole missing wing (additive number theory)**. 17 issues total, 6 severe.

---

## SEVERE

### S1. Level inversion: `fundamental-theorem-of-arithmetic` (level 2) requires `bezout-identity` (level 3)
A concept cannot sit below its own prerequisite. Any leveled rendering or learning path breaks: the learner reaches FTA at level 2 with Bézout still locked. Either FTA moves to 3+ (Hardy & Wright prove it via Euclid's lemma, which needs Bézout) or Bézout drops to 2 (defensible — it is corollary-of-Euclidean-algorithm material in Burton ch. 2). One of the two must change.

### S2. Level inversion: `pythagorean-triples` (level 2) requires `diophantine-equation` (level 3)
Same defect. Also pedagogically backwards relative to standard curricula: triples (Silverman ch. 2–3, his *opening* example) are the concrete on-ramp that *motivates* the general Diophantine concept, not the other way around. The prereq arrow should probably be removed (make `diophantine-equation` a cross_link) rather than re-leveling.

### S3. Dangling prereq id `analysis:complex-analysis` (used in `riemann-zeta-function` and `modular-forms`)
`analysis.json` has no concept `complex-analysis`; the actual nodes are `holomorphic-function` and `cauchy-integral-theorem`. These are hard prereq edges (not cross_links) pointing at nothing — the two most advanced concepts in the territory have a broken dependency each.

### S4. Fake/dead resource URLs — book "links" that point at nonexistent Wikipedia articles (3 confirmed 404)
Spot-checked with live fetches:
- `https://en.wikipedia.org/wiki/David_M._Burton` (`divisibility`) — **404**
- `https://en.wikipedia.org/wiki/Introduction_to_Analytic_Number_Theory` (`arithmetic-functions`, for Apostol) — **404**
- `https://en.wikipedia.org/wiki/A_Classical_Introduction_to_Modern_Number_Theory` (`quadratic-reciprocity` AND `gaussian-integers`, for Ireland & Rosen) — **404**, used twice

This is a systematic anti-pattern: when no real link for a book was found, a plausible-looking Wikipedia URL was invented. Same pattern, unverified but suspect targets even where the page exists: `Aleksandr_Khinchin` (author bio standing in for his *Continued Fractions* monograph) and `An_Introduction_to_the_Theory_of_Numbers` (this one likely exists, but it's an article *about* the book, not the resource). Verified good: Silverman frint.html (real, free chapters confirmed), 3Blue1Brown zeta video `sD0NjbwqlYw` (real, correct video), t5k.org, LMFDB, OEIS, Springer links plausible.

### S5. Circular definition: spine's `prime-number` formal gloss presupposes FTA
Spine: *"…every integer greater than 1 factors uniquely into primes."* That sentence **is** the Fundamental Theorem of Arithmetic — a downstream territory concept whose prereqs include `prime-number`. The definition of the prereq asserts the theorem it feeds. The uniqueness clause must be deleted from the spine gloss (the correct definition stops at "only positive divisors are 1 and itself").

### S6. Missing MAJOR area: additive number theory — and no node for Euclid's infinitude of primes
- Zero coverage of Goldbach's conjecture, twin primes, Waring's problem, or sums of two/four squares (two-squares appears only as a buried clause inside the `gaussian-integers` formal gloss). For a map that includes RH and FLT as landmark nodes, omitting Goldbach/twin primes — the other famous elementary-to-state open problems — is a coverage hole, and additive NT is a full MSC area (11P).
- Euclid's infinitude of primes, arguably the most famous theorem in elementary mathematics, has no node. The map jumps from `prime-number` (L1) straight to `prime-distribution` (L5); the sources field itself admits "Euclid's infinitude proof is the level-2 on-ramp" — but the on-ramp was never built.

---

## MODERATE

### M1. Dangling cross_links (broken ids)
- `algebra:unique-factorization-domain` (`fundamental-theorem-of-arithmetic`) — algebra's node is `unique-factorization`.
- `foundations:computability` (`diophantine-equation`) — foundations' node is `decidability`.
- References into territories that have **no data file**: `probability-statistics:probabilistic-heuristics`, `probability-statistics:random-matrix-theory`, `applied-computational:computational-complexity`, `applied-computational:quantum-computing`, `applied-computational:cryptography`, `discrete-combinatorics:inclusion-exclusion`. The spine has *some* concepts for these territories but none of these ids. If forward references are intentional they need at least a naming contract; two of them are provably misspelled against existing files, which suggests they are guesses.

### M2. Resource mislabeled: `fermats-last-theorem` "BBC Horizon: Fermat's Last Theorem (Simon Singh documentary)", type `video`
The URL is `en.wikipedia.org/wiki/Fermat's_Last_Theorem_(book)` — a text article about Singh's *book*, not the documentary. Either link the actual documentary (BBC iPlayer / official upload) or retype as `text` and retitle.

### M3. Missing concepts (secondary tier)
- **Binary quadratic forms** — the heart of Gauss's *Disquisitiones* (cited as a source!) and the classical road to class numbers; class group currently appears only inside `algebraic-number-field` at L7.
- **Geometry of numbers** (Minkowski) — standard bridge topic, MSC 11H.
- **Wilson's theorem** — minor, but it's in every elementary syllabus alongside FLT (Burton ch. 5).
- **Partitions** — Euler/Ramanujan; defensible to park in combinatorics, but nothing points there.

### M4. Gloss quality violations (intuition_gloss must be image-first plain language)
- `modular-forms`: leads with "Functions on the upper half-plane… congruence-subgroup symmetry" framing — jargon-first; "upper half-plane" is meaningless to the target reader. The "outrageous amount of symmetry" and "fifth operation" parts are good; lead with those.
- `pell-equation`: intuition gloss opens with the formula "x² − D·y² = 1" and the word "hyperbola" — formula-first, not image-first (the "endless ladder" image should lead).
- `fermats-little-theorem`: "Raise any number to a **prime power**" is wrong terminology — "prime power" means p^k, not "the p-th power." As worded it misstates the theorem; say "raise it to the clock-size power."

### M5. FLT at level 5 (statement-level placement)
Deliberate per the sources note, and prereqs correctly avoid pointing upward at `elliptic-curve` (L7) / `modular-forms` (L8). Acceptable, but the map should encode "statement vs. proof" placement policy somewhere global, or FLT-at-5 next to RH-at-7 (also elementary to state) looks inconsistent — RH's *statement* needs complex analysis, so the asymmetry is actually defensible; documenting the policy would prevent future reviewers relitigating it.

### M6. Overlap: `bezout-identity` aka "linear Diophantine equations" vs `diophantine-equation`
The linear case ax + by = c is claimed by Bézout's aka/formal gloss while the general concept lives at `diophantine-equation`. Not a duplicate node, but the aka invites double-filing; suggest scoping the aka to "extended Euclidean algorithm" only. Similarly `sieve-of-eratosthenes` aka "sieve methods (entry point)" stretches an L1 algorithm to cover an advanced analytic field with no node of its own — fine as a signpost, but Brun/Selberg sieves have no home if the territory ever deepens.

### M7. `greatest-common-divisor` bundles LCM; `eulers-totient-function` bundles Euler's theorem
Acceptable bundling (noted, not a defect) — but ids should ideally not under-describe their content since other territories may want to link `lcm` or `eulers-theorem` specifically.

---

## What checks out
- Internal prereq ids all resolve (spine + territory) except those named above; no orphan internal ids.
- Level ladder is otherwise monotone (every other concept ≥ max prereq level).
- Elementary sequence (divisibility → division algorithm → Euclid → Bézout → congruences → FLT → Euler → CRT → order/primitive roots → reciprocity) matches Burton/Silverman/Hardy-&-Wright ordering.
- The crypto cluster (primality testing, factoring, RSA) and the three L7–8 gateway nodes (algebraic number fields, p-adics, elliptic curves, modular forms) are well-chosen and well-sourced.
- Verified-live resources: Silverman frint.html, 3B1B zeta video, LMFDB, t5k.org, OEIS.

## Issue count: 17 (6 severe, 11 moderate/minor)
