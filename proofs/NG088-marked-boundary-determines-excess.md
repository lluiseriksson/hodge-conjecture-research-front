---
brick_id: NG088
status: NO-GO
base_field: C with relative chains over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a selected B058 detector, and a marked collision to a clean nodal target
smoothness: X and generic hyperplane fibers smooth; target clean nodal
projectivity: X, hyperplane family, and collision projective
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; comparison chains degree 2n
codimension: middle codimension n; target is a point of the plane base
coefficient_field: Q
cohomology_theory: rational relative chain complexes, marked boundary maps, homology, B022 quotients, and primitive ambient pairing
hodge_type: desired excess rational type (0,0) after Q(n); no such type is inferred from boundary data
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B090-B091, B112, G055, G073-G074
claim: Once the actual and pure-Hurwitz selected chains have the same marked local boundary, that boundary determines their excess homology class and in particular forces the desired nonzero detector.
falsifier: B112's family a+lambda z with one fixed boundary and arbitrary excess class lambda[z]
---

# NG088 — A marked boundary does not determine the excess class

**Status:** NO-GO

- **Route:** identify every oriented local boundary sphere for the selected
  collision chain and the pure-Hurwitz reference, then infer the nonzero
  topology-changing correction from equality of those marked boundaries.
- **Valid input:** equal boundaries make the difference a cycle and are
  necessary for the class to lie in the intended relative channel.
- **Invalid inference:** the common boundary determines the homology class of
  that difference.
- **Precise obstruction:** B112 fixes a chain $a$ with boundary $b$ and shows
  that $a+\lambda z$ has the same boundary for every $\lambda$, while the
  excess class is the arbitrary value $\lambda[z]$. Neither nonvanishing nor
  the B022 image, Hodge type, or final pairing follows from boundary data.
- **Re-entry condition:** G074 must construct the selected actual comparison
  chain and compute its excess class itself, including rational type, both
  quotient survivals, and nonzero prescribed pairing.
