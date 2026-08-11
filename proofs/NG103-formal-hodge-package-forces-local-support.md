---
brick_id: NG103
status: NO-GO
base_field: C
variety: projective parameter spaces P^d with full-support geometric Hodge coefficient objects; compared with, but not equal to, universal hyperplane families
smoothness: coefficient variation smooth on a dense open; projective source smooth
projectivity: source and target projective
dimension: arbitrary parameter dimension d at least 1
codimension: no cycle construction; local target degree -d+1
coefficient_field: Q
cohomology_theory: intersection cohomology, pure Hodge modules, hard Lefschetz, finite direct image, and ordinary cohomology sheaves
hodge_type: weight-minus-one coefficient and a nonzero rational global type-(0,0) IH^1 class
cycle_class_map: not used
cycle_equivalence: rational equivalence is not used
scope: absolute
dependencies: B014, B128-B129, G008, G086
claim: A projective-space base, full strict support, geometric polarizable weight-minus-one coefficients, purity, hard Lefschetz, and rational type (0,0) formally force a nonzero global IH^1 class to have a nonzero local H^(-d+1) invariant.
falsifier: the B129 full-support projective-space Hodge escape construction
---

# NG103 — The formal Hodge package does not force local support

**Status:** NO-GO

- **Route:** derive G008 from the facts that the base is \(\mathbf P^d\), the
  coefficient IC has full support and geometric polarizable weight-\(-1\)
  coefficients, hard Lefschetz holds, and \(s(\zeta)\) is a rational Hodge
  class.
- **Valid input:** every listed property holds for the universal-hyperplane
  coefficient object and its incidence class.
- **Invalid inference:** those formal properties force the B128 edge image to
  be nonzero.
- **Precise obstruction:** B129 constructs, for every \(d\ge1\), a
  full-support IC on \(\mathbf P^d\) with all those properties and a nonzero
  rational type-\((0,0)\) class in \(IH^1\), while
  \(\mathcal H^{-d+1}=0\) everywhere. The class lies entirely in B128's
  escape space \(H^1(\mathbf P^d,\mathcal H^{-d}K)\).
- **Re-entry condition:** use the exact universal-incidence origin
  \(s_m(\zeta)=[q_m^*\zeta]_{00}\) and prove G086's edge survival. No theorem
  about arbitrary pure geometric Hodge modules on projective space can close
  the route.
