---
brick_id: NG192
status: NO-GO
base_field: C
variety: arbitrary smooth projective complex 2n-folds, tested on Q^(2n) with primitive ruling difference a-b
smoothness: the quadric and marked point scheme are smooth and reduced; no central ODP construction is asserted
projectivity: tangent osculators, quartic mixed schemes, separator products, and line-plus-point loci are projective
dimension: dim X=d=2n>=4; the m=2 layers s=2d+6 and s=2d+7 are excluded
codimension: the ruling difference supplies a legitimate primitive codimension-n universal input
coefficient_field: Q for the Hodge input and C for sections, tensors, and incidence ranks
cohomology_theory: rational singular cohomology and coherent finite-scheme restriction
hodge_type: a-b is primitive rational type (n,n); no unknown class is assumed algebraic
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the known class only certifies the test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221-B234, G157
claim: Realize universal G148 through G157's m=2 signature s=2d+6, delta_1=d+3.
falsifier: B234 excludes O_Q(1) by tangent quotient rank, O_Q(2) by line-plus-one-point confinement, and O_Q(k), k>=3, by B233 in the excluded band
---

# NG192 — Two extra tangent-span dimensions do not realize G148

- **Route:** allow a two-dimensional quotient beyond two independent
  tangent osculators.
- **Valid premise:** this is larger than the span excluded by B233.
- **Invalid inference:** two dimensions can absorb a third tangent
  osculator or an arbitrarily large quartic point set.
- **Precise obstruction:** for \(O_Q(1)\), the third tangent quotient has
  dimension at least \(d-1\ge3\). For \(O_Q(2)\), any fifth dependent
  point must lie on a line containing three of four base points, forcing
  the whole configuration into a line plus at most one point and rank at
  most six. Higher powers are already excluded in this band.
- **Conclusion:** G157 and both slack layers \(2d+6,2d+7\) are
  **NO-GO**. G148 and HC remain open.
- **Re-entry condition:** G158 begins at
  \(s=2d+8,\delta_1=d+4\).
