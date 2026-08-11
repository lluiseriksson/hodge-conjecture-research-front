---
brick_id: B142
status: PROVED
base_field: C
variety: X=P^n x P^n, W={p} x P^n, A_m=O_X(m,m), and a general divisor Y_m in |I_W tensor A_m| for n at least 2 and m sufficiently large
smoothness: X and W are smooth; Y_m is smooth away from W and has exactly m^n isolated ordinary double points on W
projectivity: X, W, Y_m, and the complete-intersection node scheme are projective
dimension: dim_C X=2n, dim_C W=n, dim_C Y_m=2n-1, with n at least 2
codimension: W has middle codimension n in X; Y_m has codimension one; its nodes have codimension 2n in X
coefficient_field: C for jets, complete intersections, coherent cohomology, evaluation matroids, and monodromy; Q for vanishing relations and Hodge classes
cohomology_theory: coherent cohomology, complete-intersection Koszul cohomology, singular homology and cohomology, nodal vanishing cycles, Lefschetz decomposition, and local intersection cohomology
hodge_type: the unique rational nodal relation has type (0,0) after Q(n), and its ambient image spans the one-dimensional primitive rational Hodge line
cycle_class_map: CH^n(P^n x P^n)_Q -> H^(2n)(P^n x P^n,Q(n))
cycle_equivalence: rational equivalence
scope: generic
dependencies: Thomas Theorem 4.2 (S019), Saito Proposition 1 and Theorem 1 (S022), Edmonds Theorem 1 (S031), B010, B026, B028, B034, B054, and B141
claim: For every n at least 2 and all sufficiently large m, a general (m,m) divisor containing the fiber W has m^n isolated nodes, uniform O(m,m)-evaluation matroid of rank binomial(m+n,n)-n partitionable into n! independent blocks, adjoint defect one, and rank-one extra-to-primitive map pairing nontrivially with the primitive Hodge line; its node count is genuinely superlinear relative to mn-n-1.
falsifier: failure of normal-jet surjectivity, a nonreduced general complete intersection, failure of full symmetric zero monodromy, a dependent subset of at most binomial(m+n,n)-n nodes, adjoint defect other than one, or zero primitive fiber projection
---

# B142 — A dimension-scaled superlinear fiber witness

Fix \(n\ge2\), a point \(p\in\mathbf P^n\), and put

\[
 X=\mathbf P^n\times\mathbf P^n,\qquad
 W=\{p\}\times\mathbf P^n,\qquad
 A_m=\mathcal O_X(m,m).
\]

This brick constructs a special-family compatibility witness at the first
growth scale left open by B141. It deliberately retains the algebraic fiber
\(W\), so it is not an unanchored construction for an arbitrary Hodge class.

## Normal derivative and isolated nodes

The normal bundle of \(W\subset X\) is the trivial rank-\(n\) bundle. Hence

\[
 N^*_{W/X}\otimes A_m|_W
 \simeq \mathcal O_{\mathbf P^n}(m)^{\oplus n}.
\]

The normal-jet map is surjective. Indeed, under Kunneth it is the tensor
product of

\[
 H^0(\mathbf P^n,I_p(m))\longrightarrow
 (I_p/I_p^2)\otimes\mathcal O(m)|_p
\]

with \(H^0(\mathbf P^n,\mathcal O(m))\), and the first map is surjective for
\(m\ge1\). A general normal derivative is therefore an \(n\)-tuple
\((f_1,\ldots,f_n)\) of general degree-\(m\) forms on
\(W\simeq\mathbf P^n\). Its zero scheme

\[
 Z_m=V(f_1,\ldots,f_n)
\]

is a reduced complete intersection of length

\[
 N_m=\#Z_m=m^n.
\]

The linear system \(I_W\otimes A_m\) is base-point-free away from \(W\), so
Bertini makes a general lift smooth there. At a transverse zero of the
normal derivative, local coordinates \(u_1,\ldots,u_n\) normal to \(W\) and
\(v_1,\ldots,v_n\) along \(W\) put the quadratic term in the form

\[
 u_1v_1+\cdots+u_nv_n.
\]

It is nondegenerate. Thomas' normal-derivative criterion therefore gives
exactly \(m^n\) isolated ordinary double points and no other singularities.

## Full symmetric zero monodromy

Let

\[
 V=H^0(\mathbf P^n,\mathcal O(m))^{\oplus n}
\]

and restrict to the open locus of tuples with a reduced zero scheme. The
one-zero incidence is an open subset of a projective bundle over
\(\mathbf P^n\), hence irreducible. For two distinct points \(x,y\), the
evaluation map

\[
 V\longrightarrow\mathbf C^n_x\oplus\mathbf C^n_y
\]

is surjective because \(\mathcal O(m)\) separates two points. Thus the
ordered two-zero incidence is irreducible, and the zero-cover monodromy is
2-transitive.

For \(m\ge2\), degree-\(m\) forms realize the local one-parameter model

\[
 (u_1^2-\tau,u_2,\ldots,u_n).
\]

