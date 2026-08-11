---
brick_id: B275
status: PROVED
base_field: C
variety: the smooth split quadrics Q^12 and Q^14 with their primitive ruling differences; standard A=O_Q(1), H=O_Q(2), and hypothetical G194 marked schemes
smoothness: both quadrics and the reduced marked schemes are smooth; no central ODP package is constructed
projectivity: the standard quadratic embeddings, residual orthogonal quadrics, nested tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-five/seven-space contact bounds are projective
dimension: the Q^12 standard rank 66 is impossible and its floor is at least 67; consequently the Q^14 standard rank 96 is impossible and its floor is at least 97
codimension: the primitive middle ruling differences supply valid universal test inputs; the theorem excludes G194 at T(14)=96 but leaves the next standard equality and every detector clause open
coefficient_field: Q for the ruling differences and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: each ruling difference is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling differences only certify the universal test inputs
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B274, G194-G195, S081
claim: The standard tangent-absorbing span on Q^12 cannot have rank 66, and the standard tangent-absorbing span on Q^14 cannot have rank 96. Hence the standard floor is at least 97 on Q^14, G194 is NO-GO, and G195 is the next active boundary.
falsifier: a Q^12 standard rank-66 candidate, a Q^14 standard rank-96 candidate, failure of the B253/B258 nested branch classification in dimension 12, or a different next boundary
---

# B275 — The second dimension-fourteen residual equality fails

## Exclude rank 66 on \(Q^{12}\)

Specialize B258's standard-only argument to \(D=12\). Its B246/B253
inputs are valid in the required dimensions. Here

\[
 h_Z(1)=66=6D-6,\qquad q=D-5=7. \tag{1}
\]

The residual \(Q^{10}\) branch has rank at most

\[
 4D-8=40<5D-13=47. \tag{2}
\]

The mixed budgets are \(q=7\), \(q+1=8\), and \(q+2=9\). B258's
nested annihilator starts with \(\dim J=D-3=9\). The first escape has
rank 8 or 9, the descended \(J'\) has dimension 8, and a second escape
has rank at least

\[
 \dim J'-1=D-5=7>1. \tag{3}
\]

Budget 7 is below the first rank-eight escape. At budget 8 the first
escape must be the rank-eight case and fills the span, forcing the
\(\mathbf P^5\) point-rank contradiction. At budget 9, a rank-nine
escape fills, while a rank-eight escape leaves only one dimension,
less than (3). Thus every branch fails and

\[
 Q^{12},\ A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge67. \tag{4}
\]

## Exclude rank 96 on \(Q^{14}\)

For \(d=14\) and \(h=96=8d-16\), B253's parameter and the mixed budget
are

\[
 q=3d-15=27,\qquad q+2=3d-13=29. \tag{5}
\]

The residual projected span has rank at most

\[
 3d-3+q=66, \tag{6}
\]

contradicting (4). In every mixed branch the first three minimal
escapes contribute \(10+9+8=27\). Total contribution 27 or 28 leaves
two or one dimensions, below the fourth escape rank \(d-7=7\);
contribution 29 fills the span and confines every marked point to
\(\mathbf P^7\), of quadratic point rank at most \(36<96\).
Earlier filling gives the still smaller \(\mathbf P^5/\mathbf P^6\)
contact bounds. Hence

\[
 Q^{14},\ A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge97. \tag{7}
\]

B275 constructs no ODP package, Kuranishi vanishing, rational detector,
specified pairing, algebraic cycle, proof, or disproof of HC.
