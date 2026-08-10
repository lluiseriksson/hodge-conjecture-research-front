---
brick_id: B121
status: PROVED
base_field: C with rational coefficients
variety: an arbitrary polarized smooth projective complex 2n-fold X and the original smooth projective plane-net incidence family h:Y->B
smoothness: X, Y, and generic hyperplane fibers smooth; collision fiber may have isolated hypersurface singularities
projectivity: X, Y, B, and h projective
dimension: dim_C X=2n; hyperplane fibers d=2n-1; plane base dimension 2
codimension: middle cycle codimension n; full, divisor, and point supports have base codimensions 0, 1, and 2
coefficient_field: Q
cohomology_theory: rational proper direct image, perverse cohomology, canonical perverse filtration, strict support, weak Lefschetz, and Poincare duality
hodge_type: the omitted full-support constant grade may contain rational type-(0,0) vectors after Q(n); no class-specific type is forced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B080-B081, B092, B107-B109, B117-B118, S037
claim: In total normalized stalk degree -1 of K=Rh_*Q_Y[d+2], there are three possible perverse positions E_infinity^(-2,1), E_infinity^(-1,0), and E_infinity^(0,-1); the first is the generally nonzero full-support constant R^(d+1) grade, so B117-B118 do not force a nonzero ordinary lift to have nonzero relation grade.
falsifier: vanishing of E_infinity^(-2,1) for every smooth projective hyperplane family, or a perverse-shift computation placing R^(d+1) outside total normalized degree -1
---

# B121 — Total degree minus one has a third perverse grade

**Status:** PROVED

Put

\[
 d=2n-1,
 \qquad
 K=Rh_*\mathbf Q_Y[d+2].
\]

On the smooth locus, the perverse cohomology object \({}^pH^s(K)\) restricts
to

\[
 R^{d+s}h_*\mathbf Q[2].
\]

At a point of the plane base, a full-support local system shifted by \([2]\)
has its ordinary stalk in degree \(-2\). Consequently the full-support
\({}^pH^1(K)\) term contributes to total degree \(-1\) at

\[
 E_\infty^{-2,1}.
\]

Together with B081's two proper-support/relation positions, the complete
list relevant to total degree \(-1\) is

\[
 \boxed{
 E_\infty^{-2,1},\qquad
 E_\infty^{-1,0},\qquad
 E_\infty^{0,-1}.
 }
\]

They represent respectively:

1. the full-support \({}^pH^1\) constant/ambient grade;
2. the full-support middle relation term and any divisor support in
   \({}^pH^0\);
3. point support in \({}^pH^{-1}\).

The first term is generally nonzero. Indeed its smooth-locus fiber is

\[
 H^{d+1}(Y_b,\mathbf Q).
\]

By Poincare duality on the smooth \(d\)-fold \(Y_b\), this is dual to
\(H^{d-1}(Y_b,\mathbf Q)\), and weak Lefschetz identifies the latter with
the corresponding ambient cohomology. Hence it is a constant ambient local
system, not an absent term.

## Consequence for the support argument

B117 removes divisor support inside \(E_\infty^{-1,0}\), and B118 removes
\(E_\infty^{0,-1}\). Neither theorem removes
\(E_\infty^{-2,1}\). Therefore a nonzero ordinary lift can lie entirely in
the constant ambient grade and have zero relation coordinate.

The smallest exact repair is B107-B109's filtered condition: the chosen
nearby class must admit a lift in the filtration step \(S_0\) whose
associated quotient is \(E_\infty^{-1,0}\). Only after this condition is
proved do B117 and the conditional form of B119 make a nonzero relevant
coordinate full-support and type \((0,0)\).

## Scope guard

B121 does not show that the selected B058 class lands in the ambient grade;
it shows that the existing inputs do not exclude that possibility. A
primitive ambient pairing does not itself provide a canonical projection
away from this grade. The actual filtered extension class remains geometric
data, exactly as B108-B109 state.
