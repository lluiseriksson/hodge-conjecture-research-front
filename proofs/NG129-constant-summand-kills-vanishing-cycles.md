---
brick_id: NG129
status: NO-GO
base_field: C
variety: proper flat projective hypersurface families with a constant cohomology sheaf or flat class and an independently varying tracked-node specialization cone
smoothness: the counterfamily has connected fibers, tracked ordinary double points, and no untracked singularities after shrinking
projectivity: B161 supplies a projective fixed-linear-system counterfamily
dimension: arbitrary hypersurface dimension r; the counterfamily loses one node along a one-dimensional arc
codimension: one extra node branch fails to contain the basis germ although a nonzero cohomological piece is constant
coefficient_field: Q
cohomology_theory: rational proper direct images, constant local systems, nearby and vanishing cycles, and ordinary-double-point Milnor cohomology
hodge_type: a constant Tate class has fixed type, but no nonzero specified Saito detector pairing is asserted
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not resolved; constancy of an ambient class is not algebraicity of zeta
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B160-B162 and G102-G103
claim: Local constancy of one nonzero ambient cohomology sheaf, or preservation of one flat cohomology class, forces the entire disappearing-node vanishing-cycle complex to be zero.
falsifier: realize B161 on projective space with connected fibers; proper base change gives R^0 g_*Q=Q_T while the escaping node contributes a nonzero rank-one middle-degree specialization cone
---

# NG129 — A constant ambient cohomology sheaf does not kill node escape

- **Route:** preserve one ambient direct-image cohomology sheaf or one flat
  cohomology class and infer G103's total arcwise vanishing-cycle
  triviality.
- **Valid input:** the selected summand or class has no monodromy and its
  Hodge type can remain fixed.
- **Invalid inference:** the complementary middle specialization cone is
  zero.
- **Precise obstruction:** realize B161 on projective space, whose
  positive-degree hypersurfaces are connected. The unit class and proper
  base change give the constant cohomology sheaf

  \[
  \mathbf Q_T\simeq R^0g_*\mathbf Q.
  \]

  Along an arc in the basis germ with \(y\ne0\), that summand remains
  constant while the last node disappears. B162 computes the complementary
  specialization cone as one copy of \(\mathbf Q[-r]\).
- **Scope guard:** no splitting of the entire derived direct image is
  asserted. This also does not show that the actual specified Saito
  detector stays nonzero in B161. It proves only that constancy of a proper
  cohomology sheaf or class cannot imply vanishing of the whole cone.
- **Re-entry condition:** prove the full arcwise condition (1) of G103 and
  separately retain the nonzero specified relation-channel pairing.
