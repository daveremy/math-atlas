# Math Atlas v0.1 — Global Completeness Review (Cross-Territory)

Scope: `data/spine.json` (46 concepts), `data/territories.json` (12 territories), and all 12 files in
`data/territories/` (299 territory concepts; 345 total nodes). Per-territory reviews (134 issues) were
taken as read; this review covers only what can be seen **across** territories.

Verification method: programmatic cross-check of every `prereqs` and `cross_links` entry against the
set of all defined ids (spine + territories), plus duplicate-id detection and per-territory counts.

---

## 1. Major concepts missing from the ENTIRE map

Ranked by how loudly a mathematician would laugh. Items marked ⚠ are already *referenced* by other
concepts (dangling links prove the map itself thinks they should exist).

### Would get us mocked

1. **The exponential function & the number e** ⚠ — referenced as `analysis:exponential-function` by
   algebra and dynamics, but no node anywhere defines exp, e, or Euler's formula e^(iθ) = cos θ + i sin θ.
   The single most important function in analysis is absent. (Algebra's `exponential-and-logarithm` is
   the school-level exponent-rules concept, not the analytic object.)
2. **Classical inequalities: Cauchy–Schwarz, AM–GM, triangle inequality** ⚠ — Cauchy–Schwarz appears
   nowhere in 345 nodes. It is arguably the most-used inequality in mathematics (inner products,
   probability, analysis). `analysis:triangle-inequality` is referenced by algebra but undefined.
   Suggest one node "Fundamental Inequalities" in analysis (level ~3).
3. **Differential forms & exterior calculus** ⚠ — the formal gloss of `analysis:stokes-theorem`
   *literally states the theorem in terms of differential forms* (∫_∂M ω = ∫_M dω), and both
   linear-algebra (`dual-space`) and analysis reference `geometry:differential-form`. Undefined.
4. **Conditional expectation** ⚠ — referenced by linear-algebra (`orthogonal-projection`, the classic
   "conditional expectation is a projection" bridge); `martingale` buries it in an `aka`. It is the
   load-bearing concept of modern probability and deserves its own node.
5. **Calculus of variations (Euler–Lagrange)** ⚠ — referenced by `geometry:geodesic`; the bridge
   between analysis, geometry, and physics (least action). Absent.
6. **Laplace's equation / harmonic functions** — the PDE trio is heat (parabolic) + wave (hyperbolic)
   + *Laplace (elliptic)*; the classification in `partial-differential-equation` names "elliptic" but
   the canonical elliptic equation has no node. Relatedly, the **Laplace transform** (a staple of every
   ODE course incl. the cited MIT 18.03) is absent.
7. **Winding number / degree of a map** ⚠ — referenced by both `algebra:fundamental-theorem-of-algebra`
   and `analysis:cauchy-integral-theorem` as `topology:winding-number`. Undefined; topology has no node
   for it despite it being the payoff concept connecting π1(S¹) ≅ Z to FTA and residues.
8. **Coding theory / error-correcting codes** ⚠ — `information-theory` exists but Hamming/Reed–Solomon
   codes do not, despite `discrete-combinatorics:combinatorial-design` referencing
   `applied-computational:error-correcting-codes`. Half of Shannon's story is missing.
9. **Constrained optimization / Lagrange multipliers** — the standard multivariable-calculus capstone;
   only mentioned in passing inside `convex-optimization`'s KKT gloss. Absent as a concept.
10. **Principal Component Analysis** ⚠ — referenced by `singular-value-decomposition` as its flagship
    application; undefined. The single most famous applied use of linear algebra.

### Notable but more forgivable at v0.1

- **Vector field** ⚠ (`dynamics-differential-equations:vector-field` referenced by Stokes; dynamics has
  `slope-field` and `flow` but no general vector-field node).
- **Random walk** — Brownian motion is present, its discrete ancestor is not.
- **Moment generating / characteristic functions** ⚠ (referenced by `generating-function`) — the CLT's
  actual proof tool.
