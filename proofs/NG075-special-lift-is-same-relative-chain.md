---
brick_id: NG075
status: NO-GO
base_field: C with rational homology and Hodge-module coefficients
variety: an arbitrary projective collision with a B083 special lift, B057 nearby detector, and isolated clean nodal special target
smoothness: nearby fiber smooth; target nodal; good retraction available after choosing the local model
projectivity: collision and ambient family projective
dimension: ambient 2n; hyperplane fibers 2n-1
codimension: middle codimension n; target singular locus finite
coefficient_field: Q
cohomology_theory: nearby/special stalks, relative homology, good retraction, B022 quotients, and Saito ambient map
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B083, B099, G062
claim: Any B083 special-stalk lift of the B057 nearby class automatically has local relation coordinate equal to the boundary of the same B057 relative chain in Saito's good-retraction model.
falsifier: nonunique special lifts or relative-cycle lifts differing by kernel classes whose local boundaries or ambient images are not identified
---

# NG075 — A cohomological lift is not yet the same relative chain

**Status:** NO-GO

B083 gives a preimage in a stalk cohomology group after the canonical
vanishing-cycle obstruction is killed. Saito §2.5 instead starts with a
specific relative homology class $\gamma'$ whose boundary is the local
relation. Neither construction canonically identifies those representatives.

The ambiguity is material: B083 lifts form a torsor, and relative lifts of a
fixed boundary can differ by absolute or B022-kernel classes. B099 applies
only after the same-chain comparison is proved.

B100/NG076 remove literal chain equality. The re-entry condition is G064:
construct the relative comparison, identify its boundary, and retain the
primitive ambient pushforward.
