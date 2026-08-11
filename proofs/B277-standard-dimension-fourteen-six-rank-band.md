---
brick_id: B277
status: PROVED
base_field: C
variety: the smooth split quadrics Q^12 and Q^14 with their primitive ruling differences; standard A=O_Q(1), H=O_Q(2), and hypothetical G196 marked schemes
smoothness: both quadrics and the reduced marked schemes are smooth; no central ODP package is constructed
projectivity: the standard quadratic embeddings, residual orthogonal quadrics, five nested tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-seven/eight/nine-space contact bounds are projective
dimension: Q^12 has no standard rank from 72 through 77 and its floor is at least 78; Q^14 has no standard rank from 102 through 107 and its floor is at least 108
codimension: the primitive middle ruling differences supply valid universal test inputs; the theorem excludes G196 at rank 102 and removes standard equality from the next d=14 boundary, but leaves cubic/quartic equality and every detector clause open
coefficient_field: Q for the ruling differences and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: each ruling difference is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling differences only certify the universal test inputs
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B276, G196-G197, S081
claim: Standard tangent-absorbing spans on Q^12 have no ranks 72<=h_Z(1)<=77, and those on Q^14 have no ranks 102<=h_Z(1)<=107. Hence the Q^14 standard floor is at least 108, G196 is NO-GO, and G197 is active at the cubic/quartic rank 103 in dimension 14.
falsifier: a Q^12 standard candidate of rank 72 through 77, a Q^14 standard candidate of rank 102 through 107, failure of the B262 three-step escape in dimension 12, failure of the fifth nested escape/contact bound on Q^14, or a different next boundary
---

# B277 — Six further standard ranks fail in dimension fourteen

## The B262 band on \(Q^{12}\)

Set \(D=12\) in B262:

\[
 h=5D-1+q,\qquad q=2D-11+r=13+r,\qquad 0\le r\le5. \tag{1}
\]

Thus \(72\le h\le77\). The residual \(Q^{10}\) rank is at most

\[
 3D-3+q\le6D-21=51<6\cdot10-7=53, \tag{2}
\]

using B253 on \(Q^{10}\).

The first two mixed escapes have ranks at least \(D-4=8\) and
\(D-5=7\), leaving at most \(r\le5\) dimensions. The third escape
has rank at least \(D-6=6\). Filling after either earlier escape
confines the points to \(\mathbf P^5\) or \(\mathbf P^6\), of quadratic
rank at most 28. Hence

\[
 Q^{12},\ A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge78. \tag{3}
\]

## Lift to \(Q^{14}\)

Let \(d=14\) and \(102\le h\le107\). Writing

\[
 h=5d-1+q
\]

gives \(33\le q\le38\). The residual \(Q^{12}\) rank is

\[
 3d-3+q=39+q\in[72,77], \tag{4}
\]

contradicting (3).

In a mixed branch, the first three minimal escapes contribute 27
dimensions. The fourth minimum is \(d-7=7\), so four minimal escapes
contribute 34 and leave an annihilator containing
\(\operatorname{Sym}^2J_4\), \(\dim J_4=d-7=7\).

The budgets \(q+2\) range from 35 through 40. Through rank 106, fewer
than six dimensions remain after four minimal escapes, below the fifth
escape rank

\[
 \dim J_4-1=d-8=6. \tag{5}
\]

Any nonminimal earlier escape only reduces the remaining budget, unless
it fills the span; filling gives one of the already excluded
\(\mathbf P^5,\ldots,\mathbf P^8\) contact loci.

At rank 107 the budget is 40. Survival forces all four earlier ranks
to be minimal and leaves exactly six dimensions. The fifth point lies
in \(J_4\), contributes rank six, and fills. The descended
\(J_5=J_4\cap x^\perp\) has dimension \(d-8=6\), so every marked point
lies in

\[
 \mathbf P(J_5^\perp)\simeq\mathbf P^9. \tag{6}
\]

Its quadratic point rank is

\[
 h^0(\mathbf P^9,O(2))=55<107. \tag{7}
\]

Therefore

\[
 Q^{14},\ A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge108. \tag{8}
\]

B277 constructs no ODP package, Kuranishi vanishing, rational detector,
specified pairing, algebraic cycle, proof, or disproof of HC.
