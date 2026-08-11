---
brick_id: NG110
status: NO-GO
base_field: C
variety: a fixed smooth projective complex 2n-fold X with very ample H and isolated-nodal members in |H^m|
smoothness: X is smooth and the sought members have only isolated ordinary double points
projectivity: X, its H-embedding, and the hypersurface members are projective
dimension: dim_C X=2n with n at least 2
codimension: middle codimension n; the route restricts the total number of nodal singularities
coefficient_field: Q for relations and C for coherent evaluation maps
cohomology_theory: adjoint coherent cohomology, projective postulation, nodal vanishing cycles, and local intersection cohomology
hodge_type: the sought relation would have rational type (0,0) after Q(n), but the route cannot retain isolated support
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B026-B029, B136-B137, G013, S056
claim: Close G013 with isolated-nodal members whose node count is at most 2(mn-c)+1, where K_X tensor H^c is globally generated.
falsifier: B137, which forces any nonzero adjoint defect in the isolated-nodal high-power regime to have at least 2(mn-c)+2 nodes
---

# NG110 — Sub-double-linear node growth cannot detect

**Status:** NO-GO

- **Route:** let the number of nodes grow with \(m\), as required by B136,
  but keep it at most \(2(mn-c)+1\), and seek a nonzero B135 relation there.
- **Valid input:** a growing node count escapes every fixed Hilbert-scheme
  separation threshold.
- **Invalid inference:** any unbounded growth can already create an isolated
  adjoint defect.
- **Precise obstruction:** B137 turns a nonzero adjoint defect into failure
  of degree-\(t_m=mn-c\) projective postulation. Below \(2t_m+2\), the
  Eisenbud-Green-Harris bound forces \(t_m+2\) collinear nodes. For high
  \(m\), their defining line lies in \(X\), and the value plus conormal first
  derivative of the hypersurface section vanish identically along it. The
  hypersurface therefore has a positive-dimensional singular locus.
- **Re-entry condition:** construct G013 at or above
  B138's improved \(3(mn-c)\) floor, preserve isolated first jets and the
  multipart smoothing inequalities, and prove that its B135 quotient class
  pairs nontrivially with the prescribed Hodge class.
