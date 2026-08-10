---
brick_id: NG040
status: NO-GO
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold and a deformation of an isolated singular hyperplane section to its Morse critical points
smoothness: X and nearby general hyperplanes are smooth; the source has an isolated singularity and the morsified critical fibers have one ordinary double point each
projectivity: X and the hyperplane deformation are projective
dimension: dim_C X = 2n and hyperplane fibers have dimension 2n-1
codimension: middle codimension n; the separate Morse values lie on the smooth codimension-one discriminant locus
coefficient_field: Q
cohomology_theory: Milnor homology, Picard-Lefschetz theory, vanishing cycles, and local intersection cohomology
hodge_type: the desired detector would have rational type (0,0) after Q(n), but the morsified one-node stalk channel is zero
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B008, B010, B025, and G032
claim: Generic morsification and conservation of Milnor number cannot by themselves be used to transfer a detecting isolated singularity to a clean nodal Saito detector.
falsifier: a theorem deriving a nonzero one-fiber nodal relation and preserved specified pairing solely from the distinguished morsification basis and conservation of Milnor number
---

# NG040 - Generic morsification does not preserve one-fiber detection

## Failed route

Start with a detecting isolated singularity, morsify it into ordinary double
points, and infer that one of the resulting nodal fibers—or the collection
of their separate critical values—retains the local Saito detector.

## Failure point

B025 identifies the \(\mu\) distinguished cycles of the morsification as an
integral basis of the local Milnor lattice. Hence the local morsification
creates no relation among them. The Morse critical values occur separately
at smooth points of the discriminant, where B008 proves that the rational
degree-one local intersection-cohomology channel is zero.

Conservation of total Milnor rank tracks the number of local generators. It
does not create the global kernel relation required by B010, identify a
primitive ambient image, or preserve its pairing with \(\zeta\).

## Scope guard

This does not prove that a deliberate recollision or another nodalization is
impossible. It excludes only generic morsification, together with rank
conservation, as a sufficient transfer theorem.

## Re-entry condition

Supply a topology-changing comparison that recollides the Morse data at one
clean discriminant point and computes the induced map on the full
nearby-cycle complex, including the B022 quotient class, rational Hodge type,
and specified pairing. This is the unresolved content of G032.
