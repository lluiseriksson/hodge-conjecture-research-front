---
brick_id: G053
status: NO-GO
base_field: C with all detector data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold, a nonzero primitive rational Hodge class, and a B089 marked plane net through an independent-node hyperplane
smoothness: X and marked reference fiber smooth; target has only independent ordinary double points
projectivity: X, high-power hyperplane system, and marked plane net projective
dimension: ambient 2n, hyperplane fibers 2n-1, and plane-net base 2
codimension: middle codimension n; target nodal stratum codimension equals its number of independent nodes
coefficient_field: Q
cohomology_theory: local intersection cohomology, Picard-Lefschetz relations, tube and thimble maps, B022 quotients, and Saito pairing
hodge_type: local relation and ambient detector must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B015, B022, B052-B059, B088-B090, G031-G032, G052, NG064-NG066
claim: For every nonzero primitive rational Hodge class, choose an independent-node target H and a B089 marked collision disk carrying a loop-fixed rational class alpha_H whose B057 extension survives both B022 quotients and has ambient image pairing nontrivially with the prescribed Hodge class.
falsifier: a primitive Hodge class for which every marked independent-node collision has zero local relation channel, only B022-kernel extensions, or ambient detector image orthogonal to that class
---

# G053 — Replace the global detector by a marked local detector

**Status:** NO-GO
**Parent gates:** G031 / G052

For a prescribed nonzero primitive Hodge class $\zeta$, construct:

1. an independent-node hyperplane $H$;
2. a B089 marked plane net and collision disk $\Delta$ with boundary loop
   $g_H$ based at the fixed smooth reference hyperplane $H_0$;
3. a rational class $\alpha_H$ satisfying $g_H\alpha_H=\alpha_H$;
4. a B057 extension chain whose image survives the equator-extension and
   base-locus quotients; and
5. the class-specific inequality

   \[
   \left\langle\zeta,
   \Phi_H\bigl(\tau_{g_H}(\alpha_H)\bigr)
   \right\rangle\ne0.
   \]

B088 then makes the marked chain collision-monodromy invariant, B084 lifts
it to the special fiber, and B015/B052 identify the local relation channel
and its rational type $(0,0)$.

This attempted gate fails before the class-specific pairing test. B090 proves
that every class fixed by the positive total boundary of the normal-crossing
nodal cluster has all B057 coefficients zero. Hence its extension cannot
survive the B022 quotients or satisfy the displayed inequality. NG066 records
the failed route. G054 retains the nonlocal B058 word instead of replacing it
by the total local boundary.
