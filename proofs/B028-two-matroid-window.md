---
brick_id: B028
status: PROVED
base_field: C
variety: a smooth projective X of dimension 2n with n at least 2, a sufficiently ample line bundle A, and a finite reduced candidate node scheme Delta
smoothness: X is smooth; Delta is reduced; a nodal member is required only in the later G013 application
projectivity: X is projective
dimension: dim_C X = 2n with n >= 2
codimension: candidate nodes have codimension 2n in X; the Hodge application has middle codimension n
coefficient_field: C for evaluation matroids and Q for the later vanishing-cycle relation space
cohomology_theory: coherent evaluation maps, representable matroids, adjoint node defects, and by B026 singular homology and local intersection cohomology for a nodal member
hodge_type: no Hodge type is asserted by the matroid theorem; a later nodal rational relation has type (0,0) after Tate twist by B010
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: Edmonds Theorem 1 (S031), B026-B027, and the multiplication argument below
claim: A finite node candidate Delta partitions into two subsets independently smoothable by A exactly when |S| <= 2 r_A(S) for every S subset Delta; at high power the adjoint evaluation rank r_F(S) dominates r_A(S), so a partitioned set with nonzero adjoint defect must lie in the exact rank window ceil(|Delta|/2) <= r_A(Delta) <= r_F(Delta) < |Delta|.
falsifier: a finite evaluation matroid satisfying all inequalities |S| <= 2 r_A(S) but admitting no two-independent-set partition, or high-power data with r_F(S) < r_A(S) despite a multiplier nonvanishing on Delta
---

# B028 - The two-matroid window

Let \(A\) be a line bundle and \(\Delta\subset X\) a finite reduced set.
After trivializing the one-dimensional fibers over \(\Delta\), define the
evaluation rank

\[
 r_A(S)=\operatorname{rank}\!\left(
 H^0(X,A)\longrightarrow\bigoplus_{p\in S}A|_p
 \right),\qquad S\subseteq\Delta.
\]

The subsets with \(r_A(S)=|S|\) are the independent sets of the
representable evaluation matroid \(M_A(\Delta)\). They are exactly the point
subsets imposing independent conditions on \(A\), hence the subsets whose
node-smoothing directions are independently accessible in the audited
Green-Griffiths/Di Gennaro-Franco model.

Edmonds' Theorem 1 states that a matroid ground set partitions into at most
\(k\) independent sets if and only if

\[
 |S|\le k\,r(S)\qquad\text{for every subset }S.
\]

With \(k=2\), the partition \(\Delta=J\sqcup K\) required in G012 therefore
exists exactly when

\[
 |S|\le2r_A(S)\qquad(S\subseteq\Delta).
\]

If \(\Delta\) is dependent, both parts of any such partition are nonempty.
In particular every circuit of \(M_A\) is two-partitionable, because all its
proper subsets are independent.

## Comparison with the adjoint matroid

Put

\[
 F=K_X\otimes A^n,
 \qquad M=F\otimes A^{-1}=K_X\otimes A^{n-1}.
\]

When \(M\) is globally generated, choose one section \(t\) nonzero at every
point of \(\Delta\). Multiplication by \(t\) embeds the image of every
\(A\)-evaluation map into the corresponding \(F\)-evaluation image, up to
nonzero coordinate rescaling. Consequently

\[
 r_A(S)\le r_F(S)\qquad(S\subseteq\Delta).
\]

Assume also \(H^1(X,F)=0\). Then the adjoint defect is

\[
 h^1(X,I_\Delta\otimes F)=|\Delta|-r_F(\Delta).
\]

Thus a partwise-independent configuration with positive adjoint defect must
satisfy the exact numerical window

\[
 \left\lceil\frac{|\Delta|}{2}\right\rceil
 \le r_A(\Delta)\le r_F(\Delta)<|\Delta|,
\]

together with \(|S|\le2r_A(S)\) for every subset \(S\). B026 then converts
the last strict inequality into a positive nodal relation dimension once a
nodal member with this node scheme is actually constructed.

## Why an \(A\)-circuit is not enough

Dependence can disappear when the linear system is enlarged. On
\(X=\mathbf P^2\times\mathbf P^2\), let
\(A=\mathcal O(m,m)\), \(m\ge4\), and choose \(m+2\) distinct points on a
line \(C=\mathbf P^1\times\{q\}\). Their \(A\)-evaluation matroid is a
circuit because \(A|_C=\mathcal O_{\mathbf P^1}(m)\). But

\[
 F=K_X\otimes A^2=\mathcal O(2m-3,2m-3)
\]

restricts to \(\mathcal O_{\mathbf P^1}(2m-3)\), and the restriction map is
surjective. Since \(m+2\le2m-2\), these points impose independent conditions
on \(F\). Hence the smoothing circuit has zero adjoint defect. Selecting a
circuit in \(M_A\) alone is NG-025.

## Scope guard

This brick makes the partition constraint exact but does not construct a
nodal hypersurface, an adjoint-dependent configuration, a rational relation
vector, or a nonzero pairing with a specified Hodge class. Those remain the
geometric and Hodge-theoretic content of G013.
