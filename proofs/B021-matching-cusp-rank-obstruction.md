---
brick_id: B021
status: PROVED
base_field: C for the projective-surface comparison; the matching-path input is symplectic
variety: a smooth projective complex surface with a Lefschetz pencil, viewed also as a symplectic real four-manifold
smoothness: the ambient variety and reference fibers are smooth; the source has two Lefschetz critical fibers and the target cusp fiber has one isolated Milnor-number-two singularity
projectivity: required for the hyperplane-family target; not required for the matching-path source theorem
dimension: dim_C X = 2 and dim_R X = 4; the hyperplane fibers are complex curves
codimension: middle codimension 1 on X; the cusp is a codimension-two discriminant phenomenon in the audited general plane slice
coefficient_field: Q
cohomology_theory: singular homology, vanishing homology, Lefschetz thimbles, Milnor fiber intersection pairing, and specialization comparison
hodge_type: no type-(0,0) class is produced; the obstruction occurs before the Hodge-type test
cycle_class_map: CH^1(X)_Q -> H^2(X,Q(1)); no algebraic cycle or Saito detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B019 matching-pair homology and B020 cusp intersection-one independence
claim: No comparison that preserves the two individual rational vanishing-cycle classes can specialize an audited matching pair to Schnell's cusp/Milnor-number-two pair, because the source span has rank at most one while the target span has rank two.
falsifier: a rational homology comparison preserving both individual cycle classes that sends an equal-up-to-sign matching pair to a pair with intersection number one
---

# B021 - Matching/cusp rank obstruction

For a matching path in B019, orient the two isotopic vanishing cycles after
transport to the midpoint fiber. Their rational homology classes satisfy

\[
 [\delta_-]=\pm[\delta_+].
\]

Their span therefore has dimension at most one.

For the cusp/Milnor-number-two configuration in B020, Schnell's pair
\(\epsilon_1,\epsilon_2\) satisfies

\[
 (\epsilon_1,\epsilon_2)=1.
\]

It spans a two-dimensional rational subspace. Suppose a proposed collision
comparison preserved the two individual vanishing-cycle classes, up to
orientation, and sent the matching pair to this cusp pair. Linearity would
preserve the dependence relation, forcing
\([\epsilon_1]=\pm[\epsilon_2]\), contrary to their intersection-one
independence. Hence no such comparison exists.

## Exact scope

This is a rank obstruction to the simplest **class-by-class preserving**
collision. It does not rule out a more elaborate degeneration in which:

- the topology-changing collision uses more than a Hurwitz basis change
  within one fixed fibration (pure Hurwitz change is excluded by B023);
- extra vanishing cycles enter and only a larger combination specializes;
- the target is a higher singularity or an independent multi-node member
  rather than the cusp model; or
- only the resulting ambient tube class, rather than the individual fiber
  cycles, is preserved.

Any such route must explicitly compute the specialization map and show that
a nonzero rational type-\((0,0)\) relation survives. The cusp collision cannot
be used as an identity comparison between the matching pair and the local
relation pair.
