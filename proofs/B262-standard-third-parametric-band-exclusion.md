---
brick_id: B262
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, residual orthogonal quadrics, three nested tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-five/six-space contact bounds are projective
dimension: dim X=d=2n>=14; the standard polarization has h_Z(1)>=8d-18; combined with B260-B261 the common floor is L(d)=6d+6 for d=14,16,18,20, L(22)=158, and L(d)=7d+5 for even d>=24
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction closes G188 as a universal gate and reduces the next equality audit to square, one standard, and high-dimensional cubic/quartic regimes
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B261, S081
claim: On (Q^d,a-b), d even and at least fourteen, no standard tangent-absorbing point span has h_Z(1)=5d-1+q for 2d-11<=q<=3d-18. Hence the standard floor is h_Z(1)>=8d-18. Together with B260-B261, the common floor is L(d)=6d+6 for d=14,16,18,20, L(22)=158, and L(d)=7d+5 for even d>=24. G188 is NO-GO as a universal gate.
falsifier: a residual Q^(d-2) configuration below the cited recursive floor, a mixed branch outside the q+2 budget, failure of either nested Sym^2 annihilator, a third escape below d-6, a standard candidate in the stated band, a candidate below L(d), or a different piecewise boundary
---

# B262 — A third parametric standard band is impossible

Let the standard-polarized point span have

\[
 h=\dim S=5d-1+q,\qquad
 q=2d-11+r,\qquad 0\le r\le d-7,\qquad d\ge14. \tag{1}
\]

Equivalently,

\[
 2d-11\le q\le3d-18,\qquad
 7d-12\le h\le8d-19. \tag{2}
\]

## The residual branch recurses

The projected standard point span on the residual \(Q^{d-2}\) has
dimension at most

\[
 3d-3+q\le6d-21. \tag{3}
\]

For \(d=14\), the residual dimension is \(D=12\), and B253 gives the
standard floor

\[
 6D-7=6d-19>6d-21. \tag{4}
\]

For even \(d\ge16\), \(D=d-2\ge14\), and B259 gives

\[
 7D-12=7d-26>6d-21. \tag{5}
\]

Thus the residual branch is impossible throughout the band.

## A uniform three-step escape

Every mixed B253 branch leaves a budget no larger than

\[
 q+2=2d-9+r \tag{6}
\]

with \(\operatorname{Sym}^2J_0\) in the annihilator and
\(\dim J_0=d-3\). Choose a marked \(x\notin J_0^\perp\).
Its tangent contributes at least \(d-4\), leaving at most

\[
 d-5+r. \tag{7}
\]

The descended annihilator contains

\[
 \operatorname{Sym}^2J_1,\qquad
 J_1=J_0\cap x^\perp,\qquad \dim J_1=d-4. \tag{8}
\]

If the span fills, the contact locus lies in a \(\mathbf P^5\) of
quadratic point rank at most 21. Otherwise choose a marked
\(y\notin J_1^\perp\). Its tangent contributes at least \(d-5\), so
at most

\[
 r \tag{9}
\]

dimensions remain. The annihilator now contains

\[
 \operatorname{Sym}^2J_2,\qquad
 J_2=J_1\cap y^\perp,\qquad \dim J_2=d-5. \tag{10}
\]

If the span fills, all marked points lie in a \(\mathbf P^6\), of
quadratic point rank at most

\[
 h^0(\mathbf P^6,O(2))=28. \tag{11}
\]

Otherwise choose a marked \(z\notin J_2^\perp\). Its residual tangent
rank is at least

\[
 \dim J_2-1=d-6. \tag{12}
\]

But

\[
 r\le d-7<d-6, \tag{13}
\]

a contradiction. This excludes every mixed branch.

## The new standard and common floors

B259 excludes all standard values through \(7d-13\), and (1)-(13)
exclude the next band through \(8d-19\). Hence

\[
 A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge8d-18. \tag{14}
\]

Combining (14) with B260-B261 gives the common floor

\[
 L(d)=
 \begin{cases}
 6d+6,&d=14,16,18,20,\\
 158,&d=22,\\
 7d+5,&d\ge24\text{ even}.
 \end{cases} \tag{15}
\]

At equality, the survivors are:

\[
\begin{array}{c|c}
 d & \text{survivors}\\ \hline
 14,16,18,20 & k=2\\
 22 & k=1\\
 d\ge24\text{ even} & k=3,4.
\end{array} \tag{16}
\]

B262 is a necessary special-input obstruction. It constructs no
configuration, ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC.
