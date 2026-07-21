# Adversarial Review — Probability & Statistics Territory

**File reviewed:** `data/territories/probability-statistics.json` (against `data/spine.json`)
**Reviewer:** adversarial review pass, 2026-07-21
**Verdict:** Strong territory overall — glosses are among the best in the atlas (genuinely image-first: "tasting a well-stirred spoonful," "the coin has no memory," "nature's default histogram"), all spot-checked resource URLs are real, and there are no duplicate concepts. But two level inversions break level-ordered traversal, two genuinely major concepts (joint distributions, conditional expectation) are missing — one of them hidden inside another concept's `aka` — and the cross-link reference scheme has one dangling id plus three ids that only resolve by violating the file's own namespacing convention.

**Issue count: 11** (3 severe, 4 moderate, 4 minor)

---

## Severe

### S1. Level inversions — two concepts sit below their own prerequisites
Verified programmatically against the spine + all territory files:

| Concept | Level | Offending prereq | Prereq level |
|---|---|---|---|
| `variance` | 3 | `expectation` (spine) | 4 |
| `normal-distribution` | 3 | `probability-distribution` | 4 |

Any learner path or topological sort ordered by `level` is broken at these two nodes. Standard curricula (AP Stats, MIT 18.05, Blitzstein & Hwang) do teach variance and the normal curve early, so the likelier fix is that spine's `expectation` (L4) and this file's `probability-distribution` (L4) are numbered too high relative to the territory's internal scheme — but one consistent scheme must win. Note the rest of the territory is clean: these are the only two inversions.

### S2. Missing MAJOR concepts: joint distributions and conditional expectation
- **Joint / multivariate distributions** (joint, marginal, conditional distributions of several random variables) has no node. The territory jumps from single-variable `probability-distribution` straight to `covariance-correlation` — whose formal gloss `Cov(X,Y) = E[(X-E[X])(Y-E[Y])]` silently requires the joint distribution of (X,Y) to even be defined. Blitzstein & Hwang devote a full chapter (ch. 7) to it; every serious probability course has it.
- **Conditional expectation** E[X|Y] / E[X|F] has no node either — it appears only as an *aka* on `martingale`, which is a category error (see M2). The martingale definition `E[X_{n+1} | F_n] = X_n` literally cannot be stated without it, and it is the bridge from elementary conditional probability to the measure-theoretic tier. Both concepts are load-bearing prereqs for `martingale`, `brownian-motion`, and Bayesian inference.

### S3. Cross-reference integrity: one dangling id, three convention-violating ids
- `stochastic-process.cross_links` references `dynamics-differential-equations:dynamical-system` — **no such id exists anywhere** in the dataset. The dynamics territory has `system-of-odes`, `flow`, `iterated-map`, `stochastic-differential-equation`, etc., but no `dynamical-system` node.
- The file's own convention is that cross-territory links are namespaced (`applied-computational:machine-learning`, `dynamics-differential-equations:...`) while bare ids resolve to the spine or this territory. But `least-squares`, `orthogonal-projection` (both from `linear-regression`) and `dot-product` (from `covariance-correlation`) are bare ids that exist **only** in `territories/linear-algebra.json`, not the spine. They resolve only if lookups are secretly global — otherwise they are three more dangling links. Either namespace them (`linear-algebra:least-squares`, ...) or promote them to the spine.

---

## Moderate

### M1. Level gap: nothing at level 6; the L5 → L7 jump lacks its bridge
`brownian-motion` and `martingale` sit at level 7; the next-highest concepts are at level 5. Level 6 is empty. The natural bridge material — measure-theoretic probability (Lebesgue integration, σ-algebras as information, filtration/conditional expectation) — is represented only by the spine's `probability-space` (L5). Either add a level-6 measure-theoretic-probability node (which would also house conditional expectation from S2) or justify the two-level jump.

### M2. `martingale` aka list mislabels "conditional expectation" as a synonym
"Conditional expectation" is not another name for a martingale; it is a distinct prerequisite concept (see S2). An `aka` entry should be a genuine alias ("fair game process" is fine). Filing a missing prereq as an alias actively hides the gap from anyone auditing coverage by id.

### M3. No node for the other workhorse distributions: uniform, exponential, geometric
The territory names exactly three distribution families (Bernoulli/binomial, Poisson, normal). The **exponential distribution** is the most conspicuous absence — it is the interarrival-time law of the very `poisson-process` node this file defines, and the standard first example of a continuous distribution and memorylessness. Uniform (the basis of all simulation, cf. `monte-carlo`) and geometric are close behind. A single "common distributions" node or an exponential node would close the worst of this. (t and chi-square distributions are arguably folded into `hypothesis-testing`/`confidence-interval` and are only a minor gap.)

### M4. `normal-distribution` formal gloss overclaims: "the unique fixed point of the central limit theorem"
The normal is the unique fixed point only among **finite-variance** laws; the stable distributions (Cauchy, Lévy, ...) are also fixed points of the analogous renormalization with different scaling. Fix: "the unique finite-variance fixed point" or drop the clause.

---

## Minor

1. **`elementary-probability` intuition gloss is mildly circular** — "measuring how likely something is" defines probability via "likely." The second clause ("fraction of equally likely worlds where it happens") is a genuine image and rescues it; consider leading with the image instead.
2. **`brownian-motion` cross_link to `manifold` is tenuous** — stochastic analysis on manifolds is a real but decidedly niche connection; every other cross_link in the file is a first-order relationship. Suggest replacing with `stochastic-differential-equation` (which exists in the dynamics territory and is the canonical next step).
3. **`martingale` has only one resource** (Wikipedia); every other concept has two or three. Williams' *Probability with Martingales* is already in `sources` — an OCW or lecture-notes link would match the file's own standard.
4. **`descriptive-statistics` aka includes "data visualization"** — a subtopic, not an alias; same category error as M2 in miniature.

---

## Checks that passed

- **Mis-leveling vs. standard curricula:** apart from the S1 inversions, levels track AP Stats → intro course (18.05) → Casella-Berger → graduate probability sensibly. `brownian-motion`/`martingale` at 7 is defensible for measure-theoretic treatment (given M1 is addressed).
- **Glosses:** accurate and image-first throughout; no jargon-first offenders. Formal glosses for conditional probability, CLT, MLE, entropy, and the martingale definition are all correct.
- **Resource URLs, spot-checked live (2026-07-21):**
  - `https://distribution-explorer.github.io/` — real (Caltech Probability Distribution Explorer, CC-BY) ✓
  - `https://www.3blue1brown.com/lessons/clt` — real ("But what is the Central Limit Theorem?", Mar 2023) ✓
  - `https://setosa.io/ev/markov-chains/` — real ("Markov Chains explained visually", Powell & Lehe) ✓
  - Remaining URLs (Khan Academy, OpenIntro, MIT OCW 18.05 Spring 2022, Seeing Theory, randomservices.org, colah.github.io, statlearning.com, Wikipedia) are well-known stable resources; slugs look correct.
- **Duplicates/overlap:** none. `descriptive-statistics` (data) vs `variance` (random variables) and `point-estimation` vs spine's `statistical-inference` are legitimately distinct framings, correctly cross-linked rather than duplicated.
