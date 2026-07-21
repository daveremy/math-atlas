# Adversarial Review — Linear Algebra Territory

Reviewer: adversarial review pass (automated agent)
Files reviewed: `data/territories/linear-algebra.json`, `data/spine.json`
Date: 2026-07-21

Overall: this is a solid territory file. Coverage of the first-course core (systems → spaces → orthogonality → eigen-theory → SVD) is good, glosses are mostly genuinely image-first, and every resource URL spot-checked resolves to the claimed content. The problems are two leveling-invariant violations, one missing load-bearing concept (characteristic polynomial), and a handful of moderate/minor gloss and prereq issues.

**Issue count: 10** (3 severe, 3 moderate, 4 minor)

---

## SEVERE

### S1. Level inversion: `quadratic-form` (level 5) lists `spectral-theorem` (level 6) as a prereq
A prerequisite sits one level ABOVE the concept that depends on it, breaking the leveling invariant of the DAG. It is also pedagogically wrong: standard curricula (MIT 18.06 lecture 27 — the very resource this entry cites — and Strang) teach positive definiteness from symmetric matrices and eigenvalues, not gated on the full spectral theorem. The right prereqs are roughly `eigenvalue-eigenvector` (spine, level 5) + `dot-product`, with `spectral-theorem` as a cross-link. Knock-on effect: because `matrix-factorization` (level 5) lists `quadratic-form` as a prereq (for Cholesky), the level-6 spectral theorem is currently in the ancestry of a level-5 concept.

### S2. Level inversion: `norm` (level 3) lists `vector-space` (level 4) as a prereq
Same invariant violation: a level-3 concept requires a level-4 concept. Either drop `vector-space` from norm's prereqs (Euclidean length in R^n needs only `vector`, level 2) or raise norm's level. Given that norm's formal gloss states the abstract norm axioms on a general vector space, the entry is trying to be two concepts at once; the cleanest fix is prereq = `vector` + `dot-product` at level 3 with the abstract-norm material noted as pointing forward to `inner-product-space` / ANALYSIS.

### S3. Missing major concept: `characteristic-polynomial`
There is no in-territory route from `determinant` to `eigenvalue-eigenvector` (spine). The standard computational bridge — det(A − λI) = 0, the characteristic polynomial — is absent, yet `diagonalization` silently leans on it (it lists `determinant` as a prereq, presumably for exactly this reason) and `jordan-normal-form` presupposes it (algebraic vs. geometric multiplicity is unstatable without it). Any serious map covering diagonalization, spectral theorem, and Jordan form must have this node. (Cayley–Hamilton and minimal polynomial could hang off it; see M-tier below.)

---

## MODERATE

### M1. `linear-system` prereqs are inverted relative to standard curricula
It requires `vector` and `matrix`, but systems of equations are Algebra 1 material taught years before either — the entry's own Khan Academy resource is an Algebra 1 unit, and its own `sources` field says "standard secondary-school algebra curricula." The formal gloss also defines the concept jargon-first via "Ax = b" for what is billed as a level-2 concept. Suggest: no hard prereqs (or spine arithmetic only), with `matrix` as a cross-link; move the Ax = b framing to a note that the matrix view comes later.

### M2. `inner-product-space` formal gloss is technically wrong for the complex case
"Positive-definite (conjugate-)symmetric **bilinear** form" — a complex inner product is **sesquilinear** (conjugate-linear in one argument), not bilinear. A conjugate-symmetric form that were genuinely bilinear cannot be positive-definite over C. Should read "bilinear (real case) / sesquilinear (complex case)".

### M3. Missing concept: `cross-product`
Present in essentially every intro linear algebra / calc-III curriculum and in 3Blue1Brown's Essence series (ch. 10), used constantly in geometry and physics cross-links. Its absence is conspicuous next to `dot-product` at level 2-3. (Defensible to exclude from a pure LA map since it is R^3-specific, but then the exclusion should be a deliberate, documented choice.)

---

## MINOR

### m1. Missing second-tier concepts: `trace`, `cayley-hamilton` / minimal polynomial, pseudoinverse
Trace (basis-invariant, sum of eigenvalues) is cheap to add and heavily used. Cayley–Hamilton / minimal polynomial belongs with S3's characteristic polynomial in second-course material alongside Jordan form. The Moore–Penrose pseudoinverse would round out the SVD/least-squares cluster (may belong to applied-computational instead — either way, currently in neither).

### m2. MIT OCW "lecture" resources all point at the generic course landing page
Eleven entries cite specific lectures ("Lecture 15: Projections onto subspaces", etc.) but every URL is the bare course root `https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/`. Not fake — the page is real and correct — but the title over-promises what the link delivers. OCW has per-lecture pages (`/resources/lecture-N-...`); use them or retitle to "MIT OCW 18.06 (see Lecture N)".

### m3. Overlap: `gram-schmidt` vs `matrix-factorization` on QR
Gram–Schmidt's formal gloss claims "matrix form is the QR factorization," and `matrix-factorization` owns QR too. Not a duplicate node, but the ownership boundary should be explicit (e.g., QR named only in matrix-factorization, with gram-schmidt cross-linked as the algorithm behind it) so a renderer doesn't show QR twice.

### m4. `rank-nullity` intuition gloss is the weakest in the file
"Whatever directions a map doesn't crush must survive in its output — nothing is lost to bookkeeping" — the first clause is a decent image, but "nothing is lost to bookkeeping" is abstract filler, not an image. Something like "the directions a map crushes plus the directions that survive always add back up to the space you started with" keeps it image-first and states the actual conservation law.

---

## Checks that PASSED

- **Resource URLs (spot-checked 4 via live fetch):** Brunton YouTube playlist `PLMrJAkhIeNNSVjnsviglFoY2nXildDCcv` is genuinely his SVD series; Eigenchris playlist `PLJHszsWbB6hrkmmq57lX8BV-o-YIOFsiG` is genuinely "Tensors for Beginners"; `3blue1brown.com/lessons/span` is the claimed lesson; `linear.axler.net` is Axler's official LADR open-access site. All other URLs (Wikipedia, Khan Academy, matrixcalc.org, Trefethen's page, NumPy docs) are well-known stable destinations. No fake or dead links found.
- **Duplicates:** no true duplicate concepts (only the m3 QR boundary issue).
- **Other levels:** remaining levels track standard curricula well (span/basis/dimension at 4, eigen-cluster at 5, spectral/SVD/Jordan/dual/tensor at 6). Same-level prereqs (e.g., matrix-inverse ← gaussian-elimination, both 3) appear intentional and are fine.
- **Formal glosses:** aside from M2, checked and correct (determinant characterization, Eckart–Young statement in SVD, P⁻¹AP change-of-basis direction, rank–nullity statement, Jordan uniqueness up to block order).
- **Cross-territory prereq references** (`vector`, `matrix`, `vector-space`, `linear-transformation`, `eigenvalue-eigenvector`, `complex-numbers`) all resolve in `spine.json`.
