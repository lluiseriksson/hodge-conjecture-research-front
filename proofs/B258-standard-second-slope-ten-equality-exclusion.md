---
brick_id: B258
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, standard A=O_Q(1), and H=O_Q(2)
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: the standard quadratic embedding, residual orthogonal quadrics, nested tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-five-space contact bounds are projective
dimension: dim X=d=2n>=14; no standard candidate exists at h_Z(1)=6d-6, so every standard candidate has h_Z(1)>=6d-5; together with B254-B256 every polarization has h_Z(1)>=6d-5 and slack s>=10d-12
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction closes G184 and its adjacent odd layer
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B257, S081
claim: On (Q^d,a-b), d even and at least fourteen, the standard polarization cannot realize h_Z(1)=6d-6 with every marked tangent osculator absorbed. Hence every polarization has h_Z(1)>=6d-5 and slack s>=10d-12; G184 and its adjacent odd layer are NO-GO, and only the standard polarization remains at the next equality.
falsifier: a residual branch below B246's smaller-quadric floor, a q=d-5 branch escaping the d-5/d-4/d-3 budget classification, failure of the nested rank-one annihilator, a second escape of rank at most one, point rank above twenty-one on P^5, a standard equality candidate, or a different next balanced signature
---

# B258 — The second standard slope-ten equality is impossible

Assume the standard polarization and

\[
 \dim S=h_Z(1)=6d-6,\qquad d\ge14. \tag{1}
\]

In B253's notation,

\[
 6d-6=5d-1+q,\qquad q=d-5. \tag{2}
\]

The residual-\(Q^{d-2}\) branch has rank at most

\[
 3d-3+q=4d-8<5d-13, \tag{3}
\]

so B246 excludes it.

## The nested escape lemma at this rank

Suppose a current annihilator contains
\(\operatorname{Sym}^2J\), \(\dim J=d-3\), and a marked point
\(x\notin J^\perp\) must fit in a remaining budget \(b\).
Contraction modulo \(\mathbf Cx\) has rank

\[
 d-3\quad\text{if }x\notin J,\qquad
 d-4\quad\text{if }x\in J. \tag{4}
\]

After adjoining \(T_x\), the annihilator still contains

\[
 \operatorname{Sym}^2J',\qquad
 J'=J\cap x^\perp,\qquad \dim J'=d-4. \tag{5}
\]

If the span fills, every marked point lies in
\(\mathbf P((J')^\perp)\simeq\mathbf P^5\), of quadratic point rank at
most 21, a contradiction. If it does not fill, choose a marked
\(y\notin(J')^\perp\); its residual tangent rank is at least

\[
 \dim J'-1=d-5. \tag{6}
\]

Thus a budget \(b=d-4\) is impossible: (4) forces \(x\in J\) and fills
the span, after which the projective-five-space contradiction applies.
A budget \(b=d-3\) is also impossible. If \(x\notin J\), (4) fills the
span; if \(x\in J\), at most one dimension remains, while
\(d-5>1\) in (6).

## Exhaustion of B253's mixed branches

For \(t\notin W\), the remaining budgets after the next tangent are

\[
 q=d-5,\qquad q+1=d-4. \tag{7}
\]

The first is below B253's original \(d-4\) escape; the second is
excluded by the nested lemma.

For \(t\in W,\ u\in K^\perp\), the subsequent point again leaves
either \(q=d-5\) or \(q+1=d-4\), so the same argument applies.

For \(t\in W,\ u\notin K^\perp,\ u\notin K\), the budget is
\(q+1=d-4\), excluded by the nested lemma.

Finally, for

\[
 t\in W,\qquad u\notin K^\perp,\qquad u\in K, \tag{8}
\]

the budget is

\[
 q+2=d-3. \tag{9}
\]

This is the second case of the nested lemma. Hence every branch is
impossible.

## The next boundary

B254-B256 place every nonstandard polarization at \(6d+6\) or above.
Together with the standard exclusion,

\[
 h_Z(1)\ge6d-5,\qquad
 \delta_1\ge5d-6,\qquad s\ge10d-12. \tag{10}
\]

Thus G184 and its adjacent odd layer \(s=10d-13\) are NO-GO. The next
balanced signature is

\[
 s=10d-12,\qquad \delta_1=5d-6,\qquad
 N=12d-10,\qquad h_Z(1)=6d-5=N/2. \tag{11}
\]

Only \(A=O_Q(1)\) remains at (11). B258 is a necessary special-input
obstruction. It constructs no configuration, ODP package, rational
detector, specified pairing, algebraic cycle, proof, or disproof of HC.
