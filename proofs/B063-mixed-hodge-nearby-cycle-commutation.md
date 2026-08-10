---
brick_id: B063
status: PROVED
base_field: C, with the rational structure carried by mixed Hodge modules
variety: a complex manifold X times a p-dimensional polydisk with coordinate divisors
smoothness: the ambient product is smooth; the mixed Hodge module may have singular support
projectivity: not required for commutation; proper or projective hypotheses enter the separate direct-image statements
dimension: arbitrary finite dimension and arbitrary finite p
codimension: each coordinate divisor has codimension one; this is not a cycle-codimension theorem
coefficient_field: Q for the perverse-sheaf realization and C for the filtered D-module realization
cohomology_theory: mixed Hodge modules and their nearby- and vanishing-cycle functors
hodge_type: the comparison is an isomorphism of mixed Hodge modules and therefore preserves rational Hodge filtrations and type (0,0) classes, when defined
cycle_class_map: none
cycle_equivalence: none
scope: relative and fiberwise
dependencies: Kochersperger arXiv:1808.10719v1, audited as S042, and B061
claim: If the underlying D-module pair is without slopes, all permutation orders of iterated nearby cycles are isomorphic in the category of mixed Hodge modules.
falsifier: a mixed Hodge module satisfying the stated without-slopes hypothesis for which Corollary 6.2's comparison fails in MHM
---

# B063 — Mixed-Hodge commutation under the without-slopes hypothesis

**Status:** PROVED (imported conditional theorem; no algebraic cycle is constructed)  
**Gate:** G033 / G034  
**Primary source:** S042

## Mathematical type record

- **Base field:** \(\mathbf C\), with the rational realization built into the mixed Hodge module.
- **Variety/class:** \(X\times\Delta^p\) with coordinate divisors \(H_i=\{t_i=0\}\) and \(\mathcal M\in MHM(X\times\Delta^p)\).
- **Smoothness/projectivity:** the ambient product is smooth; projectivity is not needed for Corollary 6.2. Proper/projective hypotheses occur only in later direct-image results.
- **Dimension:** arbitrary finite \(\dim X\) and \(p\).
- **Codimension:** coordinate hypersurfaces are codimension one; there is no target algebraic-cycle codimension.
- **Coefficient field:** \(\mathbf Q\) on the perverse-sheaf side and \(\mathbf C\) on the filtered \(\mathcal D\)-module side.
- **Cohomology theory:** mixed Hodge modules, iterated nearby cycles, and iterated vanishing cycles.
- **Hodge type:** the comparison is internal to \(MHM\); induced maps on cohomology preserve rational mixed Hodge structures and hence rational type \((0,0)\).
- **Cycle class map:** none.
- **Equivalence relation on cycles:** none.
- **Scope:** relative and fiberwise.

## Imported theorem

Kochersperger's Theorem 6.1 treats two coordinates. Corollary 6.2 states that if the pair \((H,M)\) is without slopes for the right \(\mathcal D\)-module \(M\) underlying \(\mathcal M\), then for every permutation \(\sigma\),
\[
 \Psi_{t_1}^{HM}\cdots\Psi_{t_p}^{HM}\mathcal M
 \simeq
 \Psi_{t_{\sigma(1)}}^{HM}\cdots
 \Psi_{t_{\sigma(p)}}^{HM}\mathcal M.
\]
The analogous vanishing-cycle statement is included in the paper's Theorem A. The proof constructs the comparison in the category of mixed Hodge modules and detects its invertibility on the underlying \(\mathcal D\)-modules.

## Exact gain for G033

Conditional on verifying without slopes for the **actual** recollision coefficient object, G033's order comparison and rational Hodge lift are available together. No separate passage from a complex perverse sheaf to a rational mixed Hodge structure is needed.

## Remaining boundary

- The theorem does not prove the without-slopes hypothesis.
- Its proper-direct-image result, Theorem 8.1, assumes the stronger strict \(R\)-multispecialisability condition; without slopes alone cannot silently be pushed through a resolution.
- The theorem does not mention B022's quotient maps, Saito's ambient detector map, or the pairing with \(\zeta\). Compatibility of those maps remains G033(3)-(4).
- No algebraic cycle is produced, so this is not progress toward terminal algebraicity by itself.

