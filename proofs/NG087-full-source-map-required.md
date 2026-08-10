---
brick_id: NG087
status: NO-GO
base_field: C with comparison chains and stalks over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, one selected B058 detector, and a proposed projective collision
smoothness: X and generic hyperplane fibers smooth; target clean nodal in the application
projectivity: X, hyperplane family, and collision projective
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; selected comparison degree 2n
codimension: middle codimension n; target is a point of the plane base
coefficient_field: Q
cohomology_theory: distributed relative thimble complexes, nearby and special stalks, relative bordism, and B022 quotient homology
hodge_type: selected source, nearby, lift, and ambient classes rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B083, B104, B109-B111, G073, NG080
claim: Before G073 can define the selected nearby detector and its ordinary lift, it must construct a collision-induced morphism on the entire distributed thimble complex or on all of its homology.
falsifier: B111's class-specific sufficiency reduction and B104's one-detector relative-bordism criterion
---

# NG087 — A full source map is not required

**Status:** NO-GO

- **Route:** require a natural map
  $H(C_{\mathrm{dist}})\to P_\psi$, or a chain map on the entire distributed
  complex, before testing the selected B058 detector.
- **Valid input:** such a map would be useful, would give a realization of
  the selected class, and could control many detectors simultaneously.
- **Invalid inference:** it is necessary for the class-specific vertical
  chain.
- **Precise obstruction:** B111 observes that B083 and B109 use only the one
  nearby class $t_\psi$ and one lift $s$. The B022 and pairing checks are also
  evaluations on that selected class. B104 proves at the downstream chain
  level that one relative bordism suffices; NG080 already blocks the full-map
  requirement.
- **Re-entry condition:** G073 must construct a geometrically certified
  realization of the selected $t$ only, prove its ordinary liftability, and
  retain rational type and nonzero prescribed pairing. A global comparison
  map remains an optional stronger mechanism.
