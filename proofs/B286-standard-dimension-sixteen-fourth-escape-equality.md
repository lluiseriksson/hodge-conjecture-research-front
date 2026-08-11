---
brick_id: B286
status: PROVED
base_field: C
variety: the smooth split quadric Q^16 with primitive ruling difference zeta=a-b, standard A=O_Q(1), H=O_Q(2), and a hypothetical G206 marked scheme
smoothness: Q^16 and the reduced marked scheme are smooth; no central ODP package is constructed
projectivity: the standard quadratic embedding, residual Q^14, four nested tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-eight-space contact bound are projective
dimension: dim X=16; standard rank 119 is impossible and the floor is at least 120
codimension: the primitive codimension-eight ruling difference supplies a valid universal test input; the theorem removes the sole standard tie from G206 but leaves every nonstandard polarization and detector clause open
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (8,8); no rational type-(0,0) detector is constructed
cycle_class_map: CH^8(Q^16)_Q -> H^16(Q^16,Q(8)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B285, G206-G207, S081
claim: A standard tangent-absorbing span on Q^16 cannot have rank 119=7d+7. Equality in the fourth-escape budget forces a filled P^8 contact locus of quadratic rank at most 45. Thus the standard floor is at least 120 and only nonstandard polarizations remain at G206.
falsifier: a Q^16 standard rank-119 candidate, a residual Q^14 configuration below B277's floor 108, failure of the fourth equality escape, quadratic point rank above 45 on P^8, or a standard survivor at the refined boundary
---

# B286 — Standard rank 119 fails at fourth-escape equality

Let \(d=16\), \(h=119\), and write

\[
 h=5d-1+q,\qquad q=40. \tag{1}
\]

The residual \(Q^{14}\) rank is at most

\[
 3d-3+q=85<108, \tag{2}
\]

contradicting B277. A mixed branch has budget \(q+2=42\). Its first
three minimal escapes contribute

\[
 (d-4)+(d-5)+(d-6)=12+11+10=33. \tag{3}
\]

Exactly nine dimensions remain, equal to the fourth minimum
\(d-7=9\). Survival therefore forces all four escapes to be minimal;
any nonminimal contribution exceeds the budget. The fourth escape
fills the span.

The descended space \(J_4\) has dimension \(d-7=9\). Its surviving
rank-one annihilator confines every marked point to

\[
 \mathbf P(J_4^\perp)\simeq\mathbf P^8, \tag{4}
\]

whose quadratic point rank is

\[
 h^0(\mathbf P^8,O(2))=45<119. \tag{5}
\]

Thus standard rank 119 is impossible and the \(Q^{16}\) standard floor
is at least 120. B286 constructs no ODP package, Kuranishi vanishing,
rational detector, specified pairing, algebraic cycle, proof, or
disproof of HC.
