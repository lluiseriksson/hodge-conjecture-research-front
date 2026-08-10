---
brick_id: NG076
status: NO-GO
base_field: C with rational homology
variety: an arbitrary isolated-singularity projective collision in Saito's good-retraction setting
smoothness: nearby fiber smooth; target has isolated singularities
projectivity: collision and ambient family projective
dimension: ambient 2n; hyperplane fibers 2n-1
codimension: middle codimension n
coefficient_field: Q
cohomology_theory: relative homology, primitive Lefschetz decomposition, B022 quotients, and Saito ambient map
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B099-B100, G063
claim: To recover B057's primitive ambient detector from Saito's construction, the chosen relative cycle must equal the B057 representative through both B022 quotient coordinates.
falsifier: B100's primitive equality for any two relative lifts with the same local boundary
---

# NG076 — Literal same-chain equality is unnecessary

**Status:** NO-GO

G063 required equality of relative representatives and separate equality in
both B022 kernel coordinates. B100 proves this is stronger than Saito's
primitive ambient construction requires. Any two relative lifts of the same
local relation differ by nearby-fiber homology, and its ambient image is
nonprimitive.

The minimal re-entry condition is G064: map the B057 detector into Saito's
relative group, identify its boundary with the canonical relation coordinate,
and retain compatibility with ambient pushforward. Literal representative or
kernel-coordinate equality is not required.
