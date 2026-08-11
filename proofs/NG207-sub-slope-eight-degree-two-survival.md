---
brick_id: NG207
status: NO-GO
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=8, primitive ruling difference zeta=a-b, arbitrary A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; no central nodal divisor is constructed
projectivity: complete quadric embeddings, double-point restrictions, pair-line four-cycles, and variable hyperplane families are projective
dimension: dim X=d=2n>=8; every m=2 candidate has h_Z(1)>=5d-3 and slack s>=8d-8
codimension: records failure of every degree-two route below the slope-eight quadric floor
coefficient_field: Q for zeta and C for sections, jets, spans, hyperplanes, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to finite double schemes
hodge_type: zeta is rational type (n,n); no rational type-(0,0) relation detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); no algebraicity inference is made
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B246-B249
claim: No m=2 universal construction survives with slack s<=8d-9 on the even-quadric test family; the square fifth tangent contributes at least d-1 dimensions, every k>=3 fifth double contributes d+1, and the standard floor is 5d-3.
falsifier: a valid even-quadric candidate below rank 5d-3 or failure of one of B249's explicit residual jet maps
---

# NG207 — Survival below the slope-eight boundary

- **Label:** NO-GO
- **Route:** retain the balanced \(m=2\) construction with
  \(s\le8d-9\).
- **Valid premise:** B248 only forced the excess beyond \(4d+4\) to
  grow with dimension.
- **Invalid inference:** that the required growth can remain
  sublinear.
- **Square obstruction:** varying one hyperplane in B247's good
  four-cycle supplies at least \(d-1\) residual jets at a fifth point,
  forcing rank \(5d+3\).
- **Higher-power obstruction:** the four-cycle quartic is a unit at
  the fifth point, and multiplication by \(O_Q(2k-4)\) supplies its
  full \(d+1\) jets, forcing rank \(5d+5\).
- **Standard obstruction:** B246 already forces rank \(5d-3\).
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge8\), is a
  valid input. No special-family success is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** every layer below \(s=8d-8\) is closed. G148 and HC
  remain open.
- **Re-entry condition:** G173 begins at
  \(s=8d-8,\delta_1=4d-4,N=10d-6,h_Z(1)=5d-3\), with only the
  standard quadric polarization surviving the rank test.
