---
brick_id: NG066
status: NO-GO
base_field: C with rational homology
variety: an arbitrary polarized smooth projective complex 2n-fold and a B089 marked local disk around an independent-node hyperplane
smoothness: ambient and reference fibers smooth; central fiber nodal with normal-crossing discriminant branches
projectivity: ambient hyperplane system and marked plane net projective
dimension: ambient 2n; hyperplane fibers 2n-1; plane-net base 2
codimension: middle codimension n; nodal stratum codimension equal to its number of branches
coefficient_field: Q
cohomology_theory: Picard-Lefschetz monodromy, tube and thimble maps, and B022 quotients
hodge_type: no nonzero detector class is produced, so no type-(0,0) promotion occurs
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B057, B089-B090, G053
claim: A class fixed by the positive total boundary loop of the B089 local nodal disk can have a nonzero B057 extension surviving to an ambient detector.
falsifier: B090's sum-of-squares vanishing for every such fixed class
---

# NG066 — The total local nodal boundary cannot be the detector loop

**Status:** NO-GO

G053 proposed replacing the global B058 pair by a class fixed under the
positive boundary of B089's local collision disk. B090 proves that every
Picard-Lefschetz coefficient of such a fixed class is zero. Its B057 ordered
thimble extension is therefore zero before either B022 quotient and cannot
pair nontrivially with any Hodge class.

The obstruction is not the possible vanishing of the local relation space:
that space may be nonzero. The obstruction is that the coefficient vector
of a boundary-fixed fiber class lies simultaneously in the relation space
and its positive-definite rational orthogonal complement.

The re-entry condition is G054: retain a nonlocal distributed detector word
and compare it through the collision, instead of replacing it by the positive
total boundary of the target nodal cluster.
