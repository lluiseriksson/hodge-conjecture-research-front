---
brick_id: B280
status: PROVED
base_field: C
variety: the smooth split quadric Q^16 with primitive ruling difference zeta=a-b, standard A=O_Q(1), H=O_Q(2), and hypothetical G199 marked schemes
smoothness: Q^16 and the reduced marked schemes are smooth; no central ODP package is constructed
projectivity: the standard quadratic embedding, residual Q^14, four nested tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-seven-space contact bounds are projective
dimension: dim X=16; standard ranks 113 through 118 are impossible and the floor is at least 119
codimension: the primitive codimension-eight ruling difference supplies a valid universal test input; the theorem excludes G199 at rank 113 and removes the standard branch through rank 118, but leaves the cubic/quartic branch and every detector clause open
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (8,8); no rational type-(0,0) detector is constructed
cycle_class_map: CH^8(Q^16)_Q -> H^16(Q^16,Q(8)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B279, G199-G200, S081
claim: Standard tangent-absorbing spans on Q^16 cannot have ranks 113 through 118. Hence the standard floor is at least 119, G199 is NO-GO, and G200 is active at the cubic/quartic rank 118 in dimension 16.
falsifier: a Q^16 standard candidate of rank 113 through 118, a residual Q^14 configuration below B277's floor 108, failure of the fourth nested escape, quadratic point rank above 36 on P^7, or a different next boundary
---

# B280 — Six further standard ranks fail in dimension sixteen

Let (d=16) and

\[
 h=113+r=5d-1+q,\qquad q=34+r,\qquad 0\le r\le5. \tag{1}
\]

## Residual branch

The projected standard span on (Q^{14}) has rank at most

\[
 3d-3+q=79+r\in[79,84]. \tag{2}
\]

B277 proves that the standard floor on (Q^{14}) is at least 108.
Thus every residual branch is impossible.

## Mixed branches

Every B253 mixed branch reaches an annihilator containing
(\operatorname{Sym}^2J_0), (\dim J_0=d-3), with budget at most

\[
 q+2=36+r\in[36,41]. \tag{3}
\]

Three minimal nested escapes contribute

\[
 (d-4)+(d-5)+(d-6)=12+11+10=33. \tag{4}
\]

If the span has not filled, at most (3+r\le8) dimensions remain,
whereas a fourth escape has rank at least

\[
 d-7=9. \tag{5}
\]

Any nonminimal earlier escape reduces the remaining budget. If the
span fills after one, two, or three escapes, the surviving rank-one
annihilator confines every marked point to
(\mathbf P^5,\mathbf P^6), or (\mathbf P^7), whose quadratic point
rank is at most

\[
 h^0(\mathbf P^7,O(2))=36<113\le h. \tag{6}
\]

All branches are impossible, so

\[
 Q^{16},\ A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge119. \tag{7}
\]

B280 constructs no ODP package, Kuranishi vanishing, rational detector,
specified pairing, algebraic cycle, proof, or disproof of HC.
