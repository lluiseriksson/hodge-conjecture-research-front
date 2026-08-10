---
brick_id: NG086
status: NO-GO
base_field: C with detector and collision data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, its B058 distributed detector, and a proposed marked projective collision
smoothness: X and generic hyperplane fibers smooth; proposed target clean nodal; proper IC model required for local invariant cycles
projectivity: X, the hyperplane family, and proposed collision projective
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; plane base dimension 2
codimension: middle codimension n; target is a point of the plane base
coefficient_field: Q
cohomology_theory: relative thimble homology, nearby cycles, local invariant cycles, B022 quotients, and perverse-filtered stalks
hodge_type: all relevant classes required to be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B059, B084, B088-B091, B110, G049-G055, G072
claim: A nonzero B058 ambient detector, or a Hurwitz-fixed representative of its distributed thimble word, automatically defines an ordinarily liftable nearby class t_psi to which G072 applies.
falsifier: B110's equal-ambient-value countermodel and B091's vanishing of the pure-Hurwitz positive local-boundary realization
---

# NG086 — An ambient detector does not supply a nearby lift

**Status:** NO-GO

- **Route:** start with B058's nonzero primitive ambient detector $c$, choose
  the B057 word representing it, use a marked Hurwitz return to call that word
  $t_\psi$, and invoke B084 to choose an ordinary lift.
- **Valid input:** B057 constructs a distributed relative-thimble word;
  B058 proves that its ambient quotient pairs nontrivially with the prescribed
  Hodge class; B088 proves invariance if an actual marked collision returns
  the exact geometric datum; B084 lifts an actual invariant nearby IC class.
- **Invalid inference:** these results construct the missing collision-induced
  map from the distributed complex to the nearby stalk.
- **Precise obstruction:** B110 gives two candidate nearby realizations with
  the same exact ambient image, one liftable and one not. Moreover B091 shows
  that the pure-Hurwitz comparison sends the nonzero detector to zero in the
  positive local-boundary channel. Invariance alone neither realizes the
  class in the required nearby object nor retains the local detector.
- **Re-entry condition:** G073 must construct the actual source map and prove
  ordinary liftability and nonzero pairing. A successful construction must
  contain the topology-changing excess missing from the pure-Hurwitz map, as
  already isolated by G055.
