---
brick_id: B243
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=4, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2; Q^8 is the universal-quantifier falsifier
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, mixed double-point restrictions, residual first-jet systems, tangent contact loci, and quadric linear sections are projective
dimension: dim X=d=2n; at the G166 rank s=4d+12 and h_Z(1)=3d+7, k>=4 is impossible in every d, k=3 is impossible for d>=6, k=2 is impossible in every d, and k=1 is impossible for d>=8
codimension: the primitive codimension-n ruling difference supplies a valid universal input; Q^8 excludes the exact G166 rank and its adjacent odd layer
coefficient_field: Q for zeta and C for sections, tangent jets, spans, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to mixed double and reduced finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B221-B242, G166, S081
claim: No G166 candidate exists on (Q^8,a-b) for any very ample A=O_Q(k). Hence the universal G166 claim and the adjacent odd layer s=4d+13 are NO-GO. The next balanced universal signature is s=4d+14, delta_1=2d+7, N=6d+16, and h_Z(1)=3d+8=N/2.
falsifier: a Q^8 G166 candidate, failure of four-double interpolation for k>=4, a sextic four-double dependency off the triangle, residual quartic jet rank below two, survival of the standard quotient inequalities in d=8, or a different next balanced rank
---

# B243 — Quadrics exclude G166

At G166 the balanced signature is

\[
 s=4d+12,\qquad \dim S=h_Z(1)=3d+7. \tag{1}
\]

Here \(S\) is the \(H=A^2\) point span and contains the full tangent
osculator at every marked point. We test every very ample
\(A=O_Q(k)\).

## Powers \(k\ge4\)

B215 separates four prescribed double neighborhoods in exponent seven.
If \(k\ge4\), multiply those sections by a section of
\(O_Q(2k-7)\) that is nonzero at the four supports. The resulting dual
span has dimension

\[
 4(d+1)>3d+7 \qquad(d\ge4), \tag{2}
\]

so it cannot lie in \(S\).

## The sextic power

Let \(k=3\) and \(d\ge6\). Choose a noncollinear marked triple
\(p,q,r\), as forced by B231, and let \(\Delta\) be the union of its
three pair lines. If every marked point lay in \(\Delta\), then

\[
 h_Z(1)\le3h^0(\mathbf P^1,O(6))=21<3d+7. \tag{3}
\]

Choose \(t\notin\Delta\). B215 makes
\(2p\sqcup2q\sqcup2r\sqcup t\) independent in degree six. Choose
hyperplanes through \(pq,pr,qr\), all avoiding \(t\), and multiply their
product by two further hyperplanes avoiding \(t\). Multiplication by
this unit identifies the first jets at \(t\) of hyperplanes through
\(t\) with the full \(d\)-dimensional cotangent space. Hence the four
double neighborhoods are independent in degree six and have span
\(4d+4\), contradicting (1).

## The square power

Let \(k=2\). Choose noncollinear \(p,q,r\). Since

\[
 3h^0(\mathbf P^1,O(4))=15<3d+7, \tag{4}
\]

there is a marked \(t\notin\Delta\). B242's residual-base argument,
whose two-line bound is \(13<3d+7\), then chooses \(u,x\) so that

\[
 S_0=\langle T_p,T_q,T_r,t^4,u^4,x^4\rangle,
 \qquad \dim S_0=3d+6. \tag{5}
\]

Let \(y\) be another marked point and put

\[
 J=I_{2p\sqcup2q\sqcup2r\sqcup t\sqcup u\sqcup x}(4). \tag{6}
\]

If \(y\notin\Delta\), choose hyperplanes through \(pq,pr,qr\), all
avoiding \(y\), and denote their product by \(P\). For every linear form
\(\ell\) vanishing on \(W=\langle t,u,x\rangle\), the quartic
\(P\ell\) belongs to \(J\), while \(P(y)\ne0\).

If \(y\in\overline{pq}\), instead take

\[
 P=H_{pr}H_{qr}H_{pt},\qquad
 \ell\in I_{\langle q,u,x\rangle}(1). \tag{7}
\]

All three fixed factors avoid \(y\), because \(t\notin\Delta\). The
other pair-line cases are symmetric.

In either case the vector span defining \(W\) has dimension at most
three, so

\[
 \dim I_W(1)\ge d-1. \tag{8}
\]

The kernel of
\(H^0(Q,O_Q(1))\to H^0(2y,O_Q(1))\) is the one-dimensional tangent
hyperplane. Therefore the restrictions of the family \(P I_W(1)\) to
\(2y\) have rank at least

\[
 (d-1)-1=d-2\ge2. \tag{9}
\]

By duality, \(T_y\) contributes at least two new dimensions beyond
\(S_0\), whereas (1) leaves only one. Thus \(k=2\) is impossible in
every even dimension.

## The standard power

Let \(k=1\) and \(d\ge8\). B231's isotropic-absorption argument supplies
a nonorthogonal marked pair \(v,w\). Put
\(U=\langle v,w\rangle^\perp\). If all residual points lie in
\(U\), the quotient by \(T_v\oplus T_w\) has dimension \(d+5\). Two
nonorthogonal residual tangent images have disjoint sum of dimension

\[
 2d-2>d+5. \tag{10}
\]

Thus all residual pairs would be orthogonal, and B237's isotropic
absorption contradiction applies.

Otherwise choose \(r\notin U\), put
\(S_0=T_v+T_w+T_r\), and \(R=\langle v,w,r\rangle\). B237 gives
\(\dim S_0=3d+2\). Only five dimensions remain, while B238 shows that a
tangent outside \(R\) contributes at least

\[
 d-2\ge6. \tag{11}
\]

Every marked point would therefore lie on the plane conic
\(Q\cap\mathbf P(R)\), of \(O_Q(2)\) point rank at most five, contrary
to (1).

## Universal conclusion

On \(Q^8\), (2), the sextic argument, (9), and the standard argument
exclude every \(k\ge1\). Thus \(Q^8\) falsifies the universal G166
claim. The odd layer \(s=4d+13\) has the same integral rank budget;
lower ranks were already excluded by B242. The next balanced signature
is

\[
 s=4d+14,\qquad \delta_1=2d+7,\qquad
 N=6d+16,\qquad h_Z(1)=3d+8=N/2. \tag{12}
\]

B243 excludes only this sufficient specialization. It constructs no
ODP package, rational detector, specified pairing, algebraic cycle,
proof, or disproof of HC.
