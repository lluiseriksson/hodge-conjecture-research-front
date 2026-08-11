---
brick_id: NG162
status: NO-GO
base_field: C
variety: a smooth projective complex 2n-fold with G129's degree-m ideal generators vanishing on a reduced node scheme Z
smoothness: X and Z are smooth and the proposed central section has ODPs; the multiplier obstruction is value-theoretic
projectivity: X, H^m, the value evaluation on Z, and the degree-m generator package are projective
dimension: N nodes; every valid conformal multiplier has N nonzero coordinates, while every ideal generator has zero value vector
codimension: an ideal section cannot supply the full-support value multiplier needed in B200's quadratic congruence
coefficient_field: C for sections, values, and Hessians; Q detector data are absent
cohomology_theory: coherent value evaluation, first and second jets, and ODP inverse-Hessian linear algebra
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B191-B200, G124-G130
claim: Use the central double generator F or one of the transverse ideal generators in J_m as the multiplier t in B200's congruence.
falsifier: every element of J_m=H0(I_Z H^m) has zero value on Z, whereas B193 maximal holonomy forces every multiplier coordinate to be nonzero
---

# NG162 — The multiplier cannot be an ideal generator

- **Route:** recycle \(F\) or one of G129's \(2n\) jet generators as the
  section \(t\) in
  \[
  tF-\mu_2(Q)\in H^0(I_Z^3H^{2m}).
  \]
- **Valid input:** all these sections have the correct degree \(m\).
- **Invalid inference:** degree compatibility implies the full-support
  value condition.

Every generator in \(J_m=H^0(I_ZH^m)\) restricts to zero on \(Z\).
By B193, maximal one-node determination and nondegenerate Hessians force
every coordinate of the conformal multiplier to be nonzero. Therefore no
element of \(J_m\), including \(F\), can be \(t\).

- **Precise obstruction:** B200 needs an ambient degree-\(m\) section
  outside the point ideal whose value vector equals the conformal
  multiplier.
- **Re-entry condition:** construct \(t\in H^0(H^m)\setminus J_m\) with
  nowhere-zero values on \(Z\) and prove the global third-neighborhood
  congruence, while retaining generator minimality and every detector
  clause.