After choosing all unused coefficients generally, the central tuple has
one length-two zero and every other zero is simple. A loop around
\(\tau=0\) exchanges only the two colliding zeros. The monodromy therefore
contains a transposition. A 2-transitive subgroup containing a
transposition contains all transpositions, so the monodromy is
\(S_{m^n}\).

## Uniform smoothing matroid and the factorial partition

The degree-\(m\) part of the complete-intersection ideal is exactly the
span of \(f_1,\ldots,f_n\). Consequently the full evaluation rank of
\(\mathcal O_W(m)\) on \(Z_m\) is

\[
 R_m=\binom{m+n}{n}-n.
\]

Full symmetric monodromy upgrades this dimension calculation to every
subset. For \(1\le s\le R_m\), the cover labeling an unordered \(s\)-subset
is irreducible. Rank failure for that subset is closed and proper: the full
rank \(R_m\) supplies a basis and subsets of a basis witness every smaller
rank. Removing the finitely many proper images shows that, for a general
tuple,

\[
 r(S)=\min\{|S|,R_m\}\qquad(S\subseteq Z_m).
\]

Thus the evaluation matroid is \(U_{R_m,m^n}\). Restriction from \(X\) to
\(W\) is surjective, so this is also the \(A_m\)-smoothing matroid. Moreover,

\[
 n!R_m
 =\prod_{j=1}^n(m+j)-n\,n!
 \ge m^n
\]

for all sufficiently large \(m\). Hence \(Z_m\) partitions into \(q=n!\)
blocks, each of size at most \(R_m\), and every block is independently
smoothable. This attains the asymptotic lower bound of B034.

The tangent smoothing arrangement is the representable uniform arrangement.
This does not by itself prove that a chosen nonlinear discriminant germ and
all its intersections form a Li clean arrangement. B054 applies only after
that separate geometric hypothesis is verified.

## Adjoint defect one

Since

\[
 K_X=\mathcal O_X(-n-1,-n-1),\qquad
 F_m=K_X\otimes A_m^n
     =\mathcal O_X(d_m,d_m),\qquad
 d_m=mn-n-1,
\]

the restriction \(F_m|_W\) is \(\mathcal O_{\mathbf P^n}(d_m)\). The
Hilbert series of the complete intersection is

\[
 \frac{(1-t^m)^n}{(1-t)^{n+1}}.
\]

Its projective regularity is \(n(m-1)\), and in the preceding degree
\(d_m=n(m-1)-1\) its Hilbert function is \(m^n-1\). Therefore

\[
 h^1\bigl(W,I_{Z_m/W}(d_m)\bigr)=1.
\]

Because \(W\) is a product fiber,
\(I_W\otimes F_m=\operatorname{pr}_1^*I_p(d_m)\otimes
\operatorname{pr}_2^*\mathcal O(d_m)\). Bott and Kunneth give the required
higher-cohomology vanishings and surjectivity of restriction. Hence

\[
 h^1\bigl(X,I_{Z_m/X}\otimes F_m\bigr)=1.
\]

B026 and Saito's theorem identify one-dimensional rational relation and
extra-homology spaces, of type \((0,0)\) after \(\mathbf Q(n)\).

## Primitive ambient rank and pairing

Write \(h_1,h_2\) for the two hyperplane classes and \(L=h_1+h_2\). The
primitive middle cohomology is one-dimensional, generated by

\[
 \gamma_n=\sum_{i=0}^n(-1)^i h_1^{n-i}h_2^i,\qquad L\gamma_n=0.
\]

The fiber class is \([W]=h_1^n\), and

\[
 \int_X[W]\gamma_n=(-1)^n\ne0,\qquad
 \int_X\gamma_n^2=(-1)^n(n+1)\ne0.
\]

Thus the primitive projection of \(W\) is nonzero. The smooth-divisor image
is the Lefschetz part \(L H^{2n-2}(X,\mathbf Q(n-1))\); therefore the class
of \(W\subset Y_m\) is a nonzero extra class. Since both the extra quotient
and the primitive target are one-dimensional, Saito's canonical
extra-to-primitive map has rank one and its image pairs nontrivially with
every nonzero element of the primitive Hodge line.

## Superlinear scale and scope guard

For \(H=\mathcal O(1,1)\), choose \(c=n+1\), so
\(K_X\otimes H^c\simeq\mathcal O_X\). Then B141's adjoint parameter is

\[
 t_m=mn-n-1,\qquad
 \frac{N_m}{t_m}=\frac{m^n}{mn-n-1}\longrightarrow\infty.
\]

The construction therefore proves that B141's superlinear regime is not
geometrically empty: isolated nodes, the optimal \(n!\)-block partition,
defect one, ambient rank one, and a nonzero primitive pairing coexist in
every middle dimension.

It does not prove the nonlinear Li-clean hypothesis, compute the canonical
B135 residue vector, or select a divisor from an arbitrary pair
\((X,\zeta)\). Most importantly, \(Y_m\) was forced to contain the already
algebraic fiber \(W\). Importing this step for an arbitrary Hodge class would
assume the cycle whose existence is at issue. Thus B142 is special-family
compatibility evidence and contributes zero progress toward the general
Hodge Conjecture. The active gate remains unanchored, class-directed
incidence in G028/G013.
