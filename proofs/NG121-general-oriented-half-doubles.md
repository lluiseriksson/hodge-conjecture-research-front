---
brick_id: NG121
status: NO-GO
base_field: C
variety: P^(2n), O(d) with d not equal to 2, and a general union of N oriented half-double schemes
smoothness: projective space and the general support points are smooth
projectivity: the ambient space and zero-dimensional scheme are projective
dimension: ambient dimension 2n; each component length n+1; total length (n+1)N
codimension: G094 asks evaluation rank at most R+n with R<N, while general evaluation has maximal rank
coefficient_field: C
cohomology_theory: partial polynomial interpolation, coherent cohomology, and Hilbert functions
hodge_type: none produced
cycle_class_map: CH^n(P^(2n))_Q -> H^(2n)(P^(2n),Q(n)); no primitive detector is produced
cycle_equivalence: rational equivalence
scope: generic
dependencies: B149-B150, G094-G095, and S062
claim: Use general support points and general orientations in projective space to obtain G094's superabundant oriented half-double scheme.
falsifier: S062 Theorem 1.1 gives maximal rank and none of its five exceptions matches ambient dimension 2n with component length n+1
---

# NG121 — General oriented half-doubles cannot supply G094

- **Route:** choose general support points and general maximal-isotropic
  orientations in \(\mathbf P^{2n}\), expecting the large number of
  conditions to create G094's defect.
- **Valid input:** the local schemes have exactly the required length
  \(n+1\) and are contained in double points.
- **Invalid inference:** general partial first-jet conditions become
  superabundant.
- **Precise obstruction:** B150 applies S062, Theorem 1.1. For \(d\ne2\)
  evaluation has maximal rank and no listed exception matches the
  half-double parameters. In the injective range no nonzero hypersurface
  contains the scheme; in the surjective range its rank is
  \((n+1)N>R+n\).
- **Re-entry condition:** construct a special support-orientation
  configuration in one B151 branch and verify every G095 integration and
  pairing condition.
