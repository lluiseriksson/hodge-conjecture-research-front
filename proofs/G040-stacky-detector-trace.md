---
brick_id: G040
status: EXPLORATORY
base_field: C with all descent and Hodge data defined over Q
variety: the projective finite-group-equivariant semistable log-stack produced from the A2 root-covered family
smoothness: source and base are regular as log stacks; a scheme atlas or coarse-space comparison must be stated explicitly
projectivity: all stacky modifications, alterations, atlases, coarse maps, and pushdowns used must be proper/projective as required
dimension: arbitrary ambient dimension 2n and odd fiber dimension 2n-1
codimension: terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules or an explicitly equivalent equivariant theory, nearby cycles, proper direct image, strict support, and trace
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B063, B071-B073, G038-G039, G041, NG049-NG050
claim: The B071 equivariant semistable log-stack admits a rational nearby-cycle and proper-pushdown trace square whose invariant full-support summand maps to the original Saito detector, respects both B022 quotients, and preserves its nonzero pairing with the prescribed Hodge class.
falsifier: lack of rational MHM descent on the stack, a coarse-space correction supported on stabilizer strata, trace annihilation, loss in either B022 quotient, or failure of strict multispecialisability
---

# G040 — Stacky rational detector trace

**Status:** EXPLORATORY  
**Parent gates:** G039 / G038

## Falsifiable theorem target

For the finite group \(\Gamma\) acting on B071's semistable log-stack
\(\mathcal Y\to\mathcal B\), construct an explicit rational comparison
diagram that:

1. defines the relevant rational nearby-cycle Hodge module, either directly
   on \(\mathcal Y\) or by descent from a smooth equivariant atlas;
2. proves strict multispecialisability along the semistable boundary;
3. decomposes proper pushdown by strict support and isolates the
   \(\Gamma\)-invariant full-support detector summand;
4. defines trace to the original family and shows that stabilizer-supported
   corrections do not enter ordinary detector degree;
5. intertwines the equator-extension and base-locus quotients of B022 and
   the Saito ambient map; and
6. proves the resulting class still pairs nontrivially with the prescribed
   rational Hodge class.

## Current audit

B072 closes item 1 and the existence of nearby-cycle/proper-pushdown
operations on the stack. It also identifies the quotient-stack category with
equivariant MHM. It does not compute the full-support summand or pairing.
B073 and NG050 show that the obvious normalized trace kills the entire local
\(A_2\) root-lattice constituent.

## Smallest next audit

Prove G041 by computing the \(S_3\)-character of the full-support detector
object and locating a nonzero trivial constituent outside both B022 kernels.
Only after that representation-level survival is established should the
strict multispecialisability and Saito pairing square be promoted.
