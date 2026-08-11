---
brick_id: NG156
status: NO-GO
base_field: C
variety: a fixed smooth projective complex 2n-fold with very ample H, nodal members of high powers L=H^m, their reduced node schemes, and doubled node schemes
smoothness: the ambient variety is smooth and prospective hypersurfaces must have isolated ODPs; reduced Cayley-Bacharach carrier theorems do not ensure this
projectivity: the ambient embedding, reduced node sets, carrier curves, doubled schemes, and complete linear systems are projective
dimension: dim X=2n; reduced adjoint evaluation circuits have arbitrary size, while doubled schemes have length (2n+1)N
codimension: reduced adjoint value dependence supplies no one-node first-jet kernel equality, unique gradient-relation completion, or Hessian holonomy for L
coefficient_field: C for coherent evaluation and jets; Q for the separate nodal relation and Hodge detector
cohomology_theory: reduced Cayley-Bacharach postulation, coherent first jets, ODP deformation theory, and adjoint nodal relations
hodge_type: reduced nodal relations may have type (0,0), but no G124 detector or Hessian conclusion follows
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream; no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B029, B136-B141, B191-B193, G123-G124, S056-S060
claim: Use the reduced Cayley-Bacharach circuit extracted from adjoint defect, together with S056-S060, as a construction of B191 one-node determination and B193 conformal Hessian holonomy for the doubled node scheme.
falsifier: the cited theorems concern only reduced point evaluation for the adjoint degree and yield carrier containment, while G124 requires first jets of L on 2Z, exact kernel equalities, and inverse-Hessian similitudes
---

# NG156 — Reduced Cayley–Bacharach does not construct doubled-jet holonomy

- **Route:** start from the reduced adjoint evaluation circuit in B138-B141,
  invoke the Cayley–Bacharach carrier theorems S056-S060, and count the
  resulting dependence as G124's one-node determination.
- **Valid input:** a minimal adjoint value-evaluation circuit has a unique
  full-support relation and is intrinsically \(\mathrm{CB}(t)\). The cited
  theorems can force sufficiently small such circuits onto bounded-degree
  curves.
- **Invalid inference:** a relation among reduced values for
  \[
  F=K_X\otimes L^n
  \]
  implies redundancy of first derivatives for \(L\), or controls the ODP
  inverse Hessians.

The source and target data are different:

\[
 \begin{array}{c|c}
 \text{Cayley--Bacharach input}&\text{G124 obligation}\\ \hline
 Z\text{ reduced}&2Z\text{ and }\Psi_i\\
 H^0(F)\to F|_Z&H^0(I_ZL)/H^0(I_{2Z}L)\\
 \text{one scalar value relation}&\text{all one-node gradient completions}\\
 \text{carrier containment}&\text{rank-one inverse-Hessian tensor}
 \end{array} \tag{1}
\]

S056-S060 state no comparison map across either column of (1). Their
audited scope guards explicitly stop at reduced postulation and carrier
containment. B138-B141 use them only to derive necessary node-count floors,
not to construct nodes or first-jet defects.

The simplest carrier promotion is actively hostile to isolated nodality:
B029 proves that enough collinear singular points force the defining section
and its first normal derivative to vanish along the whole line, producing a
positive-dimensional singular locus.

- **Precise obstruction:** reduced adjoint Cayley–Bacharach is neither the
  sheaf nor the infinitesimal scheme required by B191/B193. A dimension or
  carrier count cannot fill the missing jet and Hessian maps.
- **Re-entry condition:** prove a new doubled-scheme theorem for the actual
  \(L\)-first-jet quotient that yields every equality (6) of B191, B193's
  conformal cocycle, isolated ODPs, and the rational detector. Existing
  S056-S060 do not provide it.
