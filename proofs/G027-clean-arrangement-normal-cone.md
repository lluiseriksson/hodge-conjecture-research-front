---
brick_id: G027
status: EXPLORATORY
base_field: C
variety: a nonlinear nodal discriminant germ whose smooth branch intersections form a clean subvariety arrangement, compared with its representable tangent hyperplane arrangement and wonderful model
smoothness: the base, branches, all clean intersection strata, and wonderful blow-up centers are smooth; the resolved boundary is required to be simple normal crossing
projectivity: the motivating nodal family and wonderful blow-ups are projective; the comparison is local analytic transverse to each stratum
dimension: arbitrary finite parameter dimension and any dimension-scaled number of blocks
codimension: arbitrary clean branch-intersection strata of codimension at least 2; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: rational intermediate extensions, Picard-Lefschetz local systems, normal cones, wonderful compactifications, and mixed Hodge modules
hodge_type: the comparison must preserve the pure type-(0,0) degree-one channel after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B052-B053, G015, G019, G026, Li S038, and Saito S022/S037
claim: For every clean nonlinear discriminant arrangement with representable tangent matroid, the wonderful resolution has the same degree-one rational IC/MHS channel as the tangent central arrangement, canonically equal to the full vanishing-cycle relation kernel.
falsifier: a clean stratum whose normal cone or dominant transform changes the labelled wonderful fiber, a higher-jet-dependent residue, a new degree-one coefficient or strict-support term, or failure of rational Hodge compatibility
---

# G027 - Clean-arrangement normal-cone comparison

B053 uses one common blow-up because the exact quasi-local tangent matroid is
uniform. G015's multipart analogue permits nonuniform dependencies across
blocks and requires several wonderful centers.

The next theorem must show inductively that blowing up a clean nonlinear
intersection stratum replaces its normal geometry by the corresponding
tangent flat, and that subsequent dominant transforms have the same labelled
normal wonderful fiber as the linear arrangement. It must then transport
B049-B052's divisor, coefficient, residue, and strict-support calculations.

Clean intersection alone may be insufficient for simultaneous compatibility
of every normal cone. The proof must either derive the required compatibility
from Li's subvariety-arrangement axioms or exhibit a curved clean arrangement
where the iterated normal data differs; such an example would be the precise
NO-GO for this route.
