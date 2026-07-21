# Adversarial Review — Applied & Computational Mathematics Territory

Reviewer: adversarial review pass (automated agent)
Files reviewed: `data/territories/applied-computational.json`, `data/spine.json` (plus cross-checks against `dynamics-differential-equations.json`, `discrete-combinatorics.json`, `linear-algebra.json`, `analysis.json`, `foundations.json`)
Date: 2026-07-21

Overall: a strong territory file. Leveling is clean (no prereq level inversions anywhere — every prereq resolves at or below its dependent's level), intuition glosses are consistently image-first, and all three live-fetched resource URLs resolve to exactly the claimed content. The real problems are graph-integrity ones: two cross-links point at a node ID that doesn't exist, and the territory's Numerical ODE Solvers node is a flat duplicate of a node in the dynamics territory. Below that, a cluster of moderate boundary/coverage issues with the discrete-combinatorics territory and a few gloss nitpicks.

**Issue count: 11** (2 severe, 4 moderate, 5 minor)

---

## SEVERE

### S1. Dangling cross-link: `dynamics-differential-equations:stability-theory` does not exist
Both `numerical-ode` and `control-theory` cross-link `dynamics-differential-equations:stability-theory`. The dynamics territory has no such ID — its node is `stability` (and separately `linearization`). Any renderer or graph validator resolving cross-links will hit a broken edge twice. Fix: change both references to `dynamics-differential-equations:stability`.

### S2. Duplicate concept across territories: `numerical-ode` vs `dynamics-differential-equations:numerical-solution-of-odes`
This territory's `numerical-ode` ("Euler's method", "Runge-Kutta methods", "stiff solvers", level 5) and dynamics' `numerical-solution-of-odes` ("Euler's method", "Runge–Kutta methods", "ODE solvers", level 4) are the same concept as two independent nodes: overlapping aka lists, near-identical formal glosses (time-stepping schemes, Euler → Runge-Kutta, order and stability), and even the same Wikipedia Runge–Kutta resource URL. They sit at **conflicting levels** (5 vs 4) and neither node references the other. Worse, the dynamics entry cross-links `applied-computational:numerical-analysis` — an ID that does not exist in this file — suggesting the two territories were drafted against different versions of each other. One node must own the concept (this territory's richer entry is the better keeper, since it carries the discretization/stability prereq chain and stiff solvers), with the other reduced to a cross-link or alias.

---

## MODERATE

### M1. `numerical-pde` never requires knowing what a PDE is
Its prereqs are `discretization`, `differential-equation` (spine — a generic/ODE-flavored node), `analysis:partial-derivative`, and `linear-algebra:linear-system`. But the atlas *has* a PDE node — `dynamics-differential-equations:partial-differential-equation` (plus `heat-equation`, `wave-equation`) — and this entry, whose intuition gloss is literally about heat spreading and fluids flowing, doesn't reference any of them as prereq or cross-link. A learner's prerequisite trail can reach finite element methods without ever meeting a PDE. Add `dynamics-differential-equations:partial-differential-equation` as a prereq.

### M2. `graph-algorithms` overlaps `discrete-combinatorics:network-flow` and ignores the discrete territory entirely
The formal gloss claims maximum flow / Ford-Fulkerson / max-flow min-cut for this node, but `discrete-combinatorics` has a dedicated `network-flow` node (and `tree`, `matching`, `graph-connectivity` — all directly relevant to spanning trees, flows, and matchings named here). `graph-algorithms` cross-links none of them; its only graph-side link is the spine `graph`. Not a full duplicate, but the ownership boundary for network flow is undeclared, so a renderer will show max-flow min-cut in two territories with no edge between them. Declare ownership (flow theory in discrete, flow *algorithms* here) and add the cross-links.

### M3. Missing major concept: integer / combinatorial optimization
The optimization spine here goes LP → convex → gradient descent, i.e. entirely continuous. Integer programming / combinatorial optimization (MSC 90C10, 90C27) — branch and bound, LP relaxations, the workhorse of scheduling, routing, and OR practice — appears in no territory (discrete-combinatorics has matching and network flow but no optimization framing). For a territory that includes `p-vs-np` and `linear-programming`, the node that connects them (most famous NP-hard problems *are* combinatorial optimization problems) is conspicuously absent.

