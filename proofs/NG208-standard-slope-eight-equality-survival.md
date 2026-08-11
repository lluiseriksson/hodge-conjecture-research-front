---
brick_id: NG208
status: NO-GO
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=8, primitive ruling difference zeta=a-b, standard A=O_Q(1), and H=O_Q(2)
smoothness: Q^d and the reduced marked scheme are smooth; no central nodal divisor is constructed
projectivity: the standard quadratic embedding, smaller residual quadrics, self-adjoint annihilators, rank-one maps, and projective contact loci are projective
dimension: dim X=d=2n>=8; G173 has h_Z(1)=5d-3 and slack s=8d-8
codimension: records failure of the route that tries to attain the exact standard slope-eight equality rank
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double schemes
hodge_type: zeta is rational type (n,n); no rational type-(0,0) relation detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); no algebraicity inference is made
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B235-B237, B245-B250
claim: The standard quadric cannot survive at h_Z(1)=5d-3: the residual-orthogonal branch reduces to B236 on Q^(d-2), while the only remaining equality branch has annihilator rank-one maps indexed by a (d-3)-space and confines every marked point to a projective four-space of quadratic rank at most fifteen.
falsifier: a valid standard G173 quadric candidate or failure of one of B250's recursive, rank, or contact-locus steps
---

# NG208 — Standard survival at slope-eight equality

- **Label:** NO-GO
- **Route:** attain \(h_Z(1)=5d-3\) with the standard quadratic
  embedding and absorb every marked tangent.
- **Valid premise:** B246's lower-bound arithmetic permits equality.
- **Invalid inference:** one of its minimal tangent-contribution cases
  extends to all remaining marked points.
- **Residual obstruction:** if all residual points lie in
  \(U=\langle v,w\rangle^\perp\), their quotient rank is the impossible
  B236 boundary \(3(d-2)+1\) on \(Q(U)\).
- **Mixed obstruction:** every equality case except
  \(t,u\in W\), \(u\in K\setminus K^\perp\), already contributes at
  least \(5d-2\).
- **Contact obstruction:** for
  \(J=K\cap u^\perp\), all rank-one maps \(E_z\), \(z\in J\), remain
  in the annihilator. Their common contact lies in
  \(\mathbf P(J^\perp)\simeq\mathbf P^4\), of quadratic point rank at
  most fifteen.
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge8\), is a
  valid input. No special-family success is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G173 and both layers \(8d-8,8d-7\) are closed. G148
  and HC remain open.
- **Re-entry condition:** G174 begins at
  \(s=8d-6,\delta_1=4d-3,N=10d-4,h_Z(1)=5d-2\).
