---
brick_id: NG133
status: NO-GO
base_field: C
variety: the full complete-linear-system universal hypersurface family near a member with exhaustive tracked ordinary double points and a smooth basis-node germ F_B
smoothness: the base, universal incidence, F_B, and all labeled nodal discriminant branches are smooth; no untracked singularity is present after shrinking
projectivity: the universal hypersurface map is projective
dimension: arbitrary base dimension; hyperplane dimension 2n-1 in the Hodge application; value rank R<N
codimension: F_B has codimension R and every tracked discriminant branch is a divisor
coefficient_field: Q for sheaves and C for analytic branch equations
cohomology_theory: proper direct-image microsupport, higher-discriminant envelopes, microlocal inverse image, ODP vanishing cycles, and analytic syzygies
hodge_type: no rational type-(0,0) detector is produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) only downstream; no algebraic cycle is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B155-B169, G100-G106, S068
claim: Ambient microsupport or higher-discriminant normal-cone absorption is a strictly weaker certificate than all-order critical-value factorization and can bypass the hidden-generator obstruction H_tau.
falsifier: B169 proves that, in the exhaustive tracked-ODP neighborhood required by G106, both absorption conditions are equivalent to persistence of every node and hence to H_tau=0
---

# NG133 — The microlocal envelope does not bypass analytic syzygies

- **Route:** use the ambient sheaf microsupport or the larger
  higher-discriminant envelope as a new source of absorption, without
  proving the critical-value identities required by G100/G101.
- **Valid input:** B167 gives an upper bound after microlocal pullback, and
  Migliorini--Shende give a geometric ambient envelope.
- **Invalid inference:** the zero \(i^\#\)-condition is weaker than exact
  persistence of every tracked ODP branch.
- **Precise obstruction:** B169 proves that the envelope is locally the
  union of the labeled nodal conormals, each of which also occurs in the
  actual direct-image microsupport. Its \(i^\#\)-image is zero exactly when
  the corresponding divisor contains \(F_B\). Hence absorption is
  equivalent to \(H_\tau=0\) and analytic syzygy lifting.
- **Scope guard:** this does not prove that the required syzygies are
  impossible. It proves only that microlocal language supplies no weaker
  carrier-free mechanism in the stated ODP neighborhood.
- **Re-entry condition:** construct the full-linear-system data with
  \(H_\tau=0\) and independently prove the rational type, primitive image,
  and specified nonzero Saito pairing demanded by G100/G101.
