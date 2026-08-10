---
brick_id: G026
status: PROVED
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
dependencies: B009-B010, B043, B052-B053, G015, G019, G025, and NG036
claim: Although a quasi-local discriminant need not be analytically linearizable, its degree-one rational intermediate-extension stalk and mixed Hodge structure are canonically invariant under deformation to the tangent central arrangement, compatibly with the vanishing-cycle relation map.
falsifier: a quasi-local equisingular deformation whose degree-one IC dimension, rational lattice, Hodge filtration, or canonical map to the vanishing-cycle relation space changes between the curved and tangent fibers
---

# G026 - Quasi-local IC invariance without linearization

NG036 rules out simultaneous analytic straightening. B053 proves the weaker
invariant-channel theorem directly. Blowing up the common stratum gives a
one-step SNC resolution whose exceptional normal fiber is the uniform
tangent arrangement. The divisor incidences, monodromy residues, coefficient
sheaves, transgression, and degree-one support bound depend only on the
normal covectors. Both the curved germ and tangent model are canonically the
same rational type-\((0,0)\) relation kernel.

This closes the exact Green-Griffiths quasi-local case. It does not yet cover
the nonuniform cross-block dependencies allowed by G015's proposed
multipart analogue; that clean-arrangement comparison is G027.
