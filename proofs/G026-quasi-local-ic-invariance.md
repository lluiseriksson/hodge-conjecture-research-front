---
brick_id: G026
status: EXPLORATORY
base_field: C
variety: a Green-Griffiths quasi-local normal-crossing nodal smoothing germ and the central arrangement of its tangent smoothing forms
smoothness: the base and discriminant branches are smooth and their intersections satisfy the quasi-local coordinate condition; nearby fibers are smooth and the central fiber is nodal
projectivity: the motivating family is projective; the comparison is local analytic on its base
dimension: arbitrary finite parameter dimension and any number of smoothing blocks
codimension: discriminant strata have the codimensions in the quasi-local definition; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: rational intersection complexes, Picard-Lefschetz local systems, deformation to the normal cone, and mixed Hodge modules
hodge_type: the comparison must preserve the pure type-(0,0) degree-one channel after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B009-B010, B052, G015, G019, G025, and NG036
claim: Although a quasi-local discriminant need not be analytically linearizable, its degree-one rational intermediate-extension stalk and mixed Hodge structure are canonically invariant under deformation to the tangent central arrangement, compatibly with the vanishing-cycle relation map.
falsifier: a quasi-local equisingular deformation whose degree-one IC dimension, rational lattice, Hodge filtration, or canonical map to the vanishing-cycle relation space changes between the curved and tangent fibers
---

# G026 - Quasi-local IC invariance without linearization

NG036 rules out simultaneous analytic straightening. The remaining theorem
needed for G015 is weaker: construct a deformation-to-the-normal-cone family
from the curved divisor germ to its tangent arrangement and prove that the
degree-one intermediate-extension channel is locally constant as a rational
mixed Hodge structure.

A valid proof must supply a Whitney/Thom stratification for the whole
deformation, identify the Picard-Lefschetz local system on the complements,
and show that nearby-cycle specialization commutes with intermediate
extension in the required degree. Topological constancy alone does not
automatically identify the Hodge filtration, while equality of tangent cones
alone does not give topological constancy. B052 applies only after this
comparison is established.
