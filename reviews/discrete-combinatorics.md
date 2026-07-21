# Adversarial Review — Discrete Math & Combinatorics

Reviewed: `data/territories/discrete-combinatorics.json` against `data/spine.json` (2026-07-21).
22 concepts in territory + 2 spine anchors (`counting-principles` L1, `graph` L2). No edits made.

## Severe

### S1. Prereq level inversion: `integer-partition` (L4) requires `generating-function` (L5)
A level-4 concept cannot have a level-5 prereq — this breaks any topological/level-ordered
rendering of the map. Substantively, partitions are routinely introduced *before* generating
functions (Ferrers diagrams, conjugation, bijective identities need no GFs); Euler's product
is then the payoff. Fix: drop `generating-function` from the prereq list (keep as cross_link),
or split "partitions" (L3-4) from "partition generating functions" (L5).

### S2. Dead resource URL: Alon & Spencer (`probabilistic-method`)
`https://en.wikipedia.org/wiki/The_Probabilistic_Method` — **verified 404 via fetch**.
No Wikipedia article exists at that title. This is a fabricated-looking link. Replace with a
publisher page or the general `Probabilistic_method` article (already listed separately anyway,
so this entry is also redundant).

### S3. Resource title/URL mismatch: "Andrews & Eriksson, Integer Partitions" (`integer-partition`)
URL is `https://en.wikipedia.org/wiki/George_Andrews_(mathematician)` — **verified via fetch**:
it is a biography page of George Andrews, not the book or any text of it. A reader clicking
"Integer Partitions (Andrews & Eriksson)" gets a mathematician's bio. Replace with the CUP
book page or drop.

### S4. Wrong prereq: `graph-coloring` requires `planar-graph`
Chromatic number is defined and taught for arbitrary graphs with no planarity anywhere;
every standard curriculum (Diestel ch. 5, West ch. 5, Rosen) treats coloring independently.
Planarity is only needed for the Four Color Theorem, one highlighted result. The arrow should
point the other way at most (planar → four-color as cross_link). As written it also forces
coloring after planarity in any learning path, which is backwards for e.g. greedy coloring /
Brooks' theorem.

### S5. Missing major concepts: Catalan numbers and set partitions / Stirling numbers
For a serious enumeration map these are core, not optional:
- **Catalan numbers** — arguably the single most famous counted family (Stanley wrote an
  entire book of 200+ interpretations); natural L3-4 node between `binomial-coefficient`,
  `recurrence-relation`, and `generating-function`.
- **Set partitions & Stirling numbers** (and with them the twelvefold way, Bell numbers) —
  the standard companion to integer partitions; currently the map counts subsets and
  integer partitions but has no node for partitioning a *set*.
Both appear in every intro combinatorics text (Bogart, Stanley EC1 ch. 1, Concrete Math ch. 6).

## Moderate

### M1. Backwards prereq: `probabilistic-method` requires `ramsey-theory`
The Erdős 1947 Ramsey lower bound is the *founding application* of the method (the file's own
`sources` field says so), not a prerequisite for learning it. Alon & Spencer assumes no Ramsey
theory. Demote to cross_link (which already exists in the other direction from `ramsey-theory`).

### M2. Pattern: book "resources" that link to Wikipedia articles *about* the book
Typed `"text"` as if they were readable texts, these link to encyclopedia articles or topic pages:
- Concrete Mathematics → `wiki/Concrete_Mathematics` (used twice: `binomial-coefficient`, `recurrence-relation`)
- Graham/Rothschild/Spencer "Ramsey Theory" → `wiki/Ramsey_theory` (the *topic* article, duplicating the Ramsey's-theorem link)
- Bollobás "Random Graphs" → `wiki/Random_graph` (topic article)
- CLRS → `wiki/Introduction_to_Algorithms`
- Benjamin & Quinn → `wiki/Proofs_That_Really_Count` (verified: exists, but is an article about the book)
Not dead links, but misleading as resources. Either link real texts (Wilf, Diestel, Bogart, and
Stanley EC1 entries show the right pattern — those URLs are genuine free full texts) or retype/
relabel these as "about" references.

## Minor

- **`matching` at L5**: Hall's theorem sits in the first weeks of any graph theory course
  (Diestel ch. 2); L4 alongside `planar-graph`/`poset` fits standard curricula better. Not wildly off.
- **`generating-function` at L5**: defensible (spine puts eigenvalues at 5), but it's sophomore
  discrete-math material; L4 would remove tension with S1 cleanly.
- **Advanced-end gap**: no `matroid` or set-system/hypergraph node, though
  `extremal-combinatorics`' formal gloss speaks of "set systems" with no node to link.
  Borderline for map scope; noting only.
- **`network-flow` sources cite "CLRS ch. 24 (flows)"** — chapter number matches only the
  4th edition (26 in the 3rd); specify edition.

## Passed checks

- **Glosses**: all intuition_glosses are genuinely image-first (pigeons, clotheslines, dominoes-free,
  necklaces, pipes); none circular or jargon-first. Formal glosses spot-verified correct: Euler
  circuit iff all-even-degree (connected), Cayley n^(n-2), Hall's condition, max-flow=min-cut
  (Ford-Fulkerson 1956), Burnside orbit-count, G(n,p) giant component at p ≈ 1/n, V−E+F=2,
  Kuratowski K5/K3,3, R(5,5) still open. No factual errors found.
- **Duplicates/overlap**: none material. `bijective-proof` vs `counting-principles`,
  `graph-connectivity` vs `network-flow` are properly separated.
- **URL spot-checks**: Wilf gfology2.pdf verified live (real 1.2MB PDF); Diestel, Bogart,
  Stanley EC sites are the known genuine free-text homes.
- **Other levels**: remaining assignments (pigeonhole L2, PIE L3, trees L3, Ramsey/extremal/
  probabilistic/random-graph/designs L6) match standard curricula.

## Summary

10 issues: 5 severe (S1-S5), 2 moderate, 3 minor. The skeleton and prose are strong; the
severe problems are one structural level inversion, two bad resource links (one 404, one
bio-page mismatch), one backwards prereq edge, and two missing core enumeration concepts.
