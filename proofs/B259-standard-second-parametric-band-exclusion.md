---
brick_id: B259
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, residual orthogonal quadrics, nested tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-four/five-space contact bounds are projective
dimension: dim X=d=2n>=14; the standard polarization has h_Z(1)>=7d-12; every nonstandard polarization has h_Z(1)>=6d+6; every polarization has h_Z(1)>=F(d)=min(7d-12,6d+6), delta_1>=F(d)-d-1, and slack s>=min(12d-26,10d+10)
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction closes G185 and every common layer below the piecewise post-band boundary
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B258, S081
claim: On (Q^d,a-b), d even and at least fourteen, no standard tangent-absorbing point span has h_Z(1)=5d-1+q for d-4<=q<=2d-12. Hence the standard floor is h_Z(1)>=7d-12. Together with B254-B256, every polarization has h_Z(1)>=F(d)=min(7d-12,6d+6) and slack s>=min(12d-26,10d+10). G185 and every lower common layer are NO-GO.
falsifier: a residual standard Q^(d-2) configuration of rank below B246's floor, a mixed branch outside the q/q+1/q+2 budget classification, failure of the nested Sym^2(J intersect x-perp) annihilator, a second escape below d-5, a standard candidate in the stated band, a candidate below F(d), or a different piecewise boundary
---

# B259 — A second parametric standard band is impossible

Let the standard-polarized point span have

\[
 h=\dim S=5d-1+q,\qquad
 q=d-4+r,\qquad 0\le r\le d-8,\qquad d\ge14. \tag{1}
\]

Equivalently,

\[
 d-4\le q\le2d-12,\qquad
 6d-5\le h\le7d-13. \tag{2}
\]

We retain B253's exhaustive branch classification and B258's nested
rank-one escape.

## The residual branch

If every residual marked point lies in the orthogonal
\(Q^{d-2}\), its projected standard point span has dimension at most

\[
 3d-3+q\le3d-3+(2d-12)=5d-15. \tag{3}
\]

B246's standard floor on \(Q^{d-2}\) is

\[
 5(d-2)-3=5d-13. \tag{4}
\]

Thus (3) is strictly too small throughout the band.

## A uniform two-step escape

Every mixed branch of B253 leaves a rank budget no larger than

\[
 q+2=d-2+r \tag{5}
\]

at a stage whose annihilator contains
\(\operatorname{Sym}^2J\), \(\dim J=d-3\). The marked point rank
exceeds fifteen, so choose \(x\notin J^\perp\).

Contraction modulo \(\mathbf Cx\) contributes at least \(d-4\). After
adjoining \(T_x\), the remaining budget is therefore at most

\[
 (d-2+r)-(d-4)=r+2\le d-6. \tag{6}
\]

Moreover

\[
 J'=J\cap x^\perp,\qquad \dim J'=d-4,\qquad
 \operatorname{Sym}^2J'\subset(S+T_x)^\perp. \tag{7}
\]

If the span fills, the surviving rank-one maps confine every marked
point to \(\mathbf P((J')^\perp)\simeq\mathbf P^5\), of quadratic
point rank at most 21, contradicting (1).

If the span does not fill, the same point-rank bound supplies a marked
\(y\notin(J')^\perp\). Contraction of
\(\operatorname{Sym}^2J'\) at \(y\), modulo \(\mathbf Cy\), has rank
at least

\[
 \dim J'-1=d-5. \tag{8}
\]

But (6) gives

\[
 r+2\le d-6<d-5, \tag{9}
\]

a contradiction. This excludes every mixed branch uniformly.

## Standard and common floors

B253, B257, and B258 exclude all smaller standard values from
\(5d-1\) through \(6d-6\). Equations (1)-(9) extend the exclusion
through \(7d-13\), so

\[
 A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge7d-12. \tag{10}
\]

B254-B256 give

\[
 A=O_Q(k),\ k\ge2\quad\Longrightarrow\quad h_Z(1)\ge6d+6. \tag{11}
\]

Put

\[
 F(d)=\min\{7d-12,6d+6\}. \tag{12}
\]

Then every polarization satisfies

\[
 h_Z(1)\ge F(d),\qquad
 \delta_1\ge F(d)-d-1,\qquad
 s\ge\min\{12d-26,10d+10\}. \tag{13}
\]

The next balanced signature is

\[
 h_Z(1)=F(d),\qquad
 \delta_1=F(d)-d-1,\qquad
 s=2(F(d)-d-1),\qquad N=2F(d). \tag{14}
\]

For \(d=14,16\), only the standard polarization can attain the lower
bound; for \(d=18\), the two floors coincide; for even \(d\ge20\), only
nonstandard polarizations can attain it.

B259 is a necessary special-input obstruction. It constructs no
configuration, ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC.
