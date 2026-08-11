---
brick_id: B274
status: PROVED
base_field: C
variety: the smooth split quadrics Q^12 and Q^14 with their primitive ruling differences; standard A=O_Q(1), H=O_Q(2), and hypothetical G193 marked schemes
smoothness: both quadrics and the reduced marked schemes are smooth; no central ODP package is constructed
projectivity: the standard quadratic embeddings, residual orthogonal quadrics, nested tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-five/seven-space contact bounds are projective
dimension: the Q^12 standard rank 65 is impossible and its floor is at least 66; consequently the Q^14 standard rank 95 is impossible and its floor is at least 96=8d-16
codimension: the primitive middle ruling differences supply valid universal test inputs; the theorem excludes G193 at R(14)=95 but leaves the next standard equality and every detector clause open
coefficient_field: Q for the ruling differences and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: each ruling difference is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling differences only certify the universal test inputs
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B273, G193-G194, S081
claim: The standard tangent-absorbing span on Q^12 cannot have rank 65, and the standard tangent-absorbing span on Q^14 cannot have rank 95. Hence the standard floor is at least 96 on Q^14, G193 is NO-GO, and G194 is the next active boundary.
falsifier: a Q^12 standard rank-65 candidate, a Q^14 standard rank-95 candidate, failure of the B253/B257 branch classification in dimension 12, a residual Q^12 branch not controlled by its new floor, or a different next boundary
---

# B274 — The dimension-fourteen residual equality also fails

The only reason B266 starts at \(d=16\) is its residual use of B259 on
\(Q^{d-2}\). At \(d=14\), that residual branch lands exactly on the
previously unaudited standard equality

\[
 Q^{12},\qquad h_Z(1)=65=6\cdot12-7. \tag{1}
\]

We first exclude (1), then return to \(Q^{14}\).

## Exclude the rank-65 equality on \(Q^{12}\)

Run B257's standard-only equality argument with \(D=12\). Its inputs
B246 and B253 are valid in dimensions at least 8 and 10 respectively.
In B253 notation,

\[
 q=D-6=6. \tag{2}
\]

The residual \(Q^{10}\) branch has rank at most

\[
 4D-9=39<5D-13=47, \tag{3}
\]

where 47 is B246's standard floor on \(Q^{10}\).

Every nonfinal mixed branch leaves budget \(q=6\) or \(q+1=7\),
strictly below the rank-one escape \(D-4=8\). In the sole final branch,
the current span has dimension \(5D-3=57\), leaving exactly

\[
 65-57=8=D-4. \tag{4}
\]

As in B257, an escaping marked point must lie in the surviving
\((D-3)\)-dimensional space \(J\), contributes exactly \(D-4=8\), and
fills the span. The descended rank-one annihilator then confines every
marked point to \(\mathbf P^5\), whose quadratic point rank is at most

\[
 h^0(\mathbf P^5,O(2))=21<65. \tag{5}
\]

This contradiction proves

\[
 Q^{12},\ A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge66. \tag{6}
\]

## Exclude rank 95 on \(Q^{14}\)

Now run B266 with \(d=14\). Its residual projected span has rank at most

\[
 6d-19=65, \tag{7}
\]

which contradicts (6). All mixed branches of B266 remain valid:
the first three minimal escapes contribute

\[
 (d-4)+(d-5)+(d-6)=10+9+8=27, \tag{8}
\]

inside the budget \(3d-14=28\), leaving at most one dimension. A fourth
escape contributes at least \(d-7=7>1\); a filled span confines the
marked points to \(\mathbf P^5,\mathbf P^6\), or \(\mathbf P^7\), all
of quadratic point rank at most \(36<95\). Thus

\[
 Q^{14},\ A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge96=8d-16. \tag{9}
\]

The rank \(R(14)=95\) proposed by G193 is impossible on a valid
universal input. B274 constructs no ODP package, Kuranishi vanishing,
rational detector, specified pairing, algebraic cycle, proof, or
disproof of HC.
