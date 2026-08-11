---
brick_id: B240
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=4, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, three-double and three-point spans, quartic and sextic first-jet separators, tangent contact loci, and quadric linear sections are projective
dimension: dim X=d=2n; no m=2 candidate exists with slack s<=4d+9; at the first unexcluded value s=4d+10 one has N=6d+12 and h_Z(1)=3d+6=N/2
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction removes two dimensions beyond three doubles and its odd neighbor
coefficient_field: Q for zeta and C for sections, self-adjoint endomorphisms, tangent jets, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to mixed double, reduced, and first-order finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B221-B239, S081
claim: On (Q^d,a-b), no m=2 G144 candidate exists with slack s<=4d+9. At the first unexcluded value s=4d+10, necessarily delta_1=2d+5, N=6d+12, h_Z(1)=3d+6=N/2, and the degree-one relation transport is an isomorphism.
falsifier: a candidate in the excluded band, failure of the sextic sixth-point separator, failure of the quartic exhaustive first-jet separator, a standard Q^4 contact point outside the rank-nine quadric linear section, or a different next rank
---

# B240 — Two dimensions beyond three doubles are impossible

B239 excludes through slack \(4d+7\). Suppose

\[
 4d+8\le s\le4d+9. \tag{1}
\]

The only rank not already excluded is

\[
 \delta_1=2d+4,\qquad \dim S=h_Z(1)=3d+5. \tag{2}
\]

As before, \(S\) is the \(H=A^2\) point span and contains the full
tangent osculator at every marked point.

## Polarizations of exponent at least six

Let \(A=O_Q(k)\), \(k\ge3\). B231's isotropic absorption argument forces
a noncollinear marked triple \(p,q,r\). At exponent six, B215 first
separates

\[
 2p\sqcup2q\sqcup2r\sqcup t, \tag{3}
\]

and B239's sextic separator shows that a fifth point \(u\) adds one more
condition. Their mixed dual span therefore has dimension \(3d+5\) and
equals \(S\).

Let \(x\) be a sixth marked point. At most one of the pair lines of
\(p,q,r\) contains \(x\). Choose two of the other pair lines; their two
hyperplane factors use four of the six required double-point
multiplicities. Four further hyperplanes through the two remaining
double-point supports and through \(t,u\), respectively, may all avoid
\(x\). Their product is a sextic

\[
 F\in I_{2p\sqcup2q\sqcup2r\sqcup t\sqcup u}(6),
 \qquad F(x)\ne0. \tag{4}
\]

This contradicts the fullness of \(S\). Higher exponents follow by
multiplying by a section nonzero at the six supports. Thus every
\(k\ge3\) is excluded.

## The square polarization

Let \(A=O_Q(2)\), so \(H=O_Q(4)\), and choose a noncollinear marked triple
\(p,q,r\). If every other marked point lay on the three pair lines, the
point rank would be at most \(3h^0(\mathbf P^1,O(4))=15<3d+5\).
Choose a fourth marked point \(t\) outside their union.

B235 separates the three double neighborhoods. B239 shows that every
fifth marked point \(u\) adds a value condition, because a base point of
\(I_{2p\sqcup2q\sqcup2r\sqcup t}(4)\) would force \(t\) onto a pair
line. Hence

\[
 S=\langle T_p,T_q,T_r,t^4,u^4\rangle. \tag{5}
\]

Let \(x\) be any sixth marked point. We construct a quartic in the ideal
of the mixed scheme in (5) with nonzero value or first jet at \(x\).

If \(x\) lies on none of the three pair lines, take hyperplanes through
\(pq,pr,qr\). They all avoid \(x\). Complete the product by a hyperplane
through \(t,u\). If \(x\notin\overline{tu}\), this gives a nonzero value
at \(x\). If \(x\in\overline{tu}\), choose that last hyperplane not
tangent to \(Q\) at \(x\); the product has a nonzero intrinsic first jet.

Suppose instead that \(x\in L=\overline{pq}\). Hyperplanes through
\(pr\) and \(qr\) avoid \(x\). If \(u\notin L\), complete them by
hyperplanes through \(pt\) and \(qu\); these also avoid \(x\) because
\(t,u\notin L\). If \(u\in L\), use one hyperplane containing \(L\) but
not tangent to \(Q\) at \(x\), and one hyperplane through \(t\) and
avoiding \(x\). The product has exactly one transverse vanishing factor
at \(x\). The other pair-line cases are symmetric.

In every case a section annihilates (5) but not \(T_x\), contradicting
tangent absorption. Thus the square polarization is excluded.

## The standard polarization in dimensions at least six

Let \(A=O_Q(1)\), choose a nonorthogonal marked pair \(v,w\), and put
\(U=\langle v,w\rangle^\perp\).

