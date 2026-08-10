---
brick_id: G070
status: EXPLORATORY
base_field: C with all collision stalks, filtrations, Hodge structures, and maps over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified nonzero primitive rational middle Hodge class, its B058 nearby detector t_psi, and an actual projective collision to a clean nodal hyperplane target H
smoothness: X and generic hyperplane fibers smooth; target has finitely many ordinary double points; semistable source regular where required
projectivity: X, plane-net hyperplane family, collision, and proper pushdown projective
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; plane base dimension 2
codimension: middle codimension n; H is a point of the plane base with finite nodal singular support
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, perverse filtration, strict support, special-to-nearby map, B022 quotients, Saito relation pairing, and dual vector spaces
hodge_type: S_0, t_psi, F_0, relation coordinates, and all maps restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B022, B058, B081-B084, B093-B108, G048-G059, G071, NG068-NG084, S022-S023, S037
claim: For the actual collision, identify the canonical relevant filtration step S_0, prove t_psi lies in the image of u_0=u|_(S_0), construct the canonical functional F_0 on S_0, and prove either [F_0] is nonzero in coker(u_0^*) or it vanishes and the descended functional evaluates nontrivially on t_psi.
falsifier: undefined filtration step or relation-grade map, t_psi outside im(u_0), wrong coefficient field or Hodge type, or simultaneous failure of both filtered dual branches
---

# G070 — Compute the filtered dual detector certificate

**Status:** EXPLORATORY

For the actual topology-changing collision let

\[
 u:S=H^{-1}(i_H^*K)^{(0,0)}
 \longrightarrow P_\psi
\]

be the special-to-nearby map. Let $S_0$ be B107's canonical perverse
filtration step whose associated grade contains the full-support relation
stalk.

The first obligation is stronger than ordinary B083 liftability and must be
proved geometrically:

\[
 t_\psi\in\operatorname{im}
 \bigl(u_0:S_0\to P_\psi\bigr).
\]

B108 identifies its exact obstruction as
$\omega_{\mathrm{fil}}(t_\psi)=[t_\psi]$ in
$\operatorname{im}u/u(S_0)$. G071 is the active subgate proving that coset
vanishes; NG084 blocks replacing this calculation by Hodge strictness.

Next construct the canonical relation-grade functional

\[
 F_0:S_0
 \longrightarrow R(H)_1^{(0,0)}
 \xrightarrow{\Phi_H}PH_{2n}(X,\mathbf Q(n))^{(0,0)}
 \xrightarrow{\langle\zeta,-\rangle}\mathbf Q.
\]

Finally compute the exhaustive B107 alternative:

\[
 [F_0]\ne0\text{ in }\operatorname{coker}(u_0^*)
\]

or, if $F_0=u_0^*\lambda$,

\[
 \lambda(t_\psi)\ne0.
\]

Either branch produces an admissible filtered special lift whose canonical
Saito relation coordinate detects $\zeta$. No splitting of the total special
stalk is permitted.

This is the exact parent gate. G071 is its smallest current subgate: kill the
filtration-compatible lift obstruction before the subsequent scalar
computation, retaining the official rational coefficients and arbitrary
smooth-projective scope.
