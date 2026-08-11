---
brick_id: B242
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=4, primitive ruling difference zeta=a-b, A=O_Q(2), and H=A^2=O_Q(4)
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: the complete quartic embedding, three-double and three-point spans, residual base lines, and quartic first-jet separators are projective
dimension: dim X=d=2n; at the G164 rank s=4d+10 and h_Z(1)=3d+6, the square polarization is impossible in every even dimension d>=4; Q^6 then falsifies the universal G164 claim
codimension: the primitive codimension-n ruling difference supplies a valid universal input; together with B241, the square exclusion closes G164 and its adjacent odd layer
coefficient_field: Q for zeta and C for quartic sections, tangent jets, spans, and incidence geometry
cohomology_theory: rational singular cohomology and coherent restriction to mixed double, reduced, and first-order finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B221-B241, G164-G165, S081
claim: No G164 candidate on (Q^d,a-b) can use A=O_Q(2), for any even d>=4. Since B241 leaves only A=O_Q(2) on Q^6, G164 and the adjacent odd layer are NO-GO. The next balanced universal signature is s=4d+12, delta_1=2d+6, N=6d+14, and h_Z(1)=3d+7=N/2.
falsifier: a square-polarized G164 candidate, a residual quartic base point outside the two-line locus, failure of the two-line point-rank bound, a seventh marked tangent not separated by the four-hyperplane construction, or survival of G164 on Q^6 through another polarization
---

# B242 — The square polarization does not survive G164

At G164,

\[
 s=4d+10,\qquad \dim S=3d+6. \tag{1}
\]

Take \(A=O_Q(2)\), so \(H=O_Q(4)\). Choose a noncollinear marked triple
\(p,q,r\). Let \(\Delta\) be the union of their three pair lines. If
every other marked point lay in \(\Delta\), then

\[
 h_Z(1)\le3h^0(\mathbf P^1,O(4))=15<3d+6. \tag{2}
\]

Choose a fourth point \(t\notin\Delta\), and then a fifth point \(u\).
B239-B240 show that

\[
 S_0=\langle T_p,T_q,T_r,t^4,u^4\rangle \tag{3}
\]

has dimension \(3d+5\).

## The residual value base locus has small rank

Put

\[
 J=I_{2p\sqcup2q\sqcup2r\sqcup t\sqcup u}(4). \tag{4}
\]

B240's explicit value separators give the following exhaustive
containment. If a point \(x\) lies off \(\Delta\) and off
\(\overline{tu}\), the three pair-line factors and one \(tu\)-factor
separate it. If \(x\in\overline{pq}\) and
\(u\notin\overline{pq}\), the factors through
\(pr,qr,pt,qu\) separate it. The symmetric statements hold on the other
pair lines. Therefore

\[
 \operatorname{Bs}(J)\setminus\{p,q,r,t,u\}
 \subset
 \overline{tu}\ \cup\
 \bigcup_{\substack{L\subset\Delta\\u\in L}}L. \tag{5}
\]

Because \(u\) lies on at most one pair line, the right side contains at
most two lines. If every remaining marked point were a base point, then
all of \(Z\) would lie on those lines together with \(p,q,r\), and

\[
 h_Z(1)\le2\cdot5+3=13<3d+6. \tag{6}
\]

Choose therefore a sixth marked point \(x\notin\operatorname{Bs}(J)\).
It adds one value condition to (3), so

\[
 S=\langle T_p,T_q,T_r,t^4,u^4,x^4\rangle. \tag{7}
\]

## Every seventh tangent is separated

Let \(y\) be a seventh marked point. If \(y\notin\Delta\), choose
hyperplanes through \(pq,pr,qr\), all avoiding \(y\), and one hyperplane
through \(t,u,x\). If \(y\) does not lie in
\(\langle t,u,x\rangle\), choose the last hyperplane avoiding \(y\); the
product is nonzero at \(y\). If \(y\) lies in that span, choose the last
hyperplane not tangent to \(Q\) at \(y\); the product has one nonzero
intrinsic first jet there.

Suppose \(y\in L=\overline{pq}\). Choose hyperplanes through \(pr\) and
\(qr\), both avoiding \(y\), and a hyperplane through \(pt\), also
avoiding \(y\) because \(t\notin\Delta\). Complete the product by a
hyperplane through \(q,u,x\). If \(y\notin\langle q,u,x\rangle\), this
last factor avoids \(y\); otherwise choose it not tangent to \(Q\) at
\(y\). The other pair-line cases are symmetric.

In all cases a quartic lies in

\[
 I_{2p\sqcup2q\sqcup2r\sqcup t\sqcup u\sqcup x}(4) \tag{8}
\]

and has nonzero value or first jet at \(y\). It annihilates (7) but not
\(T_y\), contradicting tangent absorption.

Thus

\[
 A=O_Q(2)\quad\Longrightarrow\quad\text{no G164 candidate}. \tag{9}
\]

On \(Q^6\), B241 has already excluded the standard and every
higher polarization. Therefore B242 removes its only remaining option
and falsifies G164's universal claim. The adjacent odd layer \(4d+11\)
has the same integral rank budget. Hence the next balanced universal
signature is

\[
 s=4d+12,\qquad \delta_1=2d+6,\qquad
 N=6d+14,\qquad h_Z(1)=3d+7=N/2. \tag{10}
\]

This is a gate transition, not a theorem that the standard \(Q^4\)
configuration is impossible. B242 constructs no ODP package, rational
detector, specified pairing, or algebraic cycle.
