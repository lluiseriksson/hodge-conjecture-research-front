---
brick_id: B199
status: PROVED
base_field: C
variety: a smooth projective complex d-fold with very ample H, a nonempty reduced point scheme Z, and a nonzero degree-m section F singular at every point of Z
smoothness: X and Z are smooth; F is assumed to have nondegenerate Hessian at each point of Z in the ODP application
projectivity: X, H^m, the homogeneous ideals of Z and 2Z, and the divisor of F are projective
dimension: dim X=d; in the maximal Hodge branch d=2n and dim V_m=d
codimension: the degree-m minimal-generator space has a double-generator kernel and a conditional-jet quotient; a new central section increases its dimension by at least one
coefficient_field: C for sections, ideals, jets, Hessians, and generators; Q remains required separately for the detector
cohomology_theory: graded coherent ideals, first and second jets, ODP Hessians, and finite-dimensional exact sequences
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B191-B198 and the product rule through second order
claim: Under lower extinction V_k=0 for k<m, with P_m=(R_+J)_m, there is an exact sequence 0 -> K_m/P_m -> J_m/P_m -> V_m -> 0. Thus a q_m=d birth plus a central nodal section F not in P_m requires at least d+1 degree-m minimal generators. If F lies in P_m, every Hessian Hess_p(F) is a value-weighted sum of Hessians of lower-degree sections double on Z and must be nondegenerate at every node.
falsifier: failure of the exact sequence, a new nonzero double generator without increasing the minimal-generator dimension, or an inherited F whose Hessian contains a first-derivative cross term or lies outside the lower-double Hessian span
---

# B199 — The central nodal generator dichotomy

Retain B198's notation

\[
 R=\bigoplus_{a\ge0}H^0(H^a),\qquad
 J_k=H^0(I_ZH^k),\qquad
 K_k=H^0(I_{2Z}H^k),
\]

and assume

\[
 J_k=K_k\qquad(0\le k<m). \tag{1}
\]

Put

\[
 P_m=(R_+J)_m=\sum_{a=1}^mR_aJ_{m-a}. \tag{2}
\]

B198 proves \(P_m\subset K_m\). The three nested spaces
\(P_m\subset K_m\subset J_m\) therefore give the exact sequence

\[
 0\longrightarrow K_m/P_m
 \longrightarrow J_m/P_m
 \longrightarrow J_m/K_m=V_m
 \longrightarrow0. \tag{3}
\]

Thus the degree-\(m\) minimal generators split numerically into

\[
 \dim(J_m/P_m)=\dim(K_m/P_m)+q_m. \tag{4}
\]

The first summand consists of new generators already double on \(Z\); the
second records their surviving conditional first jets.

## New-double branch

Let \(0\ne F\in K_m\) be the central section whose divisor is singular at
every point of \(Z\). If

\[
 F\notin P_m, \tag{5}
\]

then its class is nonzero in \(K_m/P_m\). Consequently

\[
 \dim(J_m/P_m)\ge q_m+1. \tag{6}
\]

For G128's maximal branch \(q_m=d=2n\), at least \(2n+1\) degree-\(m\)
minimal generators are required: \(2n\) independent jet classes plus at
least one new double class carrying the central member.

## Inherited-double branch

If instead \(F\in P_m\), write

\[
 F=\sum_{\nu}t_\nu s_\nu,\qquad
 t_\nu\in R_{a_\nu},\quad
 s_\nu\in J_{m-a_\nu}=K_{m-a_\nu}. \tag{7}
\]

At any \(p\in Z\), both \(s_\nu(p)\) and \(ds_\nu(p)\) vanish. The second
product rule therefore reduces to

\[
 \operatorname{Hess}_p(F)
 =\sum_\nu t_\nu(p)\operatorname{Hess}_p(s_\nu). \tag{8}
\]

All terms involving \(dt_\nu\otimes ds_\nu\) or \(s_\nu
\operatorname{Hess}(t_\nu)\) vanish. Hence an inherited central ODP section
is possible only if the value-weighted span of lower-double Hessians
contains a nondegenerate quadratic form at every marked point.

Equations (3)--(8) are necessary. They do not construct either branch,
prove simultaneous nondegeneracy, provide Hessian holonomy, close a
Kuranishi rung, or produce a rational detector or algebraic cycle.
