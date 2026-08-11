---
brick_id: B234
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=4, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and all marked points are smooth and reduced; central ODP and incidence conditions remain inherited hypotheses
projectivity: complete quadric embeddings, tangent osculators, mixed double-point schemes, quartic separator products, and collinearity loci are projective
dimension: dim X=d=2n; every m=2 candidate has slack s>=2d+8; at the first unexcluded value N=4d+10 and h_Z(1)=2d+5=N/2
codimension: the primitive codimension-n ruling difference gives a valid universal input; the obstruction removes two more degree-two slack layers
coefficient_field: Q for zeta and C for sections, symmetric tensors, tangent jets, ranks, and incidence geometry
cohomology_theory: rational singular cohomology and coherent restrictions to double and reduced finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B221-B233, S081
claim: On (Q^d,a-b), no m=2 G144 candidate exists with slack s<=2d+7. At the first unexcluded value s=2d+8, necessarily delta_1=d+4, N=4d+10, h_Z(1)=2d+5=N/2, and the degree-one relation transport is an isomorphism. B215 excludes powers A=B^ell with ell>=4 at the new threshold but no longer excludes cubes.
falsifier: a candidate in the excluded band, a third standard-quadric tangent osculator of quotient rank at most two, a square-polarization marked set escaping the line-plus-one-point confinement, or a different next-threshold rank
---

# B234 — Two extra tangent-span dimensions are still insufficient

Fix \((Q^d,a-b)\), \(d=2n\ge4\), and suppose

\[
 2d+6\le s\le2d+7. \tag{1}
\]

B233 excludes every rank with \(\delta_1\le d+2\). The sole remaining
rank is

\[
 \delta_1=d+3,\qquad \dim S=h_Z(1)=2d+4. \tag{2}
\]

Write \(A=O_Q(k)\).

## Standard polarization

For \(k=1\), choose a nonorthogonal marked pair \(v,w\), unless all
pairs are orthogonal and B231 already gives a contradiction. As in
B233, write \(V=\langle v,w\rangle\perp U\). The quotient

\[
 S/(T_v\oplus T_w) \tag{3}
\]

has dimension two. A third point \(r=av+bw+u\) has \(u\ne0\), and its
tangent osculator maps onto a subspace containing

\[
 \{u\mathbin{\odot}y:B(u,y)=0,\ y\in U\}, \tag{4}
\]

of dimension \(d-1\ge3\). This contradicts (3).

## Square polarization

Let \(k=2\), so \(H=O_Q(4)\). Choose four distinct marked points
\(p,q,r,s\).

B233's quartic separator proves that the span of
\(2p\sqcup2q\sqcup r\sqcup s\) fails to have its expected dimension
only if \(p,q,r,s\) are collinear. If every four-subset were collinear,
then \(Z\) itself would be collinear and have rank at most five, contrary
to (2). Hence choose \(p,q,r,s\) not all collinear. Their mixed dual
span has dimension

\[
 2(d+1)+2=2d+4=\dim S, \tag{5}
\]

so it equals \(S\).

Let \(t\) be any fifth marked point. It cannot be separated from this
mixed scheme. Pair \(r\) with a hyperplane through \(p\) and \(s\) with
one through \(q\), completing the product by one further hyperplane
through each of \(p,q\), all avoiding \(t\). Swapping \(r,s\) gives the
necessary conditions

\[
 t\in(\overline{pr}\cup\overline{qs})
 \cap(\overline{ps}\cup\overline{qr}). \tag{6}
\]

The four intersections in (6) are respectively based at
\(p,r,s,q\). Since \(t\) is distinct from the base points, one pair of
the corresponding lines must coincide. Thus \(t\) lies on a line
containing three of \(p,q,r,s\).

Because the four base points are not all collinear, at most one of
their four triples is collinear: two collinear triples share two points
and would determine the same line containing all four. Therefore the
existence of any fifth point forces exactly one collinear base triple,
and every remaining marked point lies on its line. Hence

\[
 Z\subset L\cup\{x\} \tag{7}
\]

for one line \(L\subset Q\) and at most one point \(x\notin L\). It
follows that

\[
 h_Z(1)\le h^0(L,O_L(4))+1=6<2d+4, \tag{8}
\]

contradicting (2).

## Higher powers and next rank

For \(k\ge3\), B233's mixed interpolation already contradicts (2).
Thus

\[
 m=2\quad\Longrightarrow\quad s\ge2d+8. \tag{9}
\]

At \(s=2d+8\), the preceding obstruction excludes
\(\delta_1\le d+3\), and the budget gives
\(\delta_1\le d+4\). The first unexcluded rank is

\[
 \delta_1=d+4,\qquad N=4d+10,\qquad
 h_Z(1)=2d+5=N/2,\qquad s-2\delta_1=0. \tag{10}
\]

The relation transport is an isomorphism. If \(A=B^\ell\) with
\(\ell\ge4\), then \(A^2\) has exponent at least eight. B215 separates
two doubles and four reduced points from exponent seven, imposing
\(2d+6\) conditions and excluding these powers. For the cube
\(\ell=3\), exponent six separates only two doubles plus three points,
which impose exactly \(2d+5\) conditions and merely fill the span.
Therefore cube polarizations must re-enter G158 rather than being
silently discarded.

B234 proves only the displayed exclusion band. It constructs no marked
configuration, ODP package, rational detector, specified pairing, or
cycle.
