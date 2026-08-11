---
brick_id: NG191
status: NO-GO
base_field: C
variety: arbitrary smooth projective complex 2n-folds, tested on Q^(2n) with primitive ruling difference a-b
smoothness: the quadric and marked scheme are smooth and reduced; no central ODP construction is asserted
projectivity: tangent osculators, quartic systems, mixed finite schemes, and secant lines are projective
dimension: dim X=d=2n>=4; the proposed m=2 slack s=2d+4 and adjacent slack 2d+5 are excluded
codimension: the ruling difference supplies a legitimate primitive codimension-n universal input
coefficient_field: Q for the Hodge input and C for sections, tensors, and ranks
cohomology_theory: rational singular cohomology and coherent finite-scheme restriction
hodge_type: a-b is primitive rational type (n,n); no unknown class is assumed algebraic
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the known class only certifies the test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221-B233, G156
claim: Realize universal G148 through G156's m=2 signature s=2d+4, delta_1=d+2.
falsifier: B233 excludes O_Q(1) by tangent-quotient rank, O_Q(2) by exact quartic separation and line confinement, and every O_Q(k), k>=3, by B215
---

# NG191 — One extra tangent-span dimension does not realize G148

- **Route:** pass from the exact two-tangent boundary to the next balanced
  code, allowing one additional span dimension.
- **Valid premise:** the point span can now strictly contain two independent
  tangent osculators.
- **Invalid inference:** one extra dimension can absorb every remaining
  point and tangent osculator.
- **Precise obstruction:** B233 exhausts all \(O_Q(k)\). For \(k=1\), a
  third tangent osculator has quotient image of dimension at least
  \(d-1\). For \(k=2\), quartic separation forces any fourth dependent
  point onto the line through the first three, collapsing the point rank
  to at most five. For \(k\ge3\), B215 gives too many independent mixed
  jets and points.
- **Conclusion:** G156 and both slack layers \(2d+4,2d+5\) are
  **NO-GO**. G148 and HC remain open.
- **Re-entry condition:** B234 later excludes G157 and its odd neighbor;
  move to G158 at \(s=2d+8,\delta_1=d+4\).
