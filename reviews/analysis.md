# Adversarial Review — Analysis & Calculus Territory

**File reviewed:** `data/territories/analysis.json` (against `data/spine.json`)
**Reviewer:** adversarial review pass, 2026-07-21
**Verdict:** Strong file overall — glosses are accurate and genuinely image-first, formal glosses are mathematically correct, no intra-territory duplicates, and every `prereqs` id resolves. But the map has one level inversion, nine dangling cross_links, a missing cornerstone theorem (Bolzano–Weierstrass), and a mislabeled resource URL.

**Issue count: 11** (3 severe, 5 moderate, 3 minor)

---

## Severe

### S1. Level inversion: `intermediate-value-theorem` (L3) requires `completeness-of-reals` (L4)
The only prereq-above-dependent inversion in the file (verified by script over all 25 concepts + spine). Any learner path sorted by `level` presents IVT before the axiom its own formal gloss leans on. Two consistent fixes: raise IVT to 4 (it sits beside EVT, also L4, with identical prereqs), or accept the Calc-1 framing and drop `completeness-of-reals` to a cross_link — but not the current half-and-half. Note the neighboring inconsistency in M2.

### S2. Missing MAJOR concept: Bolzano–Weierstrass / subsequences
No node, no alias, no mention anywhere in the file of Bolzano–Weierstrass ("every bounded sequence has a convergent subsequence") or of subsequences at all. This is a cornerstone of every intro real-analysis course (Abbott Ch. 2, Rudin Ch. 3, MIT 18.100A — the very sources this file cites), and it is the load-bearing step in the standard proofs of two theorems the map *does* include (EVT, and Cauchy ⇒ convergent in R). The chain completeness → Bolzano–Weierstrass → {Cauchy completeness, EVT} is the spine of the subject; the middle link is absent.

### S3. Nine dangling cross_links — targets exist nowhere in the dataset
Verified by script against all 12 territory files and the spine:

| From | Broken link | Closest real id |
|---|---|---|
| `taylor-series` | `applied-computational:numerical-approximation` | `interpolation` / `numerical-integration` |
| `stokes-theorem` | `geometry:differential-form` | — (none) |
| `stokes-theorem` | `dynamics-differential-equations:vector-field` | `slope-field` / `flow` |
| `asymptotic-analysis` | `number-theory:prime-number-theorem` | `prime-distribution` |
| `cauchy-integral-theorem` | `number-theory:prime-number-theorem` | `prime-distribution` |
| `convex-function` | `geometry:convex-geometry` | `convexity` |
| `hilbert-space` | `applied-computational:quantum-computing` | — (none) |
| `holomorphic-function` | `geometry:conformal-map` | — (none) |
| `cauchy-integral-theorem` | `topology:winding-number` | — (none) |

Five look like guessable renames; four (`differential-form`, `quantum-computing`, `conformal-map`, `winding-number`) have no target at all. All other cross_links (including `foundations:axiom-of-choice`, `discrete-combinatorics:generating-function`, `probability-statistics:central-limit-theorem`, and all unprefixed ids) resolve.

---

## Moderate

