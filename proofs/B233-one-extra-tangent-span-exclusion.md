---
brick_id: B233
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=4, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked point scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: the complete O_Q(k), O_Q(2k), tangent-span, double-neighborhood, quartic-separation, and secant-line data are projective
dimension: dim X=d=2n; every m=2 candidate has slack s>=2d+6; at the first unexcluded value N=4d+8 and h_Z(1)=2d+4=N/2
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction raises the degree-two slack floor by two further layers
coefficient_field: Q for zeta and C for sections, symmetric tensors, tangent jets, ranks, and quadric polarity
cohomology_theory: rational singular cohomology for the primitive input and coherent restriction to double and reduced finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B221-B232, S081
claim: On (Q^d,a-b), no m=2 G144 candidate exists with slack s<=2d+5. At the first unexcluded value s=2d+6, necessarily delta_1=d+3, N=4d+8, h_Z(1)=2d+4=N/2, and the degree-one relation transport is an isomorphism. Polarizations A=B^ell with ell>=3 remain excluded at this next threshold.
falsifier: a candidate in the excluded band, a third standard-quadric tangent osculator whose image modulo two independent tangent osculators has dimension at most one, a noncollinear fourth point not separable by ambient quartics from two doubles plus a third point, or a different next-threshold rank
---

# B233 — One extra tangent-span dimension is still insufficient

Fix \((Q^d,a-b)\), \(d=2n\ge4\). B232 excludes \(m=2\) through
slack \(2d+3\). Suppose

\[
 2d+4\le s\le2d+5. \tag{1}
\]

If \(\delta_1\le d+1\), B232 still applies. The only remaining rank is

\[
 \delta_1=d+2,\qquad \dim S=h_Z(1)=2d+3, \tag{2}
\]

where \(S\) is the \(H=A^2\) point span. Write \(A=O_Q(k)\).

## Standard polarization

Take \(k=1\), so \(H=O_Q(2)\). If every marked pair is orthogonal,
B231's isotropic-span contradiction applies. Otherwise choose
nonorthogonal marked representatives \(v,w\). With

\[
 V=\langle v,w\rangle\perp U, \tag{3}
\]

their tangent osculators

\[
 T_v=\langle v^2,vU\rangle,\qquad
 T_w=\langle w^2,wU\rangle \tag{4}
\]

are disjoint and have total dimension \(2d+2\). By (2),
\(S/(T_v\oplus T_w)\) has dimension one.

Let \(r=av+bw+u\) be a third marked representative. If \(u=0\),
isotropy of \(r\) and \(B(v,w)\ne0\) makes \([r]\) equal to \([v]\)
or \([w]\), impossible. Hence \(u\ne0\).

For every \(y\in U\) satisfying \(B(u,y)=0\), one has
\(y\in r^\perp\). Modulo \(T_v\oplus T_w\),

\[
 r\mathbin{\odot}y
 \equiv u\mathbin{\odot}y
 \quad\text{in }\operatorname{Sym}^2U. \tag{5}
\]

The space \(u^\perp\cap U\) has dimension \(d-1\), and
\(y\mapsto u\mathbin{\odot}y\) is injective. Thus the image of the
full tangent osculator \(T_r\) in the quotient has dimension at least
\(d-1\ge3\), contradicting the one-dimensional quotient allowed by
(2). Therefore \(k=1\) is impossible.

## Square polarization

Take \(k=2\), so \(H=O_Q(4)\). B215 separates two double
neighborhoods and one additional reduced point in exponent four. For
any distinct marked \(p,q,r\), their dual span therefore has dimension

\[
 2(d+1)+1=2d+3=\dim S, \tag{6}
\]

and equals \(S\). Every fourth marked point \(t\) is consequently not
separable from \(2p\sqcup2q\sqcup r\) by \(O_Q(4)\).

We now compute this failure exactly. If \(t\notin\overline{pr}\), choose
an ambient hyperplane through \(p,r\) but not \(t\), another through
\(p\) but not \(t\), and two through \(q\) but not \(t\). Their product
is a quartic vanishing on \(2p\sqcup2q\sqcup r\) but not at \(t\). If
\(t\in\overline{pr}\) but \(t\notin\overline{qr}\), use instead one
hyperplane through \(q,r\), one further through \(q\), and two through
\(p\), all avoiding \(t\).

Thus nonseparation is possible only when

\[
 t\in\overline{pr}\cap\overline{qr}. \tag{7}
\]

For four distinct points, (7) forces \(p,q,r,t\) to lie on one line.
Fixing \(p,q,r\) shows that all of \(Z\) lies on this line. Since it
contains at least three quadric points, the line lies on \(Q\). But

\[
 h_Z(1)\le h^0(\mathbf P^1,O(4))=5<2d+3, \tag{8}
\]

contradicting (2). Therefore \(k=2\) is impossible.

## Higher powers and the next rank

For \(k\ge3\), B232 already separates two doubles plus two reduced
points and gives \(2d+4\) independent conditions inside the
\((2d+3)\)-dimensional span. Hence no polarization works in (1), and

\[
 m=2\quad\Longrightarrow\quad s\ge2d+6. \tag{9}
\]

At \(s=2d+6\), the preceding obstruction excludes
\(\delta_1\le d+2\), while \(2\delta_1\le s\) gives
\(\delta_1\le d+3\). The first unexcluded rank is therefore

\[
 \delta_1=d+3,\qquad N=4d+8,\qquad
 h_Z(1)=2d+4=N/2,\qquad s-2\delta_1=0. \tag{10}
\]

The relation transport is an isomorphism and the code is diagonally
self-dual. If \(A=B^\ell\), \(\ell\ge3\), then \(A^2\) has exponent at
least six; B215 separates two doubles and three additional reduced
points, imposing \(2d+5\) conditions, so such powers are still
excluded at (10).

B233 constructs no configuration at the new threshold and no ODP,
Kuranishi, rational-detector, specified-pairing, or cycle data.
