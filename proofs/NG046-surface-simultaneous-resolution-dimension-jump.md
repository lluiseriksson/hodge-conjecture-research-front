---
brick_id: NG046
status: NO-GO
base_field: C
variety: arbitrary even-dimensional smooth projective varieties in the middle-degree reduction and their odd-dimensional singular hyperplane sections
smoothness: the ambient variety is smooth and projective; the local hyperplane fiber has a suspended A2 singularity
projectivity: yes for the global family; the imported simultaneous-resolution theorem is local and surface-specific
dimension: ambient dimension 2n and hyperplane-fiber dimension 2n-1, versus dimension two in B068
codimension: terminal cycles have codimension n; surface exceptional curves do not match this arbitrary codimension
coefficient_field: Q for the Hodge problem
cohomology_theory: rational Betti cohomology, mixed Hodge modules, and nearby cycles
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B001, B064, B067-B068, and S043
claim: A simultaneous-resolution theorem for surface rational double points cannot be imported as a dimension-uniform resolution of the suspended A2 transitions arising in the middle-degree Hodge reduction.
falsifier: a cited theorem extending the required simultaneous resolution, rational Hodge-module descent, and detector compatibility to every odd fiber dimension 2n-1
---

# NG046 — Surface simultaneous resolution does not cover the Hodge dimensions

**Status:** NO-GO

## Rejected route

Use B068's Brieskorn–Artin–Weyl simultaneous resolution of a surface \(A_2\) rational double point as the total-space resolution required by G036 for arbitrary middle-dimensional Hodge classes.

## Dimension mismatch

B001 reduces the terminal problem to a smooth projective variety of dimension \(2n\). Its hyperplane fibers have dimension \(2n-1\), and the local \(A_2\) transition is the quadratic suspension
\[
x^3+z_1^2+\cdots+z_{2n-1}^2=0.
\]
B068 concerns complex surface fibers and a configuration of exceptional \((-2)\)-curves. Since \(2n-1\) is odd, it is never equal to two. The imported theorem therefore never matches the fiber dimension in this middle-degree route.

Suspension preserves some singularity invariants, but no audited theorem here turns a simultaneous resolution of a surface rational double point into the required projective, rational-Hodge-compatible model in every odd dimension.

## Re-entry condition

Prove the dimension-uniform statement G037, including rational descent and detector pairing, or replace simultaneous resolution with a different comparison theorem that directly handles the suspended family.

