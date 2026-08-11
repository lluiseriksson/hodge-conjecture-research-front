---
brick_id: NG130
status: NO-GO
base_field: C
variety: projective hypersurface maps with smooth total space, including B164's rank-deficient escape family and the universal complete-linear-system family
smoothness: total spaces are smooth; singular fibers may have ordinary double points
projectivity: all maps are projective and satisfy the decomposition theorem
dimension: arbitrary hypersurface dimension; arbitrary B159 uniform value rank R<N
codimension: positive-codimension discriminant supports survive in the decomposed direct image
coefficient_field: Q
cohomology_theory: rational decomposition theorem, semisimple perverse sheaves, proper base change, nearby cycles, and microsupport
hodge_type: pure Hodge-module summands may exist; no specified nonzero detector pairing follows
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) remains unresolved
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B161-B164 and G103-G104
claim: For a projective map with smooth total space, decomposition of the rational direct image into semisimple shifted intersection complexes forces its restriction to a smooth basis-node germ to have microsupport only in the zero section.
falsifier: B164 has smooth total space and a decomposed projective direct image, but one node escapes on F_B and B163 gives nonzero internal microsupport
---

# NG130 — Decomposition does not force zero microsupport

- **Route:** invoke projective decomposition and semisimplicity to infer
  G104's zero-section microsupport condition.
- **Valid input:** the direct image decomposes into shifted semisimple
  intersection complexes with pure Hodge-module refinements.
- **Invalid inference:** every strict support is the whole basis germ and
  every coefficient local system extends without a singular locus.
- **Precise obstruction:** B164 makes the B161 total space smooth, so the
  projective decomposition theorem applies. The last node still escapes
  along \(F_B\); B163 therefore forces nonzero internal microsupport. The
  smooth universal hypersurface total space gives the same warning on a
  transverse Lefschetz disk.
- **Re-entry condition:** prove directly that the complete base-changed
  object in G104 has no positive-codimension strict support or other
  nonzero characteristic covector, and separately retain the specified
  relation-channel pairing.
