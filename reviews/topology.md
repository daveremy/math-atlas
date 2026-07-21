# Adversarial Review — Topology Territory

**File reviewed:** `data/territories/topology.json` (against `data/spine.json`)
**Reviewer:** adversarial review pass, 2026-07-21
**Verdict:** Content quality is high — glosses are accurate and genuinely image-first, resources are real. But the level numbering is internally broken (prereqs above their dependents in six places), one flagship concept is missing entirely, and six cross_links point at ids that exist nowhere in the dataset.

**Issue count: 12** (4 severe, 5 moderate, 3 minor)

---

## Severe

### S1. Systematic level inversions — prereqs sit at higher levels than their dependents
Six concepts list prerequisites whose level is *higher* than the concept's own level. Any learner path or topological sort ordered by `level` is broken:

| Concept | Level | Offending prereq | Prereq level |
|---|---|---|---|
| `open-closed-sets` | 4 | `metric-space` | 5 |
| `closure-interior-boundary` | 5 | `topological-space` | 6 |
| `surface` | 4 | `quotient-space` | 6 |
| `orientability` | 5 | `quotient-space` (6), `surface` (4) | 6 |
| `jordan-curve-theorem` | 5 | `connectedness` (6), `topological-space` (6) | 6 |
| `knot-theory` | 5 | `homeomorphism` | 6 |

Either these concepts should be re-leveled upward, or (more likely, matching standard curricula) `topological-space` (spine, level 6) and `metric-space` (spine, level 5) are leveled too high relative to the territory's internal numbering. Standard undergrad ordering is metric spaces → open/closed sets → topological spaces → the rest; the numbers must reflect one consistent scheme.

### S2. `topological-invariant` mis-leveled at 3
Its own formal gloss defines it as "a property preserved by homeomorphism" — but `homeomorphism` is level 6 and `topological-space` is level 6. A level-3 node whose definition requires two level-6 nodes is wildly off. Fine as an intuitive front-door concept, but then its prereqs/level must say so honestly (either raise the level or restructure as an informal entry node preceding the formal one).

### S3. Missing MAJOR concept: Poincaré conjecture / 3-manifold topology
The single most famous result in topology — the only solved Millennium Prize problem (Perelman, 2003) — is absent, and there is no node for 3-manifolds or geometrization at all. The map covers 2-manifolds thoroughly (surface, classification-of-surfaces) then jumps to fiber bundles. A serious topology map must have a Poincaré-conjecture (or 3-manifolds) node; it is also the natural payoff for `fundamental-group` ("simply connected" appears in its formal gloss with nowhere to go).

### S4. Six dangling cross_links — referenced ids exist nowhere in the dataset
Verified by grep across all territory files and the spine. Missing targets:
- `geometry:gauss-bonnet-theorem` (from euler-characteristic)
- `geometry:de-rham-cohomology` (from homology)
- `geometry:gauge-theory` (from fiber-bundle)
- `applied-computational:nash-equilibrium` (from brouwer-fixed-point)
- `applied-computational:topological-data-analysis` (from simplicial-complex, homology)
- `applied-computational:dna-topology` (from knot-theory)

There is no `applied-computational.json` territory file at all, so every `applied-computational:*` link is broken by construction. (`analysis:intermediate-value-theorem`, `geometry:curvature`, and `algebra:galois-theory` do resolve.)

---

## Moderate

### M1. `euler-characteristic` — level-3 node with a graduate-flavored formal gloss and a missing prereq
The formal gloss invokes CW decompositions, Betti numbers, and homotopy invariance, none of which are intelligible at level 3, and `simplicial-complex` (level 6) — which the gloss depends on — is not a prereq. The classical V−E+F polyhedron framing justifies level 3; the formal gloss should be split or the gloss simplified with the CW/Betti content deferred to `homology`.

### M2. `jordan-curve-theorem` aka lists "Jordan-Schoenflies theorem"
Wrong alias. Jordan–Schoenflies is a strictly stronger, distinct theorem (the curve bounds a region homeomorphic to a disk — famously *false* in higher dimensions, cf. Alexander horned sphere, while Jordan's separation statement generalizes). Listing it as an aka teaches a false identification.

### M3. `simplicial-complex` aka lists "CW complex" and "cell complex"
CW complexes are a more general, genuinely different construction (cells attached by arbitrary continuous maps, not glued along faces). Conflating them as aliases is technically wrong; acceptable only if the node is explicitly a grouped "cell structures" node, which its formal gloss (pure simplicial) is not.

### M4. `knot-theory` aka lists "Jones polynomial"
The Jones polynomial is an invariant *within* knot theory, not another name for it. (Same pattern as M2/M3: the aka field is being used as a "related terms" dump.)

### M5. Secondary coverage gaps
No node (and no alias/mention) for: **Borsuk–Ulam theorem** (the standard companion to Brouwer, and the other big "antipodes" application of π1), **cohomology** (only reachable via the *dangling* de-rham link — homology alone is defensible for an atlas but the pointer should resolve somewhere), and **basis for a topology / metrizability** (the standard bridge concepts between metric-space and topological-space). None individually severe; together they thin the point-set-to-algebraic bridge.

---

## Minor

### m1. 3Blue1Brown resource link points at the superseded upload
`https://www.youtube.com/watch?v=AmgkSdhK4K8` resolves (verified by fetch) but the video is now titled "Who cares about topology? **(Old version)**" — 3B1B re-uploaded a revised version in 2024. Link works; should point to the current upload or note the title change.

### m2. Knot Atlas URL is plain `http://katlas.org/`
Site loads and is the real Knot Atlas (verified by fetch), but the URL should be https.

### m3. `compactness` prereq `sequence` fits the wrong definition
The formal gloss defines compactness via open covers; `sequence` as a prereq gestures at sequential compactness, which the node never states. Harmless but slightly incoherent — either mention Bolzano–Weierstrass/sequential compactness in the gloss or drop the prereq.

---

## Checks that passed

- **URL spot-checks (3/3 real):** Hatcher's Algebraic Topology page (pi.math.cornell.edu), Knot Atlas (katlas.org), 3B1B video — all load and are what they claim. Topology Without Tears and all Wikipedia URLs are well-known and correctly formed.
- **Glosses:** No factually wrong or circular glosses found. Intuition glosses are consistently image-first (rubber sheets, breathing room, LEGO, unrolled spirals, stirred coffee) — this is the file's strength. All formal glosses checked are mathematically correct (Heine–Borel statement, Tychonoff, covering-space Galois correspondence, classification theorem, χ = Σ(−1)^k c_k).
- **Duplicates:** None. `surface` vs `classification-of-surfaces`, and the bundled `product-topology` (subspace + product + Tychonoff) node, are distinct and reasonably scoped.
- **Prereq referential integrity within the map:** every `prereqs` id resolves to the territory file or the spine.
