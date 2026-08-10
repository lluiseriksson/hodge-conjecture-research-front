---
brick_id: B032
status: PROVED
base_field: C
variety: X = P^2 x P^2, the diagonal W = Delta_X, A = O_X(2,2), and a general divisor Y in |I_W tensor A|
smoothness: X and W are smooth; Y is smooth away from W and has exactly seven ordinary double points on W
projectivity: X, W, and Y are projective
dimension: dim_C X = 4, dim_C Y = 3, and dim_C W = 2
codimension: Y has codimension 1 in X; W has middle codimension 2 in X
coefficient_field: C for coherent evaluation and Chern-class calculations; Q for homology and Hodge classes
cohomology_theory: coherent cohomology, Chern classes, singular homology and cohomology, vanishing cycles, Lefschetz decomposition, and limit mixed Hodge structures
hodge_type: the unique rational nodal relation has type (0,0) after Tate twist and its ambient image is the nonzero primitive projection of the diagonal class
cycle_class_map: CH^2(P^2 x P^2)_Q -> H^4(P^2 x P^2,Q(2))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: Thomas Theorem 4.2 (S019), Saito Proposition 1 and Theorem 1 (S022), B010, B026, and the Euler/Koszul/Lefschetz calculations below
claim: A (2,2) divisor in P^2 x P^2 containing the diagonal can have seven nodes independent for the defining system, adjoint defect one, and a rank-one canonical extra-to-primitive map with nonzero image.
falsifier: failure of the normal-jet map to be surjective, a nonreduced zero scheme of a general section of Omega^1_P2(4), nonsurjectivity of the seven-point O(4) evaluation, adjoint defect other than one, or zero primitive projection of the diagonal
---

# B032 - A positive ambient-rank nodal witness

Let

\[
 X=\mathbf P^2\times\mathbf P^2,\qquad
 W=\Delta_{\mathbf P^2}\subset X,\qquad
 A=\mathcal O_X(2,2).
\]

This brick is a special algebraically anchored witness. Its purpose is to
test compatibility of the three independent ranks in G013, not to select a
cycle from an unknown Hodge class.

## Seven isolated nodes

The conormal bundle of the diagonal is
\(N^*_{W/X}\simeq\Omega^1_{\mathbf P^2}\), and
\(A|_W\simeq\mathcal O_{\mathbf P^2}(4)\). The first normal derivative of a
section in \(H^0(X,I_W\otimes A)\) is therefore a section of

\[
 E=\Omega^1_{\mathbf P^2}(4).
\]

The normal-jet map is surjective in this bidegree. Indeed,

\[
 H^0(X,A)=\operatorname{Sym}^2V^*\otimes\operatorname{Sym}^2V^*
 \longrightarrow \operatorname{Sym}^4V^*=H^0(W,\mathcal O_W(4))
\]

is multiplication and is surjective. Its kernel has dimension
\(36-15=21\). The square of the diagonal ideal in bidegree \((2,2)\) is
spanned by the six independent quadratic products of the three
\((1,1)\) diagonal minors. Hence the first-normal-jet image has dimension
\(21-6=15\), equal by the Euler sequence to
\(h^0(\mathbf P^2,\Omega^1(4))=15\).

The bundle \(E\) is globally generated. A general section has a reduced
zero scheme \(Z\), and

\[
 c_2(E)=c_2(\Omega^1)+4H\,c_1(\Omega^1)+(4H)^2
       =3-12+16=7.
\]

Bertini makes the corresponding divisor \(Y\) smooth away from \(W\).
Thomas' normal-derivative criterion says that the seven simple zeros give
ordinary double points and no other singularities.

## The nodes are independent for the defining system

For any line \(L\subset\mathbf P^2\),

\[
 E|_L\simeq\mathcal O_L(2)\oplus\mathcal O_L(3).
\]

A regular section with finite zero scheme therefore has at most three zeros
on a line: if the degree-two component is nonzero, there are at most two;
if it vanishes identically, the degree-three component has at most three;
both cannot vanish identically.

Fix \(p\in Z\). The other six points can be paired so that none of the three
joining lines passes through \(p\): among lines through \(p\), every radial
group contains at most two of the other points, so the complete multipartite
graph admits a perfect matching. The product of the three joining lines is a
cubic vanishing on \(Z\setminus\{p\}\) but not at \(p\). Multiplying by a
line avoiding \(p\) gives a quartic with the same property.

