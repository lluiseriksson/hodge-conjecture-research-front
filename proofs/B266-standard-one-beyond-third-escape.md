---
brick_id: B266
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=16, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, residual orthogonal quadrics, five nested tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-seven-space contact bounds are projective
dimension: dim X=d=2n>=16; the standard polarization has h_Z(1)>=8d-16; the common floor is P(d)=6d+6 for d=14,16,18,20 and P(d)=7d+6 for every even d>=22
codimension: the primitive codimension-n ruling difference supplies a valid universal input; excluding the d=22 rank-159 standard equality closes G191 as a universal gate and leaves low square, a d=22 standard/cubic/quartic tie, and high cubic/quartic regimes
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B265, S081
claim: On (Q^d,a-b), d even and at least sixteen, the standard polarization cannot realize h_Z(1)=8d-17 with every marked tangent osculator absorbed. Hence its floor is h_Z(1)>=8d-16. Together with B260-B265, the common floor is P(d)=6d+6 for d=14,16,18,20 and P(d)=7d+6 for every even d>=22. G191 is NO-GO as a universal gate.
falsifier: a residual Q^(d-2) configuration below B259's floor, a mixed branch exceeding the q+2 budget classification, failure of the fourth descended Sym^2(J) escape, quadratic point rank above 36 on P^7, a standard rank-(8d-17) candidate, or a different common floor
---

# B266 — One dimension beyond the third escape is impossible

Assume the standard polarization and

\[
 h=\dim S=8d-17,
 \qquad q=h-(5d-1)=3d-16,
 \qquad d\ge16. \tag{1}
\]

## The residual branch

The projected standard span on \(Q^{d-2}\) has dimension at most

\[
 3d-3+q=6d-19. \tag{2}
\]

B259's standard floor on that residual quadric is

\[
 7(d-2)-12=7d-26. \tag{3}
\]

Since \(6d-19<7d-26\) for \(d>7\), the residual branch is impossible.

## Three escapes leave at most one dimension

Every mixed B253 branch reaches an annihilator containing
\(\operatorname{Sym}^2J_0\), \(\dim J_0=d-3\), with remaining budget
at most

\[
 q+2=3d-14. \tag{4}
\]

As in B262-B263, successive marked points outside the current contact
locus contribute at least

\[
 d-4,\qquad d-5,\qquad d-6. \tag{5}
\]

If the span fills after the first or second escape, every marked point
lies respectively in a \(\mathbf P^5\) or \(\mathbf P^6\), of quadratic
point rank at most 21 or 28, contradicting (1).

After the third escape, the total contribution is at least

\[
 (d-4)+(d-5)+(d-6)=3d-15. \tag{6}
\]

If it is \(3d-14\), the span fills and the descended annihilator
contains \(\operatorname{Sym}^2J_3\), \(\dim J_3=d-6\). Every marked
point then lies in \(\mathbf P(J_3^\perp)\simeq\mathbf P^7\), of
quadratic point rank at most 36, again contradicting (1). A larger
contribution exceeds the budget.

It remains only when all three ranks are minimal. Then at most

\[
 (3d-14)-(3d-15)=1 \tag{7}
\]

dimension remains, and \(\operatorname{Sym}^2J_3\) still survives. If
the span has not filled, its point rank exceeds 36, so choose a marked
point outside \(\mathbf P(J_3^\perp)\). Its residual tangent rank is at
least

\[
 \dim J_3-1=d-7>1, \tag{8}
\]

contradicting (7). Therefore

\[
 A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge8d-16
 \quad(d\ge16\text{ even}). \tag{9}
\]

## The updated common boundary

Together with B260-B265, (9) gives

\[
 P(d)=
 \begin{cases}
 6d+6,&d=14,16,18,20,\\
 7d+6,&d\ge22\text{ even}.
 \end{cases} \tag{10}
\]

Only \(k=2\) survives at equality in dimensions \(14,16,18,20\). At
\(d=22\), \(k=1,3,4\) survive, while only \(k=3,4\) survive for every
even \(d\ge24\). B266 is a necessary special-input obstruction. It
constructs no ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC.
