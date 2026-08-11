---
brick_id: NG209
status: NO-GO
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=8, primitive ruling difference zeta=a-b, standard A=O_Q(1), and H=O_Q(2)
smoothness: Q^d and the reduced marked scheme are smooth; no central nodal divisor is constructed
projectivity: the standard quadratic embedding, residual quadrics, tangent quotient spaces, rank-one annihilators, and projective contact loci are projective
dimension: dim X=d=2n>=8; G174 has h_Z(1)=5d-2 and slack s=8d-6
codimension: records failure of the route one rank beyond standard slope-eight equality
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double schemes
hodge_type: zeta is rational type (n,n); no rational type-(0,0) relation detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); no algebraicity inference is made
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B235-B237, B245-B251
claim: The standard quadric cannot survive at h_Z(1)=5d-2: the residual branch reduces to B237 on Q^(d-2), every filled mixed branch is confined to a P^4 contact locus, and the sole one-dimensional residual branch receives at least d-4 dimensions from the next tangent.
falsifier: a valid standard G174 quadric candidate or failure of one of B251's recursive, contraction-rank, contact, or final-escape steps
---

# NG209 — Standard survival one rank beyond slope eight

- **Label:** NO-GO
- **Route:** attain \(h_Z(1)=5d-2\) with the standard quadratic
  embedding.
- **Valid premise:** one extra span dimension reopens several minimal
  cases excluded at exact equality.
- **Invalid inference:** any reopened case absorbs all subsequent
  marked tangents.
- **Residual obstruction:** the orthogonal residual quotient is the
  impossible B237 boundary \(3(d-2)+2\) on \(Q^{d-2}\).
- **Filled-branch obstruction:** whenever a tangent fills the available
  quotient, a \((d-3)\)-space \(J\) of rank-one annihilators remains
  and confines contact to \(\mathbf P(J^\perp)\simeq\mathbf P^4\).
- **Last-dimension obstruction:** in the only branch leaving one
  dimension, a marked point outside \(J^\perp\) receives at least
  \(d-4>1\) residual tangent dimensions.
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge8\), is a
  valid input. No special-family success is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G174 and both layers \(8d-6,8d-5\) are closed. G148
  and HC remain open.
- **Re-entry condition:** G175 begins at
  \(s=8d-4,\delta_1=4d-2,N=10d-2,h_Z(1)=5d-1\).
