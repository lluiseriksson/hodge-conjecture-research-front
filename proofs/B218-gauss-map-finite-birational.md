---
brick_id: B218
status: PROVED
base_field: C
variety: a smooth non-linear nondegenerate complex projective d-fold X embedded by a complete very ample system H
smoothness: X is smooth; the Gauss image need not be normal or smooth
projectivity: X, its H-embedding, the Grassmannian of projective d-planes, and the ordinary Gauss map are projective
dimension: dim X=d and the ambient projective dimension r is strictly greater than d
codimension: Zak tangency excludes positive-dimensional Gauss fibers, while separable general-contact linearity makes the generic fiber one point
coefficient_field: C
cohomology_theory: none; projective tangent spaces, the Gauss morphism, and normalization are used
hodge_type: none asserted
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: S078
claim: The ordinary Gauss morphism gamma_H:X->Gr(d,P(H^0(H)^*)) of a smooth non-linear nondegenerate complex projective variety is finite and birational onto its image. Consequently X is the normalization of its Gauss image, but special fibers may still contain more than one point.
falsifier: a positive-dimensional Gauss fiber, a general fiber with more than one point, or an application to the excluded linear embedding X=P^d in P^d
---

# B218 — The ordinary Gauss map is finite birational

Let \(X^d\subset\mathbf P^r\) be smooth, nondegenerate, and non-linear,
so \(r>d\). Its ordinary Gauss morphism is

\[
 \gamma_H:X\longrightarrow\operatorname{Gr}(d,\mathbf P^r),
 \qquad p\longmapsto T_pX. \tag{1}
\]

If a fiber had a positive-dimensional irreducible component \(Y\), its
common tangent \(d\)-plane \(L\) would be tangent to \(X\) along \(Y\).
Zak's tangency inequality, in the form audited in S078, would give

\[
 d=\dim L\ge \dim X+\dim Y=d+\dim Y, \tag{2}
\]

a contradiction. Thus \(\gamma_H\) is quasi-finite. It is projective,
hence finite.

Over \(\mathbf C\) the Gauss map is separable. S078's general-contact
linearity says its general fiber is a linear variety. A finite linear
variety is a single point, so \(\gamma_H\) is generically one-to-one and
therefore birational onto its image. Since \(X\) is smooth and hence
normal, (1) is the normalization morphism of \(\gamma_H(X)\).

This theorem controls dimension and the generic fiber only. It does not
make the normalization morphism injective over singular points of the
Gauss image and supplies no uniform bound on a special fiber.
