---
brick_id: B069
status: PROVED
base_field: C
variety: a surjective morphism of complex projective varieties with geometrically integral generic fiber
smoothness: the altered base is nonsingular; the weakly semistable total space is not asserted nonsingular by the theorem
projectivity: the base alteration and total-space modification are projective
dimension: arbitrary finite base and fiber dimensions
codimension: not a cycle-codimension statement; boundary strata are toroidal divisors
coefficient_field: none in the geometric theorem; intended applications use Q
cohomology_theory: none in the theorem; intended applications use rational mixed Hodge modules and nearby cycles
hodge_type: none asserted
cycle_class_map: none
cycle_equivalence: none
scope: relative
dependencies: Abramovich-Karu Theorem 0.3 audited as S044 and G037
claim: After a projective alteration of the base and a projective modification of the main total-space pullback, any such family admits a dimension-uniform weakly semistable model, but smooth semistability is not supplied.
falsifier: failure of Abramovich-Karu Theorem 0.3 under its stated hypotheses
---

# B069 — Exact boundary of weak semistable reduction

**Status:** PROVED (imported conditional geometry)  
**Gate:** G037 / G038  
**Primary source:** S044

## Imported theorem

Abramovich–Karu Theorem 0.3 states that for a surjective morphism
\(X\to B\) of complex projective varieties with geometrically integral generic fiber, there are

- a projective alteration \(B'\to B\), and
- a projective modification \(Y\to X\times_B B'\),

such that \(Y\to B'\) is weakly semistable.

By Definition 0.1, this means the morphism is toroidal, equidimensional, has reduced fibers, and the base \(B'\) is nonsingular. It does **not** include nonsingularity of \(Y\). The paper reserves “semistable” for the additional condition that \(Y\) is nonsingular and states that stronger modification theorem as Conjecture 0.2 in the audited version.

## Exact gain for G037

The existence of a dimension-uniform toroidal, equidimensional, reduced-fiber model is not the remaining obstruction. This applies in every odd fiber dimension required by the middle-degree route, provided the local chart is algebraized inside a projective family with geometrically integral generic fiber.

## Remaining boundary

- The alteration \(B'\to B\) is not identified with B067's \(S_3\) root cover.
- The construction is not asserted \(S_3\)-equivariant.
- The total space \(Y\) need not be smooth.
- Resolving \(Y\) afterward is not proved here to preserve weak semistability, reduced fibers, or the exact toroidal map.
- No mixed-Hodge-module strict-specialisability, support decomposition, B022 quotient, or detector-pairing descent is supplied.
