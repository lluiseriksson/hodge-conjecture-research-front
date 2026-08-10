---
brick_id: NG093
status: NO-GO
base_field: C
variety: the original plane-net incidence family of hyperplane sections of an arbitrary polarized smooth projective complex 2n-fold and a transverse Lefschetz disk
smoothness: incidence total space smooth; central transverse fiber has one ordinary quadratic singularity; nearby fibers smooth
projectivity: the incidence family and its transverse restriction are projective
dimension: hyperplane fibers have dimension d = 2n-1; plane base dimension 2; transverse base dimension 1
codimension: middle cycle codimension n; tested strict support has base codimension one
coefficient_field: Q
cohomology_theory: higher direct images, perverse normalization, strict support, and the decomposition theorem
hodge_type: no selected Hodge class; the attempted implication concerns rational support multiplicity
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B080-B081, B116-B117, G078, S052
claim: The fact that R^d g_*Q is a shifted intersection complex on a transverse Lefschetz disk, by itself, excludes a punctual summand in pH^0 and hence divisor support on the plane base.
falsifier: the exact shift calculation showing that a punctual pH^0 term contributes to H^0(Rg_*Q[d+1]) = R^(d+1)g_*Q, not to R^d g_*Q
---

# NG093 — The middle direct image alone is in the wrong detector degree

**Status:** NO-GO

- **Route:** cite S052 equation (2.2.5), which identifies
  \(R^d g_*\mathbf Q\) with the intersection-complex extension, and infer
  immediately that \({}^pH^0\) has no punctual term.
- **Valid input:** the full-support middle local system does extend as an
  intersection complex.
- **Invalid inference:** this determines every summand of
  \({}^pH^0(Rg_*\mathbf Q[d+1])\).
- **Precise obstruction:** a punctual perverse term in \({}^pH^0\) lies in
  ordinary degree zero of the normalized complex, hence in
  \(R^{d+1}g_*\mathbf Q\), whereas \(R^d g_*\mathbf Q\) lies one ordinary
  degree lower. This is the transverse form of B080's divisor shift.
- **Re-entry condition:** use S052 equation (2.2.3), not only (2.2.5).
  Constancy of \(R^{d+1}g_*\mathbf Q\), combined with the direct-sum
  decomposition, kills the punctual term. B117 carries out that argument.
