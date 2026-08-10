---
brick_id: NG048
status: NO-GO
base_field: C
variety: a weakly semistable projective family with a finite group action and its functorial absolute resolution
smoothness: B070 makes the total space smooth but supplies no relative local-form theorem
projectivity: the resolution is a projective sequence of blowups
dimension: arbitrary
codimension: terminal cycles have codimension n; resolution centers vary
coefficient_field: Q for intended Hodge applications
cohomology_theory: rational mixed Hodge modules and nearby cycles
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative
dependencies: B069-B070, G038, and S044-S045
claim: Absolute equivariant desingularization cannot be assumed to preserve weak semistability or the detector comparison of the original morphism.
falsifier: a relative theorem showing Temkin's exact centers preserve toroidality, equidimensionality, reduced fibers, strict multispecialisability, and the detector trace
---

# NG048 — Absolute resolution is not relative semistable resolution

**Status:** NO-GO

## Rejected route

Apply B070 to B069's weakly semistable total space and infer that the resulting smooth equivariant total space is automatically a semistable family with the same nearby-cycle detector.

## Precise obstruction

Temkin's functor is defined from the singularities of the absolute total scheme. The theorem does not constrain its centers relative to the toroidal map. A blowup of the total space can change fiber dimensions, introduce multiplicities, or destroy the saturated monoid maps responsible for reduced fibers. None of toroidality, equidimensionality, reducedness of every fiber, or compatibility with the prior nearby-cycle comparison appears in S045's theorem.

## Re-entry condition

Prove G039: a group-equivariant relative toroidal desingularization/refinement that preserves the weakly semistable morphism and supports the rational MHM trace square.

