---
brick_id: NG079
status: NO-GO
base_field: C with rational homology
variety: Saito's isolated-singularity projective degeneration after a good retraction has been fixed
smoothness: nearby fiber smooth; special fiber has finitely many isolated singularities
projectivity: degeneration and ambient variety projective
dimension: ambient 2n; hyperplane fibers 2n-1
codimension: middle codimension n; singular support finite
coefficient_field: Q
cohomology_theory: good retraction, relative singular homology, Milnor collapses, and primitive ambient realization
hodge_type: no new Hodge assertion
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B102-B103, G066, S022 Section 2.5, S049
claim: Even after Saito's Section 2.5 good retraction is fixed, G065 still requires a separate construction gluing independent local vanishing-polyhedron collapses to an exterior trivialization.
falsifier: B103's global good retraction, which is already an isomorphism off the singular set and defines the relative pair used by Saito
---

# NG079 — Separate collapse gluing is not the remaining gate

**Status:** NO-GO

G066 treated the S049 local collapses and exterior trivialization as maps
still needing to be glued after Saito's setup was fixed. B103 shows that this
duplicates the global good-retraction datum already assumed and constructed
in S022 §2.5.

The genuine missing arrow precedes the retraction: B057's detector is a
relative chain in a total thimble complex over a nonlocal word, whereas
Saito begins with a relative class in the single nearby-fiber pair
$(Y_c,Z_c)$. G067 must construct that realization. Rebuilding the good
retraction does not define it.
