---
brick_id: NG179
status: NO-GO
base_field: C
variety: a smooth non-linear projective complex 2n-fold in the G146 branch and its possibly nonnormal Gauss image
smoothness: X is smooth; smoothness or normality of the Gauss image is not available
projectivity: the ordinary Gauss morphism is finite projective and birational onto its image
dimension: the general Gauss fiber is one point, but G146 asks about a deliberately special zero-dimensional fiber with D_(2n)(m) points
codimension: generic contact-locus theorems and Zak's dimension inequality do not bound the length or cardinality of one special finite normalization fiber
coefficient_field: C for the Gauss map; Q detector data remain separate
cohomology_theory: none for the excluded inference; primitive rational and vanishing-cycle data remain required in G146
hodge_type: no type-(0,0) detector or specified pairing follows from finiteness or birationality
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not reached
cycle_equivalence: rational equivalence remains the terminal relation
scope: absolute
dependencies: B217-B218, G146, S078
claim: Conclude that G146 is impossible merely because the ordinary Gauss map is finite birational or because its general contact locus is a point.
falsifier: finite birational morphisms can have non-singleton fibers over nonnormal points, and S078 controls the dimension of every contact locus and the shape of a general one but states no cardinality bound for a special zero-dimensional fiber.
---

# NG179 — Generic Gauss rigidity does not bound the special fiber

- **Route:** use B218's finite birational Gauss map to declare every
  fiber a singleton and close G145.
- **Valid input:** every fiber is zero-dimensional and the general fiber
  is one reduced point.
- **Invalid inference:** a finite birational normalization morphism is
  injective over every nonnormal point of its image.

Zak's inequality applied to a \(2n\)-plane excludes a positive-dimensional
contact locus, but it is insensitive to the cardinality of a finite one.
The separable higher-Gauss theorem identifies the *general* contact locus;
G146 deliberately requires a special fiber.

- **Precise obstruction:** generic-versus-special fiber mismatch, plus
  absence of a special-fiber cardinality theorem.
- **Detector guard:** even a large Gauss fiber supplies none of G146's
  Hodge, relation, profile, or pairing data.
- **Re-entry condition:** prove a uniform bound for special fibers of the
  ordinary Gauss normalization map under the exact G146 hypotheses, or
  construct and then test such a fiber with every detector clause.
