---
brick_id: NG112
status: NO-GO
base_field: C
variety: a fixed smooth projective complex 2n-fold X with very ample H and isolated-nodal members of |H^m|
smoothness: X is smooth; sought hypersurfaces have isolated ordinary double points; degree-at-most-three carrier curves may be singular or reducible
projectivity: X, carrier Hilbert families, and hypersurface members are projective
dimension: dim_C X=2n with n at least 2
codimension: middle codimension n; the route bounds node cardinality and introduces curve carriers of codimension 2n-1
coefficient_field: Q for vanishing-cycle relations and C for coherent evaluation and normalized first-jet bounds
cohomology_theory: adjoint coherent cohomology, Cayley-Bacharach postulation, normalized carrier vector bundles, nodal vanishing homology, and local intersection cohomology
hodge_type: the sought relation has rational type (0,0) after Q(n), but every carrier in the tested range creates nonisolated singularities
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B026-B029, B136-B139, G013, S058
claim: Close G013 with an isolated-nodal high-power member having at most 4(mn-c)-5 nodes and nonzero adjoint defect.
falsifier: B139, which places a minimal CB(mn-c) circuit on a curve of degree at most three and forces an occupied component into the singular locus
---

# NG112 — Sub-quartic-linear nodal detectors are nonisolated

**Status:** NO-GO

- **Route:** cross the triple-linear B138 floor but retain at most
  \(4(mn-c)-5\) nodes.
- **Valid input:** S057 controls only degree-at-most-two carriers.
- **Invalid inference:** the first degree-three Cayley-Bacharach carriers can
  support an isolated nodal defect.
- **Precise obstruction:** S058 puts a minimal
  \(\mathrm{CB}(mn-c)\) circuit in this range on a curve of degree at most
  three. B139 proves componentwise point lower bounds proportional to the
  component degree and a uniform normalized-conormal zero bound. An occupied
  line, conic, twisted cubic, or integral plane cubic is forced into the
  hypersurface singular locus.
- **Re-entry condition:** use at least \(4(mn-c)-4\) nodes and prove all
  remaining G013 conditions: isolated first jets, multipart smoothability,
  positive adjoint and ambient ranks, and a prescribed nonzero B135 pairing.
