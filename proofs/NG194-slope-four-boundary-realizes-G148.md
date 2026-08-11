---
brick_id: NG194
status: NO-GO
base_field: C
variety: arbitrary smooth projective complex 2n-folds, tested on Q^(2n) with primitive ruling difference a-b
smoothness: the quadric and marked point scheme are smooth and reduced; no central ODP construction is asserted
projectivity: the standard quadratic embedding, tangent osculators, and isotropic line geometry are projective
dimension: dim X=d=2n>=4; the m=2 layers s=4d and s=4d+1 are excluded
codimension: the ruling difference supplies a legitimate primitive codimension-n universal input
coefficient_field: Q for the Hodge input and C for quadratic forms, tensors, and ranks
cohomology_theory: rational singular cohomology and coherent double-point restriction
hodge_type: a-b is primitive rational type (n,n); no unknown class is assumed algebraic
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the known class only certifies the test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221-B236, G159
claim: Realize universal G148 through G159's exact m=2 slope-four boundary s=4d, delta_1=2d.
falsifier: B236 proves that equality forces three tangent osculators to fill the point span and that no fourth distinct point can have its tangent absorbed
---

# NG194 — The slope-four boundary cannot realize G148

- **Route:** take equality in B235's necessary floor.
- **Valid premise:** the third tangent quotient has exactly its minimum
  permitted dimension \(d-1\).
- **Invalid inference:** this equality span can absorb the remaining marked
  tangent osculators.
- **Precise obstruction:** B236 shows that equality forces the third point
  to be orthogonal to the initial nonorthogonal pair. The resulting
  three-tangent span admits no fourth point with absorbed tangent: every
  candidate lies on one of two isotropic lines, and an explicit tangent
  vector has nonzero component \(rr'-vw\) outside the span.
- **Odd-layer guard:** \(s=4d+1\) has the same integral rank budget.
- **Detector guard:** no ODP package, rational detector, specified pairing,
  algebraic cycle, proof, or disproof of HC is produced.
- **Conclusion:** G159 and both layers \(4d,4d+1\) are **NO-GO**. G148
  and HC remain open.
- **Re-entry condition:** G160 begins at
  \(s=4d+2,\delta_1=2d+1\).
