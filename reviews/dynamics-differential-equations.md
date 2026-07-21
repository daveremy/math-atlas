# Adversarial Review — Dynamics & Differential Equations Territory

**File reviewed:** `data/territories/dynamics-differential-equations.json` (against `data/spine.json` and sibling territory files)
**Reviewer:** adversarial review pass, 2026-07-21
**Verdict:** Strong territory overall — the concept selection tracks Strogatz + MIT 18.03 faithfully, glosses are genuinely image-first, and the flagship resources (Strogatz Cornell lectures, 3Blue1Brown, GeoGebra slope-field tool) all check out as real. But the level numbering is inverted in two places, one hard prereq points at an id that exists nowhere, the Laplace transform is missing from the entire atlas, the numerical-ODE node is duplicated across territories, and one resource URL resolves to the wrong course.

**Issue count: 14** (5 severe, 5 moderate, 4 minor)

---

## Severe

### S1. Level inversions — prereqs sit at higher levels than their dependents
Two concepts list prerequisites whose level is *higher* than the concept's own level, breaking any learner ordering derived from `level`:

| Concept | Level | Offending prereq | Prereq level |
|---|---|---|---|
| `slope-field` | 3 | `differential-equation` (spine) | 4 |
| `numerical-solution-of-odes` | 4 | `initial-value-problem` | 5 |

The first inversion also implicates `exponential-growth-decay` (level 3), which sits *below* the territory's own anchor concept `differential-equation` (spine, level 4) while being entirely about the ODE dy/dt = ky. Either the spine's `differential-equation` should drop to level 3 (matching AP Calculus, where slope fields and exponential models are taught), or these two nodes rise. The numerical case is independently wrong on curricular grounds: Euler's method is routinely taught (AP Calc, 18.03 unit 1) long before Picard–Lindelöf; existence-uniqueness should be a cross_link, not a prereq.

