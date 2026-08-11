---
brick_id: B276
status: PROVED
base_field: C
variety: the smooth split quadrics Q^12 and Q^14 with their primitive ruling differences; standard A=O_Q(1), H=O_Q(2), and hypothetical G195 marked schemes
smoothness: both quadrics and the reduced marked schemes are smooth; no central ODP package is constructed
projectivity: the standard quadratic embeddings, residual orthogonal quadrics, nested tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-seven/eight-space contact bounds are projective
dimension: Q^12 has no standard rank from 67 through 71 and its floor is at least 72; Q^14 has no standard rank from 97 through 101 and its floor is at least 102
codimension: the primitive middle ruling differences supply valid universal test inputs; the theorem excludes the G195 rank-97 branch and four following standard layers but leaves rank 102 and every detector clause open
coefficient_field: Q for the ruling differences and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: each ruling difference is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling differences only certify the universal test inputs
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B275, G195-G196, S081
claim: Standard tangent-absorbing spans on Q^12 have no ranks 67<=h_Z(1)<=71, and those on Q^14 have no ranks 97<=h_Z(1)<=101. Hence the Q^14 standard floor is at least 102, G195 is NO-GO, and G196 is the next active boundary.
falsifier: a Q^12 standard candidate of rank 67 through 71, a Q^14 standard candidate of rank 97 through 101, failure of the B259 two-step escape in dimension 12, failure of the fourth nested escape/contact bound on Q^14, or a different next boundary
---

# B276 — Five more standard ranks fail in dimension fourteen

## The B259 band is valid on \(Q^{12}\)

Specialize B259 to \(D=12\). Write

\[
 h=5D-1+q,\qquad q=D-4+r=8+r,\qquad 0\le r\le D-8=4. \tag{1}
\]

Thus \(h\) ranges from 67 through 71. The residual \(Q^{10}\) rank is
at most

\[
 3D-3+q\le5D-15=45<5D-13=47. \tag{2}
\]

In every mixed branch the first escape has rank at least
\(D-4=8\). The remaining budget is at most

\[
 r+2\le6<D-5=7, \tag{3}
\]

while the descended annihilator requires a second rank-seven escape
unless the span fills. Filling confines all marked points to
\(\mathbf P^5\), of quadratic point rank 21. Hence

\[
 Q^{12},\ A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge72. \tag{4}
\]

## Lift the band to \(Q^{14}\)

Let \(d=14\) and

\[
 97\le h\le101,\qquad h=5d-1+q,\qquad 28\le q\le32. \tag{5}
\]

The residual \(Q^{12}\) span has rank at most

\[
 3d-3+q=39+q\in[67,71], \tag{6}
\]

contradicting (4).

Every mixed branch has budget at most \(q+2\in[30,34]\) after the
B253 stage. The first three minimal nested escapes contribute

\[
 (d-4)+(d-5)+(d-6)=10+9+8=27. \tag{7}
\]

For \(h\le100\), at most six dimensions remain, below the fourth escape
rank

\[
 d-7=7. \tag{8}
\]

If an earlier contribution fills the span, the surviving annihilator
confines every marked point to \(\mathbf P^5,\mathbf P^6\), or
\(\mathbf P^7\), of quadratic point rank at most 36.

At \(h=101\), survival forces all first three ranks to be minimal and
leaves exactly seven dimensions. The fourth point must lie in the
surviving \(J_3\), contribute rank seven, and fill the span. The
descended space \(J_4=J_3\cap x^\perp\) has dimension \(d-7=7\);
its rank-one annihilator confines every marked point to

\[
 \mathbf P(J_4^\perp)\simeq\mathbf P^8, \tag{9}
\]

whose quadratic point rank is

\[
 h^0(\mathbf P^8,O(2))=45<101. \tag{10}
\]

Therefore

\[
 Q^{14},\ A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge102. \tag{11}
\]

B276 constructs no ODP package, Kuranishi vanishing, rational detector,
specified pairing, algebraic cycle, proof, or disproof of HC.
