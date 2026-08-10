---
brick_id: B095
status: PROVED
base_field: C with rational Hodge structures
variety: special-to-nearby type-(0,0) stalk data of a projective collision for an arbitrary polarized smooth projective complex 2n-fold
smoothness: generic hyperplane fiber smooth; special target clean nodal; proof is finite-dimensional rational linear algebra
projectivity: collision projective in the application
dimension: ambient 2n; hyperplane fibers 2n-1; collision base 1
codimension: middle codimension n; target nodal stratum of positive codimension
coefficient_field: Q
cohomology_theory: rational mixed Hodge structures, special-to-nearby map, dual vector spaces, perverse grade, B022 quotients, and Saito pairing
hodge_type: restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence in the terminal application
scope: relative and fiberwise
dependencies: B083, B094
claim: For u:S->P, t in im(u), and detector functional F in S^*, a detecting lift of t exists iff either [F] is nonzero in coker(u^*) or [F]=0 and the uniquely induced functional on im(u) evaluates nontrivially at t.
falsifier: finite-dimensional rational data for which the stated cokernel/evaluation dichotomy disagrees with direct evaluation on the affine fiber u^(-1)(t)
---

# B095 — Dual obstruction for the affine lift gate

**Status:** PROVED

Let

\[
 u:S\longrightarrow P,
 \qquad t\in\operatorname{im}u,
 \qquad F\in S^*.
\]

The lift ambiguity is $A=\ker u$. Finite-dimensional duality gives

\[
 \operatorname{im}u^*=\operatorname{Ann}(A)\subseteq S^*.
\]

If $[F]\ne0$ in $\operatorname{coker}u^*$, then $F|_A\ne0$. B094 therefore
gives an ambiguity-adjusted lift with nonzero detector value.

If $[F]=0$, choose $\lambda\in P^*$ with $u^*\lambda=F$. For every lift
$u(\beta)=t$,

\[
 F(\beta)=\lambda(u\beta)=\lambda(t).
\]

Although $\lambda$ need not be unique on all of $P$, its restriction to
$\operatorname{im}u$ is unique, so $\lambda(t)$ is well defined. Thus a
detecting lift exists exactly in the two disjoint cases

\[
 [F]\ne0
 \quad\text{or}\quad
 [F]=0\text{ and }\lambda(t)\ne0.
\]

This is B094's affine disjunction expressed without choosing a base lift.

## Boundary

B095 does not compute the actual dual map, cokernel class, or descended
evaluation. G059 is that geometric calculation.
