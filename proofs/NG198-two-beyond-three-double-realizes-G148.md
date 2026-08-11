---
brick_id: NG198
status: NO-GO
base_field: C
variety: arbitrary smooth projective complex 2n-folds, tested on Q^(2n) with primitive ruling difference a-b
smoothness: the quadric and reduced marked scheme are smooth; no central ODP construction is asserted
projectivity: three-double mixed spans, quartic and sextic first-jet separators, tangent contact loci, and quadric linear sections are projective
dimension: dim X=d=2n>=4; the m=2 layers s=4d+8 and s=4d+9 are excluded
codimension: the ruling difference supplies a legitimate primitive codimension-n universal input
coefficient_field: Q for the Hodge input and C for sections, self-adjoint endomorphisms, tangent jets, and ranks
cohomology_theory: rational singular cohomology and coherent mixed finite-scheme restriction
hodge_type: a-b is primitive rational type (n,n); no unknown class is assumed algebraic
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the known class only certifies the test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221-B240, G163
claim: Realize universal G148 through G163's m=2 signature s=4d+8, delta_1=2d+4.
falsifier: B240 excludes higher powers and the square by explicit first-jet separators, and the standard polarization by quotient ranks plus the exact Q^4 rank-nine contact section
---

# NG198 — Two dimensions beyond three doubles do not realize G148

- **Route:** add two point-span dimensions after three independent tangent
  osculators.
- **Valid premise:** three doubles plus two points fill the available span
  at exponent six.
- **Invalid inference:** a sixth marked tangent can remain absorbed.
- **Higher-power obstruction:** two triangle-edge factors and four
  single-support factors give a sextic sixth-point separator.
- **Square-polarization obstruction:** after choosing the fourth point off
  the triangle, an exhaustive four-hyperplane construction gives either a
  value separator or one transverse first jet at every sixth point.
- **Standard-polarization obstruction:** quotient ranks exclude dimensions
  at least six. On \(Q^4\), every surviving three-dimensional annihilator
  is \(\operatorname{Sym}^2K\), so the contact locus lies in a quadric
  \(\mathbf P^3\)-section of point rank at most nine.
- **Odd-layer guard:** \(s=4d+9\) has the same integral rank budget.
- **Detector guard:** no ODP package, rational detector, specified pairing,
  cycle, proof, or disproof of HC is produced.
- **Conclusion:** G163 and both layers \(4d+8,4d+9\) are **NO-GO**. G148
  and HC remain open.
- **Re-entry condition:** G164 begins at
  \(s=4d+10,\delta_1=2d+5\).
