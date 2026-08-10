---
brick_id: G057
status: EXPLORATORY
base_field: C with all classes and Hodge modules over Q
variety: an arbitrary polarized smooth projective complex 2n-fold, a prescribed primitive rational Hodge class, and the actual G055 projective collision to a clean nodal target H
smoothness: ambient and generic hyperplane fibers smooth; target clean nodal; semistable source regular as required
projectivity: plane-net family, collision, and proper pushdown projective
dimension: ambient 2n; hyperplane fibers 2n-1; plane base 2; collision base 1
codimension: middle codimension n; H is a point of the plane base and the nodal support has positive codimension
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, nearby cycles, perverse filtration, strict-support decomposition, local intersection cohomology, and B022 quotients
hodge_type: the canonical full-support coordinate must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B022, B081-B084, B092-B093, G046-G055, NG068-NG069
claim: For the actual special lift of the B058 detector, prove its canonical E_infinity^(-1,0) associated grade has a nonzero full-support component in H^(-1)(i_H^*P)=R(H)_1^(0,0), independent of lift ambiguity after both B022 quotients and retaining nonzero prescribed pairing.
falsifier: zero associated grade, confinement to divisor support, dependence on lift ambiguity, death in a B022 kernel, or orthogonality to the prescribed Hodge class
---

# G057 — Land in the canonical local-relation grade

**Status:** EXPLORATORY

Let $\beta\in H^{-1}(i_H^*K)$ be the actual special lift produced in the
G055 collision. Apply only canonical operations:

1. take the $E_\infty^{-1,0}$ associated grade of B081's perverse filtration;
2. inside ${}^pH^0(K)$, project to the unique full-support strict-support
   summand $P=j_{!*}L[2]$; and
3. use B093's canonical identification

   \[
   H^{-1}(i_H^*P)=R(H)_1^{(0,0)}.
   \]

Call the resulting coordinate $r_H$. The gate requires proof that changes of
$\beta$ allowed by B083 have zero image after the two B022 quotient maps and
the prescribed pairing, while

\[
 r_H\ne0,
 \qquad
 \langle\zeta,\gamma_{r_H}\rangle\ne0.
\]

No derived splitting may be chosen. The class-specific nonvanishing remains
terminal-level content.
