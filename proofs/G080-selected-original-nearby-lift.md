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
hodge_type: no type condition on the total nearby class or ordinary lift; B119 makes the nonzero relevant clean-nodal relation coordinate rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B059, B081-B085, B110-B120, G047-G048, G073-G079, G081-G082, NG059-NG060, NG086-NG096, S022, S037
claim: Construct a collision-certified nonzero rational nearby class t_Delta in one marked original collision disk from the selected B058 detector and kill its cyclic B085 obstruction; B120/B084 supply a rational ordinary lift, while B117-B119 force its relevant coordinate to be nonzero, full-support, and type (0,0).
falsifier: undefined source realization, zero nearby class, nonzero cyclic obstruction for every admissible disk, absence of an ordinary lift, non-clean-nodal target for B119, or loss of selected detector provenance
---

# G080 — Construct the selected nearby class and ordinary lift downstairs

**Status:** EXPLORATORY  
**Parent gates:** G079 / G073

The two support ambiguities are now structural:

- B117 eliminates divisor support in \({}^pH^0\);
- B118 eliminates point support in \({}^pH^{-1}\).

Thus G079 no longer needs a separate associated-grade multiplicity or Hodge
type calculation. It remains to construct, on the original incidence
object, a single nonzero rational class

\[
 t_\Delta\in H^0(i_p^*\Psi K_\Delta)
\]

with a collision certificate from the selected B057 chain and prove that it
is fixed by the cyclic monodromy of one marked original collision disk.
B120/B084 then prove

\[
 \operatorname{can}(t_\Delta)=0,
\]

and choose

\[
 0\ne\beta\in H^{-1}(i_p^*K),
 \qquad u_\Delta(\beta)=t_\Delta,
\]

Here \(\beta\) uses B120's canonical identification
\(H^0(i_p^*K_\Delta)=H^{-1}(i_p^*K_B)\). Nonzeroness of \(t_\Delta\)
forces nonzeroness of every lift. B081 together
with B117-B118 then places a nonzero component in
\(E_\infty^{-1,0}\), already in full support. B093/S022 and B119 prove that
this clean-nodal relation coordinate is automatically type \((0,0)\) after
\(\mathbf Q(n)\). NG095 records why requiring the total lift to have that
type was unnecessary.

## Current obstruction

B120/B084 supply the rational lift after cyclic disk-monodromy invariance is
proved, but they do not realize B058's distributed detector in the original
disk-nearby object or show that realization nonzero. Pure Hurwitz
localization is zero by B090-B091. G082 is the exact remaining gate inside G081: construct
the topology-changing selected excess on one original disk, prove its
nonzero downstairs B022 image, and kill its cyclic kernel-valued cocycle.
NG096 records why simultaneous invariance in every plane-local direction is
not required.
