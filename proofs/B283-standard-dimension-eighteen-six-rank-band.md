---
brick_id: B283
status: PROVED
base_field: C
variety: the smooth split quadric Q^18 with primitive ruling difference zeta=a-b, standard A=O_Q(1), H=O_Q(2), and hypothetical G203 marked schemes
smoothness: Q^18 and the reduced marked schemes are smooth; no central ODP package is constructed
projectivity: the standard quadratic embedding, residual Q^16, four nested tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-seven-space contact bounds are projective
dimension: dim X=18; standard ranks 128 through 133 are impossible and the floor is at least 134
codimension: the primitive codimension-nine ruling difference supplies a valid universal test input; the theorem excludes G203 at rank 128 and removes the standard branch through the nonstandard boundary 133
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (9,9); no rational type-(0,0) detector is constructed
cycle_class_map: CH^9(Q^18)_Q -> H^18(Q^18,Q(9)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B282, G203-G204, S081
claim: Standard tangent-absorbing spans on Q^18 cannot have ranks 128 through 133. Hence the standard floor is at least 134, G203 is NO-GO, and G204 is active with only nonstandard rank-133 survivors in dimension 18.
falsifier: a Q^18 standard candidate of rank 128 through 133, a residual Q^16 configuration below B280's floor 119, failure of the fourth nested escape, quadratic point rank above 36 on P^7, or a different next boundary
---

# B283 — Six standard ranks fail in dimension eighteen

Let \(d=18\) and

\[
 h=128+r=5d-1+q,\qquad q=39+r,\qquad0\le r\le5. \tag{1}
\]

The residual standard span on \(Q^{16}\) has rank at most

\[
 3d-3+q=90+r\in[90,95]<119, \tag{2}
\]

contradicting B280's standard floor. Every mixed branch has budget

\[
 q+2=41+r\in[41,46]. \tag{3}
\]

The first three minimal escapes contribute

\[
 (d-4)+(d-5)+(d-6)=14+13+12=39. \tag{4}
\]

At most \(2+r\le7\) dimensions remain, while a fourth escape has rank
at least \(d-7=11\). A nonminimal earlier escape only reduces the
remaining budget; filling after one, two, or three escapes confines the
supports to \(\mathbf P^5,\mathbf P^6\), or \(\mathbf P^7\), of
quadratic point rank at most \(36<128\). Therefore

\[
 Q^{18},\ A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge134. \tag{5}
\]

B283 constructs no ODP package, Kuranishi vanishing, rational detector,
specified pairing, algebraic cycle, proof, or disproof of HC.
