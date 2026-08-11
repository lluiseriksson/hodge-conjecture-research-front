---
brick_id: B284
status: PROVED
base_field: C
variety: the smooth split quadric Q^20 with primitive ruling difference zeta=a-b, standard A=O_Q(1), H=O_Q(2), and hypothetical G204 marked schemes
smoothness: Q^20 and the reduced marked schemes are smooth; no central ODP package is constructed
projectivity: the standard quadratic embedding, residual Q^18, four nested tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-seven-space contact bounds are projective
dimension: dim X=20; standard ranks 144 through 147 are impossible and the floor is at least 148
codimension: the primitive codimension-ten ruling difference supplies a valid universal test input; the theorem excludes G204 at rank 144 and removes the standard branch through the nonstandard boundary 147
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (10,10); no rational type-(0,0) detector is constructed
cycle_class_map: CH^10(Q^20)_Q -> H^20(Q^20,Q(10)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B283, G204-G205, S081
claim: Standard tangent-absorbing spans on Q^20 cannot have ranks 144 through 147. Hence the standard floor is at least 148, G204 is NO-GO, and G205 is active with only nonstandard rank-147 survivors in dimension 20.
falsifier: a Q^20 standard candidate of rank 144 through 147, a residual Q^18 configuration below B283's floor 134, failure of the fourth nested escape, quadratic point rank above 36 on P^7, or a different next boundary
---

# B284 — Four standard ranks fail in dimension twenty

Let \(d=20\) and

\[
 h=144+r=5d-1+q,\qquad q=45+r,\qquad0\le r\le3. \tag{1}
\]

The residual standard span on \(Q^{18}\) has rank at most

\[
 3d-3+q=102+r\in[102,105]<134, \tag{2}
\]

contradicting B283. Every mixed branch has budget

\[
 q+2=47+r\in[47,50]. \tag{3}
\]

Three minimal escapes contribute

\[
 (d-4)+(d-5)+(d-6)=16+15+14=45. \tag{4}
\]

At most \(2+r\le5\) dimensions remain, while a fourth escape has rank
at least \(d-7=13\). Nonminimal escapes reduce the budget; filling
confines the supports to at most \(\mathbf P^7\), of quadratic point
rank \(36<144\). Therefore

\[
 Q^{20},\ A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge148. \tag{5}
\]

B284 constructs no ODP package, Kuranishi vanishing, rational detector,
specified pairing, algebraic cycle, proof, or disproof of HC.
