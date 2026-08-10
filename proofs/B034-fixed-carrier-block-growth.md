---
brick_id: B034
status: PROVED
base_field: C
variety: a smooth projective complex 2n-fold X, a smooth integral middle-dimensional W subset X, an ample line bundle L, and high-power divisors in |I_W tensor L^m|
smoothness: X and W are smooth; the general fixed-carrier divisor is assumed in the Thomas normal-derivative range and has isolated ordinary double points at the regular zeros
projectivity: X, W, and the divisors are projective
dimension: dim_C X = 2n and dim_C W = n
codimension: W has middle codimension n in X; the divisors have codimension 1
coefficient_field: C for Chern classes, coherent cohomology, and evaluation ranks; Q only for the downstream Hodge application
cohomology_theory: Chow or singular Chern classes, coherent cohomology, Hilbert polynomials, and node-smoothing evaluation matroids
hodge_type: none asserted; the brick is an asymptotic geometric obstruction before the Hodge pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle-class surjectivity is assumed
cycle_equivalence: rational equivalence
scope: generic
dependencies: Thomas normal-derivative construction (S019), asymptotic Riemann-Roch, Serre vanishing, and B028
claim: A high-power fixed-carrier nodal construction needs at least n! independently smoothable blocks asymptotically; in middle dimension n at least 3 it cannot have a two-independent-block node partition for all sufficiently large powers.
falsifier: fixed-carrier regular zero schemes Z_m with node count equal to the top Chern number and a partition into a fixed q less than n! defining-system-independent blocks for arbitrarily large m
---

# B034 - Fixed-carrier block growth

Let \(X\) be a smooth projective complex \(2n\)-fold, let
\(W\subset X\) be a smooth integral \(n\)-fold, and let \(L\) be ample. Put

\[
 h=c_1(L|_W),\qquad d=\int_W h^n>0.
\]

For \(m\gg0\), a divisor in \(|I_W\otimes L^m|\) has first normal
derivative in

\[
 H^0\!\left(W,E_m\right),\qquad
 E_m=N^*_{W/X}\otimes L^m|_W.
\]

Serre vanishing makes the normal-jet map onto this space, and \(E_m\) is
globally generated. A general section is regular. Thomas' local criterion
identifies its reduced zero scheme \(Z_m\) with the ordinary double points
of a general divisor containing \(W\).

## Asymptotic node count

Under the splitting principle, write the Chern roots of \(N^*_{W/X}\) as
\(\alpha_1,\ldots,\alpha_n\). Then

\[
 \#Z_m
 =\int_W c_n(E_m)
 =\int_W\prod_{i=1}^n(\alpha_i+mh)
 =d\,m^n+O(m^{n-1}).
\]

Only the leading term will be used. It is independent of the normal bundle.

## Capacity of one independent block

Let \(S\subseteq Z_m\) impose independent conditions on the defining
system \(H^0(X,L^m)\). Its evaluation map factors through restriction to
\(W\):

\[
 H^0(X,L^m)\longrightarrow H^0(W,L^m|_W)
 \longrightarrow \bigoplus_{p\in S}L^m|_p.
\]

Therefore

\[
 |S|\le h^0(W,L^m|_W).
\]

Asymptotic Riemann-Roch and Serre vanishing give

\[
 h^0(W,L^m|_W)=\frac{d}{n!}m^n+O(m^{n-1}).
\]

If \(Z_m\) partitions into \(q\) defining-system-independent blocks, summing
their cardinalities yields

\[
 d\,m^n+O(m^{n-1})
 =\#Z_m
 \le q\,h^0(W,L^m|_W)
 =q\,\frac{d}{n!}m^n+O(m^{n-1}).
\]

Consequently every fixed integer \(q<n!\) is impossible for all
sufficiently large \(m\). Equivalently, the minimum number \(b_m\) of
independent blocks satisfies

\[
 \liminf_{m\to\infty}b_m\ge n!.
\]

For \(n\ge3\), \(2<n!\), so B028's two-block inequalities must eventually
fail for the full fixed-carrier node scheme.

## Diagonal family in all middle dimensions

Take

\[
 X=\mathbf P^n\times\mathbf P^n,\qquad
 W=\Delta_{\mathbf P^n},\qquad
 A_m=\mathcal O_X(m,m).
\]

Here \(A_m|_W=\mathcal O_{\mathbf P^n}(2m)\) and

\[
 E_m=\Omega^1_{\mathbf P^n}(2m).
\]

Writing \(k=2m\), the Euler sequence gives the exact node count

\[
 N_{n,k}
 =[H^n]\frac{(1+(k-1)H)^{n+1}}{1+kH},
\]

while one independent block has at most
\(\binom{k+n}{n}\) points. Their ratio tends to \(n!\). Thus B033's
two-block diagonal construction is dimension-specific: it is asymptotically
cardinality-compatible for \(n=2\), but impossible for the same diagonal
construction in every \(n\ge3\).

## Scope guard

This is a NO-GO only for the high-power **fixed-carrier** route with a fixed
number \(q<n!\) of smoothing-independent blocks. It does not show that an
unanchored nodal member with fewer nodes cannot satisfy the two-block
conditions, and it does not disprove G014 or the Hodge Conjecture.

It does show that HC, followed by Thomas' construction from an algebraic
representative, does not automatically establish the two-block version of
G014 in dimensions at least six. The current implication is only
\(\mathrm{G014}\Rightarrow\mathrm{HC}\); the reverse arrow has not been
proved.
