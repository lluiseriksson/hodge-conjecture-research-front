---
brick_id: B239
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=4, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, mixed double-point spans, quartic and sextic separators, tangent contact loci, and orthogonal complements are projective
dimension: dim X=d=2n; no m=2 candidate exists with slack s<=4d+7; at the first unexcluded value s=4d+8 one has N=6d+10 and h_Z(1)=3d+5=N/2
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction removes one dimension beyond three doubles and its odd neighbor
coefficient_field: Q for zeta and C for sections, self-adjoint endomorphisms, tangent jets, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to mixed double, reduced, and first-order finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B221-B238, S081
claim: On (Q^d,a-b), no m=2 G144 candidate exists with slack s<=4d+7. At the first unexcluded value s=4d+8, necessarily delta_1=2d+4, N=6d+10, h_Z(1)=3d+5=N/2, and the degree-one relation transport is an isomorphism.
falsifier: a candidate in the excluded band, failure of the sextic mixed separator, an additional square-polarization tangent absorbed along the residual pair line, a standard Q^4 common eigenvector outside the plane conic and one extra point, or a different next rank
---

# B239 — One dimension beyond three doubles is impossible

B238 excludes through slack \(4d+5\). Suppose

\[
 4d+6\le s\le4d+7. \tag{1}
\]

The only rank not already excluded is

\[
 \delta_1=2d+3,\qquad \dim S=h_Z(1)=3d+4. \tag{2}
\]

Here \(S\) is the \(H=A^2\) point span and contains the full tangent
osculator at every marked point.

## Polarizations of exponent at least six

Let \(A=O_Q(k)\), \(k\ge3\), so \(H=O_Q(2k)\). If every marked triple
were collinear, all marked points would lie on one quadric line. Their
point span would then lie in the symmetric powers of its two-dimensional
isotropic vector span, while every full tangent osculator contains a
transverse vector. This is B231's isotropic absorption contradiction.
Choose therefore a noncollinear marked triple \(p,q,r\).
B215 makes

\[
 H^0(Q,O_Q(6))\longrightarrow
 H^0(2p\sqcup2q\sqcup2r\sqcup t,O_Q(6)) \tag{3}
\]

surjective for a fourth marked point \(t\). Its target has dimension
\(3d+4\), so its dual fills \(S\).

Let \(u\) be a fifth marked point. At most one of the three pair lines
\(\overline{pq},\overline{pr},\overline{qr}\) contains \(u\). Choose a
pair, say \(p,q\), whose line avoids \(u\). A hyperplane through \(p,q\)
and avoiding \(u\), followed by five hyperplanes respectively through
\(p,q,r,r,t\) and avoiding \(u\), gives a sextic

\[
 F\in I_{2p\sqcup2q\sqcup2r\sqcup t}(6),\qquad F(u)\ne0. \tag{4}
\]

Thus the fifth point adds a condition to the already full span, a
contradiction. For exponent \(2k>6\), multiply \(F\) and the sections in
(3) by sections nonzero at the five supports. Hence every \(k\ge3\) is
excluded.

## The square polarization

Let \(A=O_Q(2)\), so \(H=O_Q(4)\). Choose a noncollinear marked triple
\(p,q,r\). B235 separates their three double neighborhoods, and B238
separates any fourth point \(t\), so

\[
 S=\langle T_p,T_q,T_r,t^4\rangle. \tag{5}
\]

We first determine the marked base locus of
\(I_{2p\sqcup2q\sqcup2r\sqcup t}(4)\). Let \(u\) be distinct from the
four supports.

If \(u\notin\langle p,q,r\rangle\), square a hyperplane through
\(p,q,r\) and avoiding \(u\), then multiply by hyperplanes through \(t\)
and through no prescribed point, both avoiding \(u\). If \(u\) lies in
that plane but on no pair line, use hyperplanes through \(pq,pr,qr,t\),
all avoiding \(u\). Finally, if \(u\in\overline{pq}\) but
\(t\notin\overline{pq}\), use hyperplanes through \(pr,qr,pt,q\), again
all avoiding \(u\). The symmetric cases are identical. Therefore

\[
 u\text{ is a base point}\quad\Longrightarrow\quad
 t,u\in L \tag{6}
\]

for one pair line \(L\), say \(L=\overline{pq}\). Conversely, restriction
to \(L\) shows why this is the sole exceptional case: a quartic vanishing
twice at \(p,q\) and once at \(t\in L\) vanishes identically on \(L\).

