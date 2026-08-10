---
brick_id: NG044
status: NO-GO
base_field: C
variety: the A2 plane cusp and its one-parameter normalization, compared with the two-parameter recollision family
smoothness: the normalization is smooth; the cusp is singular; the recollision total space is smooth
projectivity: not required; this is a local analytic statement
dimension: the cusp has dimension one inside a two-dimensional parameter base
codimension: the cusp is a divisor in the base
coefficient_field: Q for mixed Hodge modules and C for filtered D-modules
cohomology_theory: mixed Hodge modules, V-filtrations, and nearby cycles
hodge_type: rational mixed-Hodge type is controlled only for the functors actually covered by the source theorem
cycle_class_map: none
cycle_equivalence: none
scope: relative
dependencies: B063-B065 and Kochersperger Proposition 10.2/Corollary 10.3 in S042
claim: The quasi-ordinary cusp application in S042 does not supply the required two-coordinate recollision comparison.
falsifier: a theorem in the cited result applying Proposition 10.2 simultaneously to both ambient cusp coordinates and identifying the resulting comparison with G033's two-parameter detector maps
---

# NG044 — The quasi-ordinary cusp theorem is not the two-parameter comparison

**Status:** NO-GO

## Rejected route

Observe that the plane cusp is quasi-ordinary and cite Kochersperger's Proposition 10.2 and Corollary 10.3 as an automatic proof of G034.

## Precise mismatch

For a quasi-ordinary hypersurface of dimension \(p\), Proposition 10.2 uses a finite parametrization from \(\mathbf C^p\) and proves strict multispecialisability along the first \(p\) coordinate hyperplanes in its ambient space. A plane cusp has \(p=1\). The result therefore controls one selected coordinate filtration for the normalized cusp-supported Hodge module. G033 instead requires a comparison for the two independent recollision parameters, together with the pulled-back family coefficient object, B022 quotients, and the Saito pairing.

The theorem is relevant local technology, but its object, number of coordinate functions, and target maps do not match the gate.

## Re-entry condition

Prove a two-boundary-component strict-multispecialisability statement chart by chart on B065's log resolution and a descent theorem for the actual family Hodge module. This is G035 inside G034.

