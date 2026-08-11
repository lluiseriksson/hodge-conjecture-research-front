---
brick_id: NG124
status: NO-GO
base_field: C
variety: a local analytic two-parameter family with two ordinary-double-point critical-value branches and value rank R=1<N=2
smoothness: each spatial critical point is nondegenerate; the simultaneous-node base germ is nonreduced
projectivity: no projectivity is used in the local countermodel; it falsifies an analytic inference proposed inside a projective deformation germ
dimension: two base parameters x,y; tangent kernel dimension one; obstruction cokernel dimension one
codimension: expected smooth height one, but the simultaneous-node ideal is (x,y^3), of height two as a set and nonreduced in the tangent direction
coefficient_field: C
cohomology_theory: local analytic ordinary-double-point deformation theory and Kuranishi tensors
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is absent from the countermodel; no algebraic cycle or detector is produced
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B145-B154 and G097-G098
claim: Vanishing of every synchronized B146 second-order obstruction implies the rank-deficient simultaneous-node germ is reduced and smooth of height R.
falsifier: critical-value map tau(x,y)=(x,x+y^3), whose differential has rank one and whose quadratic Kuranishi tensor is zero but cubic tensor is nonzero
---

# NG124 — Second-order flatness does not integrate

Let \(q(z_1,\ldots,z_{2n})=\sum_jz_j^2\). Consider two disjoint local nodal
charts with families

\[
 f_1(z;x,y)=q(z)+x,\qquad
 f_2(z;x,y)=q(z)+x+y^3.
\]

The spatial critical point in each chart is always \(z=0\), with fixed
nondegenerate Hessian. Their critical-value map is

\[
 \tau(x,y)=(x,x+y^3).
\]

At the origin,

\[
 E=d\tau_0=
 \begin{pmatrix}1&0\\1&0\end{pmatrix},
 \qquad R=1<N=2,\qquad V=\ker E=\mathbf C\,\partial_y.
\]

The relation \((1,-1)\) kills every quadratic term because

\[
 \tau_2-\tau_1=y^3.
\]

Thus all second-order relation-Hessian tensors vanish. But the reduced
Kuranishi map is

\[
 \kappa(y)=y^3,
\]

so \(\kappa_3\ne0\). The simultaneous-node ideal is

\[
 (x,x+y^3)=(x,y^3),
\]

which is nonreduced and not the smooth height-one excess germ predicted by
the invalid inference.

This is a local analytic countermodel, not a projective Hodge construction.
It proves that G098 needs an all-order geometric mechanism; second-order
flatness alone cannot provide one.
