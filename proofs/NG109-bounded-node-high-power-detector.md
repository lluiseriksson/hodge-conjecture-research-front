---
brick_id: NG109
status: NO-GO
base_field: C
variety: a fixed polarized smooth projective complex 2n-fold and nodal hyperplane members in increasing powers of the polarization
smoothness: the ambient variety is smooth and the tested members have only ordinary double points
projectivity: the ambient variety, Hilbert schemes of points, and hypersurface members are projective
dimension: dim_C X=2n with n at least 2
codimension: middle codimension n; the number of nodal singularities is bounded independently of the power
coefficient_field: Q for the local relation channel and C for coherent evaluations
cohomology_theory: coherent evaluation maps, relative Serre vanishing, nodal vanishing cycles, and intersection cohomology
hodge_type: the sought relation would have type (0,0) after Q(n), but its space vanishes
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B026-B027, B133-B136, G013, G088-G089, S055
claim: Close G088 by increasing the embedding power while retaining a uniformly bounded number of nodes, in particular the proportional two-node residue model G089.
falsifier: B136 uniform separation, which forces the adjoint defect and relation space to vanish for every bounded node count in all sufficiently high powers
---

# NG109 — Bounded-node detectors disappear at high power

**Status:** NO-GO

- **Route:** take \(m\) larger to gain geometric flexibility while keeping a
  fixed two-node or bounded-node local model, then force a B135 residue
  mismatch there.
- **Valid input:** higher powers improve global generation, jet separation,
  and deformation flexibility.
- **Invalid inference:** improved positivity preserves a nonzero local
  relation channel.
- **Precise obstruction:** B136 proves that for every fixed \(N\) there is a
  threshold after which every node scheme of length at most \(N\) imposes
  independent conditions on \(L^m\). B027 then forces

  \[
  H^1(I_\Delta\otimes K_X\otimes(L^m)^n)=0
  \quad\text{and}\quad R(Y)=0.
  \]

  With \(N=2\), the proportional-pair target of G089 is absent, not merely
  difficult to evaluate.
- **Re-entry condition:** allow the number of nodes to grow with \(m\) and
  meet B137's quantitative floor together with G013's independent-block and
  adjoint-defect conditions, then prove the resulting B135 residue class is
  nonzero for the prescribed \(\zeta\).
