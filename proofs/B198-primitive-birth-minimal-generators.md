---
brick_id: B198
status: PROVED
base_field: C
variety: a smooth projective complex variety with a very ample H and a nonempty finite reduced point scheme Z
smoothness: X and Z are smooth at their supports; no ODP divisor or incidence smoothness follows
projectivity: X, the section ring of H, Z, and 2Z are projective or homogeneous projective data
dimension: dim X=d; a G125 birth has dim V_m=d=2n and therefore requires at least d independent degree-m minimal generators modulo products
codimension: lower jet extinction kills the first jets of every decomposable degree-m ideal section, so a nonzero birth is supported on new minimal ideal generators
coefficient_field: C for the section ring, ideal modules, jets, and generators; Q remains required separately for the detector
cohomology_theory: coherent ideal sheaves, graded section modules, first jets, and Serre vanishing
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B194-B197 and S065
claim: If V_k=0 for k<m, then the decomposable degree-m part sum_(a=1)^m H0(H^a)H0(I_Z H^(m-a)) lies in H0(I_2Z H^m). Hence V_m is a quotient of the degree-m minimal-generator space of the homogeneous ideal module of Z. A q_m=d birth requires at least d new degree-m generators with nonzero first-jet classes. For fixed Z the ideal module is finitely generated, so no primitive birth can occur beyond its largest generator degree.
falsifier: a decomposable product with a nonzero first jet despite lower extinction, q_m larger than the degree-m indecomposable generator space, or primitive births in arbitrarily high degrees for one fixed Z
---

# B198 — Primitive birth requires new ideal generators

Let

\[
 R=\bigoplus_{a\ge0}R_a,\quad R_a=H^0(X,H^a),\qquad
 J=\bigoplus_{k\ge0}J_k,\quad J_k=H^0(X,I_ZH^k), \tag{1}
\]

and let \(K_k=H^0(X,I_{2Z}H^k)\). Both \(J\) and
\(K=\bigoplus K_k\) are homogeneous ideals in the section ring \(R\).
Define the decomposable part

\[
 P_m=(R_+J)_m=\sum_{a=1}^{m}R_aJ_{m-a}. \tag{2}
\]

Assume the lower extinction required by G125:

\[
 J_k=K_k\qquad(0\le k<m). \tag{3}
\]

Every summand in (2) is then contained in \(R_aK_{m-a}\subset K_m\).
Therefore

\[
 P_m\subset K_m\subset J_m, \tag{4}
\]

and the quotient map factors as a surjection

\[
 J_m/P_m\twoheadrightarrow J_m/K_m=V_m. \tag{5}
\]

The left side is the degree-\(m\) space of minimal homogeneous generators
of the ideal module \(J\). Thus

\[
 \dim(J_m/P_m)\ge q_m. \tag{6}
\]

In G125, \(d=2n\) and \(q_m=d\), so at least \(d\) independent new
degree-\(m\) ideal generators must survive under the first-jet map. New
generators lying in \(K_m\) do not count.

## Finite birth window for fixed Z

S065 supplies finite generation directly. Choose \(r\) such that
\(I_ZH^r\) is globally generated and let

\[
 \mathcal E\longrightarrow I_ZH^r\longrightarrow0 \tag{7}
\]

be a surjection from a finite trivial bundle. After tensoring by \(H^a\),
Serre vanishing kills the first cohomology of the kernel for \(a\gg0\).
Taking global sections in (7) is then surjective, so all sufficiently high
pieces of \(J\) are products of finitely many earlier pieces. Adding the
finitely many intervening degrees gives a finite homogeneous generating
set for \(J\).

Let \(g(Z,H)\) be the largest degree in a minimal such set. If
\(m>g(Z,H)\) and (3) holds, then \(J_m=P_m\subset K_m\), hence \(V_m=0\),
contradicting a primitive birth. Therefore any G125 construction must vary
\(Z\) with the polarization and place \(m\) inside its finite
new-generator window.
This is necessary only; it supplies no ODPs, holonomy, detector, or cycle.
