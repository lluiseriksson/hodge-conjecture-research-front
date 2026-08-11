---
brick_id: NG102
status: NO-GO
base_field: C with rational coefficients
variety: arbitrary polarized smooth projective complex 2n-folds with primitive rational Hodge classes and their high-power hyperplane systems
smoothness: ambient variety smooth; clean target nodal
projectivity: ambient and universal incidence families projective
dimension: ambient 2n; hyperplane fibers 2n-1
codimension: middle codimension n; local support codimension at least two
coefficient_field: Q
cohomology_theory: admissible normal-function singularities, local intersection cohomology, and clean nodal relation support
hodge_type: primitive rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B007, B012, B125-B127, G008, G084-G085, S009
claim: Requiring the local support to meet the Li-clean nodal locus is a smaller or weaker terminal gate than requiring the support merely to be nonempty.
falsifier: the direct implication from clean intersection to support nonemptiness together with terminal equivalence of universal support nonemptiness
---

# NG102 — Clean incidence is not a smaller terminal gate

**Status:** NO-GO

- **Route:** label G084 the smallest terminal gate because it has one
  incidence formula.
- **Valid input:** B125 shows that formula is a precise sufficient condition
  for G031.
- **Invalid inference:** adding the clean-locus requirement weakens or
  reduces the terminal support theorem.
- **Precise obstruction:** every G084 witness is already a G008 witness, and
  B007/B012 prove universal G008 equivalent to rational HC. The clean target
  is an additional cleanup obligation, not a reduction. B127 gives

  \[
  G008+G085\Rightarrow G084\Rightarrow G008
  \Longleftrightarrow\mathrm{HC}_{\mathbf Q}.
  \]

- **Re-entry condition:** keep G084 as a stronger sufficient clean-nodal
  program, split off conditional G085, and return the active terminal gate
  to G008. Do not count clean geometry as formal progress on support
  nonemptiness.
