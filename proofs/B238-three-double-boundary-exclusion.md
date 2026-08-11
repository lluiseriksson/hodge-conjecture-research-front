---
brick_id: B238
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=4, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, three-double restrictions, quartic separators, tangent contact loci, and plane conics are projective
dimension: dim X=d=2n; no m=2 candidate exists with slack s<=4d+5; at the first unexcluded value s=4d+6 one has N=6d+8 and h_Z(1)=3d+4=N/2
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction removes the exact three-double boundary and its odd neighbor
coefficient_field: Q for zeta and C for quadratic sections, self-adjoint maps, tangent jets, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to mixed double and reduced finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B221-B237, S081
claim: On (Q^d,a-b), no m=2 G144 candidate exists with slack s<=4d+5. At the first unexcluded value s=4d+6, necessarily delta_1=2d+3, N=6d+8, h_Z(1)=3d+4=N/2, and the degree-one relation transport is an isomorphism.
falsifier: a candidate in the excluded band, failure of quartics to separate three noncollinear doubles plus a fourth point, a standard-polarization tangent quotient of rank below d-2 outside the plane contact locus, or a different next rank
---

# B238 — The three-double boundary is still impossible

B237 excludes through slack \(4d+3\). Suppose

\[
 4d+4\le s\le4d+5. \tag{1}
\]

The only rank not already excluded is

\[
 \delta_1=2d+2,\qquad \dim S=h_Z(1)=3d+3. \tag{2}
\]

## Polarizations of exponent at least six

If \(A=O_Q(k)\), \(k\ge3\), then \(H=O_Q(2k)\) has exponent at least
six. B215 separates three double neighborhoods and one additional
reduced point at exponent six. Their target has dimension

\[
 3(d+1)+1=3d+4>\dim S, \tag{3}
\]

a contradiction.

## Square polarization

Let \(A=O_Q(2)\), so \(H=O_Q(4)\). If every marked triple were
collinear, all points would lie on one quadric line and have rank at
most five. Choose therefore a noncollinear triple \(p,q,r\). B235's
coordinate monomials separate their three double neighborhoods, so
their tangent osculators form a direct sum of dimension \(3d+3\) and
fill \(S\).

Let \(t\) be a fourth marked point. We construct a quartic vanishing on
\(2p\sqcup2q\sqcup2r\) but not at \(t\).

If \(t\) lies on none of the three pair lines, choose hyperplanes through
\(p,q\), through \(p,r\), and through \(q,r\), all avoiding \(t\).
Their product already vanishes twice at each base point; multiply by any
further hyperplane avoiding \(t\).

If, say, \(t\in\overline{pq}\), noncollinearity gives
\(t\notin\overline{pr}\cup\overline{qr}\). Choose one hyperplane through
\(p,r\), one through \(q,r\), one further through \(p\), and one further
through \(q\), all avoiding \(t\). The other pair-line cases are
symmetric.

Thus every fourth point is separated, contradicting \(t^4\in S\).

## Standard polarization

Take \(A=O_Q(1)\). Choose a nonorthogonal pair \(v,w\). If every
residual point lies in \(U=\langle v,w\rangle^\perp\), the quotient by
\(T_v\oplus T_w\) has dimension \(d+1\). Two nonorthogonal residual
tangents would have total dimension \(2d-2>d+1\); hence all residual
pairs are orthogonal, and B237's isotropic absorption contradiction
applies.

Otherwise choose a third point \(r\) meeting \(\langle v,w\rangle\).
Put

\[
 S_0=T_v+T_w+T_r,\qquad R=\langle v,w,r\rangle. \tag{4}
\]

B237 gives \(\dim S_0=3d+2\) and identifies its tangential contact locus
with \(Q\cap\mathbf P(R)\). Equation (2) leaves only one dimension in
\(S/S_0\).

For \(t\notin R\), consider the self-adjoint annihilator maps that vanish
on \(R\). The rank-one maps \(E_z(x)=B(z,x)z\), \(z\in R^\perp\), show
that the vectors \(E_z t\) span all of \(R^\perp\): the functional
\(z\mapsto B(z,t)\) is nonzero, and polarization with one fixed
nonzero-value \(z\) recovers its kernel as well. Restriction to
\(t^\perp\) kills at most the one-dimensional intersection
\(R^\perp\cap\mathbf Ct\). Therefore the image of \(T_t\) modulo
\(S_0\) has dimension at least

\[
 \dim R^\perp-1=(d-1)-1=d-2\ge2. \tag{5}
\]

It cannot fit in \(S/S_0\). Hence every marked point lies in \(R\), but
then its point span lies on one plane conic and has dimension at most
five, again contradicting (2).

All polarizations are impossible in (1). Therefore

\[
 m=2\quad\Longrightarrow\quad s\ge4d+6. \tag{6}
\]

At \(s=4d+6\), the budget and the exclusion give

\[
 \delta_1=2d+3,\qquad N=6d+8,\qquad
 h_Z(1)=3d+4=N/2,\qquad s-2\delta_1=0. \tag{7}
\]

The relation transport is an isomorphism. B238 constructs no threshold
configuration, ODP package, rational detector, specified pairing, or
cycle.
