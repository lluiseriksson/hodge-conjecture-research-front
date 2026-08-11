---
brick_id: B285
status: PROVED
base_field: C
variety: the smooth split quadric Q^22 with primitive ruling difference zeta=a-b, standard A=O_Q(1), H=O_Q(2), and hypothetical G205 marked schemes
smoothness: Q^22 and the reduced marked schemes are smooth; no central ODP package is constructed
projectivity: the standard quadratic embedding, residual Q^20, four nested tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-seven-space contact bounds are projective
dimension: dim X=22; standard ranks 160 and 161 are impossible and the floor is at least 162
codimension: the primitive codimension-eleven ruling difference supplies a valid universal test input; the theorem excludes G205 at rank 160 and removes the standard branch at the nonstandard boundary 161
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (11,11); no rational type-(0,0) detector is constructed
cycle_class_map: CH^11(Q^22)_Q -> H^22(Q^22,Q(11)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B284, G205-G206, S081
claim: Standard tangent-absorbing spans on Q^22 cannot have ranks 160 or 161. Hence the standard floor is at least 162, G205 is NO-GO, and G206 is the uniform rank-7d+7 boundary.
falsifier: a Q^22 standard candidate of rank 160 or 161, a residual Q^20 configuration below B284's floor 148, failure of the fourth nested escape, quadratic point rank above 36 on P^7, or a different next boundary
---

# B285 — Standard ranks 160 and 161 fail in dimension twenty-two

Let \(d=22\) and

\[
 h=160+r=5d-1+q,\qquad q=51+r,\qquad0\le r\le1. \tag{1}
\]

The residual standard span on \(Q^{20}\) has rank at most

\[
 3d-3+q=114+r\in[114,115]<148, \tag{2}
\]

contradicting B284. Every mixed branch has budget

\[
 q+2=53+r\in[53,54]. \tag{3}
\]

Three minimal escapes contribute

\[
 (d-4)+(d-5)+(d-6)=18+17+16=51. \tag{4}
\]

At most \(2+r\le3\) dimensions remain, while a fourth escape has rank
at least \(d-7=15\). Nonminimal escapes reduce the budget; filling
confines the supports to at most \(\mathbf P^7\), of quadratic point
rank \(36<160\). Therefore

\[
 Q^{22},\ A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge162. \tag{5}
\]

B285 constructs no ODP package, Kuranishi vanishing, rational detector,
specified pairing, algebraic cycle, proof, or disproof of HC.
