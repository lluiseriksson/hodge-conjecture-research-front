---
brick_id: B072
status: PROVED
base_field: C
variety: complex algebraic stacks locally of finite type, including finite quotient and semistable Deligne-Mumford stacks
smoothness: arbitrary in the formalism; B071 supplies a regular semistable stack in the application
projectivity: all six operations exist; proper Deligne-Mumford pushforward satisfies f_! = f_*
dimension: arbitrary
codimension: arbitrary support codimension; terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: derived rational mixed Hodge modules on stacks, six operations, weights, nearby cycles, and vanishing cycles
hodge_type: preserved inside the rational Hodge formalism; no detector type is inferred
cycle_class_map: not constructed here; downstream map is CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence in the downstream Hodge application
scope: relative
dependencies: B071, S047
claim: Rational mixed Hodge modules extend canonically to algebraic stacks with six operations and nearby and vanishing cycles; nearby cycles are compatible with proper pushforward and smooth pullback, and on quotient stacks the theory agrees with equivariant mixed Hodge modules.
falsifier: failure of the cited stack extension, nearby-cycle comparison, or quotient-stack identification
---

# B072 — Rational mixed Hodge modules on stacks

**Status:** PROVED

## Imported theorem

Tubach constructs the derived category of rational mixed Hodge modules on
complex algebraic stacks. Theorem 3.1 supplies the six operations. Proposition
3.15 identifies \(f_!\simeq f_*\) for proper morphisms represented by
Deligne–Mumford stacks. Section 3.4 constructs nearby cycles on stacks;
Theorem 3.36 proves constructibility, perverse exactness, duality, and smooth
locality, while the preceding coherent construction makes unipotent nearby
cycles compatible with proper pushforward and smooth pullback. Proposition
3.38 gives vanishing cycles. Proposition 3.39 identifies the quotient-stack
category with Achar's equivariant mixed Hodge modules and states compatibility
of the six operations.

Applied to B071, this closes the categorical existence portion of G040: one
does not need to force a noncanonical scheme realization merely to define
rational nearby cycles and proper pushdown.

## Scope guard

The theorem supplies a formalism, not the class-specific calculation required
by the Hodge route. It does not identify the particular strict-support
summand carrying the detector, prove strict multispecialisability for the
specific multi-boundary object, compare the two B022 quotients, or show that
the finite-group trace of the detector is nonzero.

Thus B072 is not a proof of G040, G038, G031, or the Hodge Conjecture.
