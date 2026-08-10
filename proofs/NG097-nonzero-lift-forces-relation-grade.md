---
brick_id: NG097
status: NO-GO
base_field: C with exact countermodel over Q
variety: the original smooth projective plane-net incidence pushdown and an abstract pure-Hodge model of its degree-minus-one perverse filtration
smoothness: original incidence total space and generic fibers smooth; countermodel linear
projectivity: original family projective; countermodel records its allowed decomposition grades
dimension: ambient 2n; hyperplane fibers d=2n-1; plane base dimension 2
codimension: middle cycle codimension n; full support has base codimension zero
coefficient_field: Q
cohomology_theory: perverse filtration, proper direct image, rational pure Hodge structures, and strict support
hodge_type: both the ambient and relation coordinates may be pure type (0,0) after Q(n)
cycle_class_map: not used; downstream map is CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence downstream
scope: relative and fiberwise
dependencies: B092, B107-B109, B117-B121, G079-G082, S037
claim: Nonzeroness of an ordinary special lift, even together with B117-B118 and total type (0,0), does not force a nonzero nodal relation grade because the lift may lie entirely in E_infinity^(-2,1).
falsifier: a theorem eliminating the constant full-support pH^1 grade from the actual primitive-normalized object used by the selected class, with the required quotient and pairing compatibilities proved
---

# NG097 — A nonzero ordinary lift need not have relation grade

**Status:** NO-GO

- **Route:** combine nonzeroness of an ordinary lift with B117-B118 and infer
  that its \(E_\infty^{-1,0}\) relation coordinate is nonzero.
- **Valid input:** B117 eliminates divisor support in that grade, and B118
  eliminates the point grade \(E_\infty^{0,-1}\).
- **Invalid inference:** those are all possible positions in total degree
  \(-1\).
- **Precise obstruction:** B121 supplies the omitted constant ambient grade
  \(E_\infty^{-2,1}\). In the pure type-\((0,0)\) model

  \[
  S=\mathbf Qa\oplus\mathbf Qr,
  \]

  let \(a\) span the ambient grade and \(r\) the relation grade. The nonzero
  lift \(\beta=a\) has zero point and divisor coordinates and is total type
  \((0,0)\), but its relation coordinate is zero.
- **Re-entry condition:** prove the selected nearby class lies in
  \(u(S_0)\), equivalently kill B108's
  \(\omega_{\mathrm{fil}}\). Then the conditional form of B119 applies.
