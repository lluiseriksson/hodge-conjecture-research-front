---
brick_id: B279
status: PROVED
base_field: C
variety: the smooth split quadric Q^16 with primitive ruling difference zeta=a-b, standard A=O_Q(1), H=O_Q(2), and a hypothetical G198 marked scheme
smoothness: Q^16 and the reduced marked scheme are smooth; no central ODP package is constructed
projectivity: the standard quadratic embedding, residual Q^14, four nested tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-seven-space contact bounds are projective
dimension: dim X=16; standard equality rank 112 is impossible and the floor is at least 113
codimension: the primitive codimension-eight ruling difference supplies a valid universal test input; the theorem excludes G198 via its sole d=16 survivor but leaves the next standard rank and every detector clause open
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (8,8); no rational type-(0,0) detector is constructed
cycle_class_map: CH^8(Q^16)_Q -> H^16(Q^16,Q(8)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B278, G198-G199, S081
claim: A standard tangent-absorbing span on Q^16 cannot have rank 112=8d-16. Hence its standard floor is at least 113, G198 is NO-GO, and G199 is the next active boundary.
falsifier: a Q^16 standard rank-112 candidate, a residual Q^14 configuration below B277's floor 108, failure of the fourth nested escape, quadratic point rank above 36 on P^7, or a different next boundary
---

# B279 — Standard equality 112 fails on \(Q^{16}\)

Let \(d=16\), \(h=112=8d-16\), and write

\[
 h=5d-1+q,\qquad q=33=3d-15. \tag{1}
\]

## Residual branch

The projected standard span on \(Q^{14}\) has rank at most

\[
 3d-3+q=78. \tag{2}
\]

B277 proves that the standard floor on \(Q^{14}\) is at least 108.
Thus the residual branch is impossible.

## Mixed branches

Every B253 mixed branch reaches an annihilator containing
\(\operatorname{Sym}^2J_0\), \(\dim J_0=d-3\), with budget at most

\[
 q+2=35. \tag{3}
\]

Three minimal nested escapes contribute

\[
 (d-4)+(d-5)+(d-6)=12+11+10=33. \tag{4}
\]

If the span has not filled, at most two dimensions remain, whereas a
fourth escape has rank at least

\[
 d-7=9. \tag{5}
\]

Any nonminimal earlier escape reduces the remaining budget. If the
span fills after one, two, or three escapes, the surviving rank-one
annihilator confines every marked point to
\(\mathbf P^5,\mathbf P^6\), or \(\mathbf P^7\), whose quadratic point
rank is at most

\[
 h^0(\mathbf P^7,O(2))=36<112. \tag{6}
\]

All branches are impossible, so

\[
 Q^{16},\ A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge113. \tag{7}
\]

B279 constructs no ODP package, Kuranishi vanishing, rational detector,
specified pairing, algebraic cycle, proof, or disproof of HC.
