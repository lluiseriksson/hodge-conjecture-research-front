---
brick_id: NG111
status: NO-GO
base_field: C
variety: a fixed smooth projective complex 2n-fold X with very ample H and isolated-nodal members of |H^m|
smoothness: X is smooth and the sought hypersurface members have only isolated ordinary double points
projectivity: X, its projective embedding, carrier curves, and hypersurface members are projective
dimension: dim_C X=2n with n at least 2
codimension: middle codimension n; the route bounds the total node count
coefficient_field: Q for vanishing-cycle relations and C for coherent evaluation and first-jet calculations
cohomology_theory: adjoint coherent cohomology, Cayley-Bacharach postulation, nodal vanishing homology, and local intersection cohomology
hodge_type: the sought relation would have rational type (0,0) after Q(n), but its carrier forces nonisolated singularities
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B026-B029, B136-B138, G013, S057
claim: Close G013 with an isolated-nodal high-power member having at most 3(mn-c)-1 nodes and nonzero adjoint defect.
falsifier: B138, which places a minimal degree-(mn-c) evaluation circuit on a degree-at-most-two curve and forces that carrier into the singular locus
---

# NG111 — Sub-triple-linear nodal detectors are nonisolated

**Status:** NO-GO

- **Route:** satisfy B137 by allowing at least \(2(mn-c)+2\) nodes, but
  remain below \(3(mn-c)\) while seeking a nonzero B135 relation.
- **Valid input:** the conic exception prevents the plane postulation theorem
  S056 from extending B137 by itself.
- **Invalid inference:** the conic exception supplies an isolated nodal
  configuration.
- **Precise obstruction:** a minimal dependent subset of the adjoint
  evaluation functionals is intrinsically \(\mathrm{CB}(mn-c)\). S057 puts
  every such circuit of at most \(3(mn-c)-1\) points on a curve of degree at
  most two. Componentwise Cayley-Bacharach bounds provide enough nodes on a
  line or conic to annihilate both the hypersurface restriction and all
  conormal first derivatives. The carrier lies in the singular locus.
- **Re-entry condition:** construct G013 with at least \(3(mn-c)\) nodes,
  isolated first jets, the multipart smoothing inequalities, positive
  adjoint and ambient ranks, and a class-specific nonzero B135 quotient.
