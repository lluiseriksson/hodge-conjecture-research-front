---
brick_id: NG195
status: NO-GO
base_field: C
variety: arbitrary smooth projective complex 2n-folds, tested on Q^(2n) with primitive ruling difference a-b
smoothness: the quadric and reduced marked scheme are smooth; no central ODP construction is asserted
projectivity: tangent contact loci, plane conics, orthogonal complements, and isotropic spans are projective
dimension: dim X=d=2n>=4; the m=2 layers s=4d+2 and s=4d+3 are excluded
codimension: the ruling difference supplies a legitimate primitive codimension-n universal input
coefficient_field: Q for the Hodge input and C for self-adjoint operators, tangents, and ranks
cohomology_theory: rational singular cohomology and coherent double-point restriction
hodge_type: a-b is primitive rational type (n,n); no unknown class is assumed algebraic
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the known class only certifies the test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221-B237, G160
claim: Realize universal G148 through G160's m=2 post-slope-four signature s=4d+2, delta_1=2d+1.
falsifier: B237's exhaustive dichotomy gives either a plane-conic contact locus of point rank at most five or an impossible isotropic residual configuration
---

# NG195 — The post-slope-four core does not realize G148

- **Route:** add one span dimension after the slope-four equality
  obstruction.
- **Valid premise:** a third point meeting the initial hyperbolic plane now
  contributes exactly the available \(d\)-dimensional quotient.
- **Invalid inference:** the resulting contact locus contains enough
  points to realize the required rank.
- **First branch:** self-adjoint annihilator duality identifies the full
  tangential contact locus with one plane conic, whose quadratic point
  span has dimension at most five.
- **Second branch:** if every residual point is orthogonal to the initial
  pair, the \(d\)-dimensional quotient cannot contain two nonorthogonal
  residual tangents; pairwise orthogonality then contradicts full tangent
  absorption.
- **Odd-layer guard:** \(s=4d+3\) has the same integral rank budget.
- **Detector guard:** no ODP package, rational detector, specified pairing,
  algebraic cycle, proof, or disproof of HC is obtained.
- **Conclusion:** G160 and both layers \(4d+2,4d+3\) are **NO-GO**. G148
  and HC remain open.
- **Re-entry condition:** B238 later excludes the exact three-double
  boundary; move to G162.
