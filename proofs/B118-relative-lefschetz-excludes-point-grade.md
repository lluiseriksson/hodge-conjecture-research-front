---
brick_id: B118
status: PROVED
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a sufficiently high generic plane net, its original smooth incidence family h:Y->B, and a collision fiber with isolated hypersurface singularities
smoothness: X and the incidence total space Y smooth; nearby hyperplane fibers smooth; the collision fiber has finitely many isolated complete-intersection hypersurface singularities
projectivity: X, B, Y, and h projective; a relative ample class is fixed
dimension: dim_C X = 2n; hyperplane fibers have dimension d = 2n-1; dim_C B = 2; dim_C Y = d+2
codimension: middle cycle codimension n; tested strict support is a point of base codimension two
coefficient_field: Q
cohomology_theory: singular Betti cohomology, vanishing cycles, perverse cohomology, relative hard Lefschetz, strict-support decomposition, and polarizable rational Hodge modules
hodge_type: no class is selected; the point-support multiplicity vanishes over Q in every Hodge type
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B010, B077, B080-B081, B117, B121, G079, NG094, NG097, S022, S037
claim: For the original smooth incidence pushdown K=Rh_*Q_Y[2n+1], pH^(-1)(K) has no point-strict-support summand at a collision fiber with isolated hypersurface singularities; hence B081's competing E_infinity^(0,-1) detector grade is zero.
falsifier: a nonzero point summand in pH^(-1)(K), equivalently via relative hard Lefschetz a point summand in pH^1(K) and hence in R^(2n+2)h_*Q, despite isolated vanishing cohomology being concentrated in degree 2n-1
---

# B118 — Relative Lefschetz excludes the point detector grade

**Status:** PROVED

Put

\[
 d=2n-1,
 \qquad
 K=Rh_*\mathbf Q_{\mathcal Y}[d+2].
\]

Suppose that the point \(p\in B\) supports a nonzero strict-support summand

\[
 i_{p*}V\subset{}^pH^{-1}(K).
\]

Let \(\eta\) be a relative ample class. Saito's relative hard Lefschetz
theorem S037 gives an isomorphism

\[
 \eta:{}^pH^{-1}(K)
 \xrightarrow{\sim}
 {}^pH^{1}(K)(1).
\]

The strict-support decomposition is unique, so this isomorphism preserves
supports. It sends \(i_{p*}V\) to a nonzero point-supported summand of
\({}^pH^1(K)(1)\).

## The reflected summand lies in a constant high direct image

The projective decomposition theorem writes the reflected point term inside
\(K\) as

\[
 i_{p*}V'[-1].
\]

It therefore contributes a punctual direct summand to

\[
 \mathcal H^1(K)
 =R^{d+3}h_*\mathbf Q
 =R^{2n+2}h_*\mathbf Q.
\]

Choose, as in S022, an analytic curve through \(p\) whose punctured germ is
in the smooth-fiber locus. The collision fiber has isolated hypersurface
singularities. S022 Proposition 2 and §2.2 prove that the reduced local
vanishing cohomology is concentrated in degree

\[
 d=2n-1.
\]

Apply the special/nearby/vanishing distinguished triangle from S022 §2.1.
In degree \(d+3=2n+2\), both adjacent vanishing groups are zero, so
specialization is an isomorphism

\[
 H^{d+3}(Y_p,\mathbf Q)
 \xrightarrow{\sim}
 H^{d+3}(Y_t,\mathbf Q).
\]

Consequently \(R^{d+3}h_*\mathbf Q\) restricts to a constant sheaf on this
curve germ. It cannot contain a nonzero direct summand supported only at
\(p\). This contradicts the reflected summand, so

\[
 ({}^pH^{-1}(K))_{\{p\}}=0.
\]

For \(n=1\), the same conclusion is immediate because \(d+3=4\) exceeds
the top cohomological degree of a curve; the uniform argument still reads
the target direct image as zero.

## Consequence for G079

B081 places the point-supported detector alternative in
\(E_\infty^{0,-1}\). B118 makes that grade zero for the original incidence
pushdown. B117 already removes divisor support from the relation grade.
B121 corrects the earlier consequence: the constant ambient
\(E_\infty^{-2,1}\) grade still survives. Therefore B118 forces a nonzero
relation coordinate only after the selected lift is proved to lie in
B107's filtration step \(S_0\); it does not do so for an arbitrary ordinary
lift.

B123/NG099 show that the proposed G083 obligation is impossible for a
nonzero nearby class. The surviving obligation is G065's relative-boundary
construction.

## Scope guard

The proof requires the original smooth incidence source, projectivity, and
isolated hypersurface singularities. It does not exclude point supports
created in a semistable alteration's pushdown or apply to a collision with a
positive-dimensional singular locus. It constructs no selected class and no
algebraic cycle.
