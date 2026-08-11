---
brick_id: NG197
status: NO-GO
base_field: C
variety: arbitrary smooth projective complex 2n-folds, tested on Q^(2n) with primitive ruling difference a-b
smoothness: the quadric and reduced marked scheme are smooth; no central ODP construction is asserted
projectivity: mixed double-point spans, quartic and sextic separators, tangent contact loci, and orthogonal complements are projective
dimension: dim X=d=2n>=4; the m=2 layers s=4d+6 and s=4d+7 are excluded
codimension: the ruling difference supplies a legitimate primitive codimension-n universal input
coefficient_field: Q for the Hodge input and C for sections, self-adjoint endomorphisms, tangent jets, and ranks
cohomology_theory: rational singular cohomology and coherent mixed finite-scheme restriction
hodge_type: a-b is primitive rational type (n,n); no unknown class is assumed algebraic
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the known class only certifies the test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221-B239, G162
claim: Realize universal G148 through G162's m=2 signature s=4d+6, delta_1=2d+3.
falsifier: B239 excludes higher powers by a sextic separator, the square polarization by residual-line jet separation, and the standard polarization by contact-locus rigidity including the exceptional fourfold
---

# NG197 — One dimension beyond three doubles does not realize G148

- **Route:** add one point-span dimension beyond the exact three-double
  boundary.
- **Valid premise:** three doubles plus one point exactly fill that span
  for exponent-six systems.
- **Invalid inference:** a fifth marked tangent can be absorbed.
- **Higher-power obstruction:** six hyperplane factors separate a fifth
  point from three doubles and one reduced point.
- **Square-polarization obstruction:** the only residual quartic base
  locus is a pair line containing the fourth point, but an explicit
  quartic has a nonzero transverse first jet at every further point of
  that line.
- **Standard-polarization obstruction:** quotient ranks exclude dimensions
  at least six. On \(Q^4\), self-adjoint annihilator duality leaves only
  the initial plane conic and one extra point in the tangential contact
  locus, of point rank at most six.
- **Odd-layer guard:** \(s=4d+7\) has the same integral rank budget.
- **Detector guard:** no ODP package, rational detector, specified pairing,
  cycle, proof, or disproof of HC is produced.
- **Conclusion:** G162 and both layers \(4d+6,4d+7\) are **NO-GO**. G148
  and HC remain open.
- **Re-entry condition:** B240 later excludes G163 and its odd neighbor;
  move to G164.
