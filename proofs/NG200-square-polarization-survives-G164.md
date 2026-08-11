---
brick_id: NG200
status: NO-GO
base_field: C
variety: the even quadrics Q^d with primitive ruling difference a-b at the G164 balanced rank, with A=O_Q(2) and H=O_Q(4)
smoothness: the quadric and reduced marked scheme are smooth; no central ODP construction is asserted
projectivity: quartic mixed spans, residual base lines, and first-jet separator products are projective
dimension: dim X=d=2n>=4; the G164 signature has s=4d+10, N=6d+12, and h_Z(1)=3d+6
codimension: the ruling difference supplies a legitimate primitive codimension-n universal input
coefficient_field: Q for the Hodge input and C for quartic sections, tangent jets, and ranks
cohomology_theory: rational singular cohomology and coherent mixed finite-scheme restriction
hodge_type: a-b is primitive rational type (n,n); no unknown class is assumed algebraic
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the known class only certifies the test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221-B242, G164-G165
claim: Realize the G164 necessary quadric-survival test with A=O_Q(2).
falsifier: B242's two-line base-locus rank bound and exhaustive seventh-point quartic first-jet separator
---

# NG200 — The square polarization does not survive G164

- **Route:** use \(A=O_Q(2)\) after B241 removes every other
  higher-dimensional quadric polarization.
- **Valid premise:** three doubles plus three values fit the G164 point
  span.
- **Invalid inference:** all later marked tangents remain absorbed.
- **Base-locus obstruction:** after choosing one point off the triangle,
  the residual value base locus lies on at most two lines; its point rank
  is too small to contain the marked set.
- **First-jet obstruction:** after choosing a sixth point outside that
  base locus, four hyperplane factors give a nonzero value or transverse
  first jet at every seventh point.
- **Detector guard:** no ODP package, rational detector, specified pairing,
  cycle, proof, or disproof of HC is produced.
- **Universal-quantifier guard:** on \(Q^6\), B241 has already excluded
  every other polarization. The standard \(Q^4\) exception cannot rescue
  a theorem required for all inputs.
- **Conclusion:** \(O_Q(2)\) is impossible in every even dimension; G164
  and G165 are **NO-GO**. HC remains open.
- **Re-entry condition:** move to G166 at
  \(s=4d+12,\delta_1=2d+6,N=6d+14,h_Z(1)=3d+7\).
