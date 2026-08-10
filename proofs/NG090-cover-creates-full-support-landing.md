---
brick_id: NG090
status: NO-GO
base_field: C with finite-cover and Hodge data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, its original plane-net collision, and the S3 root-covered semistable model
smoothness: X and generic hyperplane fibers smooth; covered source semistable regular
projectivity: X, hyperplane family, finite cover, semistable model, and pushdown projective
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; plane base dimension 2
codimension: middle codimension n; collision support positive codimension
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, nearby cycles, strict support, perverse grades, finite unit and trace, and S3 invariants
hodge_type: desired selected coordinate rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B074-B076, B114, G042-G043, G075-G076, NG053
claim: Passing to the S3 root cover and projecting to the invariant full-support summand can create a nonzero selected landing even when the corresponding original downstairs full-support specialization is zero.
falsifier: B114's invariant full-support isomorphism and unit/normalized-trace inverse pair
---

# NG090 — The cover cannot create full-support landing

**Status:** NO-GO

- **Route:** use the richer semistable root-covered object to obtain a
  nonzero invariant full-support coordinate without first proving the
  selected original specialization is nonzero.
- **Valid input:** the cover supplies a semistable model, a canonical
  invariant object, and exact rational averaging.
- **Invalid inference:** those operations create a new class-level landing.
- **Precise obstruction:** B114 identifies the invariant full-support
  perverse-grade object with the original one; unit and normalized trace are
  inverse there. Nonzero covered landing is equivalent to nonzero downstairs
  landing. This is the selected-excess version of NG053.
- **Re-entry condition:** G076 must construct the original selected
  specialization and prove its canonical full-support coordinate nonzero.
  Only afterward may the cover transport that established coordinate.
