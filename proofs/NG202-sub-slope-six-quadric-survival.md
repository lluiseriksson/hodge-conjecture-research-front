---
brick_id: NG202
status: NO-GO
base_field: C
variety: the smooth even quadrics Q^d with d=2n>=8 and primitive ruling difference a-b, tested against every very ample A=O_Q(k)
smoothness: the quadric and reduced marked scheme are smooth; no central ODP construction is asserted
projectivity: complete quadric embeddings, mixed double-point spans, tangent quotients, self-adjoint contact loci, and plane conics are projective
dimension: every m=2 candidate on Q^d has slack s>=6d; G167 and every smaller fixed-additive slope-four layer are excluded on a suitable valid quadric
codimension: the ruling difference supplies a legitimate primitive codimension-n universal input
coefficient_field: Q for the Hodge input and C for sections, tangent jets, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to mixed finite schemes
hodge_type: a-b is primitive rational type (n,n); no unknown class is assumed algebraic
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the known ruling difference only certifies the test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B221-B244, G167
claim: Survive the m=2 quadric test with slack s<=6d-1, including G167 and any fixed additive extension of the slope-four branch.
falsifier: B244's nonstandard rank-four-double floor, standard rank-4d floor, and exact equality contact-locus obstruction
---

# NG202 — Sub-slope-six quadric survival fails

- **Route:** continue adding a fixed number of dimensions beyond the
  three-double slope-four core.
- **Valid premise:** each added pair of slack units enlarges the balanced
  point span by one.
- **Invalid inference:** finitely many such dimensions can absorb the
  fourth independent tangent block on quadrics of growing dimension.
- **Nonstandard obstruction:** every \(O_Q(k\ge2)\) candidate has
  \(h_Z(1)\ge4d+4\).
- **Standard obstruction:** every \(O_Q(1)\) candidate has
  \(h_Z(1)\ge4d\), and equality confines the contact locus to either two
  residual points or one plane conic plus one point.
- **Universal-quantifier guard:** for any fixed additive slope-four
  offset, a sufficiently large even quadric lies below \(6d\) and
  falsifies the universal claim.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G167 and every m=2 layer \(s\le6d-1\) are closed on
  even quadrics \(d\ge8\). G148 and HC remain open.
- **Re-entry condition:** G168 begins at
  \(s=6d,\delta_1=3d,N=8d+2,h_Z(1)=4d+1\).
