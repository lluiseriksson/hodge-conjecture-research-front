---
brick_id: NG083
status: NO-GO
base_field: C with rational mixed Hodge modules
variety: an arbitrary polarized smooth projective complex 2n-fold with a projective plane-net collision and clean nodal target
smoothness: ambient and generic hyperplane fibers smooth; target clean nodal
projectivity: ambient variety, hyperplane family, and proper collision pushdown projective
dimension: ambient 2n; hyperplane fibers 2n-1; plane base dimension 2
codimension: middle codimension n; target is a point of the plane base
coefficient_field: Q
cohomology_theory: perverse filtration, associated grades, strict support, nearby/special maps, and dual Hodge structures
hodge_type: restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B081, B093-B095, B107, G057-G059, NG069, S037
claim: The canonical perverse associated grade and strict-support decomposition define a canonical detector functional on the entire special stalk S, so G059 may form coker(u^*) without restricting the domain.
falsifier: B107's filtered-vector-space extensions and S037's noncanonical splitting warning
---

# NG083 — An associated grade is not a total-stalk functional

**Status:** NO-GO

- **Route:** compose the whole special stalk
  $S=H^{-1}(i_H^*K)$ directly with the $E_\infty^{-1,0}$ relation grade and
  regard the result as a canonical $F\in S^*$.
- **Valid input:** the perverse filtration, its associated grades, and the
  strict-support decomposition inside each perverse cohomology object are
  canonical.
- **Invalid inference:** a canonical filtration canonically splits, or gives
  a projection from all of $S$ to one grade.
- **Precise obstruction:** the quotient map exists only on the relevant
  filtration step $S_0$. A functional on $S_0$ has many extensions to $S$;
  choosing one is the same kind of unaudited splitting already excluded by
  B081/NG069.
- **Re-entry condition:** G070 must first prove
  $t_\psi\in\operatorname{im}(u|_{S_0})$, then compute B107's dual
  certificate using $u_0:S_0\to P_\psi$ and $F_0\in S_0^*$.

