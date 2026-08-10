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
dependencies: B022, B057-B059, B081-B085, B092-B093, B107-B109, B110-B122, G047-G048, G071-G079, G081-G083, NG059-NG060, NG086-NG098, S022, S037
claim: Construct a collision-certified nonzero rational nearby class t_Delta in one marked original collision disk from the selected B058 detector, preserve both B022 quotients and the nonzero pairing, and prove t_Delta lies in u_Delta(S_0); B122 gives ordinary liftability and conditional B119 then controls the relation grade.
falsifier: undefined source realization, zero nearby class, death in a B022 quotient, zero prescribed pairing, nonzero filtered obstruction for every admissible disk, or non-clean-nodal target for B119
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

with a collision certificate from the selected B057 chain. B122 proves
directly, from isolated vanishing-cycle concentration, that

\[
 \operatorname{can}(t_\Delta)=0,
\]

and supplies an ordinary lift

\[
 0\ne\beta\in H^{-1}(i_p^*K),
 \qquad u_\Delta(\beta)=t_\Delta,
\]

Here \(\beta\) uses B120's canonical identification
\(H^0(i_p^*K_\Delta)=H^{-1}(i_p^*K_B)\). Nonzeroness of \(t_\Delta\)
forces nonzeroness of every lift. However B121 corrects B081's grade list:
the constant ambient \(E_\infty^{-2,1}\) term remains, so an arbitrary
nonzero lift need not have a relation coordinate. G083 must prove

\[
 t_\Delta\in u_\Delta(S_0),
\]

equivalently \(\omega_{\mathrm{fil}}(t_\Delta)=0\). Only then do B117-B119
make the nonzero relation coordinate full-support and type \((0,0)\) after
\(\mathbf Q(n)\).

## Current obstruction

B122 makes the full degree-$(d+1)$ nearby target cyclically invariant and
ordinarily liftable. NG098 therefore removes G082's raw thimble-cocycle
condition as unnecessary. Pure Hurwitz localization remains zero by
B090-B091. G083 is the exact remaining gate: construct the selected
disk-nearby class, preserve both B022 quotients and the prescribed pairing,
and kill its filtered—not monodromy—obstruction.
