# Adversarial Review — Algebra Territory

Reviewer: adversarial review pass over `data/territories/algebra.json` against `data/spine.json`.
Verdict: **solid overall** — leveling broadly tracks standard curricula (Common Core → Dummit & Foote → Princeton Companion), prereq chains are mostly sound, and all spot-checked resource URLs are real. 9 issues found: 3 severe, 6 minor/moderate.

---

## SEVERE

### S1. Dangling prereq: `foundations:category-theory` does not resolve (homological-algebra)
`homological-algebra.prereqs` = `["module", "homomorphism", "foundations:category-theory"]`. Every other prereq in the file is a bare ID resolving to spine.json or this territory. `category-theory` exists nowhere in spine.json, and the `territory:id` prefix form is used only in `cross_links` elsewhere. This is a broken graph edge: any prereq resolver will either crash or silently drop it. Either add category-theory to the spine/foundations territory or move it to `cross_links` (where `foundations:category-theory` already appears under homomorphism).

### S2. Homological algebra intuition_gloss is garbled AND mathematically wrong
> "A bookkeeping machine of linked maps whose failures to compose to zero-perfectly measure the hidden holes..."

Two problems. (a) The sentence is broken English ("compose to zero-perfectly"). (b) The math is backwards: in a chain complex, consecutive maps compose to zero *by definition* (d∘d = 0). Homology measures the failure of **exactness** — the gap between kernels and images — not any failure to compose to zero. A correct image-first gloss would be something like: "chains of maps where doing two steps always gives zero; homology measures the leftover slack — things that die at the next step but didn't come from the previous one — and that slack detects hidden holes."

### S3. Missing MAJOR concept: Sylow theorems
The group-theory track runs subgroup → cyclic → permutation → quotient → group-action → **straight to the Classification of Finite Simple Groups**. Sylow theory — the workhorse of finite group theory, chapter 4 of Dummit & Foote, in every first abstract algebra course, and the actual bridge from orbit-stabilizer counting to classification results — is absent (not even as a cross_link). A map that includes the CFSG and the Monster but not Sylow is upside down: it has the summit without the base camp. Suggested node: level 5, prereqs [group-action, subgroup, prime-number].

---

## MODERATE / MINOR

### M1. exponential-and-logarithm: missing `real-numbers` prereq
Its own formal_gloss says b^x is "extended from integer exponents to the reals," but prereqs stop at `rational-numbers`. Defining b^x for irrational x requires the reals (spine level 2, so no level conflict). Add `real-numbers`.

### M2. Missing concept: tensor product
The file includes module (with the structure theorem) and homological algebra (whose gloss name-drops **Tor**), but tensor products — which Tor literally derives from — appear nowhere, not even as a cross_link. Hard to justify Ext/Tor at level 8 with no tensor product at level 6-7.

### M3. Missing school-algebra concept: rational expressions / rational functions
Between polynomial factoring and exp/log there is no node for rational expressions (Common Core HSA-APR.D, standard Algebra 2). Asymptotes/domain issues are also the classic on-ramp to limits. Arithmetic/geometric sequences & series are likewise absent, though those could defensibly live in analysis or discrete.

### M4. simple-group level 6 is arguably one notch low
CFSG sits at level 6, below Galois theory (7) and tied with modules — yet it depends on solvable/alternating-group ideas that the map itself surfaces only at level 7 (galois-theory cross-links simple-group). As a survey/appreciation node level 6 is defensible (the 3Blue1Brown resource matches that intent), but 7 would sit more honestly. Not "wildly off," so not severe.

### M5. FTA intuition_gloss overclaims slightly
"No polynomial equation is unsolvable — every one of degree n has exactly n roots." Needs "nonconstant" (the formal_gloss has it right); as written, degree-0 equations like 1 = 0 are counterexamples. One-word fix: "every one of degree n ≥ 1."

### M6. module intuition_gloss leads with jargon
"A rougher, **torsion-prone** habitat" — 'torsion' is undefined jargon inside what must be an image-first gloss. Swap for the image itself (e.g., "where scaling can crush things to zero, like clock arithmetic").

---

## Checks that came back clean

- **Leveling**: school track (0-3) matches Common Core placement cited in `sources`; abstract track (3-8) matches a standard undergrad → grad sequence. Prereq levels never exceed the dependent concept's level.
- **Prereqs** (other than S1/M1): spot-verified chains — quadratic→FTA→field-extension→galois; group→subgroup→quotient; ring→ideal→UFD — all sound. All bare prereq IDs resolve to spine.json or this file.
- **Duplicates**: none. `binary-operation` is a deliberate bridge into the spine's group/ring/field, not a duplicate; exp/log ↔ `analysis:exponential-function` overlap is handled via cross_link, which is correct.
- **Glosses**: apart from S2/M5/M6, intuition glosses are genuinely image-first (balance scale, clock hand, tiling cosets, blurring) and formal glosses are accurate — including the ED ⊂ PID ⊂ UFD ⊂ domain chain and the prime/maximal ideal characterizations.
- **Resources** (4 spot-checked live, all genuine and correctly attributed):
  - Numberphile FTA video `shEk8sz1oOw` → "Fundamental Theorem of Algebra - Numberphile" ✓
  - 3Blue1Brown Monster video `mH0oCDa74tE` → "Group theory, abstraction, and the 196,883-dimensional monster" ✓
  - judsonbooks.org → official site for Judson's *Abstract Algebra: Theory and Applications* ✓
  - Socratica playlist `PLi01...TP6` → "Abstract Algebra" by Socratica ✓
  - Unverified but well-known-real: Paul's Online Notes, Desmos, WolframAlpha, Evan Chen's Napkin, Etingof's replect.pdf, GAP, Wikipedia pages.
