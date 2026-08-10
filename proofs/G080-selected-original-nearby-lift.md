---
brick_id: G080
status: EXPLORATORY
base_field: C with collision and Hodge data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified primitive rational Hodge class zeta, its selected B058 detector, and the original smooth plane-net incidence family
smoothness: X and incidence total space smooth; nearby hyperplane fibers smooth; collision target has finitely many isolated hypersurface singularities
projectivity: X, plane net, incidence family, and pushdown projective
dimension: dim_C X = 2n; hyperplane fibers dimension 2n-1; plane base dimension 2; collision curve dimension 1
codimension: middle cycle codimension n; collision target is a base point and singularities are isolated in the fiber
coefficient_field: Q
cohomology_theory: relative thimble chains, B022 quotient homology, original nearby and special mixed Hodge-module stalks, local invariant cycles, and vanishing-cycle obstruction
hodge_type: selected source, nearby class, and ordinary lift rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B059, B081-B084, B110-B118, G047-G048, G073-G079, NG059-NG060, NG086-NG094, S022, S037
claim: Construct a collision-certified nonzero nearby class t_psi in the original incidence object from the selected B058 detector, prove can(t_psi)=0, and construct a rational type-(0,0) ordinary special lift beta; B117-B118 then force beta's relevant perverse coordinate to be nonzero and full-support.
falsifier: undefined source realization, zero nearby class, nonzero vanishing-cycle obstruction, absence of an ordinary lift, wrong rational Hodge type, or loss of selected detector provenance
---

# G080 — Construct the selected nearby class and ordinary lift downstairs

**Status:** EXPLORATORY  
**Parent gates:** G079 / G073

The two support ambiguities are now structural:

- B117 eliminates divisor support in \({}^pH^0\);
- B118 eliminates point support in \({}^pH^{-1}\).

Thus G079 no longer needs a separate associated-grade multiplicity
calculation. It remains to construct, on the original incidence object, a
single nonzero class

\[
 t_\psi\in H^{-1}(i_p^*\Psi K)^{(0,0)}
\]

with a collision certificate from the selected B057 chain, prove

\[
 \operatorname{can}(t_\psi)=0,
\]

and choose

\[
 0\ne\beta\in H^{-1}(i_p^*K)^{(0,0)},
 \qquad u(\beta)=t_\psi.
\]

Nonzeroness of \(t_\psi\) forces nonzeroness of every lift. B081 together
with B117-B118 then places a nonzero component in
\(E_\infty^{-1,0}\), already in full support.

## Current obstruction

B084 supplies the lift after collision-monodromy invariance is proved, but
it does not realize B058's distributed detector in the original nearby
object or show that realization nonzero. Pure Hurwitz localization is zero
by B090-B091. The missing datum is the topology-changing selected excess of
G074, with its original-downstairs image and rational type retained.
