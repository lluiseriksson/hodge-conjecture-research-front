---
brick_id: G034
status: EXPLORATORY
base_field: C
variety: a proper target modification resolving the cusp discriminant of the A2 recollision chart, together with the pulled-back and resolved family
smoothness: the modified boundary must be simple normal crossing and the total family must carry an explicit smooth or stratified model
projectivity: the local modification is proper; a global use requires a projective algebraic compactification compatible with the original family
dimension: arbitrary suspended fiber dimension and a two-dimensional parameter base
codimension: boundary components are codimension one; the terminal cycle remains codimension p on the original smooth projective variety
coefficient_field: Q for mixed Hodge modules and target Hodge classes
cohomology_theory: mixed Hodge modules, nearby and vanishing cycles, proper direct image, and primitive ambient homology
hodge_type: rational type (0,0) after the relevant Tate twist
cycle_class_map: CH^p(X)_Q -> H^(2p)(X,Q(p))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B063, B064, G033, NG043, and S042
claim: After an explicit resolution of the A2 cusp boundary, a strict multispecialisability comparison descends to the original recollision and preserves the quotient-level detector pairing without exceptional-only support.
falsifier: failure of strict multispecialisability on every suitable resolution, noncanonical descent, or a nonzero detector term supported only on the exceptional boundary and killed on the target fiber
---

# G034 — Resolved \(A_2\) comparison and descent

**Status:** EXPLORATORY  
**Parent gate:** G033

## Falsifiable theorem target

For the chart in B064, construct a proper modification of the parameter plane resolving the cusp discriminant and a compatible modification of the family such that:

1. the total boundary is simple normal crossing and the exact pulled-back mixed Hodge module is strictly \(R\)-multispecialisable along its components;
2. B063 and Kochersperger's proper-direct-image theorem produce a rational mixed-Hodge comparison independent of the resolution flag;
3. pushing the comparison to the original base intertwines the B022 quotient maps and the Saito ambient map;
4. the nonzero pairing with the prescribed \(\zeta\) is carried by the target nodal relation, not solely by a summand supported on an exceptional divisor or the \(A_2\) fiber.

Any failure is a falsifier for this proposed bridge.

## Attempt 1 — no target modification

This is NG043. The raw discriminant is cuspidal, and B064 proves that the critical locus is not over the coordinate boundary. The without-slopes theorem cannot be invoked.

## Smallest next calculation

B065 completes the embedded-resolution calculation: three point blowups give
an SNC divisor with exceptional multiplicities \((2,3,6)\). G035 is now the
smallest obligation: test the pulled-back graph Hodge module against strict
\(R\)-multispecialisability on those exact charts and glue the comparisons.
Even a positive local result must then pass items 3-4; normal crossings alone
are not a descent or pairing theorem.

## Propagation boundary

G034 would settle only the simplest \(A_2\) transition inside G033. Arbitrary singular detectors and multipart recollisions would still require reduction to this chart or additional local models. It is not a proof of G032, G031, or the Hodge Conjecture.
