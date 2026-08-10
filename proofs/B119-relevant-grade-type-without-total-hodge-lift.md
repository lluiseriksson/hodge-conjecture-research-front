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
hodge_type: the total ordinary lift need not be type (0,0); conditional on a nonzero relation-filtered lift, its relation grade is rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B040, B081, B093, B107-B108, B117-B118, B121, NG097, S022, S037
claim: At a clean nodal collision, if a nonzero nearby class has a special lift beta_0 in B107's relation filtration step S_0, then beta_0 has a nonzero full-support E_infinity^(-1,0) coordinate automatically of rational type (0,0) after Q(n), without any type assumption on the total lift.
falsifier: a nonzero filtered lift in S_0 with zero relation grade after B118, a surviving divisor summand in pH^0, or a rational vector in the nodal relation group that is not type (0,0) after Q(n)
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

be a rational nearby class with a rational special lift

\[
 u(\beta_0)=t_\psi,
 \qquad
 \beta_0\in S_0\subset H^{-1}(i_p^*K),
\]

where \(S_0\) is B107's relation filtration step. No Hodge-type hypothesis is imposed on the total vector
\(\beta_0\). Because \(u(\beta_0)\ne0\), necessarily \(\beta_0\ne0\).

## The filtered relevant grade is nonzero

B121 corrects the complete total-degree list to

\[
 E_\infty^{-2,1},
 \quad
 E_\infty^{-1,0}
 \quad\text{and}\quad
 E_\infty^{0,-1}.
\]

B107's condition \(\beta_0\in S_0\) excludes the higher constant ambient
grade \(E_\infty^{-2,1}\). B118 proves that the only lower point grade is zero for
the original incidence pushdown at an isolated hypersurface collision.
Hence the image of \(\beta_0\) in \(E_\infty^{-1,0}\) is nonzero. B117 proves that
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

Thus the nonzero canonical full-support coordinate of \(\beta_0\) has the
required type even when \(\beta_0\) itself is mixed or has other Hodge
components.

## Scope guard

B119 removes only the Hodge-type requirement on a lift already proved to
lie in the correct filtered domain. Its first version incorrectly claimed
that B117-B118 eliminated every competing grade; B121/NG097 record the
omitted \(E_\infty^{-2,1}\) ambient term and make the filtered hypothesis
mandatory. B119 does not construct \(t_\psi\), prove
\(\omega_{\mathrm{fil}}(t_\psi)=0\), or produce a filtered lift. The clean
nodal hypothesis is used
for the type-\((0,0)\) conclusion; an \(A_2\) target would require its own
relation-grade Hodge calculation.
