# Adversarial Review: Geometry Territory

Reviewer: adversarial review subagent
Date: 2026-07-21
Files reviewed: `data/territories/geometry.json`, `data/spine.json`
Verdict: Solid territory overall — glosses are consistently image-first, prereq IDs all resolve against the spine, and no fake resources were found. But there are 2 severe structural problems and a handful of moderate/minor issues.

## Severe

### 1. Congruence / Isometry circular definition with inverted levels
- `congruence` (level 1) has this formal gloss: *"Two figures are congruent iff some isometry maps one onto the other..."* — it is **defined in terms of isometry**.
- `isometry` (level 3) lists `congruence` as a **prereq**.
- So the level-1 concept's definition depends on a level-3 concept that in turn claims to depend on the level-1 concept. A learner walking the DAG hits a forward reference two levels up, and the dependency arrow points the wrong way relative to the glosses. Ironically, both nodes cite Common Core transformational geometry, which resolves this by teaching rigid motions *first* and defining congruence from them.
- Fix options: (a) make congruence's formal gloss self-contained at level 1 (superposition / equal corresponding parts) and keep isometry later, or (b) move isometry down and make it a prereq of congruence, matching the cited transformational-geometry sources. Either way, remove the cycle.

### 2. Affine geometry is missing but load-bearing
- The `erlangen-program` formal gloss orders geometries as **"Euclidean ⊂ affine ⊂ projective by group inclusion"** — but there is no `affine-geometry` concept anywhere in the territory or spine. The map's own capstone node references a geometry the map never defines. For a serious atlas, affine geometry (or at least affine transformations) is a standard rung between Euclidean and projective and should exist as a node, sitting naturally at level 4-5 between `isometry` and `projective-geometry`.

## Moderate

### 3. `similarity` has the wrong number prereq
Prereqs are `congruence, rational-numbers`. But similarity ratios are generically **irrational** (the diagonal-to-side ratio of a square is √2; similar right isoceles triangles realize it). The honest prereq is `real-numbers` (spine, level 2 — still below similarity's consumers). As written, the map implies proportionality theory lives inside Q, which is exactly the error that broke the Pythagorean school.

### 4. Missing: computational / discrete geometry
No node for convex hulls, Voronoi diagrams, Delaunay triangulations, or computational geometry generally — despite the atlas having an `applied-computational` territory and this territory already cross-linking into it (`applied-computational:computer-graphics`, `curse-of-dimensionality`). For a modern "serious map," a `computational-geometry` node (level ~4-5) is a major omission; `convexity` is already present as its natural prereq.

### 5. Level gap: nothing at level 6
The territory jumps from level 5 (`curvature`, `geodesic`, `projective-geometry`, `erlangen-program`) straight to level 7 (`riemannian-geometry`, `algebraic-geometry`), and the spine's `manifold` is also level 7 while being a prereq of same-level `riemannian-geometry`. Either `manifold` should be level 6 (it is the bridge concept, and `topological-space` in the spine is level 6) or a level-6 bridge node is missing. As is, the two capstones have no on-ramp tier.

## Minor

### 6. `circle` aka includes "disk"
A disk is the filled 2D region; a circle is its boundary curve. The formal gloss itself defines only the locus `{P : d(P,O) = r}` and then assigns it an "enclosed area," compounding the conflation. Drop "disk" from aka or add one clarifying clause.

### 7. `conic-sections` formal gloss: "classified up to isometry"
The clean three-way classification (ellipse / parabola / hyperbola) is an **affine** classification; up to isometry there is a continuum of classes (every eccentricity-and-scale combination is distinct). The gloss conflates type classification with congruence classification. Say "classified by type" or "up to affine equivalence."

### 8. `dimension` formal gloss outruns its prereqs
The gloss invokes "cardinality of a basis" of a vector space and Hausdorff dimension, but the only prereq is `coordinate-system` (level 1); `vector-space` is demoted to a cross-link. Either add `vector-space` as a prereq or soften the formal gloss for its level-3 position.

### 9. `dimension` / `fractal-geometry` overlap
Both nodes claim Hausdorff/fractal dimension (dimension's gloss and sources cite Hausdorff 1918; so does fractal-geometry). Not a duplicate, but the ownership boundary should be explicit — suggest `dimension` mentions it only as a pointer.

### 10. Generic Khan Academy landing-page URLs
Six concepts (`angle`, `congruence`, `similarity`, `area-volume`, `pythagorean-theorem`, `isometry`, plus `point-line-plane`) all cite the identical `khanacademy.org/math/geometry` landing page with "(X unit)" appended to the title. The URLs are real but do not deep-link to the named units — weak resources masquerading as targeted ones. Use actual unit URLs (e.g. `/math/geometry/hs-geo-congruence`).

### 11. `trigonometry` missing `function` prereq
Its own intuition gloss pivots on ratios "becoming functions," but `function` (spine, level 1) is not a prereq. Cheap fix.

## Checks that passed

- **Mis-leveling**: Levels 0-2 concepts track K-12 curricula well (angle 0, congruence/similarity/Pythagorean 1, trig/Euclidean geometry 2). `convexity` at 4 is defensible given the Helly/separation content. No wild mis-levels found beyond issues 1 and 5.
- **Prereq ID integrity**: Every prereq ID in geometry.json resolves to a concept in the territory or the spine. No dangling references.
- **Glosses**: Intuition glosses are uniformly image-first and non-circular (turn between rays, photographic enlargement, tiling a floor, dents, tiny rulers). No jargon-first violations found.
- **Resources (spot-checked via WebFetch)**:
  - `youtube.com/watch?v=lFlu60qs7_4` — verified: "How One Line in the Oldest Math Text Hinted at Hidden Universes" (Veritasium). Title matches.
  - `youtube.com/watch?v=GNcFjFmqEc8` — verified: "But why is a sphere's surface area four times its shadow?" (3Blue1Brown). Title matches.
  - `mathcs.clarku.edu/~djoyce/java/elements/elements.html` — verified: live web edition of Euclid's Elements with applet illustrations (Joyce's site).
  - Remaining URLs (Wikipedia, GeoGebra, Boyd & Vandenberghe cvxbook, Project Gutenberg #201 = Flatland) are well-known canonical addresses; no fabricated-looking URLs present.
- **Duplicates**: No true duplicates. congruence/isometry and similarity/"scaling" are deliberate paired granularity, acceptable once issue 1 is fixed.
- **Factual spot-checks**: Wantzel 1837, Fedorov 1891 wallpaper groups, Hausdorff 1918, Hutchinson 1981, Gauss 1827, Riemann 1854, Klein 1872, and the 2023 aperiodic monotile are all correctly attributed.

## Summary

| Severity | Count |
|---|---|
| Severe | 2 |
| Moderate | 3 |
| Minor | 6 |
| **Total** | **11** |
