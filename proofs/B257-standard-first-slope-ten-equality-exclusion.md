---
brick_id: B257
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, standard A=O_Q(1), and H=O_Q(2)
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: the standard quadratic embedding, residual orthogonal quadrics, tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-five-space contact bounds are projective
dimension: dim X=d=2n>=14; no standard candidate exists at h_Z(1)=6d-7, so every standard candidate has h_Z(1)>=6d-6; together with B254-B256 every polarization has h_Z(1)>=6d-6 and slack s>=10d-14
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction closes G183 and its adjacent odd layer
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B256, S081
claim: On (Q^d,a-b), d even and at least fourteen, the standard polarization cannot realize h_Z(1)=6d-7 with every marked tangent osculator absorbed. Hence every polarization has h_Z(1)>=6d-6 and slack s>=10d-14; G183 and its adjacent odd layer are NO-GO, and only the standard polarization remains at the next equality.
falsifier: a residual branch below B246's smaller-quadric floor, a nonfinal mixed branch fitting B253's d-4 escape, a final equality point outside J, failure of Sym^2(J intersect x-perp) to survive, point rank above twenty-one on P^5, a standard equality candidate, or a different next balanced signature
---

# B257 — The first standard slope-ten equality is impossible

Assume the standard polarization and

\[
 \dim S=h_Z(1)=6d-7,\qquad d\ge14. \tag{1}
\]

Write B253's parameter as

\[
 6d-7=5d-1+q,\qquad q=d-6. \tag{2}
\]

We retain B253's notation and branch classification.

## Every branch but one remains strictly excluded

The residual-\(Q^{d-2}\) branch has rank at most

\[
 3d-3+q=4d-9<5d-13, \tag{3}
\]

below B246's standard floor on the smaller quadric.

In the branch \(t\notin W\), the two possible remaining budgets are

\[
 q=d-6,\qquad q+1=d-5, \tag{4}
\]

both strictly below B253's \(d-4\) rank-one escape. In the branch
\(t\in W\), the subcase \(u\in K^\perp\) has the same two budgets, and
the subcase \(u\notin K^\perp,\ u\notin K\) has budget \(q+1=d-5\).
All are impossible.

Only B253's final subcase remains:

\[
 t\in W,\qquad u\notin K^\perp,\qquad u\in K. \tag{5}
\]

After adding \(T_u\), the current span has dimension at least \(5d-3\).
Put

\[
 J=K\cap u^\perp,\qquad \dim J=d-3. \tag{6}
\]

The annihilator contains \(\operatorname{Sym}^2J\), and only

\[
 (6d-7)-(5d-3)=d-4 \tag{7}
\]

dimensions remain. If \(T_u\) contributed more than \(d-3\), the
remaining budget would be smaller than \(d-4\), already contradicting
B253's escape. Hence survival forces equality before (7).

## Equality forces the last point into \(J\)

The quadratic point rank on
\(\mathbf P(J^\perp)\simeq\mathbf P^4\) is at most fifteen, so choose a
marked point

\[
 x\notin J^\perp. \tag{8}
\]

Contraction of \(\operatorname{Sym}^2J\) at \(x\) has image \(J\).
After quotienting by \(\mathbf Cx\), its rank is

\[
 \begin{cases}
 d-3,&x\notin J,\\
 d-4,&x\in J.
 \end{cases} \tag{9}
\]

The first case exceeds (7). Therefore equality forces \(x\in J\), and
its tangent contribution is exactly \(d-4\), filling \(S\).

## The filled span has tiny contact rank

Set

\[
 J'=J\cap x^\perp. \tag{10}
\]

Because \(x\notin J^\perp\), the defining functional is nonzero and

\[
 \dim J'=d-4. \tag{11}
\]

For every \(z\in J'\), the rank-one self-adjoint map

\[
 E_z(y)=B(z,y)z \tag{12}
\]

already belongs to \(\operatorname{Sym}^2J\) and satisfies \(E_zx=0\).
Thus all \(E_z\) remain in the annihilator after adding \(T_x\).

Since \(S\) is filled, every marked point must be a common eigenvector
of all \(E_z\), hence must lie in

\[
 \mathbf P((J')^\perp)\simeq\mathbf P^5. \tag{13}
\]

Its quadratic point rank is at most

\[
 h^0(\mathbf P^5,O(2))=21<6d-7, \tag{14}
\]

contradicting (1). Therefore the standard equality is impossible.

## The next boundary

B254-B256 place every nonstandard polarization at \(6d+6\) or above.
Together with the exclusion just proved,

\[
 h_Z(1)\ge6d-6,\qquad
 \delta_1\ge5d-7,\qquad s\ge10d-14. \tag{15}
\]

Thus G183 and its adjacent odd layer \(s=10d-15\) are NO-GO. The next
balanced signature is

\[
 s=10d-14,\qquad \delta_1=5d-7,\qquad
 N=12d-12,\qquad h_Z(1)=6d-6=N/2. \tag{16}
\]

Only \(A=O_Q(1)\) remains at (16). B257 is a necessary special-input
obstruction. It constructs no configuration, ODP package, rational
detector, specified pairing, algebraic cycle, proof, or disproof of HC.