If every residual point lies in \(U\), the quotient by
\(T_v\oplus T_w\) has dimension \(d+3\). For \(d\ge6\), two
nonorthogonal residual tangent images have disjoint sum of dimension
\(2d-2>d+3\). The residual points would all be pairwise orthogonal,
contradicting B237's isotropic absorption argument.

Otherwise choose \(r\notin U\) and put

\[
 S_0=T_v+T_w+T_r,\qquad R=\langle v,w,r\rangle. \tag{6}
\]

B237 gives \(\dim S_0=3d+2\). Only three dimensions remain, whereas a
tangent outside \(R\) contributes at least \(d-2\ge4\). Thus every
marked point lies on \(Q\cap\mathbf P(R)\), of point rank at most five,
contrary to (2).

## The exceptional standard fourfold

Take \(d=4\). First suppose every residual point lies in
\(U=\langle v,w\rangle^\perp\). The quotient has dimension seven. A
nonorthogonal residual pair contributes two disjoint three-dimensional
tangents. A third residual tangent can fit in the remaining dimension
only at an isotropic point of their orthogonal complement. After adding
it, the annihilator on the quadric surface \(Q(U)\) is spanned, in a
hyperbolic basis \(a,b\), by \(a^2\) and \(ab\). Its common isotropic
eigenvectors are only the two initial points and \(a\). No fourth
distinct residual tangent is absorbed. The all-orthogonal alternative
again contradicts B237.

Now retain (6), so \(\dim S_0=14\), and put \(W=R^\perp\),
\(\dim W=3\). Modulo scalars,

\[
 L_0=\operatorname{Sym}^2W \tag{7}
\]

is the annihilator of \(S_0\).

Choose a marked point \(t\notin R\). If \(t\notin W\), contraction with
\(B(-,t)|_W\) has rank three. Its kernel is
\(\operatorname{Sym}^2K\), where

\[
 K=W\cap t^\perp,\qquad \dim K=2. \tag{8}
\]

The tangent at \(t\) fills the three available quotient dimensions.
The common eigenvector locus of \(\operatorname{Sym}^2K\) is exactly
\(K^\perp=R+\mathbf Ct\): outside \(K^\perp\), a rank-one map
\(E_z\), \(z\in K\), moves the vector to a nonproportional line. Hence
all marked points lie on the quadric linear section
\(Q\cap\mathbf P(K^\perp)\), whose \(O_Q(2)\) point rank is at most

\[
 h^0(\mathbf P^3,O(2))-1=9<17. \tag{9}
\]

Indeed the restricted quadratic equation is nonzero: a four-dimensional
totally isotropic subspace cannot occur in the six-dimensional quadratic
space.

It remains to take \(t\in W\). Its tangent contributes two dimensions,
leaving one. The four-dimensional annihilator is the space of
self-adjoint maps on \(W\) for which \(t\) is an eigenvector. If \(W\)
is nondegenerate, use a Witt basis \(t,f,g\); this space is spanned by

\[
 t^2,\ tf,\ tg,\ g^2. \tag{10}
\]

If \(W\) has radical \(\mathbf C\rho\), use
\(\rho,t,f\); it is spanned by

\[
 \rho^2,\ \rho t,\ t^2,\ tf. \tag{11}
\]

If all marked points lay in \(R\cup\{t\}\), their point rank would be at
most six. Choose another marked point \(u\) outside that contact locus.
Its tangent can impose only one further condition.

In the nondegenerate basis (10), evaluation at \(u\notin W\) has rank
one only when

\[
 B(t,u)=B(g,u)=0. \tag{12}
\]

Then \(K=\langle t,g\rangle\), \(u\in K^\perp\), and the kernel is
\(\operatorname{Sym}^2K=\langle t^2,tg,g^2\rangle\). If instead
\(u\in W\) is isotropic and distinct from \(t\), then \(B(t,u)\ne0\)
and the eigenvector condition has codimension at least two.

In the degenerate basis (11), evaluation at \(u\notin W\) has rank one
only when

\[
 B(\rho,u)=B(t,u)=0. \tag{13}
\]

Then \(K=\langle\rho,t\rangle\) and the kernel is
\(\operatorname{Sym}^2K\). An isotropic \(u\in W\) on the same ruling
lies in \(R+\mathbf Ct=K^\perp\) and removes only \(tf\); the other
ruling imposes at least two conditions. Thus every surviving case again
has annihilator \(\operatorname{Sym}^2K\), and (9) applies.

Every standard-fourfold branch is impossible.

All polarizations are excluded in (1), so

\[
 m=2\quad\Longrightarrow\quad s\ge4d+10. \tag{14}
\]

At \(s=4d+10\), the obstruction and the budget give

\[
 \delta_1=2d+5,\qquad N=6d+12,\qquad
 h_Z(1)=3d+6=N/2,\qquad s-2\delta_1=0. \tag{15}
\]

The relation transport is an isomorphism. B240 constructs no threshold
configuration, ODP package, rational detector, specified pairing, or
algebraic cycle.
