---
brick_id: G036
status: EXPLORATORY
base_field: C
variety: a total-space resolution or semistable alteration of the B066 pulled-back A2 family over the B065 resolved base
smoothness: the sought total space is smooth and the relevant boundary fiber is SNC; these are conclusions to prove
projectivity: the alteration and resolution must be proper, and a global application must remain projective over the parameter base
dimension: two-dimensional base and arbitrary suspended fiber dimension
codimension: boundary components are divisors; the terminal target cycle has codimension p
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, nearby cycles, proper direct image, and primitive ambient homology
hodge_type: rational type (0,0) after the relevant Tate twist
cycle_class_map: CH^p(X)_Q -> H^(2p)(X,Q(p))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B063, B065-B066, G035, and NG045
claim: A proper semistable model of the resolved A2 family carries a strictly multispecialisable rational Hodge module whose pushdown is the intended family module and whose comparison preserves the quotient-level detector pairing.
falsifier: unavoidable non-semistable singularities, required ramified base change that destroys descent, extra summands carrying all detector pairing, or failure of filtered proper-direct-image compatibility
---

# G036 — Semistable Hodge-module model for the resolved \(A_2\) family

**Status:** EXPLORATORY  
**Parent gates:** G035 / G034

## Falsifiable theorem target

Starting from either explicit equation in B066, construct a proper modification, and if indispensable a stated finite base change, such that:

1. the total space is smooth and the inverse image of the resolved boundary is an SNC divisor;
2. the chosen rational Hodge module is strictly \(R\)-multispecialisable for every local pair of boundary equations;
3. proper pushdown recovers the intended nearby-cycle object on the original \(A_2\) family, with all decomposition-theorem summands labeled by support;
4. any finite base-change trace or invariant operation is defined over the stated field and does not replace rational classes by an unjustified integral or complex statement;
5. the B022 quotient class and nonzero Saito pairing survive in the full-support summand rather than only on an exceptional component.

## Attempt 1 — use the raw base pullback

Failed by B066. Both final charts have positive-dimensional singular loci over their boundary axes. NG045 records why base SNC alone is insufficient.

## Attempt 2 — use the Weyl root cover

B067 makes the finite cover explicit and replaces the cusp by the \(A_2\)
reflection arrangement, but the raw total family remains singular along all
three pair-collision sections. B068 provides simultaneous resolution for a
surface rational double point only. NG046 shows that this dimension never
matches the odd-dimensional hyperplane fibers in the middle-degree route.
G037 isolates the missing dimension-uniform extension and rational descent.

## Smallest next calculation

Analyze B067's factorized root-cover equation in arbitrary odd fiber
dimension and determine whether a functorial \(S_3\)-equivariant weighted
resolution exists. Determine the exceptional strata, their monodromy, and
whether a rational full-support summand descends. This is G037; no such
dimension-uniform construction is yet proved in this repository.
