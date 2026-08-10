---
brick_id: NG089
status: NO-GO
base_field: C for the A2 collision and Q for rational descent
variety: an arbitrary polarized smooth projective complex 2n-fold X, a selected B058 detector, and a root-covered local A2 collision
smoothness: X and generic hyperplane fibers smooth; local Milnor fibers smooth
projectivity: X and hyperplane family projective; local collision chart alone need not be global
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; local vanishing lattice rank 2
codimension: middle codimension n; local support at the collision point
coefficient_field: Q
cohomology_theory: local A2 vanishing homology, S3-equivariant nearby cycles, normalized trace, B022 quotients, and primitive ambient pairing
hodge_type: desired descended excess rational type (0,0) after Q(n); none is supplied locally
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B073, B113, G041-G042, G074-G075, NG050-NG054
claim: A nonzero selected excess computed entirely in the local A2 root lattice descends by rational S3 averaging to a nonzero class suitable for G074.
falsifier: B113's zero Reynolds projector on the rational A2 standard representation
---

# NG089 — A purely local (A_2) excess does not descend

**Status:** NO-GO

- **Route:** compute a nonzero difference of local (A_2) vanishing chains
  on the ordered-root cover and use normalized (S_3)-trace as G074's
  rational topology-changing excess downstairs.
- **Valid input:** the local difference can be a nonzero cycle and the
  rational averaging morphism exists.
- **Invalid inference:** its average is nonzero.
- **Precise obstruction:** B113 applies B073's exact matrices: the local
  (A_2) lattice is the standard (S_3)-representation and its Reynolds
  projector is identically zero.
- **Re-entry condition:** G075 must compute the selected excess inside the
  full global coefficient object and prove that its projection to the
  invariant full-support constituent is nonzero. This is the selected-chain
  landing clause already present in G042, not a new terminal reduction.
