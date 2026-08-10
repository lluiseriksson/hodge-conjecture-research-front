---
brick_id: B119
status: PROVED
base_field: C with all linear and Hodge data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a sufficiently high generic plane net, its original incidence family h:Y->B, and a clean nodal collision point p
smoothness: X and Y smooth; nearby hyperplane fibers smooth; the target fiber has finitely many ordinary double points satisfying the clean nodal hypotheses of B009/B052
projectivity: X, B, Y, and h projective
dimension: dim_C X = 2n; hyperplane fibers dimension 2n-1; plane base dimension 2
codimension: middle cycle codimension n; collision target has base codimension two
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, nearby and special stalks, the canonical perverse filtration, strict-support decomposition, and nodal local intersection cohomology
hodge_type: the total ordinary lift need not be type (0,0); its forced nonzero full-support relation grade is rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B040, B081, B093, B108, B117-B118, G079-G080, S022, S037
claim: At a clean nodal collision in the original incidence pushdown, every rational ordinary special lift of a nonzero nearby class has a nonzero canonical E_infinity^(-1,0) coordinate in the full-support summand, and that coordinate is automatically rational type (0,0) after Q(n), without any type assumption on the total lift.
falsifier: a nonzero ordinary lift supported entirely in the excluded E_infinity^(0,-1) grade, a surviving divisor summand in pH^0, or a rational vector in the nodal relation group that is not type (0,0) after Q(n)
---

# B119 — The relevant grade has the right type without a Hodge lift

**Status:** PROVED

Let

\[
 K=Rh_*\mathbf Q_Y[2n+1]
\]

be the original plane-net incidence pushdown, and let

\[
 0\ne t_\psi\in H^{-1}(i_p^*\Psi K)
\]

be a rational nearby class with a rational ordinary special lift

\[
 u(\beta)=t_\psi,
 \qquad
 \beta\in H^{-1}(i_p^*K).
\]

No Hodge-type hypothesis is imposed on the total vector \(\beta\).
Because \(u(\beta)\ne0\), necessarily \(\beta\ne0\).

## The relevant associated grade is forced to be nonzero

B081 gives only two possible canonical associated grades in total degree
\(-1\):

\[
 E_\infty^{-1,0}
 \quad\text{and}\quad
 E_\infty^{0,-1}.
\]

B118 proves that the second grade is zero for the original incidence
pushdown at an isolated hypersurface collision. Hence the image of every
nonzero \(\beta\) in \(E_\infty^{-1,0}\) is nonzero. B117 proves that
\({}^pH^0(K)\) has no discriminant-divisor strict-support summand. Therefore
the resulting nonzero associated-grade class lies in the full-support
summand.

## Its Hodge type is automatic in the clean nodal target

On the smooth locus, \({}^pH^0(K)\) is the middle direct-image local system
shifted by the base dimension. Its constant ambient part has zero
degree-\(-1\) stalk at \(p\). B093 therefore identifies the full-support
degree-\(-1\) stalk with the nodal relation group

\[
 H^{-1}(i_p^*j_{!*}L[2])\simeq R(p)_1.
\]

Saito's Theorem 3 in S022 identifies each ordinary-double-point local
vanishing group with \(\mathbf Q(-n)\). Consequently the rational relation
kernel, after the normalization \(\mathbf Q(n)\), is a direct sum of copies
of \(\mathbf Q(0)\). B040 records the same mixed-Hodge conclusion in the
explicit arrangement calculation. Every rational vector in this relation
group is therefore of Hodge type \((0,0)\).

Thus the nonzero canonical full-support coordinate of \(\beta\) has the
required type even when \(\beta\) itself is mixed or has other Hodge
components.

## Scope guard

B119 removes only the Hodge-type requirement on the *total ordinary lift*.
It does not construct \(t_\psi\), prove collision-monodromy invariance, or
produce an ordinary lift. It also does not repair B108's independent
perverse-filtered-lift obstruction in settings where the competing grades
have not been structurally eliminated. The clean nodal hypothesis is used
for the type-\((0,0)\) conclusion; an \(A_2\) target would require its own
relation-grade Hodge calculation.
