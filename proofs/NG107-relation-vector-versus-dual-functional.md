---
brick_id: NG107
status: NO-GO
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold and a clean nodal hyperplane degeneration
smoothness: the ambient variety and nearby fibers are smooth; the special fiber has ordinary double points
projectivity: the ambient variety and degeneration are projective
dimension: dim_C X=2n and dim_C Y_p=2n-1
codimension: middle codimension n; local support codimension at least two
coefficient_field: Q, with Q(n)
cohomology_theory: rational intersection cohomology, intermediate extensions, vanishing-cycle relations, and mixed Hodge duality
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B026, B052, B093, B133-B134, S022-S024
claim: Treat the cohomological local incidence class as a canonically selected vector in the vanishing-cycle relation kernel, and infer nonvanishing from the existence of a nonzero relation.
falsifier: the canonical S022 identification E(Y_p)=R(Y_p)^vee and the zero functional in R(Y_p)^vee when R(Y_p) is nonzero
---

# NG107 — A local incidence class is not a selected relation vector

**Status:** NO-GO

- **Route:** identify the degree-one cohomological IC stalk literally with
  \(R(Y_p)\), regard \(s_m(\zeta)_p\) as a relation vector, and use
  \(R(Y_p)\ne0\) to force \(s_m(\zeta)_p\ne0\).
- **Valid input:** polarization gives a perfect pairing and the resolved
  coefficient-kernel calculations correctly determine the rank and Tate type
  of the local channel.
- **Invalid inference:** a cohomological class canonically selects a vector
  of the homological relation space, or a nonzero target forces that class to
  be nonzero.
- **Precise obstruction:** B134 gives the intrinsic typing

  \[
  s_m(\zeta)_p\in E(Y_p)=R(Y_p)^\vee.
  \]

  It is the functional
  \(\beta\mapsto\langle\zeta,\gamma_\beta\rangle\). Even when
  \(R(Y_p)\ne0\), this functional can vanish identically. A polarization
  model of \(R(Y_p)^\vee\) does not remove that class-specific condition.
- **Re-entry condition:** construct a boundary point and one actual relation
  \(\beta\) for which the B134 evaluation is nonzero. Dimension, Hodge type,
  and existence of relations alone remain insufficient.
