---
brick_id: B221
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^(2n) in P^(2n+1), n>=2, with the primitive middle class zeta=a-b from the two rulings by maximal linear P^n subspaces
smoothness: Q is smooth because its defining quadratic form is nondegenerate; the ruling cycles are smooth; no nodal divisor or incidence smoothness is asserted
projectivity: Q, both ruling families, every complete O_Q(k)-embedding, and its ordinary Gauss map are projective
dimension: dim X=2n>=4; the equality branch requires N=D_(2n)(m)>1 while every Gauss fiber for every very ample line bundle on X is a singleton
codimension: a and b are codimension-n algebraic cycle classes; their difference is a nonzero primitive middle class; no codimension-n cycle is constructed for an unknown Hodge class
coefficient_field: Z for the cohomology-ring and Picard computations, Q for zeta and the cycle-class map, and C for sections and Gauss maps
cohomology_theory: singular cohomology with integral or rational coefficients, coherent cohomology in the exponential-sequence Picard calculation, and coherent first jets for Gauss maps
hodge_type: zeta=a-b has rational type (n,n), is nonzero, primitive for h, and is already algebraic
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); zeta is cl([P^n_+]-[P^n_-])
cycle_equivalence: rational equivalence on cycles; only the induced cohomology classes are used
scope: absolute
dependencies: B215-B220, G145-G147, S081
claim: For every n>=2, the valid arbitrary-input pair (Q^(2n),zeta=a-b) has no very ample polarization whose ordinary Gauss map has a fiber of cardinality greater than one; consequently the universal extremal equality gates G145-G147 are false.
falsifier: a very ample line bundle on Q^(2n) outside the powers O_Q(k), a noninjective standard-quadric polarity map, a noninjective power Gauss map contrary to B220, or failure of a-b to be nonzero primitive rational type (n,n)
---

# B221 — An even quadric closes the universal extremal Gauss branch

Let \(X=Q^{2n}\subset\mathbf P^{2n+1}\), \(n\ge2\), be the smooth
quadric of a nondegenerate quadratic form. Its maximal linear
\(\mathbf P^n\)'s have two connected families. Write \(a,b\in
H^{2n}(X,\mathbf Z)\) for the fundamental classes of one member of each
family and \(h=c_1(O_X(1))\).

S081 audits the integral cohomology computation

\[
 H^{2n}(X,\mathbf Z)=\mathbf Za\oplus\mathbf Zb,
 \qquad a+b=h^n,
 \qquad h(a-b)=0. \tag{1}
\]

Thus

\[
 \zeta=a-b\ne0 \tag{2}
\]

is primitive. Both summands are fundamental classes of algebraic
codimension-\(n\) subspaces, so \(\zeta\) is rational of Hodge type
\((n,n)\) and is already algebraic. This makes \((X,\zeta)\) a legitimate
input to the universal G145-G147 claim; algebraicity is used only to
certify the input, never to infer the Hodge Conjecture.

## Every very ample line bundle is a positive power

The same cohomology computation gives \(H^2(X,\mathbf Z)=\mathbf Zh\).
The hypersurface sequence

\[
0\longrightarrow O_{\mathbf P^{2n+1}}(-2)
 \longrightarrow O_{\mathbf P^{2n+1}}
 \longrightarrow O_X\longrightarrow0 \tag{3}
\]

and standard projective-space cohomology give
\(H^1(X,O_X)=H^2(X,O_X)=0\). The exponential sequence therefore makes
\(c_1:\operatorname{Pic}(X)\to H^2(X,\mathbf Z)\) an isomorphism. Hence
every very ample line bundle is \(O_X(k)\) for some \(k\ge1\).

## Every such Gauss map is injective

Let \(B:V\to V^*\) be the linear isomorphism induced by the polar form
of the defining quadratic form. For the standard \(O_X(1)\)-embedding,
the tangent hyperplane at \([v]\in X\) is

\[
 \mathbf P\ker B(v,-). \tag{4}
\]

The Gauss map is therefore the restriction of the projective linear
isomorphism \([v]\mapsto[B(v,-)]\). It is injective (indeed, it identifies
\(X\) with its dual quadric).

For \(k\ge2\), factor

\[
 O_X(k)=O_X(1)\otimes O_X(k-1). \tag{5}
\]

Both factors separate every ordered pair of points. B220 then proves
that the ordinary Gauss map of the complete \(O_X(k)\)-embedding is
injective. Consequently every Gauss fiber for every very ample
polarization of \(X\) is a singleton.

But G145-G147 require a fiber containing

\[
 N=D_{2n}(m)\ge2(2n+1)>1. \tag{6}
\]

The pair \((Q^{2n},a-b)\) therefore falsifies their universal
quantifier. This closes only the extremal equality sufficient branch.
It neither disproves nor proves the rational Hodge Conjecture; the
strict-slack range \(N>D_{2n}(m)\) remains open as G148.
