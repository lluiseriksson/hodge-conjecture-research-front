---
brick_id: NG203
status: NO-GO
base_field: C
variety: the smooth even quadrics Q^d with d=2n>=8 and primitive ruling difference a-b, under the standard polarization A=O_Q(1)
smoothness: the quadric and reduced marked scheme are smooth; no central ODP construction is asserted
projectivity: the standard quadratic embedding, tangent quotients, self-adjoint annihilators, and projective three-space contact loci are projective
dimension: the slope-six boundary has s=6d, N=8d+2, and h_Z(1)=4d+1; its adjacent odd layer has the same rank
codimension: the ruling difference supplies a legitimate primitive codimension-n universal input
coefficient_field: Q for the Hodge input and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: a-b is primitive rational type (n,n); no unknown class is assumed algebraic
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the known ruling difference only certifies the test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221-B245, G168
claim: Survive the G168 slope-six boundary using the only remaining standard quadric polarization.
falsifier: B245's residual third-tangent rank and projective-three-space contact-locus bounds
---

# NG203 — The standard slope-six boundary does not survive

- **Route:** use \(A=O_Q(1)\) at \(h_Z(1)=4d+1\), after B244 removes all
  nonstandard polarizations.
- **Valid premise:** G168 leaves one dimension beyond the standard
  rank-\(4d\) equality obstruction.
- **Invalid inference:** that dimension absorbs a third residual tangent
  or an additional point outside the conic-plus-point contact locus.
- **Residual-\(U\) obstruction:** a third tangent contributes at least
  \(d-3>1\).
- **Other-branch obstruction:** every possible rank-one continuation
  leaves annihilator \(\operatorname{Sym}^2K\), whose contact locus lies
  in one projective three-space of quadratic point rank at most ten.
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge8\), is a
  valid input; success elsewhere would not rescue G168.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G168 and both layers \(6d,6d+1\) are closed. G148 and
  HC remain open.
- **Re-entry condition:** G169 begins at
  \(s=6d+2,\delta_1=3d+1,N=8d+4,h_Z(1)=4d+2\).