- **Quantum computing** ⚠ (referenced twice: `hilbert-space`, `integer-factorization` — Shor's is in a
  gloss but no node).
- **Additive combinatorics / Szemerédi's theorem** ⚠ (referenced by `ramsey-theory`,
  `extremal-combinatorics`) — Green–Tao-adjacent; a live field with zero presence.
- **Gauss–Bonnet theorem** ⚠ — referenced by `euler-characteristic`; the crown jewel connecting
  curvature to topology, absent (both endpoints exist!).
- **Percolation** ⚠, **random matrix theory** ⚠ (referenced by NT's zeta node), **cross product**,
  **special distributions beyond normal/Poisson (exponential, uniform, t/χ²)**, **spectral graph
  theory**, **Catalan/Stirling numbers**, **universal properties** (category theory exists but its
  killer app doesn't), **distributions/generalized functions** ⚠, **wavelets**.

---

## 2. Duplicate concepts under different ids (merge pairs)

### Hard id collisions (same id defined twice — breaks any global id lookup)

| id | Territory A | Territory B | Problem |
|---|---|---|---|
| `diagonalization` | foundations ("Diagonalization & Cantor's Theorem") | linear-algebra ("Diagonalization" = eigendecomposition) | **Two completely different concepts sharing one id.** Rename to `cantor-diagonalization` and `eigendecomposition` (or keep LA as `diagonalization` and rename foundations). Highest-priority data bug in the map. |
| `dimension` | geometry ("Dimension", broad: topological/fractal) | linear-algebra ("Dimension", basis cardinality) | Same name, overlapping content, colliding id. Either merge into one spine-level node with territory-specific children (`vector-space-dimension`, `hausdorff-dimension`), or rename one. |

### Same concept, two ids (merge or explicitly differentiate)

| Merge pair | Recommendation |
|---|---|
| `foundations:partial-order` ↔ `discrete-combinatorics:poset` | Same object (both formal glosses: reflexive/antisymmetric/transitive). Merge; keep one node, move Dilworth/Möbius material into it or into a child. Ironically each territory's concepts cross-link the *other* territory's nonexistent alias (`foundations:order-theory`, `foundations:zorns-lemma`). |
| `probability-statistics:monte-carlo` ↔ `applied-computational:monte-carlo-method` | Near-identical glosses, same O(1/√n) claim, same Metropolis–Ulam source. Merge into one (suggest applied-computational owns it; prob-stats cross-links). |
| `dynamics-differential-equations:numerical-solution-of-odes` ↔ `applied-computational:numerical-ode` | Both are "Euler + Runge–Kutta". Merge (applied-computational owns; dynamics cross-links). |
| `probability-statistics:entropy` ↔ `applied-computational:information-theory` | Both define Shannon entropy H = −Σ p log p with the same 1948 source. Keep `entropy` (the quantity) and refocus `information-theory` on coding/channel-capacity, or merge outright. |
| `analysis:convex-function` (aka "Convex Set") ↔ `geometry:convexity` | Overlapping: analysis node's aka claims convex sets, geometry node defines them. Split cleanly (sets → geometry, functions → analysis) and cross-link; fix analysis's dangling `geometry:convex-geometry` → `convexity`. |
| `discrete-combinatorics:permutation` ↔ `algebra:permutation-group` | Substantial overlap (both define S_n and cycle decomposition). Acceptable as counting-view vs. group-view, but each must link the other's *real* id (currently both link nonexistent aliases `algebra:symmetric-group`, `discrete-combinatorics:permutation-enumeration`). |
| `linear-algebra:least-squares` ↔ `probability-statistics:linear-regression` | Deliberate algebra-vs-statistics split — fine — but `least-squares` links dangling `PROBABILITY-STATISTICS:regression`; point it at `linear-regression`. |
| `linear-algebra:inner-product-space` ↔ `analysis:hilbert-space` | Fine as pair (incomplete vs. complete) — but hilbert-space's aka "Inner Product Space" should go; link the two nodes. |
| `analysis:asymptotic-analysis` ↔ `applied-computational:computational-complexity` | Overlap on Big-O; acceptable, ensure mutual links (currently only one-directional). |

---

## 3. Unresolved placeholder / dangling references

**97 distinct dangling references** were found (full machine-checked list below). Two style bugs first:

- **Casing inconsistency**: linear-algebra.json uses `ANALYSIS:banach-space`-style UPPERCASE prefixes;
  every other file uses lowercase. Normalize to lowercase.
- **Prefix convention inconsistency**: cross-territory prereqs are sometimes bare (`induction`,
  `metric-space`) and sometimes prefixed (`algebra:field-extension`). Since ids are (meant to be)
  globally unique, pick one convention — recommend bare ids everywhere and drop prefixes entirely,
  which also eliminates the entire alias-guessing failure class below.

### 3a. Dangling **prereqs** (block the learning graph — fix first)

| Placeholder | Used by | Canonical resolution |
|---|---|---|
| `analysis:complex-analysis` | number-theory: riemann-zeta-function, modular-forms | → `holomorphic-function` (+ `cauchy-integral-theorem`) |
| `analysis:multivariable-calculus` | dynamics: hamiltonian-system, partial-differential-equation | → `partial-derivative` + `multiple-integral` |

### 3b. Dangling cross_links that have an existing canonical id (pure renames)

| Placeholder | Canonical id |
|---|---|
| `linear-algebra:system-of-linear-equations` | `linear-system` |
| `analysis:fourier-series`, `ANALYSIS:fourier-series` | `fourier-analysis` |
| `number-theory:prime-number-theorem` | `prime-distribution` |
| `number-theory:primitive-root` | `multiplicative-order` |
| `number-theory:euler-totient` | `eulers-totient-function` |
| `number-theory:algebraic-number-theory` | `algebraic-number-field` |
| `algebra:unique-factorization-domain` | `unique-factorization` |
| `algebra:representation-theory` | `group-representation` |
| `algebra:symmetric-group` | `permutation-group` |
| `ALGEBRA:quotient-structure`, `ALGEBRA:first-isomorphism-theorem` | `quotient-group` |
| `discrete-combinatorics:burnside-counting` | `polya-enumeration` |
| `discrete-combinatorics:permutation-enumeration` | `permutation` |
| `discrete-combinatorics:lattice` | `poset` (approx.) |
| `dynamics-differential-equations:linear-ode-systems` | `system-of-odes` |
| `dynamics-differential-equations:stability-theory` | `stability` |
| `dynamics-differential-equations:dynamical-system` | `flow` |
| `dynamics-differential-equations:oscillation` | `harmonic-oscillator` |
| `foundations:computability` | `decidability` |
| `foundations:order-theory` | `partial-order` |
| `foundations:zorns-lemma` | `axiom-of-choice` (Zorn is an aka) |
| `geometry:fractal` | `fractal-geometry` |
| `geometry:convex-geometry` | `convexity` |
| `geometry:polyhedra` | `polygons-polyhedra` |
| `geometry:isometry-group` | `isometry` |
| `geometry:algebraic-variety` | `algebraic-geometry` |
| `geometry:riemannian-metric` | `riemannian-geometry` |
| `GEOMETRY:volume` | `area-volume` |
| `topology:surfaces` | `surface` |
| `probability-statistics:binomial-distribution` | `bernoulli-binomial` |
| `PROBABILITY-STATISTICS:regression` | `linear-regression` |
| `PROBABILITY-STATISTICS:covariance-matrix`, `PROBABILITY-STATISTICS:uncorrelated` | `covariance-correlation` (approx.) |
| `probability-statistics:stable-matching` | `discrete-combinatorics` `matching` (approx.) |
| `applied-computational:public-key-cryptography` | `rsa-cryptosystem` (number-theory) |
| `applied-computational:nash-equilibrium` | `game-theory` |
| `applied-computational:algorithm-analysis` | `computational-complexity` |
| `applied-computational:graph-search` | `graph-algorithms` |
| `applied-computational:deep-learning` | `neural-network` |
| `applied-computational:numerical-approximation` | `interpolation` |
| `applied-computational:numerical-analysis` | `numerical-stability` or `numerical-ode` |
| `ANALYSIS:jacobian` | `partial-derivative` |
| `ANALYSIS:banach-space` | `banach-space` (case fix only) |
| `ANALYSIS:hilbert-space` | `hilbert-space` (case fix only) |
| `ANALYSIS:spectral-theory` | `hilbert-space` (approx.) |
| `ANALYSIS:second-derivative-test` | `convex-function` (approx.) |
| `analysis:triangle-inequality` | `norm` (approx., pending an Inequalities node) |
| `analysis:exponential-function` | **missing — create** (see §1.1) |
| `mathematical-practice:proof-techniques` | `direct-proof` (or spine `proof`) |
| `geometry:gauss-bonnet-theorem` | **missing — create** (both endpoints exist) |
| `topology:winding-number` | **missing — create** (see §1.7) |
| `dynamics-differential-equations:vector-field` | **missing — create** (or `slope-field`) |
| `probability-statistics:conditional-expectation` | **missing — create** (see §1.4) |

### 3c. Dangling links to genuinely absent concepts (decide: create node or drop link)

Application-flavored stubs concentrated in applied-computational and geometry:
`applied-computational:{cryptography, error-correcting-codes, principal-component-analysis,
quantum-computing, quantum-mechanics, topological-data-analysis, data-structures, data-compression,
network-science, mathematical-finance, computer-graphics, constraint-satisfaction, assignment-problem,
traveling-salesman, randomized-algorithms, dna-topology, curse-of-dimensionality, logarithmic-scale,
physics-gauge-theory}`; `geometry:{differential-form, de-rham-cohomology, sheaf-cohomology,
symplectic-geometry, gauge-theory, conformal-map, finite-projective-planes}`;
`analysis:{calculus-of-variations, distribution-theory}`; `number-theory:{szemeredi-theorem,
additive-combinatorics, equidistribution, partition-congruences}`; `probability-statistics:{percolation,
random-matrix-theory, probabilistic-heuristics, moment-generating-function}`;
`dynamics-differential-equations:{general-relativity, orbital-mechanics, phase-transition}`;
`foundations:{universal-algebra, infinite-ramsey}`; `discrete-combinatorics:` (none missing inbound).

Recommendation for v0.1: create the ~8 flagged in §1; for the rest either drop the link or adopt an
explicit `"planned:"` prefix so tooling can distinguish intent from typo.

---

## 4. Territory imbalances

Node counts (territory + spine): number-theory **34**, linear-algebra **34**, probability-statistics
**33**, analysis **31**, foundations 30, algebra 30, dynamics 29, mathematical-practice 29, geometry 28,
applied-computational 27, **discrete-combinatorics 24, topology 24**.

- **Applied-computational is the most under-supplied territory relative to demand.** It receives by far
  the most dangling inbound references (~25 of the 97): other territories keep promising payoffs
  (cryptography, codes, PCA, TDA, quantum computing, network science, finance) that it doesn't deliver.
  It is also lopsided toward numerical analysis (10 of 24 nodes) with zero cryptography/coding despite
  number-theory building an entire RSA pipeline pointing at it.
- **Geometry is thin at the top.** 7+ dangling inbound refs (differential forms, Gauss–Bonnet,
  symplectic, de Rham, sheaves, conformal maps): the map's differential-geometry ceiling
  (riemannian-geometry) has no supporting floor of forms/integration-on-manifolds, even though Stokes
  in analysis assumes it.
- **Topology is the thinnest territory and has no on-ramp.** 22 nodes, lowest level 3, median level ~6.
  Every other territory has level 0–2 entry points; topology starts at "topological invariant". One or
  two intuitive level-1/2 nodes (e.g., "Möbius band & one-sidedness", "deformation & rubber-sheet
  equivalence") would fix the cliff.
- **Number theory is the deepest and arguably slightly bloated at the research edge** (levels 7–8:
  p-adics, algebraic number fields, elliptic curves, modular forms — 5 nodes) while analysis, its
  stated prerequisite supplier, lacks even the exponential function. Depth asymmetry, not a defect per
  se, but v0.1 polish is better spent on the gaps above than more NT depth.
- **Mathematical-practice** is fine in size but 10 of 26 nodes are Polya-style heuristics of similar
  granularity; could compress later. Not urgent.
- **Spine skew**: spine allocates 6 nodes to algebra/analysis but only 1 to dynamics and 2 each to
  topology/discrete — defensible pedagogically, worth a deliberate pass.

---

## 5. Ten highest-leverage concepts across the whole map

1. **`function` (foundations, spine)** — the universal glue; direct or transitive prerequisite of
   nearly every node in all 12 territories.
2. **`limit` (analysis, spine)** — the gateway move of analysis; unlocks continuity, derivative,
   integral, and even p-adic numbers and fractals in other territories.
3. **`equivalence-relation` (foundations, spine)** — the quotient-construction engine behind
   modular arithmetic, quotient groups/rings, quotient topologies, and cardinality.
4. **`isomorphism` (algebra, spine)** — the map's master template for "sameness"; homeomorphism,
   isometry, and the Erlangen program are all territory-local instances of it.
5. **`group` (algebra, spine)** — symmetry made algebraic; load-bearing in geometry (Erlangen),
   topology (π1), number theory (units mod n), combinatorics (Burnside), and dynamics (flows).
6. **`vector-space` (linear-algebra, spine)** — the workhorse abstraction; function spaces, field
   extensions, representation theory, and PDE methods all stand on it.
7. **`eigenvalue-eigenvector` (linear-algebra, spine)** — the map's single most-crossed bridge:
   stability of ODEs, Markov chain steady states, spectral theorem, PCA/SVD, quantum mechanics.
8. **`graph` (discrete-combinatorics, spine)** — the universal model of relational structure;
   feeds algorithms, networks, Markov chains, topology (Euler characteristic), and Ramsey theory.
9. **`random-variable` (probability-statistics, spine)** — the pivot from measure-theoretic
   foundations to all of statistics, stochastic processes, information theory, and Monte Carlo.
10. **`fourier-analysis` (analysis)** — the busiest inter-territory junction in the file data itself
    (referenced by dynamics ×4, geometry, linear-algebra, NT via modular forms, probability via CLT,
    computation via FFT); decomposition-into-frequencies is the shared trick of half of applied math.

---

## 6. Priority fixes for v0.1 (condensed)

1. **Fix the two id collisions** (`diagonalization`, `dimension`) — they silently corrupt any
   id-keyed lookup or graph build. (§2)
2. **Resolve all 97 dangling refs**: the two dangling *prereqs* first, then the ~45 pure renames in
   §3b (mechanical), then decide create-vs-drop for §3c; normalize prefix casing/convention.
3. **Add the 8 missing high-embarrassment concepts**: exponential function (e), fundamental
   inequalities (Cauchy–Schwarz/AM–GM), differential forms, conditional expectation, winding
   number, Laplace equation (+ transform), calculus of variations, error-correcting codes; plus
   Gauss–Bonnet and PCA as near-free wins (all endpoints/prereqs already exist).
4. Merge the 4 clear duplicate pairs (poset, Monte Carlo, numerical ODEs, entropy). (§2)
5. Rebalance: grow applied-computational's application payoffs, give topology a low-level on-ramp,
   backfill geometry's differential-forms floor. (§4)
