---
brick_id: NG106
status: NO-GO
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold and a generic transverse two-node hyperplane in its universal family
smoothness: X and nearby fibers are smooth; the central fiber has two ordinary double points and a normal-crossing discriminant germ
projectivity: X and the family are projective
dimension: dim_C X=2n; fiber dimension 2n-1; parameter stratum codimension two
codimension: middle codimension n on X; proposed detector support codimension two
coefficient_field: Q
cohomology_theory: rational Picard-Lefschetz theory, local intersection cohomology, and the G088 filtered stalk spectral sequence
hodge_type: primitive type (n,n), normalized to (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B008-B009, B020, B027, B133-B134, G088, S009, S021
claim: A generic transverse codimension-two intersection of two nodal discriminant branches automatically supplies a nonzero ordinary target for the canonical B132 filtered section.
falsifier: two rationally independent nonzero vanishing cycles, for which B133 gives a zero relation kernel and zero local IC target
---

# NG106 — A generic transverse double node does not force survival

**Status:** NO-GO

- **Route:** choose a generic codimension-two intersection of two smooth
  discriminant branches and infer that the B132 section has acquired a
  possible nonzero ordinary boundary stalk.
- **Valid input:** the point has the smallest parameter codimension allowed
  by B012, two independently smoothable nodes, and a normal-crossing local
  discriminant.
- **Invalid inference:** two branches automatically give a nonzero
  degree-one IC channel.
- **Precise obstruction:** B133-B134 compute the target as the dual of

  \[
  \ker\!\left(\mathbf Q^2
  \xrightarrow{(a,b)\mapsto a\delta_1+b\delta_2}
  H_{2n-1}(X_s,\mathbf Q(n))\right).
  \]

  The kernel and its dual are zero when the two vanishing cycles are
  independent. B020's audited
  intersection-one pair is explicitly independent, and B027 proves more
  generally that full node independence kills the high-power relation
  channel.
- **Re-entry condition:** produce a class-directed boundary point with a
  genuine rational relation among its vanishing cycles and prove that the
  canonical incidence class has nonzero coordinate in that relation kernel.
  In the two-branch case the cycles must be proportional. More complicated
  multipart relation points remain allowed by G088.
