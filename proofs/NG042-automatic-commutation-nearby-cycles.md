---
brick_id: NG042
status: NO-GO
base_field: C
variety: complex analytic or algebraic multi-parameter degenerations
smoothness: unrestricted in the rejected inference; clean boundary incidence is insufficient
projectivity: unrestricted; projectivity does not repair the inference
dimension: arbitrary finite dimension
codimension: coordinate degeneration divisors have codimension one
coefficient_field: C for the audited D-module theorem and general constructible coefficients for the sheaf formulation
cohomology_theory: iterated topological or algebraic nearby cycles
hodge_type: none; the route fails before a Hodge-type conclusion
cycle_class_map: none
cycle_equivalence: none
scope: relative
dependencies: B061, B062, and primary-source audit S041
claim: It is invalid to treat the orders of iterated nearby cycles as automatically equivalent or to infer equivalence solely from clean reduced boundary incidence.
falsifier: an unconditional general theorem proving arbitrary multi-parameter nearby-cycle functors commute
---

# NG042 — Automatic commutation of nearby cycles

**Status:** NO-GO  
**Gate:** G032 / G033  
**Primary sources:** S041

## Mathematical type record

- **Base field:** \(\mathbf C\).
- **Variety/class:** complex analytic or algebraic multi-parameter degenerations.
- **Smoothness/projectivity:** unrestricted in the rejected inference; projectivity does not repair it.
- **Dimension:** arbitrary finite dimension.
- **Codimension:** coordinate degeneration divisors have codimension one.
- **Coefficient field:** \(\mathbf C\) for the audited \(\mathcal D\)-module theorem; general constructible coefficients in the sheaf formulation.
- **Cohomology theory:** iterated topological or algebraic nearby cycles.
- **Hodge type:** none; the route fails before a Hodge-type conclusion.
- **Cycle class map:** none.
- **Equivalence relation on cycles:** none.
- **Scope:** relative.

## Rejected route

Treat
\[
\psi_{f_1}\psi_{f_2}F\simeq\psi_{f_2}\psi_{f_1}F
\]
as a formal identity for an arbitrary two-parameter degeneration, or infer it merely because the base-coordinate divisors meet cleanly.

## Decisive obstruction

Nearby-cycle functors for multiple functions do not commute in general. Natural lax comparison arrows exist, but audited theorems make them invertible only under additional hypotheses such as Kochersperger's without-slopes condition or Nadler's non-characteristic plus Thom conditions. B062 further shows that the graph construction does not make non-characteristicity automatic at a critical collision.

## Reopening criterion

This route may be reopened for a specific family only after:

1. naming the exact coefficient sheaf, \(\mathcal D\)-module, or mixed Hodge module;
2. verifying a published sufficient hypothesis at every relevant stratum; and
3. separately proving the rational Hodge and pairing compatibilities required by G033.

## Scope of the NO-GO

This rejects an automatic inference, not the possibility that nearby cycles commute in a particular recollision model.
