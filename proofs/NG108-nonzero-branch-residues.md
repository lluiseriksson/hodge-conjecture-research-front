---
brick_id: NG108
status: NO-GO
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold and a two-branch normal-crossing nodal hyperplane degeneration
smoothness: the ambient variety and nearby fibers are smooth; the central fiber has two ordinary double points
projectivity: the ambient variety and universal hyperplane family are projective
dimension: dim_C X=2n and dim_C Y_p=2n-1
codimension: middle codimension n; boundary parameter codimension two
coefficient_field: Q, with Q(n)
cohomology_theory: logarithmic Gauss-Manin residues, Picard-Lefschetz monodromy, the local Koszul complex, and intersection cohomology
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B133-B135, G088-G089, S021 Section 4.3.2
claim: Infer a nonzero local incidence class from one or more nonzero individual logarithmic branch residues at a proportional two-node point.
falsifier: a nonzero residue vector in im(Delta^*), for example (a_1,a_2)=q(1,c) when delta_2=c delta_1
---

# NG108 — Nonzero branch residues can be a coboundary

**Status:** NO-GO

- **Route:** at a proportional two-node point, prove that one or both
  logarithmic residues \(a_i\delta_i\) are nonzero and conclude that the
  local incidence class survives.
- **Valid input:** individual residues are concrete coefficients in the
  degree-one Green–Griffiths Koszul term.
- **Invalid inference:** a nonzero cochain has a nonzero cohomology class.
- **Precise obstruction:** if \(\delta_2=c\delta_1\), then

  \[
  \operatorname{im}\Delta^\ast=\mathbf Q(1,c).
  \]

  For \(q\ne0\), the vector \(q(1,c)\) may have every coordinate nonzero but
  is a coboundary. Its invariant relation evaluation is

  \[
  c(q)-(cq)=0.
  \]

  More generally, B135 proves that only
  \([a]\in\operatorname{coker}\Delta^\ast\), not its individual
  coordinates, is intrinsic.
- **Re-entry condition:** compute the lift-invariant mismatch
  \(c a_1-a_2\) and prove it nonzero at an actual class-directed boundary
  point, as required by G089.
