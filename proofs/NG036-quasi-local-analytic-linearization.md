---
brick_id: NG036
status: NO-GO
base_field: C
variety: a two-dimensional analytic smoothing base carrying five smooth discriminant branches, realized as a pullback of a projective family with five ordinary double points
smoothness: the base and every discriminant branch are smooth; every pair of branches is transverse; nearby projective fibers are smooth off the prescribed nodal divisors
projectivity: the five-node source family is projective and projectivity is preserved by analytic base change
dimension: base dimension 2, five singleton smoothing blocks, and odd-dimensional nodal fibers in an arbitrary projective realization
codimension: the common branch intersection has codimension 2; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: analytic discriminant germs and rational Picard-Lefschetz local systems; no IC inequality is asserted
hodge_type: the obstruction is analytic and makes no Hodge-class claim
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative
dependencies: G015, G025, Green-Griffiths quasi-local definition S021, and B047's projective submersion realization
claim: Green-Griffiths quasi-local normal crossings and separate block independence do not imply simultaneous analytic equivalence of the discriminant branches to their tangent central arrangement.
falsifier: an analytic coordinate change sending the explicit five curved branches simultaneously to their five tangent lines
---

# NG036 - Quasi-local branches need not be analytically linear

Let

\[
 M=\{0,1,2,4,8\},\qquad
 D_m=\{s_m(x,y)=y-mx-m^4x^2=0\}\subset(\mathbf C^2,0).
\]

Every (D_m) is smooth. For (m\ne m'), the differentials
(ds_m(0)=dy-m,dx) and (ds_{m'}(0)) are independent. The common
intersection has codimension two, so any subset of at most two defining
functions is part of a local coordinate system. This is exactly the
quasi-local coordinate condition in Green-Griffiths Section 4.1.1. Taking
five singleton blocks gives separate block independence.

The tangent arrangement is the union of the lines (y-mx=0). The set (M)
has trivial projective stabilizer: checking the image of any ordered triple
determines a unique Mobius transformation, and the only one preserving all
five slopes is the identity. Hence the derivative of any analytic
equivalence from the curved union to its tangent arrangement is projectively
scalar and fixes each tangent direction.

After removing that scalar, write the quadratic jet of a coordinate change
as

\[
 X=x+Ax^2+Bxy+Cy^2,qquad
 Y=y+Dx^2+Exy+Fy^2.
\]

If a branch has expansion (y=mx+a_mx^2+O(x^3)), its new quadratic
coefficient is

\[
 a'_m=a_m+D+(E-A)m+(F-B)m^2-Cm^3.
\]

Thus simultaneous straightening can alter the five curvature values only
by evaluation of one polynomial of degree at most three. Here (a_m=m^4).
No cubic agrees with (-m^4) at five distinct values: their sum would be a
nonzero degree-four polynomial with five roots. Therefore no simultaneous
analytic linearization exists. Higher coordinate jets cannot change this
quadratic obstruction.

Finally, take a sufficiently high-degree projective hypersurface with five
prescribed nodes and a submersive map from its parameter space to the five
local smoothing parameters, as in B047. Pull it back by
((x,y)\mapsto(s_m(x,y))_{m\in M}). This realizes the example with
projective fibers and commuting disjoint-node Picard-Lefschetz monodromies.

The obstruction is only to analytic equivalence. It does not prove that the
rational IC stalk or its Hodge structure differs from the tangent model.
G026 retains exactly that weaker, still useful comparison.