### M1. `partial-derivative` resource labeled "Khan Academy: Multivariable calculus" points at single-variable Calculus 1
URL is `https://www.khanacademy.org/math/calculus-1` — the single-variable Calc 1 course, not multivariable. Should be `/math/multivariable-calculus`. (The `asymptotic-analysis` entry uses the same calculus-1 URL but at least labels it "Calculus," so it's merely weak rather than wrong.)

### M2. The Calc-1 theorem cluster is leveled inconsistently
IVT (L3) and FTC (L3) vs. EVT (L4) and MVT (L4). All four are standard first-semester-calculus theorems taught in one arc; MVT in particular is core Calc 1 (and a *prereq* here for `taylor-series`). The file seems torn between a "when first met" scheme (IVT, FTC) and a "when proved rigorously" scheme (EVT, MVT). Either scheme is defensible; mixing them within one cluster is not, and it's what produced the S1 inversion.

### M3. `aka` field used as a related-terms dump — worst cases teach false identifications
Same disease the topology review found (its M2–M4):
- `mean-value-theorem` aka **"Rolle's Theorem"** — a distinct theorem (the special case f(a)=f(b)), not another name for MVT.
- `gradient` aka **"Directional Derivative"** — a different object (the gradient *computes* directional derivatives).
- `lebesgue-integral` aka **"Dominated Convergence Theorem"** — a theorem about the integral, not a name for it.
- Milder: `power-series` aka "Radius of Convergence" (a property), `banach-space` aka "Functional Analysis" and `lebesgue-measure` aka "Measure Theory" (whole fields), `fourier-analysis` aka "Harmonic Analysis" (broader field).

### M4. `convex-function` ("Convexity") overlaps `geometry:convexity`
Cross-territory near-duplicate: the analysis node's aka already claims "Convex Set", which is exactly the geometry node's turf. The analysis node even cross-links the *nonexistent* `geometry:convex-geometry` (S3) instead of the real `geometry:convexity`. Scope the analysis node to convex *functions* (drop "Convex Set" from aka) and point the cross_link at the real geometry node.

### M5. Missing secondary concept: uniform continuity
No node and no alias. It's a standard topic in every source the file cites (Abbott Ch. 4, Rudin Ch. 4), the hypothesis actually needed to prove continuous ⇒ Riemann-integrable (a bridge between two spine nodes), and the natural sibling of `uniform-convergence`, which *is* included. Lesser gaps, defensible for an atlas but worth noting: Weierstrass approximation theorem, Arzelà–Ascoli, L^p spaces (only implicitly reachable via `banach-space`).

---

## Minor

### m1. Paul's Online Math Notes linked as bare homepage, three times
`infinite-series`, `power-series`, and `multiple-integral` all cite `https://tutorial.math.lamar.edu/` with no path. The site has stable per-topic URLs (e.g. `classes/calcii/series_intro.aspx`); a homepage link forces the learner to navigate a whole site.

### m2. `holomorphic-function` intuition gloss slightly misses the point
"Differentiable in every direction at once" is also true of any smooth real map R²→R². The actual miracle is that the derivative is the *same complex number* from every direction (rotation-and-scaling only). Small wording fix; the "so rigid it forces infinite smoothness" payoff is right.

### m3. `implicit-function-theorem` — the least image-first gloss in the file, and a resource stretch
The intuition gloss ("linear snapshot ... invertible ... locally invertible") is a softened restatement of the formal gloss, not an image. Also its resource cites MIT 18.100A, which does not cover the inverse/implicit function theorems (that's Rudin Ch. 9 / 18.101 material — the `sources` field gets this right).

---

## Checks that passed

- **URL spot-checks (3 fetched):** 3Blue1Brown Taylor-series lesson — real, is what it claims. Khan Academy `math/calculus-1` — real course (exposing the M1 label mismatch). Springer Abbott link — redirects to Springer's auth wall, but the DOI `10.1007/978-1-4939-2712-8` is the genuine *Understanding Analysis* 2nd-ed. record. MIT OCW slugs (18-01sc, 18-02sc, 18-100a-fall-2020, 18-102-spring-2021), Tao's measure-theory page, Boyd & Vandenberghe cvxbook, Coursera Wesleyan complex analysis, and Stein & Shakarchi's Princeton page are all well-known and correctly formed. No fabricated resources found.
- **Formal glosses:** all 25 checked; all mathematically correct (Cauchy criterion, sup definition of uniform convergence, generalized Stokes ∫_∂M ω = ∫_M dω, residue theorem with winding numbers, Fubini caveat on multiple integrals, C^1 hypothesis on IFT — all stated carefully).
- **Intuition glosses:** consistently image-first (pinholes in the number line, river crossing, speedometer, prism splitting a signal, slicing by height); none circular; only m2/m3 above are even arguable.
- **Prereq referential integrity:** every `prereqs` id resolves to the territory or spine; only one level inversion (S1).
- **Duplicates within territory:** none. `power-series` vs `taylor-series`, and the bundled `partial-derivative` (partials + Jacobian + total derivative) and `stokes-theorem` (Green/divergence/Stokes) nodes are distinct and sensibly scoped.
- **Coverage otherwise:** single-variable → multivariable → measure → functional → complex analysis arc is complete and well-chosen for a 25-node territory; levels 4–6 are broadly consistent with standard curricula apart from M2.
