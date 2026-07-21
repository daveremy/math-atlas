# The Math Atlas

**A comprehensive, beautiful, maintained concept map of mathematics — the territory itself, independent of any traveler.**

Conceived 2026-07-21 (Dave Remy, with Sagan). Sibling to the private structural-intelligence project, which overlays a learner's states onto this map. The atlas itself knows no learner.

## Principles

1. **The territory, not the traveler.** Built from first principles and primary taxonomies — never from any individual's learning history.
2. **A graph on an infinite canvas.** Mathematics is a cross-linked DAG, not a tree and not columns. Territories cluster; edges roam.
3. **Every node has two faces**: an intuition face (what it *is*, image-first) and a formalism face (its precise definition and notation). Tracked, rendered, and — for learners downstream — assessed separately.
4. **Foundational weight is a first-class attribute** — a leverage score per concept, meaning *pedagogical reach*: how much of the map a learner unlocks by mastering it, computed on the atlas's own prerequisite DAG. This is deliberately not centrality over a formal library's import graph — ["The Network Structure of Mathlib"](https://arxiv.org/abs/2604.24797) (May 2026) showed that raw centrality there measures language infrastructure (simp lemmas, typeclass plumbing), not mathematical importance. The atlas asks a different question of a different graph: prerequisite edges for learners, not logical imports for a compiler. Every score is cross-checked by curation with a written rationale; mathlib data enters only as one corroborating signal, pre-filtered for the infrastructure-vs-importance confound (see the method note below).
5. **Living document.** Mathematics is being perturbed (AI-assisted proof, formalization at scale). The atlas absorbs updates on a scheduled cadence (see maintenance).
6. **Honest provenance.** Every structural claim carries its source; contested placements carry flags. House rules inherited from the parent project.

## Deliverable ladder

- **v0.1** — ~12 top-level territories; 200–300 core concepts; prerequisite edges; leverage scores (computed + curated); source dossier; first infinite-canvas render.
- **v0.x** — territory-by-territory deepening; two-face content per node; resource attachments (video/text/GAP/Lean per node).
- **v1.0** — public-ready: viewer, documentation, contribution guide.

## Primary sources under study (deep notes to follow)

- Mathematics Subject Classification (MSC 2020) — the profession's taxonomy
- *The Princeton Companion to Mathematics* (Gowers et al.) — the human-curated landscape
- Metacademy (open-source prerequisite-graph project) — prior art, possibly ingestible
- Lean mathlib dependency graph — machine-checked empirical structure
- Khan Academy knowledge map; "Map of Mathematics" visualizations — pedagogical & aesthetic layer

## Maintenance

Monthly perturbation review, fed by the standing Wednesday math-trends scan (AI-assisted mathematics, formalization news, new results that reshape dependencies).

## Leverage: method note

How the leverage score is actually computed, and why it dodges the known failure mode:

1. **Primary signal — reach on the atlas's prerequisite DAG.** For each concept, count (with distance discounting) the downstream concepts whose prerequisite chains pass through it. The graph is the atlas's own curated learner-facing DAG — a different object, answering a different question, than any formal library's dependency graph.
2. **Curation cross-check.** Every computed score is reviewed by a curator, who records a rationale (or a dissent) alongside it. A score with no rationale is provisional, per the provenance principle.
3. **Mathlib as one signal, filtered.** [arXiv:2604.24797](https://arxiv.org/abs/2604.24797) demonstrated that naive centrality over mathlib's 8.4M-edge dependency graph surfaces language infrastructure, not mathematical importance. So before mathlib data touches a leverage score: declarations are aggregated up to atlas concepts, typeclass/simp plumbing is dropped (using the paper's edge-decomposition approach), and centrality is computed on the cleaned concept-level quotient graph. Even then it only corroborates or flags disagreement with signals 1–2 — it never sets a score on its own.
