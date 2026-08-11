---
brick_id: NG190
status: NO-GO
base_field: C
variety: arbitrary smooth projective complex 2n-folds, tested on Q^(2n) with primitive ruling difference a-b
smoothness: the quadric and marked points are smooth; no central ODP construction is asserted
projectivity: all complete quadric embeddings, tangent spans, double neighborhoods, and secant data are projective
dimension: dim X=d=2n>=4; the proposed m=2 slack s=2d+2 is excluded, and so is the adjacent odd slack s=2d+3
codimension: the ruling difference is a legitimate primitive codimension-n universal input
coefficient_field: Q for the Hodge input and C for jets, tensors, and ranks
cohomology_theory: rational singular cohomology and coherent finite-jet restriction
hodge_type: a-b is primitive rational type (n,n); no unknown class is assumed algebraic
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the known class only certifies the test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221-B232, G155
claim: Realize universal G148 through G155's m=2 dimension-scaled threshold s=2d+2, delta_1=d+1.
falsifier: B232 proves that a span of this dimension cannot contain a third marked point after absorbing two independent tangent osculators, while the all-defective alternative is isotropically impossible
---

# NG190 — The first dimension-scaled threshold is still too small

- **Route:** repair G154 by replacing fixed slack ten with the first B231
  dimension-scaled value \(s=2d+2\).
- **Valid premise:** this is exactly where two \(d+1\)-dimensional tangent
  jet spaces first fit in the degree-one point span.
- **Invalid inference:** fitting two tangent spaces leaves room for the
  remaining marked points.
- **Precise obstruction:** B232 shows that the span has exactly dimension
  \(2d+2\). For powered quadric polarizations, B215 separates two doubles
  and a third point. For \(O_Q(1)\), either every pair is orthogonal and
  tangent absorption fails, or a nonorthogonal pair fills the entire span;
  the symmetric-square decomposition then permits no third point.
- **Conclusion:** G155 and also the adjacent slack \(2d+3\) are
  **NO-GO**. G148 and HC remain open.
- **Re-entry condition:** B233 later excludes G156 and the adjacent odd
  layer; move to G157 at \(s=2d+6,\delta_1=d+3\).
