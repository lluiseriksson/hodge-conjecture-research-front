---
brick_id: B070
status: PROVED
base_field: characteristic zero, applied over C
variety: noetherian quasi-excellent generically reduced schemes, including finite-type complex varieties with finite group actions
smoothness: the output scheme is regular and all blowup centers are regular; centers avoid the original regular locus
projectivity: each blowup is projective; the composite is projective over the original scheme
dimension: arbitrary finite dimension
codimension: blowup centers have variable codimension; this is not a terminal cycle-codimension theorem
coefficient_field: none in the geometric theorem
cohomology_theory: none in the theorem; later intended use is rational mixed Hodge modules
hodge_type: none asserted
cycle_class_map: none
cycle_equivalence: none
scope: absolute
dependencies: Temkin Theorem 1.2.1 audited as S045 and G038
claim: Functorial desingularization yields a regular projective resolution equivariant under every finite group action, but only as an absolute resolution of the total variety.
falsifier: a characteristic-zero finite group automorphism that does not lift to Temkin's functorial blowup sequence
---

# B070 — Equivariant absolute desingularization in characteristic zero

**Status:** PROVED (imported theorem plus formal equivariance consequence)  
**Gate:** G038 / G039  
**Primary source:** S045

## Imported theorem

Temkin's Theorem 1.2.1 assigns to every noetherian quasi-excellent generically reduced scheme over \(\mathbf Q\) a sequence of blowups with regular centers, disjoint from the inverse image of the regular locus, whose output is regular. The construction is functorial for all regular morphisms.

## Equivariance consequence

Let a finite group \(\Gamma\) act on \(Y\). Every automorphism \(g:Y\to Y\) is an isomorphism and hence a regular morphism. Functoriality identifies the pullback of the canonical blowup sequence by \(g\) with the same sequence (up to the prescribed empty blowups). Consequently every center is \(\Gamma\)-stable and the action lifts through the sequence. The final regular resolution is \(\Gamma\)-equivariant.

This applies uniformly to B069's weakly semistable total variety after passing to a finite Galois domination of the alteration, provided all objects are kept in the stated characteristic-zero quasi-excellent category.

## Boundary

The theorem resolves the abstract total variety. It is not a relative desingularization theorem for a toroidal morphism \(Y\to B'\). It does not assert that the resolved morphism remains equidimensional, toroidal, or reduced-fiber, and it does not construct the MHM trace or detector pairing.

