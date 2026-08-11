---
brick_id: NG135
status: NO-GO
base_field: C
variety: an affine-linear two-parameter hypersurface deformation with two disjoint ODP charts, realizable as a projective linear slice by finite-jet interpolation
smoothness: both tracked spatial Hessians are fixed and nondegenerate; the simultaneous-node germ is reduced smooth of height one
projectivity: the exact model is local analytic; its finite jets occur on a sufficiently ample projective linear slice
dimension: two parameters x,y; two ODP branches; central rank R=1<N=2
codimension: the critical-value ideal is the smooth height-one ideal (x), while the Jacobian rank jumps to two off x=0
coefficient_field: C
cohomology_theory: affine-linear ODP deformation theory, critical-value Hessians, determinantal tangent spaces, and analytic syzygies
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B145-B171, G100-G107, NG134, S065
claim: Smooth reduced excess, H_tau=0, or all B146 Hessian equations on ker E times ker E force G107's constant critical-evaluation rank.
falsifier: the affine-linear ODP model has tau=(x,(1+y)x), ideal (x), H_tau=0, and zero pure conditional Hessian, but det(d tau)=x and the mixed W times ker E obstruction is nonzero
---

# NG135 — Smooth excess does not force constant critical rank

Use a nondegenerate quadratic form containing a hyperbolic block

\[
 q(u,v,z')=uv+\sum_j(z'_j)^2.
\]

Take two disjoint ODP charts. In the first put

\[
 F_1=q+x.
\]

In the second put the affine-linear family

\[
 F_2=q+x+xu-yv. \tag{1}
\]

The second critical-point equations give

\[
 u=y,\qquad v=-x,\qquad z'=0.
\]

Substitution into (1) yields

\[
 \tau_1=x,\qquad
 \tau_2=x+xy=(1+y)x. \tag{2}
\]

Therefore

\[
 I_\tau=(x),\qquad H_\tau=0,
\]

and the central relation lifts analytically as

\[
 (1+y)\tau_1-\tau_2=0. \tag{3}
\]

The simultaneous-node germ is reduced smooth of codimension one. On
\(V=\ker d\tau_0=\mathbf C\,\partial_y\), every B146 quadratic pairing is
zero. Nevertheless

\[
 d\tau=
 \begin{pmatrix}
 1&0\\
 1+y&x
 \end{pmatrix},
\qquad
 \det(d\tau)=x. \tag{4}
\]

Thus the rank is two whenever \(x\ne0\). Equivalently, for the relation
\((1,-1)\),

\[
 (1,-1)\,d^2\tau_0(\partial_x,\partial_y)=-1\ne0,
\]

which is precisely B171's mixed \(W\times V\) obstruction.

As in NG134, S065 finite-jet interpolation realizes the displayed
Hessians, values, and deformation gradients on a projective linear slice.
This does not make the full complete-system value rank equal to one.

## Consequence

G107 remains a valid sufficient theorem, but it is strictly stronger than
the exact gate \(H_\tau=0\) and can exclude already successful smooth
excess germs. It should therefore be treated as an optional mechanism,
not as the replacement for G100. Any use of G107 must supply its mixed
determinantal equations directly and still prove the specified pairing.
