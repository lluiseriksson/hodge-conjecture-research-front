---
brick_id: B220
status: PROVED
base_field: C
variety: a smooth projective complex d-fold X with a very ample polarization H=A tensor B, where A and B each separate every ordered pair of distinct closed points
smoothness: X is smooth so first-order vanishing defines the embedded tangent space; no Gauss-image smoothness is assumed
projectivity: the point-separating systems of A and B, their product subsystem, the complete very ample H-embedding, and the ordinary H-Gauss map are projective
dimension: dim X=d; every ordinary Gauss fiber of the H-embedding has cardinality one
codimension: products of point-separating sections give, for every ordered pair p!=q, an H-section whose full first jet vanishes at p but whose value at q is nonzero
coefficient_field: C for sections, first jets, tangent spaces, and the Gauss map
cohomology_theory: coherent first principal parts and multiplication of global sections; no Hodge cohomology is used
hodge_type: none asserted; no rational detector or specified Hodge pairing is constructed
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196, S080
claim: If H=A tensor B is very ample and A,B each separate every ordered pair of distinct points, then the ordinary Gauss map of the complete H-embedding is injective on closed points. In particular, for every very ample A and every k>=2, the Gauss map of A^k is injective, so no G146 marked fiber with more than one point can occur in a positive-power re-embedding.
falsifier: distinct p,q with equal H-tangent spaces despite sections a in H^0(A), b in H^0(B) vanishing at p and nonzero at q, or a failure of ab to have zero first jet at p and nonzero value at q
---

# B220 — A factorized polarization has injective Gauss map

Let \(H=A\otimes B\) be very ample, and assume that \(A\) and \(B\)
each separate every ordered pair of distinct points. Fix
distinct points \(p,q\in X\). Point separation supplies

\[
 a\in H^0(X,A),\quad a(p)=0,\ a(q)\ne0,
 \qquad
 b\in H^0(X,B),\quad b(p)=0,\ b(q)\ne0. \tag{1}
\]

Their product \(s=ab\in H^0(X,H)\) satisfies

\[
 s\in H^0(X,H\otimes\mathfrak m_p^2),
 \qquad s(q)\ne0. \tag{2}
\]

Thus the H-hyperplane defined by \(s\) contains the complete embedded
tangent space \(T_pX\) but not the point \(q\). Since \(q\in T_qX\),

\[
 T_pX\ne T_qX. \tag{3}
\]

This holds for every ordered pair of distinct points, so the ordinary
Gauss map of the complete H-embedding is injective on closed points.
The proof uses the product subsystem only; projective normality and
surjectivity of
\(H^0(A)\otimes H^0(B)\to H^0(H)\) are unnecessary.

If \(A\) is very ample and \(k\ge2\), take the two very ample factors
\(A\) and \(A^{k-1}\). Therefore

\[
 \gamma_{A^k}\text{ is injective for every }k\ge2. \tag{4}
\]

B220 rules out nontrivial special Gauss fibers only for polarizations
with two point-separating factors. It neither classifies the residual line
bundles nor constructs any Hodge detector or cycle.
