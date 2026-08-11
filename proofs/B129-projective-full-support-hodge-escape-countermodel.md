---
brick_id: B129
status: PROVED
base_field: C
variety: P^d for arbitrary d at least 1, obtained from a finite image of P^1 x P^(d-1); this is a coefficient-object countermodel, not a universal hyperplane family
smoothness: the dense variation locus is smooth; the double-cover curve and product source are smooth projective
projectivity: all compactifications and the finite target P^d are projective
dimension: arbitrary parameter dimension d at least 1
codimension: no algebraic-cycle construction; the tested local cohomology sheaf is degree -d+1 and vanishes on all supports
coefficient_field: Q
cohomology_theory: intersection cohomology, finite direct image, polarizable variations of Hodge structure, pure Hodge modules, and the decomposition theorem
hodge_type: coefficient variation has weight -1; global IH^1 contains a nonzero rational type (0,0) class
cycle_class_map: no cycle class map is used; the construction is not a Hodge-Conjecture counterexample
cycle_equivalence: rational equivalence is not used
scope: absolute
dependencies: B014, B074, B128, S037 decomposition/strict-support facts, projective Noether normalization, and the cohomology of a double cover of P^1 branched at four points
claim: For every d at least 1 there is a full-support IC(W) on P^d, with W a polarizable rational weight-minus-one variation of geometric origin, such that IH^1(P^d,W) contains a nonzero rational type-(0,0) class while H^(-d+1)(IC(W)) is zero everywhere.
falsifier: nonzero local invariants or coinvariants for monodromy -1 at a puncture, vanishing of the anti-invariant H^1 of the branched double cover, failure of finite pushforward to preserve the single ordinary-sheaf degree, or absence of a type-(0,0) tensor
---

# B129 — A projective full-support Hodge escape countermodel

**Status:** PROVED

This strengthens B014 from an elliptic base with a constant coefficient to a
full-support geometric Hodge coefficient on every projective space.

## The curve model

Let \(C\to\mathbf P^1\) be the double cover branched at four points \(B\),
so \(C\) is an elliptic curve. On \(U=\mathbf P^1\setminus B\), let \(L\)
be the anti-invariant rank-one rational local system. Its local monodromy at
every puncture is (-1). Thus both invariants and coinvariants vanish because
\(-1-1=-2\) is invertible over \(\mathbf Q\). For \(j:U\hookrightarrow
\mathbf P^1\),

\[
 IC_{\mathbf P^1}(L)=j_{!*}L[1]=j_!L[1]=Rj_*L[1]
\]

has only the ordinary cohomology sheaf in degree (-1). Finite pushdown of
the double cover gives

\[
 IH^1(\mathbf P^1,L)=H^1(C,\mathbf Q)^-.
\]

The deck involution is \(-1\) on \(H^1(C,\mathbf Q)\), so this is the full
two-dimensional \(H^1(C,\mathbf Q)\).

Let \(A=H^1(C,\mathbf Q)(1)\), viewed as a constant polarizable Hodge
structure of weight \(-1\), and replace \(L\) by \(V=L\otimes A\). Then

\[
 IH^1(\mathbf P^1,V)
 =H^1(C,\mathbf Q)\otimes H^1(C,\mathbf Q)(1)
\]

contains the rational identity tensor of Hodge type \((0,0)\), while
\(\mathcal H^0(IC(V))=0\) at every point.

## Promotion to every projective space

For \(d>1\), external-product with
\(\mathbf Q_{\mathbf P^{d-1}}[d-1]\) on
\(B_d=\mathbf P^1\times\mathbf P^{d-1}\). The resulting pure perverse
Hodge module \(M_d\) has only \(\mathcal H^{-d}\), and its
\(IH^1\) retains the type-\((0,0)\) tensor above.

Projective Noether normalization supplies a finite surjective morphism
\(f:B_d\to\mathbf P^d\). A finite morphism has no higher direct images for
constructible sheaves and is small. Hence

\[
 K_d=Rf_*M_d=f_*M_d
\]

is the intermediate extension of a semisimple polarizable variation of
geometric origin on a dense open of \(\mathbf P^d\), all its simple
constituents have full support, and it still has only
\(\mathcal H^{-d}\). Its \(IH^1\) contains the pushed-forward nonzero
rational \((0,0)\) class. Decompose \(K_d\) into simple full-support IC
summands and choose one on which that class is nonzero. Calling its dense
variation \(W\), we obtain

\[
 0\ne\eta\in IH^1(\mathbf P^d,W)^{(0,0)}_{\mathbf Q},
 \qquad
 \mathcal H^{-d+1}(IC(W))=0.
\]

## Consequence

Projective base, full strict support, geometric origin, polarizability,
weight \(-1\), purity, hard Lefschetz, and rational Hodge type do not force a
global \(IH^1\) class to have a local invariant. Any proof of G008 must use
the specific universal-hyperplane variation and the incidence origin of
\(s_m(\zeta)\).

## Scope guard

The coefficient \(W\) is not asserted to equal the vanishing-cohomology
variation of any universal hyperplane family, and \(\eta\) is not asserted to
come from an incidence pullback. B129 is not a counterexample to G008 or HC.