It remains to test tangent absorption along \(L\). Choose hyperplanes
\(H_{pr},H_{qr}\) through the indicated pairs and avoiding \(u\), a
hyperplane \(H_L\supset L\) that is not tangent to \(Q\) at \(u\), and a
hyperplane \(H_0\) avoiding \(u\). Then

\[
 H_{pr}H_{qr}H_LH_0
 \in I_{2p\sqcup2q\sqcup2r\sqcup t}(4) \tag{7}
\]

has a nonzero intrinsic first jet at \(u\). It annihilates (5) but not
\(T_u\), contradicting \(T_u\subset S\). Thus the square polarization is
excluded.

## The standard polarization in dimensions at least six

Let \(A=O_Q(1)\). Choose a nonorthogonal pair \(v,w\), put
\(H_0=\langle v,w\rangle\), and \(U=H_0^\perp\).

If every residual point lies in \(U\), the quotient of \(S\) by
\(T_v\oplus T_w\) has dimension \(d+2\). For \(d\ge6\), two
nonorthogonal residual tangent images have disjoint sum of dimension
\(2d-2>d+2\). Hence all residual pairs would be orthogonal, and B237's
isotropic absorption contradiction applies.

Otherwise choose \(r\notin U\), and put

\[
 S_0=T_v+T_w+T_r,\qquad R=\langle v,w,r\rangle. \tag{8}
\]

B237 gives \(\dim S_0=3d+2\). Only two dimensions remain in \(S/S_0\),
whereas B238 shows that a tangent at any \(t\notin R\) contributes at
least \(d-2\ge4\). Hence every marked point lies on the plane conic
\(Q\cap\mathbf P(R)\), whose point rank is at most five. This contradicts
(2).

## The exceptional standard fourfold

It remains to take \(d=4\). In the residual-\(U\) branch the quotient has
dimension six. If it contains a nonorthogonal residual pair, their two
three-dimensional tangent spaces fill the quotient. The direct
symmetric-square decomposition used in B232, now on the quadric surface
\(Q(U)\), shows that their span contains no third distinct residual point.
If no such pair exists, B237's isotropic contradiction applies. Both
alternatives are impossible because there are many residual marked
points.

In the other branch retain (8), so \(\dim S_0=14\). If all marked points
lie in \(R\), their point rank is at most five. Otherwise choose
\(t\notin R\). Put \(W=R^\perp\), so \(\dim W=3\). Modulo scalars, the
annihilator of \(S_0\) is

\[
 L_0=\operatorname{Sym}^2W, \tag{9}
\]

viewed as the self-adjoint endomorphisms that vanish on \(R\). If
\(t\notin W\), contraction with \(B(-,t)|_W\ne0\) maps \(L_0\) onto
\(W\); imposing \(At=0\) has codimension three, but \(S/S_0\) has only
dimension two. Therefore tangent absorption forces \(t\in W\), and then

\[
 L=\{A\in L_0:At\in\mathbf Ct\} \tag{10}
\]

has dimension four.

The common eigenvectors of \(L\) are exactly \(R\) together with
\(\mathbf Ct\). This remains true whether \(W\) is nondegenerate or has
one-dimensional radical. In the nondegenerate case take a Witt basis
\(t,f,g\); (10) is spanned by
\(t^2,t f,t g,g^2\). In the degenerate case take a basis \(u,t,f\), with
\(u\) radical and \(B(t,f)=1\); (10) is spanned by
\(u^2,ut,t^2,tf\). Direct contraction shows that any common eigenvector
outside \(R=W^\perp\) is proportional to \(t\).

Thus the full tangential contact locus of \(S=S_0+T_t\) is contained in

\[
 (Q\cap\mathbf P(R))\cup\{t\}. \tag{11}
\]

Its \(O_Q(2)\) point rank is at most \(5+1=6\), not the required
\(3d+4=16\). This excludes the last case.

All polarizations are impossible in (1). Therefore

\[
 m=2\quad\Longrightarrow\quad s\ge4d+8. \tag{12}
\]

At \(s=4d+8\), the obstruction and the budget give

\[
 \delta_1=2d+4,\qquad N=6d+10,\qquad
 h_Z(1)=3d+5=N/2,\qquad s-2\delta_1=0. \tag{13}
\]

The relation transport is an isomorphism. B239 constructs no threshold
configuration, ODP package, rational detector, specified pairing, or
algebraic cycle.
