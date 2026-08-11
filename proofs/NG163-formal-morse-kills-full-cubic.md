---
brick_id: NG163
status: NO-GO
base_field: C
variety: a smooth projective complex 2n-fold with G130's central ODP section and a selected 2n-dimensional jet-generator slice
smoothness: the central ODP germs admit formal or holomorphic Morse normal forms; smoothness of the full ordered-node incidence is not implied
projectivity: X and the full linear system are projective, but the local coordinate normalization is formal or analytic and nodewise
dimension: the selected U slice has dimension 2n, while the full value-zero tangent kernel also contains Kbar=H0(I_2Z H^m)/C F
codimension: formal normalization of F can control the pure U^3 cubic block but omits the mixed Kbar tensor U^2 block
coefficient_field: C for formal coordinates and cubic jets; Q detector data are absent
cohomology_theory: formal Morse normalization, ODP critical values, coherent second jets, and cubic Kuranishi tensors
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B154, B157, B200-B201, G130-G131, NG150
claim: Normalize the central section formally to its common quadratic form on the U slice and conclude that the full cubic Kuranishi tensor vanishes.
falsifier: B201's mixed component Xi(a)(b,c) is the nodewise Hessian of an omitted double direction a contracted with two U displacements and is unaffected by normalizing F alone
---

# NG163 — Formal Morse normalization does not kill the full cubic tensor

- **Route:** divide G130 by \(t\), formally normalize the central ODP germ
  to \(Q\) at each node, and infer \(\kappa_3=0\).
- **Valid input:** the formal Morse lemma removes higher spatial terms of
  the fixed central function after nodewise coordinate changes.
- **Invalid inference:** this controls the critical values of every
  parameter direction in the full linear system.

The full value-zero tangent kernel is

\[
 U\oplus\overline K,\qquad
 \overline K=H^0(I_{2Z}H^m)/\mathbf CF.
\]

For \(a\in\overline K\) and \(b,c\in U\), B201 gives

\[
 \kappa_3(a,b,c)=
 \left[
 \bigl(\operatorname{Hess}_{p_i}(a)
 (H_i^{-1}d_ib,H_i^{-1}d_ic)\bigr)_i
 \right]\in\mathcal T/S. \tag{1}
\]

Changing coordinates to normalize \(F\) does not force the Hessians of all
independent double directions \(a\) to satisfy (1). B157 and NG150 already
show that fixed ODP normal forms coexist with arbitrary or unequal higher
critical-value terms.

- **Precise obstruction:** central spatial normal form is not uniform
  parameter-jet synchronization for the full projective tangent system.
- **Re-entry condition:** prove both B201 filters \(\Theta=0\) and
  \(\Xi=0\) without deleting \(\overline K\), retaining G130 and every
  detector clause.
