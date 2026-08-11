---
brick_id: NG196
status: NO-GO
base_field: C
variety: arbitrary smooth projective complex 2n-folds, tested on Q^(2n) with primitive ruling difference a-b
smoothness: the quadric and reduced marked scheme are smooth; no central ODP construction is asserted
projectivity: three-double spans, quartic separators, tangent contact loci, and plane conics are projective
dimension: dim X=d=2n>=4; the m=2 layers s=4d+4 and s=4d+5 are excluded
codimension: the ruling difference supplies a legitimate primitive codimension-n universal input
coefficient_field: Q for the Hodge input and C for sections, self-adjoint operators, and ranks
cohomology_theory: rational singular cohomology and coherent mixed finite-scheme restriction
hodge_type: a-b is primitive rational type (n,n); no unknown class is assumed algebraic
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the known class only certifies the test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221-B238, G161
claim: Realize universal G148 through G161's exact three-double balanced signature s=4d+4, delta_1=2d+2.
falsifier: B238 excludes higher powers by B215, the square by an explicit quartic separator, and the standard polarization by the d-2 tangent quotient bound
---

# NG196 — The three-double balanced boundary does not realize G148

- **Route:** let three tangent osculators fit exactly at the first boundary
  where every quadric polarization re-enters.
- **Valid premise:** \(h_Z(1)=3d+3\) equals the dimension of three
  independent tangent spaces.
- **Invalid inference:** a fourth marked point or tangent can remain inside
  that span.
- **Higher powers:** B215 separates three doubles plus one point.
- **Square polarization:** explicit products of four hyperplanes separate
  a fourth point from any three noncollinear doubles; the all-collinear
  alternative has rank at most five.
- **Standard polarization:** outside the plane contact conic, a fourth
  tangent contributes at least \(d-2\ge2\) quotient dimensions, while only
  one is available.
- **Odd-layer guard:** \(s=4d+5\) has the same integral rank budget.
- **Detector guard:** no ODP package, rational detector, specified pairing,
  cycle, proof, or disproof of HC is produced.
- **Conclusion:** G161 and both layers \(4d+4,4d+5\) are **NO-GO**. G148
  and HC remain open.
- **Re-entry condition:** B239 later excludes G162 and its odd neighbor;
  move to G163.
