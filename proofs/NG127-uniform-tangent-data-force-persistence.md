---
brick_id: NG127
status: NO-GO
base_field: C
variety: ordered ordinary-double-point critical-value germs with arbitrary uniform value rank R<N, projectively realizable after nonlinear analytic pullback
smoothness: all labeled branches and every intersection of at most R branches are smooth of expected codimension
projectivity: the countergerms have projective realizations through B157; the base maps into the linear system are generally nonlinear
dimension: base dimension R+1; N branches; differential rank R
codimension: the basis germ has codimension R, but the full escaping ideal (x_1,...,x_R,y^m) has reduced support of codimension R+1 and one hidden generator
coefficient_field: C for analytic germs and Q for unchanged local A1 data
cohomology_theory: representable matroids, analytic critical-value ideals, and local ordinary-double-point deformation theory
hodge_type: no specified type-(0,0) detector is constructed
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is absent; no algebraicity conclusion is drawn
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B155-B159 and G100-G101
claim: A uniform conormal matroid U_(R,N), smooth expected intersections through rank R, and agreement with a saturated arrangement to any fixed finite jet order force every extra node branch to contain a basis-node germ.
falsifier: B159 perturbs one branch by y^m; it preserves all stated data through order m-1 but restricts to y^m on the basis germ
---

# NG127 — Uniform tangent geometry does not force node persistence

- **Route:** use a uniform value matroid, smooth intersections of at most
  \(R\) branches, and finitely many matching jets to infer B158's branch
  containment.
- **Valid input:** these hypotheses determine the entire clean arrangement
  through rank \(R\) and its prescribed finite-order neighborhood.
- **Invalid inference:** an extra branch must contain the basis-node germ
  to all analytic orders.
- **Precise obstruction:** B159 takes Vandermonde linear forms
  \(\ell_i(x)\) and replaces only the last critical value by

  \[
  \tau_N=\ell_N(x)+y^m.
  \]

  The conormal matroid remains \(U_{R,N}\), all intersections through rank
  \(R\) remain smooth, and the \((m-1)\)-jet equals the saturated linear
  model. On \(F_B=\{x=0\}\), however, the last node escapes by \(y^m\), and
  the full ideal is \((x_1,\ldots,x_R,y^m)\).
- **Scope guard:** B157 makes this a projective nonlinear-pullback
  counterexample, not a counterexample to an unknown theorem using the
  full universal linear-system incidence.
- **Re-entry condition:** prove G101 by a global all-order incidence
  identity that retains the specified Hodge pairing.