Thus the evaluation map

\[
 H^0(W,\mathcal O_W(4))\longrightarrow H^0(Z,\mathcal O_Z(4))
\]

is surjective. Since restriction from \(H^0(X,A)\) is surjective, all seven
nodes are independent for \(A\). In particular they satisfy every
two-part Edmonds inequality.

## The adjoint defect is one

Here

\[
 F=K_X\otimes A^2=\mathcal O_X(1,1),\qquad
 F|_W=\mathcal O_W(2).
\]

The Koszul resolution of the regular zero scheme of
\(E=\Omega^1(4)\), twisted by \(\mathcal O_W(2)\), is

\[
 0\longrightarrow\mathcal O_W(-3)
 \longrightarrow T_{\mathbf P^2}(-2)
 \longrightarrow I_{Z/W}(2)\longrightarrow0.
\]

The Euler sequence gives
\(H^1(T_{\mathbf P^2}(-2))=H^2(T_{\mathbf P^2}(-2))=0\), while
\(H^2(\mathcal O_W(-3))\simeq\mathbf C\). Therefore

\[
 h^1(W,I_{Z/W}(2))=1.
\]

The restriction sequence for the diagonal and multiplication
\(V^*\otimes V^*\to\operatorname{Sym}^2V^*\) give
\(H^1(X,I_W(1,1))=H^2(X,I_W(1,1))=0\). Consequently

\[
 h^1(X,I_Z\otimes F)=1.
\]

Bott vanishing on each \(\mathbf P^2\) factor and Künneth verify Schoen's
coherent-vanishing hypotheses for the \((2,2)\) divisor: for every \(k>0\)
and every \(j\ge0\), the higher cohomology of
\(\Omega_X^j\otimes\mathcal O_X(2k,2k)\) vanishes. The already-proved
independence of the nodes supplies B009's local normal-crossing hypothesis.
B026 therefore identifies the coherent defect with one-dimensional rational
relation and extra-homology spaces.

## The extra-to-primitive map has rank one

Write \(h_1,h_2\) for the two hyperplane classes. The diagonal has class

\[
 [W]=h_1^2+h_1h_2+h_2^2.
\]

For a nearby smooth \((2,2)\) divisor \(Y_\infty\), weak Lefschetz identifies
\(H^2(Y_\infty,\mathbf Q)\) with \(H^2(X,\mathbf Q)\). Its Gysin image in
middle cohomology is

\[
 (h_1+h_2)H^2(X,\mathbf Q)
 =\operatorname{span}\{h_1^2+h_1h_2,\ h_1h_2+h_2^2\}.
\]

The diagonal class is not in this subspace. Hence its homology class on
\(Y\) gives a nonzero element of the one-dimensional quotient
\(E^\vee(Y)\), so it generates that quotient.

The primitive middle line is generated by

\[
 \gamma=h_1^2-h_1h_2+h_2^2,
\qquad (h_1+h_2)\gamma=0.
\]

The Lefschetz decomposition is

\[
 [W]
 =\frac23(h_1+h_2)^2+\frac13\gamma.
\]

Saito's canonical map is ambient pushforward followed by primitive
projection. It therefore sends the generator of \(E^\vee(Y)\) to
\(\frac13\gamma\ne0\). Thus

\[
 \operatorname{rank}\Phi_Y=1.
\]

Moreover \(\int_X\gamma^2=3\), so this detector pairs nontrivially with the
primitive rational Hodge class \(\gamma\).

## Scope guard

The class \(\gamma\) is visibly algebraic and the diagonal is built into
the defining incidence. This is exactly the algebraic-anchor input that is
forbidden in the general G013 construction. The brick proves compatibility
of isolated nodality, smoothing independence, positive adjoint defect,
positive ambient rank, and nonzero pairing only in one anchored special
family. It contributes zero progress toward algebraicity of an arbitrary
Hodge class. It is also a low-degree witness: \(A=\mathcal O(2,2)\) has
\(K_X\otimes A=\mathcal O(-1,-1)\), so B027's high-power multiplier
hypothesis does not apply. The example does not reopen the fully
independent-node high-power route.
