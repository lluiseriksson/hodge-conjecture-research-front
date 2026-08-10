---
brick_id: NG070
status: NO-GO
base_field: C with rational type-(0,0) Hodge structures
variety: an arbitrary projective one-parameter collision with a nonempty special-lift torsor for the specified B058 detector
smoothness: generic fiber smooth; special target clean nodal
projectivity: collision projective
dimension: ambient 2n; hyperplane fibers 2n-1
codimension: middle codimension n
coefficient_field: Q
cohomology_theory: nearby/special exactness, perverse filtration, B022 quotient homology, and Saito pairing
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B059, B083, B094, G057
claim: Detection requires the entire special-lift ambiguity space to vanish under the canonical quotient-level pairing functional.
falsifier: B094's case F(beta_0)=0 and F(A) nonzero, where an ambiguity-adjusted detecting lift exists
---

# NG070 — Lift ambiguity need not be invisible

**Status:** NO-GO

G057 required every allowed change of special lift to die after the quotient
and pairing tests. That would make the detector value canonical, but the
terminal conjecture requires only existence of one nonorthogonal local
detector.

B094 proves the precise alternative. If the ambiguity image under the scalar
detector functional is nonzero, then some ambiguity adjustment produces a
nonzero pairing even when the chosen base lift has zero pairing. Requiring
that image to vanish would discard this successful case.

The re-entry condition is G058: compute the affine image of the entire
type-$(0,0)$ lift torsor and prove it is not the singleton $\{0\}$.
