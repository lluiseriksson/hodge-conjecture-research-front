---
brick_id: B134
status: PROVED
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a sufficiently high universal hyperplane system, and an isolated nodal member Y_p with a quasi-local normal-crossing discriminant germ
smoothness: X and nearby hyperplane fibers are smooth; Y_p has finitely many ordinary double points
projectivity: X, the universal incidence family, and the parameter space are projective
dimension: dim_C X=2n; dim_C Y_p=2n-1; parameter dimension d is arbitrary
codimension: middle codimension n on X; the local parameter support has codimension at least two
coefficient_field: Q, with Q(n) throughout the Hodge-normalized comparison
cohomology_theory: rational intersection cohomology, limit mixed Hodge structures, vanishing homology, intermediate extension, and the perverse local Green-Griffiths invariant
hodge_type: the input is primitive rational type (0,0) after Q(n); the nodal relation space and its dual are pure type (0,0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B012, B125, B128, B133, S022 equations (0.3)-(0.5), Theorem 1 and Section 2.4, S024 Definition 3.3 and Proposition 3.8
claim: Intrinsically, the cohomological local IC stalk receiving s_m(zeta)_p is E(Y_p), canonically the dual R(Y_p)^vee of the nodal vanishing-cycle relation space; under this duality s_m(zeta)_p is the functional beta |-> <zeta,gamma_beta>. For two proportional cycles delta_2=c delta_1, its sole coordinate is evaluation on c e_1-e_2.
falsifier: a nodal degeneration satisfying the hypotheses for which the S022 canonical pairing does not identify E(Y_p) with R(Y_p)^vee, or for which the S024 local incidence class differs from the restriction cocycle used by S022
---

# B134 — The local incidence class is a dual relation functional

**Status:** PROVED

Let

\[
 R(Y_p)=\ker\!\left(
 \bigoplus_{y\in\operatorname{Sing}Y_p}
 H_{2n-1}(Z_{y,\infty},\mathbf Q(n))
 \longrightarrow H_{2n-1}(Y_\infty,\mathbf Q(n))
 \right)
\]

and let

\[
 E(Y_p)=\ker\!\left(
 H^{2n}(Y_p,\mathbf Q(n))
 \longrightarrow H^{2n}(Y_\infty,\mathbf Q(n))
 \right).
\]

S022 equation (0.3) identifies the latter with the degree-one
intermediate-extension stalk, with the ambient parameter shift restored:

\[
 E(Y_p)\simeq
 \mathcal H^{-d+1}\!\left(IC(V_m)\right)_p.
\]

The exact sequence dual to the vanishing-cycle sequence gives the canonical
perfect pairing

\[
 E(Y_p)\times R(Y_p)\longrightarrow\mathbf Q,
 \qquad E(Y_p)\simeq R(Y_p)^\vee.
\]

Thus the intrinsic cohomological stalk is the **dual** relation space. A
polarization and compatible Picard-Lefschetz orientations can model this
dual by a coefficient kernel, as in B009 and B038-B054, but that model must
not turn a cohomology class into a canonically selected relation vector.

## Identification of the specified class

S024 Definition 3.3 defines

\[
 s_m(\zeta)_p=[\zeta|_{Y_p}]_{00}
 \in\mathcal H^{-d+1}(IC(V_m))_p.
\]

For a sufficiently high embedding, Proposition 3.8 identifies this with the
canonical local restriction component. S022 Theorem 1(i) places that same
restriction cocycle in \(E(Y_p)\). If

\[
 \beta\in R(Y_p),\qquad
 \gamma_\beta\in H_{2n}(X,\mathbf Q(n))_{\mathrm{prim}}
\]

is the primitive ambient class constructed by equations (0.4)-(0.5), the
proof in S022 Section 2.4 gives

\[
 \boxed{
 s_m(\zeta)_p(\beta)
 =\langle\zeta,\gamma_\beta\rangle.
 }
\]

The equality is the canonical evaluation pairing between \(E(Y_p)\) and
\(E(Y_p)^\vee\simeq R(Y_p)\); primitive projection does not change it because
primitive and nonprimitive ambient parts are orthogonal.

Consequently

\[
 s_m(\zeta)_p\ne0
 \Longleftrightarrow
 \exists\beta\in R(Y_p):
 \langle\zeta,\gamma_\beta\rangle\ne0.
\]

## Two-branch coordinate

If \(\delta_2=c\delta_1\ne0\), then

\[
 R(Y_p)=\mathbf Q(c e_1-e_2),
 \qquad
 E(Y_p)=R(Y_p)^\vee.
\]

The unique intrinsic scalar required by G088 is therefore

\[
 s_m(\zeta)_p(c e_1-e_2)
 =\langle\zeta,\gamma_{c e_1-e_2}\rangle.
\]

If the cycles are independent, both \(R(Y_p)\) and its dual vanish. Hence
B133 and NG106 retain their rank conclusions after the duality correction.

## Scope guard

B134 identifies the coordinate exactly; it proves neither that a relation
point exists for a prescribed class nor that the displayed scalar is
nonzero. Universal existence of such a nonzero functional remains the
terminal-equivalent support gate G008/G088.
