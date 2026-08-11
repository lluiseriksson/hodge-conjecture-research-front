---
brick_id: NG211
status: NO-GO
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=10, primitive ruling difference zeta=a-b, standard A=O_Q(1), and H=O_Q(2)
smoothness: Q^d and the reduced marked scheme are smooth; no central nodal divisor is constructed
projectivity: the standard quadratic embedding, residual quadrics, tangent quotient spaces, rank-one annihilators, and projective contact loci are projective
dimension: dim X=d=2n>=10; standard ranks h_Z(1)=5d-1+q with 0<=q<=d-7 are excluded; G176-G178 lie in this band
codimension: records failure of the entire standard parametric band and the resulting common layers below slack 8d+4
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double schemes
hodge_type: zeta is rational type (n,n); no rational type-(0,0) relation detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); no algebraicity inference is made
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B253
claim: The standard quadric cannot survive in the band 5d-1<=h_Z(1)<=6d-8. Together with B249, every polarization has h_Z(1)>=5d+3, closing G176-G178 and every slack layer through 8d+3.
falsifier: a valid standard tangent-absorbing configuration in the excluded band, failure of B253's q-dependent residual or mixed-branch inequalities, or a candidate below the common floor
---

# NG211 — Standard survival in the parametric band

- **Label:** NO-GO
- **Route:** continue the standard quadratic embedding through ranks
  \(h_Z(1)=5d-1+q\), \(0\le q\le d-7\).
- **Valid premise:** each added rank enlarges the last mixed quotient.
- **Invalid inference:** the enlarged quotient eventually absorbs the
  next tangent before the square polarization re-enters.
- **Residual obstruction:** the residual rank is at most
  \(3d-3+q\le4d-10<5d-13\), below B246 on \(Q^{d-2}\).
- **Mixed obstruction:** every branch leaves
  \(\operatorname{Sym}^2J\) for \(\dim J=d-3\); the worst remaining
  budget is \(q+2\le d-5<d-4\), smaller than the next tangent.
- **Common-floor consequence:** B249 then gives
  \(h_Z(1)\ge5d+3\) and \(s\ge8d+4\) for every polarization.
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge10\), is a
  valid input. No special-family success is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G176-G178 and every layer through \(s=8d+3\) are
  closed. G148 and HC remain open.
- **Re-entry condition:** G179 begins at
  \(s=8d+4,\delta_1=4d+2,N=10d+6,h_Z(1)=5d+3\), with only
  \(A=O_Q(2)\) surviving on even quadrics \(d\ge12\).