### M4. Missing concepts: divide-and-conquer and greedy algorithm paradigms
The file commits to CS algorithmic content at depth (complexity, P vs NP, dynamic programming, graph algorithms), so covering exactly one of the three canonical design paradigms is a coverage hole: `dynamic-programming` is a node, but divide-and-conquer (which the FFT entry silently depends on — its gloss opens "A divide-and-conquer trick") and greedy algorithms (which Dijkstra, Kruskal, and Prim in `graph-algorithms` all instantiate) have no home anywhere in the atlas. Either add a paradigms node (or two) or document the exclusion as deliberate.

---

## MINOR

### m1. `neural-network` lists single-variable `derivative` as prereq but backpropagation is multivariable
Backprop is the chain rule over partial derivatives of a many-variable loss; `analysis:partial-derivative` (or `analysis:gradient`, already required by its prereq `gradient-descent`) belongs in prereqs, not just cross-links. Low stakes because the gradient requirement arrives transitively, but the direct prereq list under-states what the concept needs.

### m2. `linear-programming` intuition gloss over-claims: "the best point always sits at a corner of the fence"
False for unbounded problems (no best point), feasible regions without vertices, and degenerate objectives where an entire face is optimal ("a corner" is then merely *among* the optima). The standard careful phrasing — "if there's a best point, one always sits at a corner" — costs three words and keeps the image.

### m3. `computational-complexity` formal gloss defines classes via "the best algorithm solving them"
Complexity classes are defined by the *existence* of an algorithm within a resource bound, not by a best algorithm — by Blum's speedup theorem, some problems provably have no best algorithm. "…by the asymptotic resources sufficient to solve them" is both correct and simpler.

### m4. `root-finding` glosses describe only Newton despite aka claiming bisection and fixed-point iteration
"Slide down the tangent line… each step roughly doubles your correct digits" is Newton-specific (and even for Newton only near a simple root); bisection gains one bit per step and involves no tangents. Either narrow the aka list or widen the gloss ("bracket-and-halve, or slide down the tangent…").

### m5. Two book "resources" link to Wikipedia articles *about* the books, not the texts
"Sipser, Introduction to the Theory of Computation" and "Cover & Thomas — Elements of Information Theory" both resolve to Wikipedia pages describing the books (`type: "text"` over-promises). Not fake links, but a learner clicking through gets a book review, not a resource. Retitle ("Wikipedia — about Sipser's textbook") or link a legitimate open resource instead.

---

## Checks that PASSED

- **Leveling invariant:** resolved every prereq (spine + cross-territory) to its declared level; no prereq sits above its dependent. Same-level pairs (numerical-integration ← interpolation at 4, monte-carlo ← random-variable/expectation at 4, information-theory ← probability-space at 5, machine-learning ← least-squares at 5) are all pedagogically defensible.
- **Levels vs standard curricula:** floating point at 3, root-finding/quadrature/interpolation at 4, numerical stability and FFT at 5, Krylov/FEM/convex/control at 6, inverse problems at 7 — tracks a real undergrad-to-grad numerical/applied sequence well. Nothing wildly off.
- **Cross-territory references:** all 21 prefixed IDs checked against their territory files; every one resolves **except** the two S1 `stability-theory` references.
- **Resource URLs (spot-checked 3 via live fetch):** `claymath.org/millennium/p-vs-np/` is the live Clay Millennium Problem page; `3blue1brown.com/lessons/newtons-fractal` is the genuine Newton's-fractal lesson (Oct 2021); the CMU `painless-conjugate-gradient.pdf` is genuinely Shewchuk's paper (503 KB PDF). Remaining URLs (Boyd cvxbook, Trefethen ATAP, hastie.su.domains, deeplearningbook.org, float.exposed, Chebfun, VisuAlgo, OCW course roots, Oracle Goldberg mirror, Harvard Shannon PDF) are well-known stable destinations. No fake or dead links found.
- **Formal glosses:** aside from m2/m3, checked and correct — backward-stability definition, Newton quadratic convergence at simple roots, Gaussian quadrature exactness framing, Lax-style consistency+stability→convergence, FFT-as-polynomial-evaluation at roots of unity, Monte Carlo 1/√N via LLN+CLT, Nash existence in mixed strategies for finite games (correct statement of Nash 1950), Tikhonov functional, KKT/duality claims.
- **In-territory duplicates:** none. root-finding (nonlinear scalar) vs iterative-methods (linear systems) are properly distinct; LP / convex / gradient-descent layer cleanly over the spine `optimization` node; machine-learning vs neural-network are correctly separated (theory vs architecture).
- **Intuition glosses:** uniformly image-first plain language — no circularity, no jargon-first openings. Several (FFT, Monte Carlo, inverse problems, convex "no false valleys") are excellent.