### S2. Dangling hard prereq: `analysis:multivariable-calculus` does not exist
Both `partial-differential-equation` and `hamiltonian-system` list `analysis:multivariable-calculus` as a **prereq** — a hard dependency — but no concept with that id exists in `analysis.json` or anywhere in the dataset (verified by grep across all 12 territory files + spine). The analysis territory instead has `partial-derivative`, `gradient`, and `multiple-integral`. The prereqs should point at `analysis:partial-derivative` (as `applied-computational.json`'s `numerical-pde` correctly does).

### S3. Missing MAJOR concept: Laplace transform
Absent from this territory and from the entire atlas (grep for "laplace" across all files returns nothing). The Laplace transform is a full unit of MIT 18.03 — a source this file cites eight times — and is the standard engineering route to constant-coefficient ODEs, transfer functions, and control theory (which the atlas *does* have, in applied-computational). A serious ODE map cannot omit it. Natural placement: level 5, prereqs `linear-ode` + `integral`, cross_links `applied-computational:control-theory`, `analysis:fourier-analysis`.

### S4. Duplicate concept across territories: `numerical-solution-of-odes` vs `applied-computational:numerical-ode`
`applied-computational.json` contains `numerical-ode` ("Numerical ODE Solvers", level 5) covering exactly the same content — Euler and Runge–Kutta stepping — as this territory's `numerical-solution-of-odes` (level 4). Same concept, two ids, two different levels, and neither node cross-links the other. One should own the concept and the other should reference it (or be deleted).

### S5. Wrong resource URL: Complexity Explorer link resolves to a different course
`iterated-map` cites "Complexity Explorer — Introduction to Dynamical Systems and Chaos (Feldman)" at `https://www.complexityexplorer.org/courses/144-introduction-to-dynamical-systems-and-chaos`. Fetched 2026-07-21: the page that loads is **"Introduction to Complexity" (Melanie Mitchell / Santiago Guisasola)** — a different course by a different instructor. The course id/slug is wrong; Feldman's course lives under a different id and the link should be corrected to the current offering.

---

## Moderate

### M1. Seven dangling cross_links
Verified by grep across all territory files and the spine. Missing targets, with the near-miss real id where one exists:
- `analysis:fourier-series` (from harmonic-oscillator, partial-differential-equation, heat-equation, wave-equation) — analysis has `fourier-analysis`
- `analysis:exponential-function` (from exponential-growth-decay) — no such node
- `geometry:fractal` (from attractor) — geometry has `fractal-geometry`
- `geometry:symplectic-geometry` (from hamiltonian-system) — no such node
- `applied-computational:numerical-analysis` (from numerical-solution-of-odes) — no such node; nearest is `numerical-ode`/`numerical-stability`
- `applied-computational:mathematical-finance` (from stochastic-differential-equation) — no such node
- `number-theory:equidistribution` (from ergodic-theory) — no such node

The `fourier-series` case is the worst since it recurs four times.

### M2. Inbound id mismatch: other territories reference `dynamics-differential-equations:stability-theory`
`applied-computational.json` (`numerical-ode`, `control-theory`) links to `dynamics-differential-equations:stability-theory`, but this territory's id is `stability`. Whichever file is wrong, the id contract is broken in both directions; flagged here so the rename (or alias) is decided once.

### M3. Missing concept: Laplace's equation / harmonic functions
`partial-differential-equation`'s own formal gloss introduces the elliptic/parabolic/hyperbolic trichotomy, and the territory then provides the parabolic exemplar (heat) and hyperbolic exemplar (wave) but no elliptic one. Laplace's equation ∇²u = 0 is the third member of the canonical trio in every PDE curriculum; the classification currently points at a hole.

### M4. `limit-cycle` formal gloss overstates Poincaré–Bendixson
"the Poincaré–Bendixson theorem guarantees one [an isolated closed orbit] inside any trapping region containing no equilibria" — the theorem guarantees a *closed orbit* (periodic orbit), not necessarily an isolated one. As written in a node whose subject is defined by isolation, the gloss claims more than the theorem gives.

### M5. `lyapunov-exponent` intuition contradicts its formal gloss
Intuition says the divergence rate is "measured in doublings per unit time"; the formal gloss defines λ with a natural logarithm, i.e. e-foldings per unit time. Doublings would be λ/ln 2. Either drop "doublings" or say "e-foldings"; a gloss pair shouldn't disagree about units.

---

## Minor

### m1. "Basin of attraction" listed as an aka on two different nodes
Both `stability` and `attractor` carry "Basin of attraction" in their aka lists. Search/alias resolution will be ambiguous; it belongs on `attractor` (or as its own node), not both.

### m2. `exponential-growth-decay` formal gloss assumes y₀ > 0
"growing without bound for k > 0 and decaying to zero for k < 0" is false for y₀ ≤ 0 (y₀ = 0 stays at zero; y₀ < 0 diverges to −∞). Trivial fix: "for y₀ > 0" or "in magnitude".

### m3. `lyapunov-exponent` prereq on `chaos` is borderline circular
`chaos` cross-links to `lyapunov-exponent` as its quantitative signature, while `lyapunov-exponent` hard-requires `chaos`. Pedagogically defensible, but the exponent is definable for any smooth system; a soft cross_link both ways would be cleaner than a hard prereq.

### m4. Secondary coverage gaps
Defensible omissions, listed for completeness: integrating factor / first-order linear method (only implicitly inside `linear-ode`), boundary value problems & Sturm–Liouville theory (natural bridge to Fourier series), stable/unstable manifolds (used implicitly by `linearization`'s Hartman–Grobman gloss), KAM theory (natural capstone next to `hamiltonian-system` and `ergodic-theory`).

---

## What checked out

- **Resources spot-checked live (2026-07-21):** Strogatz Cornell playlist `PLbN57C5Zdl6j_qJA-pARJnKsmROzPnO9V` resolves to "Nonlinear Dynamics and Chaos - Steven Strogatz, Cornell University" (Cornell MAE) ✓; GeoGebra `W7dAdgqc` is a real slope-field plotter (Adrian Jannetta) ✓; 3Blue1Brown `p_di4Zn4wz4` = "Differential equations, a tourist's guide | DE1" ✓; Veritasium `ovJcsL7vyrk` = "This equation will change how you see the world (the logistic map)" ✓. Remaining URLs (Paul's Notes, MIT OCW 18.03SC, myPhysicsLab, Falstad, Øksendal Springer DOI 978-3-642-14394-6, Susskind Theoretical Minimum, Wikipedia/Scholarpedia) match known-good canonical URLs by inspection.
- **Glosses:** consistently image-first (marble-in-a-bowl for stability, strobe-light for Poincaré map, "fruit fly of chaos theory" for the logistic map); no circular or jargon-first intuition glosses found beyond the M4/M5 precision issues.
- **Leveling elsewhere:** the 3→7 progression (AP-Calc entry → ergodic theory/SDEs) matches standard curricula apart from S1; Feigenbaum δ ≈ 4.669, Hartman–Grobman statement, Birkhoff ergodic theorem, Itô SDE form, and d'Alembert's formula are all stated correctly.
- **Internal graph:** all intra-territory and spine-targeted prereqs/cross_links resolve (the breakages are exclusively cross-territory, per S2/M1/M2).
