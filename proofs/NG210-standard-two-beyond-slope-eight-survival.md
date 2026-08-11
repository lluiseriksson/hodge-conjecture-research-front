---
brick_id: NG210
status: NO-GO
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=10, primitive ruling difference zeta=a-b, standard A=O_Q(1), and H=O_Q(2)
smoothness: Q^d and the reduced marked scheme are smooth; no central nodal divisor is constructed
projectivity: the standard quadratic embedding, residual quadrics, tangent quotient spaces, rank-one annihilators, and projective contact loci are projective
dimension: dim X=d=2n>=10; G175 has h_Z(1)=5d-1 and slack s=8d-4
codimension: records failure of the route two ranks beyond standard slope-eight equality
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double schemes
hodge_type: zeta is rational type (n,n); no rational type-(0,0) relation detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); no algebraicity inference is made
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B245-B252
claim: The standard quadric cannot survive at h_Z(1)=5d-1: the residual branch lies below B246's standard floor on Q^(d-2), every filled mixed branch is confined to a P^4 contact locus, and the residual branches with one or two dimensions receive at least d-4 dimensions from the next tangent.
falsifier: a valid standard G175 quadric candidate or failure of one of B252's recursive, contraction-rank, contact, or final-escape steps
---

# NG210 — Standard survival two ranks beyond slope eight

- **Label:** NO-GO
- **Route:** attain \(h_Z(1)=5d-1\) with the standard quadratic
  embedding.
- **Valid premise:** two extra span dimensions reopen the B251 minimal
  branches and the residual quotient reaches \(3(d-2)+3\).
- **Invalid inference:** the reopened residual or mixed branches absorb
  all subsequent marked tangents.
- **Residual obstruction:** for \(d\ge10\), the orthogonal residual
  quotient has rank at most \(3(d-2)+3\), strictly below B246's
  standard floor \(5(d-2)-3\) on \(Q^{d-2}\).
- **Filled-branch obstruction:** every branch that fills the budget
  retains rank-one annihilators indexed by a \((d-3)\)-space \(J\), so
  contact remains inside \(\mathbf P(J^\perp)\simeq\mathbf P^4\).
- **Residual-budget obstruction:** if one or two dimensions remain, a
  marked point outside \(J^\perp\) contributes at least \(d-4>2\).
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge10\), is a
  valid input, and one such input falsifies the universal G175 claim.
  No special-family success is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G175 and both layers \(8d-4,8d-3\) are closed. G148
  and HC remain open.
- **Re-entry condition:** G176 begins at
  \(s=8d-2,\delta_1=4d-1,N=10d,h_Z(1)=5d\).
