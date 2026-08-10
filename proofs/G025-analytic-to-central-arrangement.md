---
brick_id: G025
status: NO-GO
base_field: C
variety: a germ of a q-block nodal smoothing slice and its discriminant, compared with the central arrangement of its node-smoothing linear forms
smoothness: the smoothing base is smooth, nearby fibers are smooth, and the central fiber has only ordinary double points
projectivity: the motivating family is projective; the comparison is local analytic on the parameter base
dimension: arbitrary finite parameter dimension and q at least 3
codimension: middle codimension n on the ambient 2n-fold; node strata have their expected smoothing codimensions
coefficient_field: Q
cohomology_theory: rational local intersection complexes, Picard-Lefschetz local systems, and analytic stratified equivalence
hodge_type: the comparison must preserve the rational type-(0,0) relation channel after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B009-B010, B028, B052, G015, G019, and NG036
claim: Every q-block quasi-local nodal smoothing germ satisfying G015's independent-block hypotheses is stratified-analytically equivalent, for its degree-one IC channel and rational Hodge structure, to a representable central arrangement covered by G019.
falsifier: nonlinear discriminant terms or nonversal directions that preserve all block hypotheses but change the degree-one IC stalk, its rational lattice, or its Hodge filtration relative to the tangent central arrangement
---

# G025 - Analytic-to-central-arrangement comparison

B052 proves the complete relation channel for central representable
arrangements. G015 is stated for a quasi-local nodal smoothing germ, so a
promotion still requires an explicit comparison rather than silently
replacing the analytic discriminant by its tangent arrangement.

NG036 disproves the asserted analytic equivalence. Five smooth plane
branches with distinct tangent lines satisfy Green-Griffiths' quasi-local
coordinate condition, yet their quadratic curvatures carry analytic moduli
not present in the tangent line arrangement. The example is the pullback of
a projective five-node family, so projectivity does not remove the
obstruction.

This does not show that the degree-one IC channel changes. The justified
replacement is G026: prove invariance of precisely the rational IC/MHS
channel under deformation to the tangent arrangement, without asserting an
analytic equivalence that is false.
