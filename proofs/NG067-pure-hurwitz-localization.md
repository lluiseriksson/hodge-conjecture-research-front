---
brick_id: NG067
status: NO-GO
base_field: C with rational homology
variety: an arbitrary polarized smooth projective complex 2n-fold, a B058 detector, and a marked collision to a clean nodal hyperplane
smoothness: ambient and reference fibers smooth; target has normal-crossing independently smoothable ordinary double points
projectivity: ambient hyperplane family, plane net, and collision algebraic/projective
dimension: ambient 2n; hyperplane fibers 2n-1
codimension: middle codimension n; target nodal stratum of positive codimension
coefficient_field: Q
cohomology_theory: relative thimble homology, Picard-Lefschetz monodromy, B022 quotients, and primitive ambient homology
hodge_type: input ambient detector type (0,0) after Q(n); no target type is obtained
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B088-B091, G054
claim: Pure marked Hurwitz transport can carry a nonzero B058 detector chain to the positive total boundary extension of the target nodal cluster.
falsifier: B091's contradiction between preservation of the chain and B090's target vanishing
---

# NG067 — Pure Hurwitz transport cannot localize the detector

**Status:** NO-GO

The valid part of the route is that Hurwitz moves preserve the geometric B057
extension when the loop, marking, and input class return exactly. The invalid
step is to identify that preserved nonzero chain with the extension around the
positive total boundary of the target nodal cluster. B090 makes the latter
extension zero for every fixed input class, and B091 gives the contradiction.

The re-entry condition is G055: construct the actual nearby-to-special
comparison and exhibit a nonzero topology-changing correction in the local
relation channel, with rational Hodge type, B022 survival, and prescribed
pairing checked separately.
