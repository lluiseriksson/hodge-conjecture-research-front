---
brick_id: NG125
status: NO-GO
base_field: C
variety: local analytic two-parameter families with two ordinary-double-point critical-value branches
smoothness: every spatial critical point is nondegenerate; the simultaneous-node base schemes in the counterfamily are nonreduced
projectivity: no projectivity is used in the local counterfamily; it falsifies any finite-order analytic inference inside a projective deformation germ
dimension: two base parameters; value rank R=1<N=2; tangent kernel and obstruction cokernel both one-dimensional
codimension: every prescribed finite Kuranishi truncation vanishes, while the ideal (x,y^m) is nonreduced
coefficient_field: C
cohomology_theory: analytic Kuranishi theory and local ordinary-double-point critical values
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is absent from the counterfamily; no algebraic cycle or detector is produced
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B154-B155 and G098-G099
claim: There exists a fixed finite order k such that vanishing of all Kuranishi tensors through order k forces reduced smooth rank-R excess for every nodal critical-value germ.
falsifier: for every k choose m>k and tau_m=(x,x+y^m), which has the same k-jet as the smooth factorized germ (x,x) but defines the nonreduced ideal (x,y^m)
---

# NG125 — No finite Kuranishi truncation certifies integration

- **Route:** compute \(\kappa_2,\ldots,\kappa_k\) for some fixed \(k\), prove
  they vanish, and declare the simultaneous-node germ smooth.
- **Valid input:** the first nonzero Kuranishi tensor is a genuine
  obstruction.
- **Invalid inference:** absence of obstructions through one finite order
  proves absence at every higher order.
- **Precise obstruction:** for every \(m\ge3\), the nodal critical-value
  model

  \[
  \tau_m(x,y)=(x,x+y^m)
  \]

  has \(\kappa_j=0\) for all \(j<m\) and
  \(\kappa_m(y)=y^m\ne0\). Given \(k\), choose \(m>k\). Its \(k\)-jet equals
  that of the smooth factorized germ \((x,x)\), while its ideal
  \((x,y^m)\) is nonreduced.
- **Re-entry condition:** prove B155's structural factorization
  \(\tau=A f\), or another theorem implying the entire analytic Kuranishi
  germ vanishes, and then verify the specified pairing.
