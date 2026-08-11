---
brick_id: B135
status: PROVED
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, its sufficiently high hyperplane family, and a quasi-local normal-crossing nodal parameter p
smoothness: X and nearby hyperplane fibers are smooth; the central fiber has finitely many ordinary double points and independently smoothable local branches
projectivity: X and the universal hyperplane family are projective
dimension: dim_C X=2n; dim_C Y_p=2n-1; the normal-crossing parameter slice has arbitrary rank r
codimension: middle codimension n on X; the local boundary support has parameter codimension at least two
coefficient_field: Q, after clearing the denominator of the rational admissible normal function and with Q(n)
cohomology_theory: rational admissible normal functions, logarithmic Gauss-Manin connection, Picard-Lefschetz monodromy, the Cattani-Kaplan-Schmid/Green-Griffiths Koszul complex, and local intersection cohomology
hodge_type: the input is primitive rational type (0,0) after Q(n); every rational nodal relation and the resulting local quotient are pure type (0,0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B026, B133-B134, S021 Sections 4.2.3 and 4.3.2, S022 Theorem 1, and S024 Definition 3.3
claim: At a quasi-local normal-crossing nodal point, if the logarithmic residues of a local lift of the canonical normal function are a_i delta_i, then the specified local incidence class is the canonical quotient [a] in coker(Delta^*), which pairs perfectly with R=ker(Delta) by <[a],b>=sum_i b_i a_i; changing the lift adds Delta^*(v). For delta_2=c delta_1, the sole invariant coordinate is c a_1-a_2.
falsifier: a nodal normal-crossing model satisfying the hypotheses where changing the normal-function lift changes the displayed relation evaluations, where coker(Delta^*) is not dual to ker(Delta), or where the Green-Griffiths residue class differs from the Saito/de Cataldo-Migliorini local incidence class
---

# B135 — The local class is the residue cokernel

**Status:** PROVED

Let \(V=H_{2n-1}(Y_t,\mathbf Q(n))\) and let \(Q\) be its nondegenerate
Picard-Lefschetz polarization. For the nodal vanishing cycles
\(\delta_1,\ldots,\delta_r\), define

\[
 \Delta:\mathbf Q^r\longrightarrow V,
 \qquad e_i\longmapsto\delta_i,
\]

and its polarized transpose

\[
 \Delta^\ast:V\longrightarrow\mathbf Q^r,
 \qquad
 v\longmapsto\bigl(Q(v,\delta_i)\bigr)_{i=1}^r.
\]

The relation space is \(R_p=\ker\Delta\).

## Residues of the specified normal function

Green–Griffiths Section 4.3.2 starts with a local multivalued lift
\(\widetilde\nu_\zeta\) of the admissible normal function. After clearing one
integer denominator, the logarithmic residue along branch \(D_i\) lies in
\((T_i-I)V\). For a node, Picard–Lefschetz gives

\[
 (T_i-I)V=\mathbf Q\delta_i.
\]

Thus write

\[
 \operatorname{Res}_{D_i}\nabla\widetilde\nu_\zeta
 =a_i\delta_i
\]

up to the common cleared denominator. The degree-one residue vector is
\(a=(a_i)\in\mathbf Q^r\).

Changing the lift by a flat lattice vector \(v\in V\) changes the residues
by \(((T_i-I)v)_i\). In coefficient coordinates this is

\[
 a\longmapsto a+\Delta^\ast(v),
\]

up to the universal Picard-Lefschetz sign, which changes neither the quotient
nor nonvanishing. Hence the intrinsic residue class is

\[
 [a]\in\operatorname{coker}\Delta^\ast.
\]

The other lift ambiguity is addition of a holomorphic Hodge-filtration
section. S021 Section 4.3.2 checks that its contribution vanishes in the
infinitesimal-invariant complex. Thus neither allowed ambiguity changes
\([a]\).

Green–Griffiths' map from the logarithmic complex to the monodromy Koszul
complex sends the infinitesimal invariant to this class. Their comparison
with local intersection cohomology, together with S024 Definition 3.3,
identifies it with \(s_m(\zeta)_p\).

## Canonical duality with relations

For \(b=(b_i)\in R_p\), put

\[
 \langle[a],b\rangle=b^{\mathsf T}a=\sum_i b_i a_i.
\]

This is independent of the lift because

\[
 b^{\mathsf T}\Delta^\ast(v)
 =Q(v,\Delta b)=0.
\]

Conversely, nondegeneracy of \(Q\) gives

\[
 \operatorname{im}\Delta^\ast=(\ker\Delta)^\perp.
\]

Therefore the dot-product pairing induces a canonical perfect pairing

\[
 \operatorname{coker}\Delta^\ast
 \xrightarrow{\sim}(\ker\Delta)^\vee.
\]

This recovers B134's intrinsic typing and makes the filtered cancellation
concrete:

\[
 s_m(\zeta)_p=0
 \Longleftrightarrow
 a\in\operatorname{im}\Delta^\ast
 \Longleftrightarrow
 \sum_i b_i a_i=0\quad\text{for every }b\in R_p.
\]

## Minimal two-branch scalar

If \(\delta_2=c\delta_1\ne0\), then

\[
 R_p=\mathbf Q(c e_1-e_2),\qquad
 \operatorname{im}\Delta^\ast=\mathbf Q(1,c).
\]

The entire local incidence class is the lift-invariant scalar

\[
 \boxed{\rho_{\zeta,p}=c\,a_1-a_2.}
\]

It is unchanged by adding \(q(1,c)\) to the residue vector. It agrees with
B134 because

\[
 \rho_{\zeta,p}
 =s_m(\zeta)_p(c e_1-e_2)
 =\langle\zeta,\gamma_{c e_1-e_2}\rangle.
\]

## Scope guard

B135 converts the minimal filtered-stalk calculation into an exact residue
mismatch. It does not produce a proportional two-node fiber and does not
prove \(\rho_{\zeta,p}\ne0\). Universal existence of such a mismatch remains
the terminal-hard gate G088; G089 records its smallest clean two-branch
specialization.
