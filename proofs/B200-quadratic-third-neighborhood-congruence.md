---
brick_id: B200
status: PROVED
base_field: C
variety: a smooth projective complex d-fold with a line bundle L=H^m, a reduced point scheme Z, a central ODP section F in H0(I_2Z L), and a d-dimensional splitting U of the conditional first-jet quotient
smoothness: X and Z are smooth; every Hessian of F at Z is nondegenerate; no smoothness of the global incidence follows
projectivity: X, L, L^2, the second and third infinitesimal neighborhoods of Z, and all section spaces are projective coherent data
dimension: dim X=d; dim U=dim V=d; every node derivative U -> T_p^*X tensor L_p is an isomorphism
codimension: conformal inverse-Hessian rank one with multiplier in the value image is equivalent to one degree-2m congruence modulo I_Z^3
coefficient_field: C for sections, jets, Hessians, inverse forms, and quadratic multiplication; Q remains required separately for the Hodge detector
cohomology_theory: coherent second jets, ODP inverse Hessians, symmetric-square multiplication, and finite-dimensional linear algebra
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B191-B199, G124-G129, and the second product rule
claim: After choosing a splitting U isomorphic to V, B191's nonzero rank-one inverse-Hessian tensor with full-support multiplier lambda in the value image of H0(L) is equivalent to the existence of t in H0(L), nonzero on Z, and a nondegenerate Q in Sym^2 U such that tF-mu_2(Q) lies in H0(I_Z^3 L^2), with the symmetric multiplication normalized by its quadratic Taylor coefficient. Under this equivalence lambda=t|_Z and the common inverse form is Q^(-1).
falsifier: a conformally synchronized multiplier without the third-neighborhood congruence, a congruence whose pulled-back inverse Hessians are not rank one, or a degenerate/zero Q or multiplier under the ODP and one-node-isomorphism hypotheses
---

# B200 — Hessian holonomy is a quadratic congruence modulo \(I_Z^3\)

Let \(L=H^m\), let

\[
 V=H^0(I_ZL)/H^0(I_{2Z}L),\qquad \dim V=d,
\]

and choose a linear splitting \(U\subset H^0(I_ZL)\) mapping
isomorphically to \(V\). Assume every derivative map

\[
 d_i:U\xrightarrow{\sim}G_i=T_{p_i}^*X\otimes L_{p_i} \tag{1}
\]

is an isomorphism. Let \(0\ne F\in H^0(I_{2Z}L)\) have a nondegenerate
Hessian at every \(p_i\).

Write

\[
 \mu_2:\operatorname{Sym}^2U\longrightarrow H^0(X,L^2) \tag{2}
\]

for multiplication, normalized so that the quadratic Taylor coefficient
of \(\mu_2(Q)\) at \(p_i\) is
\(\operatorname{Sym}^2(d_i)(Q)\). Over \(\mathbf C\), this only fixes the
usual harmless factor of two.

## From conformal inverse Hessians to the congruence

Let \(B_i\) be the inverse-Hessian pairing on \(G_i\). Suppose B191's
rank-one condition holds:

\[
 d_i^*B_i=\lambda_iB_V, \qquad
 \lambda=(\lambda_i)\in
 \operatorname{im}\!\left(H^0(L)\to H^0(Z,L|_Z)\right), \tag{3}
\]

with every \(\lambda_i\ne0\). Choose \(t\in H^0(L)\) with

\[
 t(p_i)=\lambda_i. \tag{4}
\]

The common form \(B_V\) is nondegenerate. Put

\[
 Q=B_V^{-1}\in\operatorname{Sym}^2U. \tag{5}
\]

Choose local frames and bases. If \(A_i\) is the matrix of \(d_i\) and
\(H_i\) the Hessian matrix of \(F\), equation (3) is

\[
 A_i^{\mathsf T}H_i^{-1}A_i=\lambda_iB_V. \tag{6}
\]

Inverting (6) gives

\[
 \lambda_iH_i=A_iQA_i^{\mathsf T}. \tag{7}
\]

The left side is the quadratic Taylor coefficient of \(tF\), because
\(F\) vanishes to first order. The right side is the coefficient of
\(\mu_2(Q)\). Both sections already vanish to first order on \(Z\);
equality of (7) for every node is therefore exactly

\[
 tF-\mu_2(Q)\in H^0(X,I_Z^3\otimes L^2). \tag{8}
\]

## Converse

Conversely, assume \(t|_Z\) is nowhere zero, \(Q\) is nondegenerate, and
(8) holds. Equality of quadratic coefficients gives (7). Since \(A_i\),
\(Q\), and \(t(p_i)\) are invertible/nonzero, every \(H_i\) is
nondegenerate. Inverting (7) yields

\[
 A_i^{\mathsf T}H_i^{-1}A_i=t(p_i)Q^{-1}. \tag{9}
\]

Thus B191's tensor has rank one, common inverse form \(Q^{-1}\), and
multiplier \(t|_Z\) in the value image. Equations (8) and (9) are
frame-independent because both sides are second jets of global
\(L^2\)-sections.

B200 is an exact reformulation of the quadratic holonomy/multiplier
obligation. It does not construct \(F,U,t,Q,Z\), prove that their
degree-\(m\) classes are minimal generators, close cubic or higher
Kuranishi equations, or supply a rational detector or cycle.
