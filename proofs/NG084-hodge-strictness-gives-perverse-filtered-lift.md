---
brick_id: NG084
status: NO-GO
base_field: C with rational mixed Hodge structures
variety: an arbitrary polarized smooth projective complex 2n-fold with a proper projective plane-net collision and clean nodal target
smoothness: ambient and generic hyperplane fibers smooth; target clean nodal
projectivity: ambient variety, family, and collision projective
dimension: ambient 2n; hyperplane fibers 2n-1; plane base dimension 2
codimension: middle codimension n; target is a point of the plane base
coefficient_field: Q
cohomology_theory: local invariant cycles, nearby/special stalks, perverse filtration, and rational Hodge structures
hodge_type: restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B083-B084, B107-B108, G070, S037
claim: B084's ordinary local-invariant-cycle surjectivity together with strictness of Hodge morphisms forces every liftable type-(0,0) nearby detector to lift from the relation-grade perverse filtration step S_0.
falsifier: B108's pure-Tate filtered countermodel or an actual collision with nonzero omega_fil(t_psi)
---

# NG084 — Hodge strictness does not imply perverse-filtered liftability

**Status:** NO-GO

- **Route:** combine B084's surjectivity from the special stalk with purity
  or strictness of Hodge morphisms and conclude
  $t_\psi\in u(S_0)$.
- **Valid input:** a locally invariant nearby class has some rational special
  lift; morphisms of rational Hodge structures respect the Hodge and weight
  data.
- **Invalid inference:** those facts make the special-to-nearby map strict
  for the separate perverse filtration.
- **Precise obstruction:** B108 constructs pure Tate data in which the map is
  a Hodge morphism and $t$ has an ordinary lift, but
  $[t]\ne0$ in $\operatorname{im}u/u(S_0)$. B084 contains no assertion about
  this quotient.
- **Re-entry condition:** G071 must compute the actual class
  $\omega_{\mathrm{fil}}(t_\psi)$ and prove it vanishes, either by an audited
  perverse-strictness theorem for the collision map or by constructing a
  lift explicitly inside $S_0$.

