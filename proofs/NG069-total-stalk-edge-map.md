---
brick_id: NG069
status: NO-GO
base_field: C with rational Hodge-module coefficients
variety: the proper plane-net collision pushdown for an arbitrary polarized smooth projective complex 2n-fold
smoothness: generic hyperplane fibers smooth; special target clean nodal; semistable source regular where used
projectivity: collision and proper pushdown projective
dimension: ambient 2n; hyperplane fibers 2n-1; plane base 2
codimension: middle codimension n; target point codimension 2 in the plane base
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, derived direct image, perverse filtration, strict support, and local intersection cohomology
hodge_type: target relation type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B081, B092-B093, G056
claim: The decomposition theorem canonically supplies a total-stalk morphism from H^(-1)(i_H^*K) directly to the local relation group H^(-1)(i_H^*P).
falsifier: B081's noncanonical derived splitting and B093's required associated-grade-then-strict-support route
---

# NG069 — There is no canonical total-stalk edge map

**Status:** NO-GO

G056 asked for a morphism from the total special stalk directly to the local
relation group. B081 proves that a derived decomposition of the proper
pushdown is noncanonical. B093 identifies the correct target but also the
only canonical route to it: perverse associated grade first, strict-support
projection second.

Choosing a derived splitting could manufacture a map, but its detector
coordinate would depend on that choice and would not be auditable. G057 is
the re-entry condition: prove the specified class lands nontrivially in the
canonical grade and full-support summand.
