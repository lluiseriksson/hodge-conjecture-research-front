---
brick_id: NG117
status: NO-GO
base_field: C
variety: a smooth projective complex 2n-fold X, a high-power line bundle L, and an ordered nodal member whose node-value evaluation has rank R<N
smoothness: X and the nodes are smooth/ordinary double points; smoothness of the excess incidence is the invalid conclusion under audit
projectivity: X and |L| are projective; the obstruction is local analytic
dimension: dim_C X=2n; N ordered nodes; value rank R<N
codimension: the tangent codimension is 2nN+R, but the actual incidence need not be smooth of that codimension
coefficient_field: C for the deformation calculation; Q only in the absent downstream Hodge relation
cohomology_theory: first- and second-jet nodal deformation theory, evaluation matroids, and analytic obstruction theory
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B145-B146 and G091-G092
claim: A value-rank degeneracy point with R<N and the B145 tangent dimension automatically lies on a smooth excess ordered-node component.
falsifier: conditional gradient surjectivity makes a B146 Hessian obstruction nonzero for every nonzero value relation
---

# NG117 — Value-rank drop does not produce smooth excess

**Status:** NO-GO

- **Route:** impose the determinantal condition
  \(\operatorname{rank}E_\Delta=R<N\), use B145's tangent dimension, and
  infer the smooth component required by G091.
- **Valid input:** the Zariski tangent of the ordered-node incidence has
  codimension \(2nN+R\).
- **Invalid inference:** equality of this tangent codimension with the
  desired geometric codimension proves reducedness or smoothness.
- **Precise obstruction:** each value relation \(c\in\ker E^*\) gives the
  B146 quadratic obstruction

  \[
  q_c((da_{p_i}))=
  \sum_i c_i\,da_{p_i}(H_i^{-1}da_{p_i}).
  \]

  Smoothness forces this form to vanish on the conditional gradient image.
  If conditional gradients are surjective, choose one node in the support
  of \(c\) and a covector with nonzero Hessian square; then \(q_c\ne0\).
  Under a uniform \(U_{R,N}\) value matroid, smoothness in fact requires
  conditional-gradient corank at least \(n(R+1)\).
- **Re-entry condition:** construct the common Hessian-isotropic gradient
  degeneracy, integrate it through all higher orders to a reduced smooth
  height-\(R\) smoothing ideal, and prove a nonzero class-specific Saito
  pairing as in G092.
