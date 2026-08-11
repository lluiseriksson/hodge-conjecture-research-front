---
brick_id: NG134
status: NO-GO
base_field: C
variety: a two-parameter affine-linear hypersurface deformation with two disjoint tracked ODP charts, realizable as a linear slice of a sufficiently ample projective hypersurface system
smoothness: both spatial critical points have fixed nondegenerate quadratic Hessian; projective realization is smooth away from the prescribed nodes after a general choice
projectivity: the explicit calculation is local analytic; finite-jet interpolation and Bertini realize it on a projective linear slice, not as a rank-deficient full complete-system germ
dimension: two base parameters x,y; two ODPs; central slice-value rank R=1<N=2
codimension: the simultaneous-node ideal is (x,y^2), not the desired smooth height-one ideal
coefficient_field: C
cohomology_theory: affine-linear ODP deformation theory, critical-point elimination, coherent finite-jet interpolation, and analytic local algebra
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B145-B170, G100-G107, NG117, S065
claim: Affine-linearity of the hypersurface deformation together with central uniform value rank R<N forces the moving critical-point evaluation rank to remain R and hence forces H_tau=0.
falsifier: the linear two-chart family q(z)+x and q(w)+x+2yw_1 has critical values (x,x-y^2), central uniform rank one, moving rank two off y=0, and one-dimensional H_tau
---

# NG134 — A linear family can still have quadratic node escape

Let

\[
 q(z)=z_1^2+\cdots+z_d^2
\]

and take two disjoint spatial charts with the affine-linear families

\[
 F_1(z;x,y)=q(z)+x,
\qquad
 F_2(w;x,y)=q(w)+x+2yw_1. \tag{1}
\]

Both Hessians are the fixed nondegenerate matrix \(2I\). The first
critical point is \(z=0\), while the second is

\[
 w_1=-y,\qquad w_2=\cdots=w_d=0.
\]

Their critical values are

\[
 \tau_1=x,\qquad \tau_2=x-y^2. \tag{2}
\]

Thus

\[
 d\tau_0=
 \begin{pmatrix}
 1&0\\
 1&0
 \end{pmatrix},
\]

whose row matroid is \(U_{1,2}\). Nevertheless

\[
 d\tau_{(x,y)}=
 \begin{pmatrix}
 1&0\\
 1&-2y
 \end{pmatrix}
\]

has rank two whenever \(y\ne0\). Moreover,

\[
 I_\tau=(x,y^2),\qquad
 \mu(I_\tau)=2,\qquad
 H_\tau\simeq\mathbf C.
\]

The relation \((1,-1)\) among the central differentials therefore does
not lift to a syzygy nonzero at the origin.

The family (1) is affine-linear in its parameters; no nonlinear base
pullback creates the escape. Using sufficiently ample finite-jet
interpolation, choose two global deformation sections with precisely the
displayed value and gradient jets at two prescribed ODPs. A general
section with those finite jets is smooth elsewhere by Bertini, so the
same nonzero quadratic obstruction occurs on a projective linear slice.

## Scope guard

Jet separation in that high-power realization makes the **full**
complete-system value evaluation larger than the rank-one evaluation on
the chosen slice. Hence NG134 does not refute G107, whose hypothesis is
about the full affine chart and its global determinantal locus. It proves
that projectivity, ODPs, and affine-linearity alone add no all-order
syzygy mechanism beyond the Hessian obstruction already exposed by
B146/NG117.
