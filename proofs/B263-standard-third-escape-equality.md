---
brick_id: B263
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, residual orthogonal quadrics, four nested tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-seven-space contact bounds are projective
dimension: dim X=d=2n>=14; the standard polarization has h_Z(1)>=8d-17; the common floor is K(d)=6d+6 for d=14,16,18,20 and K(d)=7d+5 for every even d>=22
codimension: the primitive codimension-n ruling difference supplies a valid universal input; excluding the d=22 standard equality closes G189 as a universal gate and leaves square or cubic/quartic equality regimes
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B262, S081
claim: On (Q^d,a-b), d even and at least fourteen, the standard polarization cannot realize h_Z(1)=8d-18 with every marked tangent osculator absorbed. Hence its floor is h_Z(1)>=8d-17. Together with B260-B262, the common floor is K(d)=6d+6 for d=14,16,18,20 and K(d)=7d+5 for every even d>=22. G189 is NO-GO as a universal gate.
falsifier: a residual Q^(d-2) configuration below B253/B259, a mixed equality branch not forcing three minimal tangent ranks, failure of a descended Sym^2(J) annihilator, quadratic point rank above 36 on P^7, a standard equality candidate, or a different common floor
---

# B263 — Equality at the third escape is impossible

Assume the standard polarization and

\[
 h=\dim S=8d-18,\qquad d\ge14. \tag{1}
\]

In B253 and B262 notation this is

\[
 h=5d-1+q,\qquad q=3d-17. \tag{2}
\]

## The residual branch remains impossible

The projected standard point span on the residual \(Q^{d-2}\) has
dimension at most

\[
 3d-3+q=6d-20. \tag{3}
\]

For \(d=14\), B253 gives the residual floor \(6d-19\). For even
\(d\ge16\), B259 gives the residual floor \(7d-26\), and

\[
 6d-20<7d-26 \tag{4}
\]

because \(d>6\). Thus no residual branch survives.

## Equality forces three minimal contractions

Every mixed B253 branch reaches an annihilator containing
\(\operatorname{Sym}^2J_0\), \(\dim J_0=d-3\), with budget at most

\[
 q+2=3d-15. \tag{5}
\]

Choose a marked \(x\notin J_0^\perp\). Contraction modulo
\(\mathbf Cx\) has rank \(d-3\) if \(x\notin J_0\), and rank \(d-4\)
if \(x\in J_0\). The descended annihilator contains

\[
 \operatorname{Sym}^2J_1,\qquad
 J_1=J_0\cap x^\perp,\qquad \dim J_1=d-4. \tag{6}
\]

If the span fills here, every marked point lies in
\(\mathbf P(J_1^\perp)\simeq\mathbf P^5\), of quadratic point rank at
most 21, contradicting (1).

If the span has not filled, choose a marked
\(y\notin J_1^\perp\). Its corresponding ranks are \(d-4\) outside
\(J_1\) and \(d-5\) inside \(J_1\), and the next annihilator contains

\[
 \operatorname{Sym}^2J_2,\qquad
 J_2=J_1\cap y^\perp,\qquad \dim J_2=d-5. \tag{7}
\]

If the span fills here, every marked point lies in
\(\mathbf P(J_2^\perp)\simeq\mathbf P^6\), of quadratic point rank at
most 28, again contradicting (1).

If the span still has not filled, choose
\(z\notin J_2^\perp\). Its ranks are \(d-5\) outside \(J_2\) and
\(d-6\) inside \(J_2\). The sum of the three minimal ranks is exactly

\[
 (d-4)+(d-5)+(d-6)=3d-15. \tag{8}
\]

Therefore survival through (5) forces

\[
 x\in J_0,\qquad y\in J_1,\qquad z\in J_2, \tag{9}
\]

and all three contractions have their minimal ranks. Any failure of
(9) exceeds the budget. Equality in (8) fills \(S\).

## The filled span has point rank at most 36

Put

\[
 J_3=J_2\cap z^\perp. \tag{10}
\]

Since \(z\notin J_2^\perp\), the defining functional is nonzero, so
\(\dim J_3=d-6\). Every rank-one map from
\(\operatorname{Sym}^2J_3\) remains in the annihilator after adjoining
the three tangents. Because \(S\) is filled, every marked point is a
common eigenvector and hence lies in

\[
 \mathbf P(J_3^\perp)\simeq\mathbf P^7. \tag{11}
\]

Its quadratic point rank is at most

\[
 h^0(\mathbf P^7,O(2))=36<8d-18 \tag{12}
\]

for \(d\ge14\), contradicting (1). Thus

\[
 A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge8d-17. \tag{13}
\]

## The updated common boundary

Combining (13) with B260-B262 gives

\[
 K(d)=
 \begin{cases}
 6d+6,&d=14,16,18,20,\\
 7d+5,&d\ge22\text{ even}.
 \end{cases} \tag{14}
\]

At equality, only \(k=2\) survives for \(d=14,16,18,20\); at
\(d=22\), \(k=1,3,4\) survive; and for every even \(d\ge24\), only
\(k=3,4\) survive. B263 is a necessary special-input obstruction. It
constructs no configuration, ODP package, rational detector, specified
pairing, algebraic cycle, proof, or disproof of HC.
