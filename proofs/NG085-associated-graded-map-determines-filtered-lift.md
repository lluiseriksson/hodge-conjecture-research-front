---
brick_id: NG085
status: NO-GO
base_field: C with filtered rational Hodge structures
variety: an arbitrary polarized smooth projective complex 2n-fold with a projective plane-net collision and clean nodal target
smoothness: ambient and generic hyperplane fibers smooth; target clean nodal
projectivity: ambient variety, family, and collision projective
dimension: ambient 2n; hyperplane fibers 2n-1; plane base dimension 2
codimension: middle codimension n; target is a point of the plane base
coefficient_field: Q
cohomology_theory: perverse filtration, associated-graded special-to-nearby maps, quotient obstructions, and extension classes
hodge_type: restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B081, B107-B109, G071, S037
claim: Computing the dimensions and maps on every perverse associated grade determines omega_fil(t_psi) and hence filtered liftability.
falsifier: B109's pair u_0,u_1 with identical associated-graded maps and different filtered-lift obstruction
---

# NG085 — Associated-graded data do not determine the filtered lift

**Status:** NO-GO

- **Route:** compute $E_\infty$ ranks and the induced maps on every perverse
  grade, then infer $\omega_{\mathrm{fil}}(t_\psi)=0$.
- **Valid input:** associated grades and strict-support summands are canonical
  and detect where a class could land.
- **Invalid inference:** they recover the extension data of the filtered map.
- **Precise obstruction:** B109 gives filtered maps $u_0,u_1$ with identical
  maps on all associated grades. The same class $t$ has a filtered lift for
  $u_0$ and only an unfiltered lift for $u_1$; the difference is an
  off-diagonal coefficient invisible in $E_\infty$.
- **Re-entry condition:** G072 must compute an actual ordinary lift class in
  $S/(S_0+\ker u)$, equivalently the off-diagonal extension, or construct a
  dual functional separating $t_\psi$ from $u(S_0)$.

