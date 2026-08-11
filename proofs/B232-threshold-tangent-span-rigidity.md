---
brick_id: B232
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=4, primitive ruling class difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the marked point scheme are smooth and reduced; central ODP and incidence clauses remain inherited hypotheses
projectivity: the complete A and H embeddings, double neighborhoods, tangent osculators, point spans, and secant geometry are projective
dimension: dim X=d=2n; every m=2 candidate has slack s>=2d+4; at equality N=4d+6 and h_Z(1)=2d+3=N/2
codimension: the threshold obstruction uses one legitimate primitive codimension-n input and raises the degree-two universal slack floor by two
coefficient_field: Q for zeta and C for sections, tangent jets, symmetric tensors, ranks, and quadric polarity
cohomology_theory: rational singular cohomology for the primitive input and coherent restriction to finite double-point schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B221-B231, S081
claim: On (Q^d,a-b), no m=2 G144 candidate exists with slack s<=2d+3. At the first unexcluded value s=2d+4, necessarily delta_1=d+2, N=4d+6, h_Z(1)=2d+3=N/2, and the degree-one relation transport is an isomorphism. At this threshold no polarization A=B^ell with ell>=3 can occur.
falsifier: a candidate in the excluded band, a third marked point in the span of two independent standard-quadric tangent osculators, failure of B215 mixed interpolation for two doubles plus reduced points, or a different equality rank signature
---

# B232 — Threshold tangent spans cannot hold a third point

Retain the valid input \((Q^d,a-b)\), \(d=2n\ge4\), and let
\(S\) be the degree-one point span for \(H=A^2\).

## Reduction to the boundary rank

B231 already excludes \(m=2\) when \(s<2d+2\). Suppose now

\[
 2d+2\le s\le2d+3. \tag{1}
\]

B222 gives \(2\delta_1\le s\). If \(\delta_1\le d\), B231's
pairwise-defect argument still applies. The only remaining rank is

\[
 \delta_1=d+1,\qquad \dim S=h_Z(1)=2d+2. \tag{2}
\]

There are more than two marked points because
\(N=2(d+1)+s\ge4d+4\).

## Powered quadric polarizations

Write \(A=O_Q(k)\). If \(k\ge2\), then
\(H=O_Q(2k)\) has exponent at least four. B215 applied to two double
neighborhoods and one additional reduced point gives the surjection

\[
 H^0(Q,H)\longrightarrow
 H^0(2p\sqcup2q\sqcup r,H) \tag{3}
\]

for any three distinct points. Its target has dimension
\(2(d+1)+1=2d+3\), but all three dual jet spaces lie in \(S\), whose
dimension is only \(2d+2\). This is impossible.

## The standard quadric polarization

It remains to take \(k=1\). Let \(V\) be the quadratic vector space,
and write

\[
 T_v=v\mathbin{\odot}v^\perp\subset\operatorname{Sym}^2V \tag{4}
\]

for the vector tangent osculator of the \(O_Q(2)\)-embedding at
\([v]\).

If all marked representatives are pairwise orthogonal, they span a
totally isotropic \(W\), and B231's vector
\(v\mathbin{\odot}u\), \(u\in v^\perp\setminus W\), contradicts
\(T_v\subset S\subset\operatorname{Sym}^2W\).

Otherwise choose marked \(v,w\) with \(B(v,w)\ne0\). The hyperbolic
plane they span has an orthogonal complement \(U\), so

\[
 V=\langle v,w\rangle\perp U,\qquad
 v^\perp=\langle v\rangle\oplus U,\qquad
 w^\perp=\langle w\rangle\oplus U. \tag{5}
\]

The symmetric-square decomposition shows

\[
 T_v=\langle v^2,vU\rangle,\qquad
 T_w=\langle w^2,wU\rangle,\qquad T_v\cap T_w=0. \tag{6}
\]

Both spaces have dimension \(d+1\). By (2) and tangent absorption,

\[
 S=T_v\oplus T_w. \tag{7}
\]

Take any marked representative \(r=av+bw+u\), \(u\in U\). Since
\(r^2\in S\), its components in the direct complementary summands
\(\langle vw\rangle\oplus\operatorname{Sym}^2U\) vanish:

\[
 2ab\,vw+u^2=0. \tag{8}
\]

Thus \(ab=0\) and \(u=0\); hence \([r]=[v]\) or \([w]\). This
contradicts the presence of a third distinct marked point. Therefore

\[
 m=2\quad\Longrightarrow\quad s\ge2d+4. \tag{9}
\]

## First unexcluded signature

At \(s=2d+4\), the same obstruction excludes
\(\delta_1\le d+1\), while \(2\delta_1\le s\) gives
\(\delta_1\le d+2\). Consequently the only unexcluded rank is

\[
 \delta_1=d+2,\qquad N=4d+6,\qquad
 h_Z(1)=2d+3=N/2,\qquad s-2\delta_1=0. \tag{10}
\]

The relation transport is an isomorphism and the degree-one code is
diagonally self-dual. Moreover, if \(A=B^\ell\) with \(\ell\ge3\),
then \(A^2=B^{2\ell}\) has exponent at least six. B215 separates two
double neighborhoods and two additional reduced points from exponent
five onward, imposing \(2d+4\) independent conditions inside the
\((2d+3)\)-dimensional span. Thus such powers are excluded at (10).

B232 is a necessary projective obstruction only. It supplies no marked
configuration at the new threshold, no ODP or Kuranishi package, no
rational detector or specified pairing, and no algebraic cycle.
