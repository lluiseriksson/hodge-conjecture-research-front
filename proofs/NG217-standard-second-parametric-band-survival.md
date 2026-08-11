---
brick_id: NG217
status: NO-GO
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, standard A=O_Q(1), and H=O_Q(2)
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: the standard quadratic embedding, residual orthogonal quadrics, nested tangent quotient spaces, rank-one self-adjoint maps, and contact loci are projective
dimension: dim X=d=2n>=14; every standard candidate has h_Z(1)>=7d-12; every polarization has h_Z(1)>=F(d)=min(7d-12,6d+6) and slack s>=min(12d-26,10d+10)
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the failed route is standard survival in the band 6d-5<=h_Z(1)<=7d-13
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B253-B259, G185, S081
claim: The route in which the standard polarization survives with 6d-5<=h_Z(1)<=7d-13 is impossible on every even Q^d with d>=14; the residual branch lies below B246 and every mixed branch fails a uniform two-step nested rank-one escape.
falsifier: a valid standard candidate in the stated band on one such quadric or a failure of B259's residual or two-step inequality
---

# NG217 — Standard survival through the second parametric band

- **Label:** NO-GO
- **Route:** retain \(A=O_Q(1)\) with
  \(6d-5\le h_Z(1)\le7d-13\).
- **Valid premise:** B258 treats only the first two ranks for which the
  nested escape is needed.
- **Invalid inference:** the residual budget grows quickly enough to
  absorb the second nested tangent.
- **Residual obstruction:** throughout the band, the smaller-quadric
  rank is at most \(5d-15<5d-13\), below B246.
- **First escape:** every mixed branch has budget at most
  \(d-2+r\), \(0\le r\le d-8\), and the first tangent contributes at
  least \(d-4\).
- **Second escape:** at most \(r+2\le d-6\) remains, while the descended
  rank-one system contributes at least \(d-5\).
- **Standard-floor consequence:** \(h_Z(1)\ge7d-12\).
- **Common-floor consequence:** with B254-B256,
  \(h_Z(1)\ge F(d)=\min(7d-12,6d+6)\) and
  \(s\ge\min(12d-26,10d+10)\).
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge14\), is a
  valid input. No special-family success is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G185 and every lower common layer are closed. G148
  and HC remain open.
- **Re-entry condition:** G186 begins at the piecewise signature
  \(h_Z(1)=F(d)\), \(s=2(F(d)-d-1)\), \(N=2F(d)\).
