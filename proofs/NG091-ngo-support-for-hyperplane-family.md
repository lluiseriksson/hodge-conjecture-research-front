---
brick_id: NG091
status: NO-GO
base_field: C with rational Hodge coefficients downstream
variety: an arbitrary polarized smooth projective complex 2n-fold X and its universal sufficiently high-power hyperplane family
smoothness: X and generic hyperplane fibers smooth; hypothetical weak-abelian total space smooth
projectivity: X and hyperplane family projective
dimension: dim_C X = 2n with n at least 1; hyperplane fibers dimension 2n-1
codimension: middle codimension n; hyperplanes codimension one
coefficient_field: Q
cohomology_theory: perverse direct images, decomposition theorem, strict supports, Ngô support theorem, and canonical bundles
hodge_type: desired full-support coordinate rational type (0,0) after Q(n); no such coordinate is produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: generic
dependencies: B115, B117, G043, G076-G079, S051-S052
claim: Ngô's support theorem applies to the arbitrary high-power hyperplane family from projectivity and irreducibility alone and forces G076's selected class into full support.
falsifier: S051's weak-abelian hypotheses and B115's ample-canonical versus abelian-homogeneous contradiction
---

# NG091 — Ngô support does not apply to the hyperplane family

**Status:** NO-GO

- **Route:** invoke the decomposition theorem, irreducibility of generic
  high-power hyperplane sections, and Ngô's support theorem to remove every
  proper-support summand in G076.
- **Valid input:** the hyperplane family is projective, and generic members
  are smooth and irreducible.
- **Invalid inference:** these are all hypotheses of Ngô's theorem.
- **Precise obstruction:** S051 requires a same-dimensional smooth
  commutative group scheme action with affine stabilizers, polarizable Tate
  module, and delta-regularity. B115 proves such a structure is incompatible
  with the high-power generic fiber: it has ample canonical bundle, whereas
  the weak-abelian hypotheses would make it an abelian homogeneous quotient
  with trivial canonical bundle.
- **Re-entry condition:** B117 supplies a different family-specific support
  theorem for the original incidence map. G079 must still construct the
  selected relevant-grade class; no weak-abelian theorem creates it.
