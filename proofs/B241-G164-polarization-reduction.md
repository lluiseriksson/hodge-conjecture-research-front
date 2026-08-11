---
brick_id: B241
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=4, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, three-double and four-point spans, sextic first-jet separators, tangent contact loci, and orthogonal decompositions are projective
dimension: dim X=d=2n; at the G164 rank s=4d+10 and h_Z(1)=3d+6, every k>=3 is impossible and the standard k=1 polarization is impossible for d>=6
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the reduction leaves only k=2 in dimensions d>=6 and k in {1,2} when d=4
coefficient_field: Q for zeta and C for sections, self-adjoint endomorphisms, tangent jets, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to mixed double, reduced, and first-order finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B221-B240, G164, S081
claim: Any G164 candidate on (Q^d,a-b) must use A=O_Q(2) when d>=6. When d=4, only A=O_Q(1) or O_Q(2) can remain. In particular, no polarization O_Q(k), k>=3, survives in any dimension, and the standard polarization does not survive in dimensions d>=6.
falsifier: a G164 candidate with k>=3, a standard candidate in d>=6, failure of the sextic seventh-point first-jet separator, failure of the d=6 residual equality calculation, or an additional common eigenvector in the d=6 standard contact locus
---

# B241 — G164 reduces to the square polarization and \(Q^4\)

At G164 the balanced signature is

\[
 m=2,\qquad s=4d+10,\qquad
 \delta_1=2d+5,\qquad \dim S=3d+6. \tag{1}
\]

B241 does not raise this floor. It removes the powered and
higher-dimensional standard polarizations from the surviving audit.

## Exponent at least six

Let \(A=O_Q(k)\), \(k\ge3\). Choose a noncollinear marked triple
\(p,q,r\). B215 together with B239-B240 shows that

\[
 2p\sqcup2q\sqcup2r\sqcup t\sqcup u\sqcup x \tag{2}
\]

imposes \(3d+6\) independent conditions in exponent six. Its dual span
therefore equals \(S\).

Let \(y\) be a seventh marked point. If \(y\) lies on none of the three
pair lines of \(p,q,r\), take hyperplanes through \(pq,pr,qr\) and three
further hyperplanes through \(t,u,x\), all avoiding \(y\). Their product
is a sextic nonzero at \(y\).

Suppose \(y\in L=\overline{pq}\). Hyperplanes through \(pr\) and \(qr\)
avoid \(y\). If at least one of \(t,u,x\), say \(t\), lies outside \(L\),
use a third hyperplane through \(p,t\), which also avoids \(y\), followed
by hyperplanes through \(q,u,x\). This again gives six factors and a
nonzero value at \(y\).

If \(t,u,x\in L\), choose a hyperplane \(H_L\supset L\) that is not
tangent to \(Q\) at \(y\), then multiply by hyperplanes through
\(p,q,r,r\) and by one further hyperplane avoiding \(y\). The product
vanishes on (2) and has a nonzero intrinsic first jet at \(y\).

Thus no seventh marked tangent is absorbed at exponent six. Multiplying
by a section nonzero at all supports proves the same for every
\(2k>6\). Hence

\[
 k\ge3\quad\Longrightarrow\quad\text{no G164 candidate}. \tag{3}
\]

## The standard polarization in dimensions at least eight

Take \(A=O_Q(1)\) and choose a nonorthogonal pair \(v,w\). Put
\(U=\langle v,w\rangle^\perp\).

If every residual point lies in \(U\), the quotient of \(S\) by
\(T_v\oplus T_w\) has dimension \(d+4\). For \(d\ge8\),

\[
 2d-2>d+4, \tag{4}
\]

so two nonorthogonal residual tangents cannot fit. Pairwise orthogonality
then gives B237's isotropic absorption contradiction.

Otherwise choose \(r\notin U\) and put

\[
 S_0=T_v+T_w+T_r,\qquad R=\langle v,w,r\rangle. \tag{5}
\]

Only four dimensions remain after \(\dim S_0=3d+2\). A tangent outside
\(R\) contributes at least \(d-2>4\), so all marked points lie on the
plane conic \(Q\cap\mathbf P(R)\), of point rank at most five. This is
impossible.

## The standard sixfold

Let \(d=6\). In the residual-\(U\) branch the quotient has dimension ten.
Two nonorthogonal residual tangent images are disjoint and have total
dimension

\[
 2(d-1)=10. \tag{6}
\]

They fill the quotient. The direct symmetric-square decomposition of
B232, applied to the four-dimensional quadric \(Q(U)\), shows that their
span contains no third distinct residual point. The all-orthogonal
alternative is again impossible.

In the other branch retain (5). Now \(W=R^\perp\) has dimension five and
only four dimensions remain in \(S/S_0\). A point \(t\notin R\) but
outside \(W\) contributes five quotient dimensions and cannot occur.
Thus tangent absorption forces \(t\in W\); it contributes exactly four
dimensions and fills \(S\).

Modulo scalars, the annihilator of \(S\) consists of the self-adjoint
endomorphisms of \(W\) for which \(t\) is an eigenvector. Their common
eigenvectors outside \(R=W^\perp\) are exactly \(\mathbf Ct\). Indeed,
rank-one self-adjoint maps inside \(t^\perp\cap W\), together with one
map acting nontrivially on \(t\), move every other vector to a
nonproportional line. The same argument holds when \(W\) has
one-dimensional radical; that radical lies in \(R\).

Consequently every marked point lies on

\[
 (Q\cap\mathbf P(R))\cup\{t\}, \tag{7}
\]

whose \(O_Q(2)\) point rank is at most six, not \(3d+6=24\). The standard
sixfold is impossible.

Combining the three cases gives

\[
 d\ge6\Longrightarrow A=O_Q(2),\qquad
 d=4\Longrightarrow A\in\{O_Q(1),O_Q(2)\}. \tag{8}
\]

B241 is a necessary polarization reduction only. It constructs no G164
configuration, ODP package, rational detector, specified pairing, or
algebraic cycle, and it does not prove or disprove HC.
