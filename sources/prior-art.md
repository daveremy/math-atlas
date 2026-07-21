# Prior Art — Concept Maps, Ontologies, and Prerequisite Graphs of Mathematics

Survey for the Math Atlas. Compiled 2026-07-21 (web research pass; links verified live unless noted).
Question asked of each project: what is it, what does it cover, does it have edges, is it pedagogical, what's its license, is it alive, and what can the Atlas learn or ingest from it. Ends with an honest accounting of which of the Atlas's claimed novelties survive contact with the field.

---

## 1. MSC 2020 — Mathematics Subject Classification

- **What**: The profession's own taxonomy of mathematics, jointly maintained by Mathematical Reviews (AMS) and zbMATH. Revised every ~10 years; MSC2020 is current. [msc2020.org](https://msc2020.org/) · [zbMATH browsable version](https://zbmath.org/classification/) · [PDF](https://zbmath.org/static/msc2020.pdf)
- **Coverage**: All of research mathematics — 63 two-digit top-level classes (00–97), ~6,000 three- and five-digit codes. Includes 97 (math education) and applied areas.
- **Edges**: Essentially none. It's a **tree** (with informal "see also" cross-references in entry descriptions). It classifies *literature*, not concepts — the leaves are subjects papers get filed under, not things you learn.
- **Pedagogy**: None. Ordering is bibliographic, not prerequisite.
- **License**: **CC BY-NC-SA** ([msc2020.org](https://msc2020.org/)). The NC clause matters: if the Atlas ever becomes commercial, ingested MSC text (descriptions) would be a problem; the *codes and structure* as facts are less encumbered, but attribute anyway.
- **Alive?**: Yes — institutionally maintained, next revision ~2030.
- **For the Atlas**: The authoritative sanity check on top-level territory boundaries and completeness ("did we forget commutative algebra?"). Use it as a coverage checklist and a stable ID scheme (tag Atlas nodes with MSC codes for interop with zbMATH/MaRDI). Do **not** inherit its top level wholesale — 63 classes with historical baggage (e.g., separate classes for potential theory, several analysis silos) is not a 12-territory map.

## 2. OntoMathPRO

- **What**: The first Linked-Open-Data OWL ontology of *professional* mathematical knowledge, from Kazan Federal University. v2.0 (2023) adds a foundational-ontology layer, reified relationships, and a linguistic layer. [ontomathpro.org](http://ontomathpro.org/) · [GitHub (CLLKazan/OntoMathPro)](https://github.com/CLLKazan/OntoMathPro) · [2014 paper](https://arxiv.org/pdf/1407.4833) · [OntoMathPRO 2.0 paper (2023)](https://arxiv.org/pdf/2303.13542) · [Doklady overview](https://link.springer.com/article/10.1134/S1064562422700016)
- **Coverage**: Thousands of concepts across several fields (strong in analysis, algebra, numerical math — reflects its Russian-curriculum and formula-search origins). Bilingual English/Russian.
- **Edges**: Yes — taxonomic (is-a) hierarchies of mathematical objects, plus reified relations (e.g., "X is defined by Y"). **Not prerequisite edges** in the pedagogical sense, though an educational-level annotation exists in places.
- **Pedagogy**: Marginal. Built for information extraction and semantic formula search, not learning paths.
- **License**: **Apache 2.0** (repo, last pushed Jan 2024 — verified via GitHub API).
- **Alive?**: Semi-alive. Papers through 2023–24, repo activity into 2024; slow cadence, small group.
- **For the Atlas**: The best existing example of *formal ontology engineering* applied to math concepts — worth reading for its modeling decisions (kinds vs. roles, reified relations, the three-layer model, and the [verification paper](https://link.springer.com/chapter/10.1007/978-3-031-53488-1_23) on QA-ing such an ontology). Ingestible under Apache 2.0 as a cross-check vocabulary. Its weakness is exactly the Atlas's target: no intuition faces, no prerequisite direction, no leverage weighting.

## 3. Metacademy

- **What**: "A package manager for knowledge" (Roger Grosse & Colorado Reed, ~2012–2016): an open-source prerequisite DAG where each concept node carries learning goals, time estimates, and pointers to resources; the app computes a personalized learning path to any target concept. [App repo](https://github.com/metacademy/metacademy-application) · [Content repo](https://github.com/metacademy/metacademy-content) · [John Langford's writeup](https://hunch.net/?p=2714) · [foldl commentary](http://www.foldl.me/2014/metacademy/)
- **Coverage**: Hundreds of concepts, heavily skewed to machine learning and its math prerequisites (linear algebra, probability, some analysis). Never a balanced map of mathematics.
- **Edges**: Yes — genuine directed **prerequisite edges**, human-curated, with per-concept "goals" the dependencies attach to. This is the closest ancestor to the Atlas's edge model.
- **Pedagogy**: Entirely — that was the point. Also pioneered exactly the Atlas's "shortest path of prerequisites to a target" interaction.
- **License**: App **GPLv3** ([LICENSE](https://github.com/metacademy/metacademy-application/blob/master/LICENSE.txt)); content **CC BY-SA 3.0** ([content repo](https://github.com/metacademy/metacademy-content)).
- **Alive?**: **Dead.** metacademy.org refuses connections (verified 2026-07-21, ECONNREFUSED). Application repo archived, last push May 2023; content repo last touched **2017** (verified via GitHub API). But the data survives: content is plain-text files (per-concept directories with dependency lists) in the GitHub repo, fully ingestible.
- **For the Atlas**: The single most ingestible prior artifact. CC BY-SA 3.0 means the Atlas can absorb its concept entries and prerequisite edges with attribution — but note **ShareAlike is viral**: derived node content would need CC BY-SA compatibility. Design lesson: Metacademy died of curation cost — hand-maintaining a prerequisite graph plus per-node content plus resource lists exceeded a two-person side project. The Atlas's "monthly perturbation review + agent-assisted curation" is a direct answer to that failure mode; take it seriously.

## 4. Khan Academy Knowledge Map

- **What**: KA's original (2010–2013) "starry night" zoomable map of math exercises with prerequisite arrows; retired in favor of linear course mastery. [Fandom description](https://khanacademy.fandom.com/wiki/Knowledge_Map) · [Help-center thread confirming removal](https://support.khanacademy.org/hc/en-us/community/posts/115007007148-Bring-back-the-Knowledge-Map) · [Community recreation project](https://support.khanacademy.org/hc/en-us/community/posts/4422868962701--Knowledge-Map-World-of-Math-Replacing-or-recreating-it-A-long-term-project)
- **Coverage**: School math (arithmetic → early calculus) at exercise granularity.
- **Edges**: Yes, prerequisite edges between exercises.
- **Pedagogy**: Entirely.
- **License**: Proprietary; the API that exposed the knowledge tree was **shut down July 2020**.
- **Alive?**: **Dead** since 2013 (map UI) / 2020 (API). KA states no plans to revive; "most students and teachers found linear progression works best."
- **For the Atlas**: Nothing ingestible. Two lessons instead. (1) UX: an infinite-canvas map of mastery is *motivating* — its removal is still protested on KA forums a decade later; there's demonstrated appetite. (2) Product warning: KA retired it because most learners want a path, not a map. The Atlas dodges this by separating territory (atlas) from traveler (the sibling project), but the viewer should still support extracted linear paths.

## 5. ALEKS / Knowledge Space Theory

- **What**: The deepest *theory* of prerequisite structure in existence: Doignon & Falmagne's Knowledge Space Theory (1985), where knowledge states are the feasible subsets of a domain of items and prerequisites are "surmise relations"; commercialized as McGraw-Hill's ALEKS adaptive tutor. [ALEKS KST page](https://www.aleks.com/about_aleks/knowledge_space_theory) · [Wikipedia](https://en.wikipedia.org/wiki/Knowledge_space) · [KST + ALEKS data paper](https://www.sciencedirect.com/science/article/abs/pii/S0022249621000134) · [Knowledge Spaces and Learning Spaces survey](https://arxiv.org/pdf/1511.06757)
- **Coverage**: School and early-college math, item (exercise) granularity; ALEKS's structures are fitted from millions of learner responses.
- **Edges**: Yes — but richer than a DAG: KST allows AND/OR prerequisite combinations (a state space, not just a graph). Empirically calibrated.
- **Pedagogy**: Entirely; it's an assessment engine.
- **License**: Theory is open literature; ALEKS's actual knowledge structures are **proprietary trade secrets**.
- **Alive?**: Very — ALEKS is a major commercial product; KST research continues.
- **For the Atlas**: Not ingestible, but theoretically load-bearing: KST is the formal argument that "hard prereq" edges alone under-model reality — real prerequisite structure has disjunctions (you can reach measure theory via analysis *or* probability routes). The Atlas's edge kinds (hard / soft / illuminates) should be checked against KST's surmise systems; and KST's empirical fitting is the pattern for how the traveler-side sibling project could someday calibrate the Atlas's curated edges against learner data.

## 6. Cambridge Mathematics Framework (CMF)

- **What**: Cambridge University Press & Assessment's research-based "connected map" of school mathematics ages 3–19: concept nodes ("waypoints") with typed edges, built on a graph database, with an explicit multi-layer design (mathematical-ideas layer + research layer with its own nodes/edges) and a published ontology paper. [Project page](https://www.cambridgemaths.org/the-cmf/) · [Framework overview PDF](https://www.cambridgemaths.org/Images/562964-a-connected-approach-to-mathematics-learning-the-cambridge-mathematics-framework.pdf) · [Ontology paper](https://www.cambridgemaths.org/Images/ontology.pdf) · [Evaluation approaches](https://www.cambridgemaths.org/Images/evaluating-the-cambridge-mathematics-framework.pdf)
- **Coverage**: School math only (3–19). Nothing at university/research level.
- **Edges**: Yes — typed relationships between waypoints, explicitly *not* purely prerequisite ("connections between ideas," progression implied).
- **Pedagogy**: Entirely — curriculum design tool for ministries/publishers.
- **License**: **Closed.** "Not currently commercially available for direct consultation by individuals and institutions" — partnership access only (verified on project page 2026-07-21).
- **Alive?**: Yes, actively maintained by a funded professional team.
- **For the Atlas**: The strongest *methodological* prior art: this is what "the territory, not the traveler" looks like when a professional team does it — including the discipline of an explicit ontology document, edge typing, and a provenance layer tying every structural claim to research (their "research layer" is precisely the Atlas's "honest provenance" principle, implemented). Read their ontology and evaluation papers before finalizing the Atlas schema. Nothing ingestible; coverage is disjoint anyway (they stop where the Atlas mostly starts).

## 7. Lean mathlib dependency graph

- **What**: The dependency structure of the largest unified formal math library (~1.8M lines; >300k declarations). Machine-checked, hence the only *empirical, complete* dependency data on mathematics in existence. Tools: [leanprover-community/import-graph](https://github.com/leanprover-community/import-graph) (module-level import DAG), [MathlibExplorer](https://github.com/Crispher/MathlibExplorer) (interactive visualization), [leanblueprint](https://github.com/PatrickMassot/leanblueprint) (per-project dependency DAGs).
- **Published analysis**: **"The Network Structure of Mathlib"** ([arXiv:2604.24797](https://arxiv.org/abs/2604.24797), May 2026) — 308,129 declarations, 8.4M edges, 7,563 modules, with decompositions separating explicit, compiler-synthesized, and proof-driven edges. Three findings directly relevant to the Atlas: (1) human namespace taxonomy diverges from logical structure (~50.9% cross-namespace coupling); (2) imports are used sparsely (median 1.6% of imported scope); (3) **network centrality in mathlib captures language infrastructure, not mathematical importance** — simp lemmas and typeclass plumbing dominate raw centrality.
- **Coverage**: Undergraduate + increasingly graduate pure math, with formalization-driven skew (strong order theory/algebra/topology; historically weaker in e.g. PDE, geometry-as-geometers-know-it). See also [100 theorems in Lean](https://leanprover-community.github.io/100.html) vs. [Wiedijk's benchmark list](https://www.cs.ru.nl/~freek/100/) for coverage measurement.
- **Edges**: Yes — millions, machine-checked, but at *declaration* granularity, and they are **logical dependency**, not pedagogical prerequisite (a proof may cite a lemma no learner needs to "learn first").
- **Pedagogy**: None.
- **License**: **Apache 2.0** — fully ingestible.
- **Alive?**: Extremely — one of the fastest-growing artifacts in mathematics.
- **For the Atlas**: The README's Principle 4 (mathlib-derived leverage scores) is *directly warned about* by the arXiv paper: raw centrality over mathlib measures infrastructure, not foundational weight. The leverage computation must use the paper's style of edge decomposition (or aggregate declarations up to concept level first, and drop typeclass/simp plumbing) before centrality means anything. Plan: map Atlas concepts → mathlib namespaces/modules (imperfect, per finding 1), compute centrality on the cleaned concept-level quotient graph, and treat the result as *one input* cross-checked by curation — which is what the README already says; the paper tells you why that hedge is necessary, not optional.

## 8. Formal Abstracts (Hales)

- **What**: Tom Hales's 2017 project to give every mathematical theorem statement (not proof) a formal, machine-readable abstract in Lean/CNL, creating a semantic index of the literature. [Site](https://formalabstracts.github.io/) · [GitHub](https://github.com/formalabstracts/formalabstracts) · [Hales's slides](https://bertini.nd.edu/ICMS2018/HalesICMS2018.pdf)
- **Coverage**: Aspirational; only a small demonstration corpus was ever produced.
- **Edges**: Implicitly (formal statements reference formal definitions), never materialized at scale.
- **Pedagogy**: None.
- **License**: Repo is open (mixed; check per-file).
- **Alive?**: **Dormant.** Main repo last pushed **Nov 2019** (verified via GitHub API); the site still says "design phase." The energy went into mathlib itself and, later, AI-assisted formalization/autoformalization research (e.g. [an accessibility-focused successor approach, 2026](https://arxiv.org/pdf/2603.20893); Hales's own [Mathematics and the formal turn](https://arxiv.org/pdf/2311.00007) context).
- **For the Atlas**: A cautionary tale about scope: "formalize the interface of all of mathematics" stalled even with a Fields-adjacent leader. The Atlas's analogous ambition (two-face content for every node) must stay at *concept* granularity (~10² – 10³ nodes), not statement granularity (~10⁶). Watch autoformalization progress in the Wednesday trends scan — if FAbstracts-style semantic indexes revive via LLMs, they become an Atlas data source.

## 9. Wikidata, DBpedia, MaRDI, MathGloss

- **Wikidata**: [WikiProject Mathematics](https://www.wikidata.org/wiki/Wikidata:WikiProject_Mathematics) actively curates math items; the [1000+ Theorems focus list](https://www.wikidata.org/wiki/Wikidata:WikiProject_Mathematics) structures notable theorems with properties. Coverage of *concepts* is broad but shallow and uneven; relations available include instance-of/subclass-of, named-after, "generalization-of" in places — **no prerequisite relation exists in the property vocabulary**. License **CC0** (maximally ingestible). Alive. For the Atlas: the natural source of stable external IDs (QIDs) + multilingual labels + links out to everything else (MathWorld, nLab, MSC codes are all linked from Wikidata items). Ingest identifiers and crosslinks; don't expect structure.
- **DBpedia**: Auto-extracted from Wikipedia infoboxes; math infoboxes are sparse, so math coverage is markedly worse than Wikidata's. License CC BY-SA. Effectively superseded by Wikidata for this purpose. Skip.
- **MaRDI** (Mathematical Research Data Initiative): German NFDI project; a Wikibase knowledge graph of contemporary mathematics research data — papers, software, datasets, formulas, and links into zbMATH Open/swMATH. [Bravo MaRDI paper](https://arxiv.org/abs/2309.11484) · [portal](https://portal.mardi4nfdi.de). Alive and funded. Research-metadata orientation, not concepts-for-learners; useful later as the "living document" news feed for research-frontier nodes.
- **MathGloss**: Horowitz & de Paiva, [arXiv:2311.12649](https://arxiv.org/pdf/2311.12649) — an automatically built linked knowledge graph of *undergraduate* math concepts, unifying Wikidata, U Chicago course glossaries, the French curriculum (with Lean 4 links!), MuLiMa, and nLab. Small, academic, but its five-way alignment table is exactly the crosswalk the Atlas needs between curricula, wikis, and Lean. Check the repo for license before ingesting (repo location not confirmed via API this pass).

## 10. OpenMath Content Dictionaries (and OMDoc)

- **What**: A 1990s-era standard for the *semantics of mathematical objects* — Content Dictionaries define symbols (e.g., `arith1.plus`) so software can exchange formulas meaningfully; OMDoc extends this to whole documents/theories. [openmath.org](https://openmath.org/) · [CD catalog by status](https://openmath.org/cdnamess/) · [Standard](https://openmath.org/standard/om20-2019-07-01/omstd20.html) · [Semantics of OpenMath and MathML3](https://kwarc.info/people/mkohlhase/papers/mcs12.pdf)
- **Coverage**: Symbol-level: arithmetic, calculus, linear algebra, sets, etc. — the vocabulary of *formulas*, not the map of *fields*.
- **Edges**: CDs reference each other; no concept-prerequisite structure.
- **Pedagogy**: None.
- **License**: Open (CDs are public; typically permissive).
- **Alive?**: The society persists and the standard is referenced (MathML), but momentum has largely moved to proof-assistant libraries. Low activity.
- **For the Atlas**: Wrong granularity to ingest. One idea worth stealing: the CD **status lifecycle** (experimental → public → official → deprecated) is a clean, proven model for the Atlas's "contested placement" flags and monthly perturbation review.

## 11. "Map of Mathematics" — Domain of Science (Walliman)

- **What**: Dominic Walliman's 2017 poster + [YouTube video](https://www.youtube.com/watch?v=OmJ-4B-mS-Y) (~10M+ views): a single hand-drawn image splitting math into pure/applied regions with subfield islands. [Flickr](https://www.flickr.com/photos/95869671@N08/32264483720/sizes/l/) · [DFTBA poster](https://store.dftba.com/products/map-of-mathematics-poster) · [Walliman's post](https://dominicwalliman.com/post/157283769280/poster-summarising-the-main-subjects-of)
- **Coverage**: Top-level fields only (~50 labels), one static image.
- **Edges**: Adjacency-as-metaphor; no real edges, admitted inaccuracies (Walliman lists errata himself).
- **Pedagogy**: Inspirational only.
- **License**: **All rights reserved** (verified on Flickr) — do not ingest imagery.
- **Alive?**: Walliman is active (more maps, books); the math map itself is a finished 2017 artifact.
- **For the Atlas**: Proof of *demand* — millions of people want a picture of the whole territory. The Atlas's aesthetic bar ("beautiful") is set here; its content bar must be far higher. Nothing to ingest.

## 12. "The Map of Mathematics" — Quanta Magazine (2020)

- **What**: Interactive scrollytelling map ([mathmap.quantamagazine.org](https://mathmap.quantamagazine.org/)) by Kevin Hartnett, Kim Albrecht, Jonas Parnow — [article](https://www.quantamagazine.org/the-map-of-mathematics-20200213/) · [designer's writeup](https://jonasparnow.com/map-of-mathematics/). Four territories (numbers, shapes, change, passages), ~41 nodes, each linking to Quanta reporting on the research frontier.
- **Edges**: Yes, hand-drawn conceptual connections; not prerequisite, not systematic. (FOM mailing list [complained it omits foundations](https://cs.nyu.edu/pipermail/fom/2020-February/022012.html) — an early example of the "contested placement" problem.)
- **Pedagogy**: Journalism, not curriculum.
- **License**: Proprietary (Quanta/Simons Foundation).
- **Alive?**: Static since 2020; still hosted.
- **For the Atlas**: The best existing *interaction design* for a small math map (zoom, territory clustering, narrative on node-click). Study it for the v0.1 render; ingest nothing.

## 13. OpenMathMap (KWARC)

- **What**: 2013 research prototype (Kohlhase et al., Jacobs U): rendered the MSC as a literal OpenStreetMap-style world map, with area sizes from zbMATH publication counts. [Paper](https://ceur-ws.org/Vol-1010/paper-12.pdf) · [GitHub](https://github.com/KWARC/openmathmap)
- **Edges/Pedagogy**: None/none — cartographic metaphor over the MSC tree.
- **Alive?**: **Dead** (prototype era ~2013).
- **For the Atlas**: Prior art specifically for the "infinite canvas / cartographic" rendering idea, including its failure: a map projected from a *tree + publication volume* has nothing for edges to mean. The Atlas's insistence that edges (prerequisite/dependency) drive layout is the fix.

## 14. Wikipedia, MathWorld, nLab, ProofWiki (encyclopedic taxonomies)

- **Wikipedia**: [Areas of mathematics](https://en.wikipedia.org/wiki/Areas_of_mathematics), [Lists of mathematics topics](https://en.wikipedia.org/wiki/Lists_of_mathematics_topics), the category system, and thousands of concept articles with organic hyperlinks. Edges exist but are undirected, unlabeled hyperlinks; taxonomy is a loose polyhierarchy. CC BY-SA 4.0. Very alive. For the Atlas: the default *content* source behind each node's faces (summaries, images), and the hyperlink graph is a weak empirical signal for edge candidates (this is what the academic prerequisite-learning literature mines — see §15).
- **MathWorld** (Wolfram): ~13k entries in a subject **tree** (Algebra > … ), cross-linked "see also"s. Proprietary (Wolfram terms). Alive, slow. Reference-checking only; nothing ingestible.
- **nLab**: Category-theoretic wiki; deep, opinionated, densely crosslinked; excellent for the *formalism face* of higher-structural concepts, actively maintained. Effectively open (site licensing is permissive-ish; verify per-page). Already integrated by MathGloss.
- **ProofWiki**: Theorem/proof wiki with explicit dependency links between proofs and definitions — a small human-curated logical-dependency graph. CC BY-SA. Alive. Possible secondary edge-evidence source at theorem granularity.

## 15. Academic literature: prerequisite-relation learning; other pedagogy maps

- **Prerequisite learning from data** is an established NLP/EDM research task: inferring "learn A before B" from Wikipedia links, MOOCs, textbooks. Key entry points: [Prerequisite Relation Learning: A Survey and Outlook (ACM Comp. Surveys, 2025)](https://dl.acm.org/doi/10.1145/3733593) · [curated paper list](https://github.com/harrylclc/concept-prerequisite-papers) · [AAAI concept-extraction paper](https://ojs.aaai.org/index.php/AAAI/article/view/5033) · [ACE: AI-assisted construction of educational KGs (JEDM)](https://jedm.educationaldatamining.org/index.php/JEDM/article/view/737). Datasets exist (e.g., LectureBank, university course prerequisite pairs) but are small, noisy, and mostly CS/ML-domain. For the Atlas: methods (and LLM-era successors like ACE) are candidate *edge-candidate generators* feeding human curation; none produced a maintained public map of mathematics.
- **Mathigon** ([content map](https://mathigon.org/map)) — beautiful interactive school-math courses with a course-level map; content proprietary-ish (free to use, not open data); alive under Amplify. UX inspiration for "intuition faces."
- **Expii** ([expii.com](https://www.expii.com/)) — Po-Shen Loh's crowdsourced topic-graph learning site; the original topic-map framing has faded; effectively dormant as a graph project.
- **Evan Chen's Napkin** ([napkin.html](https://web.evanchen.cc/napkin.html), [GitHub](https://github.com/vEnhance/napkin)) — a single-author tour of undergrad/grad math **with an explicit chapter-dependency flowchart**; the closest thing in print to "intuition face first, formalism second" at Atlas scope. Open source (repo). Ingest the flowchart as curated edge evidence; imitate the voice.
- **Wiedijk's Formalizing 100 Theorems** ([list](https://www.cs.ru.nl/~freek/100/)) — cross-prover benchmark; useful as a canonical "famous theorems" node seed list.

---

## Comparison at a glance

| Project | Concept nodes? | Prerequisite edges? | Pedagogical? | Whole-of-math? | Open data? | Alive? |
|---|---|---|---|---|---|---|
| MSC 2020 | subjects, not concepts | no (tree) | no | yes (research) | CC BY-NC-SA | yes |
| OntoMathPRO | yes | no (is-a) | weak | partial | Apache 2.0 | barely |
| Metacademy | yes | **yes** | **yes** | no (ML-skewed) | CC BY-SA 3.0 | **dead** |
| Khan knowledge map | exercises | yes | yes | school only | no | dead |
| ALEKS / KST | items | yes (rich) | yes | school only | theory only | yes |
| Cambridge CMF | yes | yes (typed) | yes | ages 3–19 only | **closed** | yes |
| mathlib dep graph | declarations | logical, not pedagogical | no | growing | Apache 2.0 | very |
| Formal Abstracts | statements (aspirational) | implicit | no | aspirational | open | dormant |
| Wikidata/MaRDI/MathGloss | yes | no prereq property | no | broad, shallow | CC0 / open | yes |
| OpenMath CDs | symbols | no | no | formula vocab | open | low |
| Walliman map | ~50 labels | no | inspirational | top-level | all rights reserved | static |
| Quanta map | ~41 | conceptual | no | frontier sampler | proprietary | static |
| Wikipedia/nLab/ProofWiki | yes | hyperlinks only | no | broad | CC BY-SA | yes |

## Which of the Atlas's claimed novelties survive?

Honest scoring against the README's principles:

1. **"Comprehensive, maintained concept map of the territory" — partially survives.** Every ingredient exists somewhere: curated concept nodes + typed edges (Cambridge CMF — but closed and school-only), prerequisite DAG + learning paths (Metacademy — but dead and ML-skewed), whole-of-math coverage (MSC/Wikipedia — but no pedagogical edges), maintained + living (Wikidata/MaRDI — but no prerequisite structure). **No single artifact is simultaneously: concept-granular, prerequisite-edged, spanning school-to-frontier, open, and maintained.** That intersection is genuinely unoccupied — but the novelty is the intersection, not any component, and the README should say so.
2. **"Graph on an infinite canvas, not a tree" — not novel as an idea** (Khan's map, Quanta, OpenMathMap, MathlibExplorer all did canvas renders; CMF is a genuine graph). Novel only in execution quality + edge semantics driving layout.
3. **"Two faces per node (intuition / formalism), tracked and assessed separately" — largely survives.** Nothing in the survey treats intuition-vs-formalism as a first-class, separately-tracked attribute of every node. Nearest neighbors: Napkin (voice, not data model), Mathigon (intuition only), nLab (formalism only), Metacademy's goals (neither exactly). This is the Atlas's most defensible structural novelty.
4. **"Leverage score from graph structure incl. mathlib" — survives with a bruise.** Nobody has computed pedagogical leverage from formal-library data. But [The Network Structure of Mathlib (2026)](https://arxiv.org/abs/2604.24797) has already done the network analysis and *found that raw centrality measures infrastructure, not mathematical importance* — so the Atlas's method must be centrality over a curated concept-level quotient graph with mathlib as cross-evidence, and must cite/answer that paper. The naive version of Principle 4 is pre-refuted.
5. **"Living document with scheduled perturbation review" — novel among pedagogical maps** (Metacademy/Khan died precisely of staleness; CMF is maintained but closed). Not novel among research KGs (MaRDI, Wikidata).
6. **"Honest provenance per structural claim" — not novel in kind** (CMF's research layer does exactly this; OpenMath's CD status lifecycle is a governance model to copy), but rare and worth doing.

**Ingestion shortlist for v0.1**: Metacademy content repo (CC BY-SA 3.0 — mind ShareAlike), mathlib import/declaration graph via importGraph (Apache 2.0), MSC 2020 codes as node tags (CC BY-NC-SA — attribution, mind NC if commercialized), Wikidata QIDs + crosslinks (CC0), Napkin dependency flowchart (open repo), MathGloss crosswalk tables (license TBC), OntoMathPRO as vocabulary cross-check (Apache 2.0). **Study but don't ingest**: Cambridge CMF ontology papers, Quanta map interaction design, KST edge semantics, the Network Structure of Mathlib methodology.
