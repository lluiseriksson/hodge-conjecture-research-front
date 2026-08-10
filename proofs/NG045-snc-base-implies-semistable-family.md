---
brick_id: NG045
status: NO-GO
base_field: C
variety: the A2 recollision family after the B065 log resolution of its cusp discriminant
smoothness: the modified base and reduced discriminant are SNC, while the raw total family remains singular over the E3 and E2 boundary sections by B066
projectivity: not relevant to the local obstruction
dimension: two-dimensional base and arbitrary suspended fiber dimension
codimension: singular sections lie over the E3 and E2 boundary divisors
coefficient_field: Q for the intended Hodge module and C for the local equations
cohomology_theory: mixed Hodge modules and nearby cycles in the rejected inference
hodge_type: none; the route fails before type preservation
cycle_class_map: none
cycle_equivalence: none
scope: relative
dependencies: B065-B066 and G035
claim: Resolving the discriminant divisor in the base does not by itself produce a smooth or semistable total family or verify strict multispecialisability.
falsifier: smoothness of the raw pulled-back hypersurface along the displayed E3 and E2 sections
---

# NG045 — SNC discriminant does not imply a semistable total family

**Status:** NO-GO

## Rejected route

Use B065's SNC total transform of the cusp as if it automatically made the pulled-back \(A_2\) family smooth with a normal-crossing central fiber, then apply normal-crossing Hodge-module theory.

## Precise obstruction

B066 writes both final pullback equations and computes their full Jacobian
singular loci. The family remains singular along the \(E_3\) and \(E_2\)
sections (while it is smooth over generic \(E_1\)). The base divisor and the
total family are different geometric objects; resolving the former does not
resolve the latter.

## Re-entry condition

Construct a total-space resolution or semistable alteration, specify the resulting rational mixed Hodge module, and prove that its proper pushdown gives the intended family object and detector map. This is G036.
