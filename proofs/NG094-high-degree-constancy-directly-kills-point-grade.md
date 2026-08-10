---
brick_id: NG094
status: NO-GO
base_field: C
variety: the original plane-net incidence family of hyperplane sections of an arbitrary polarized smooth projective complex 2n-fold and an isolated-singularity collision fiber
smoothness: incidence total space smooth; nearby fibers smooth; collision fiber has isolated hypersurface singularities
projectivity: the incidence family is projective
dimension: hyperplane fibers have dimension d = 2n-1; plane base dimension 2
codimension: middle cycle codimension n; tested support is a base point of codimension two
coefficient_field: Q
cohomology_theory: higher direct images, vanishing cycles, perverse normalization, strict support, and relative hard Lefschetz
hodge_type: no selected Hodge class; the attempted implication concerns rational support multiplicity
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B080-B081, B118, G079-G080, S022, S037
claim: Constancy of sufficiently high direct images outside the isolated vanishing degree directly excludes the point-supported term in pH^(-1)(K), without using relative hard Lefschetz.
falsifier: the exact shift calculation placing a point pH^(-1) summand in H^(-1)(K)=R^(d+1), which can jump by the vanishing-cycle relation space
---

# NG094 — High-degree constancy is not in the original point-term degree

**Status:** NO-GO

- **Route:** cite concentration of isolated vanishing cohomology in degree
  \(d\), note that high direct images are constant, and immediately discard
  point support in \({}^pH^{-1}(K)\).
- **Valid input:** \(R^{d+3}h_*\mathbf Q\) is unchanged across the isolated
  collision.
- **Invalid inference:** the proposed point term contributes directly to
  that high direct image.
- **Precise obstruction:** a point perverse sheaf in
  \({}^pH^{-1}(K)\) occurs in \(K\) shifted by \([1]\), hence contributes
  to \(\mathcal H^{-1}(K)=R^{d+1}h_*\mathbf Q\). That sheaf can and does
  jump by the relation/extra-cohomology group in S022 Proposition 1.
- **Re-entry condition:** B118 uses relative hard Lefschetz to reflect the
  hypothetical point summand supportwise into \({}^pH^1(K)\). Only the
  reflected term contributes to the constant
  \(R^{d+3}h_*\mathbf Q\), giving the contradiction.
