---
brick_id: NG054
status: NO-GO
base_field: C with rational Hodge data
variety: the proper pushdown of the B071 semistable stack and the specialized B058 class
smoothness: smooth semistable source stack; arbitrary target degeneration
projectivity: proper/projective pushdown
dimension: arbitrary ambient dimension 2n and odd singular-fiber dimension 2n-1
codimension: terminal cycles have codimension n; exceptional supports have positive base codimension
coefficient_field: Q
cohomology_theory: pure rational mixed Hodge modules, strict-support decomposition, nearby cycles, and proper pushforward
hodge_type: rational type (0,0) after Q(n) is required for the detector
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B077
claim: The existence of B077's full-support direct summand forces every nonzero specialized tube class to have nonzero full-support projection.
falsifier: a nonzero vector lying entirely in the direct sum of proper-support constituents
---

# NG054 — Decomposition does not force full-support landing

**Status:** NO-GO

## Route tested

Invoke the decomposition theorem of B077 and treat a nonzero specialized
class as automatically contributing to the full-support summand.

## Failure

For a direct sum

\[
M_{\mathrm{fs}}\oplus M_{<\mathrm{fs}},
\]

the existence of \(M_{\mathrm{fs}}\) says nothing about the projection of a
specified vector. Any nonzero vector in \(M_{<\mathrm{fs}}\) is a
counterexample to the inference. Geometrically, semistable modifications can
create exceptional strata supporting such constituents.

## Re-entry condition

Prove G043 by computing the strict-support projection of the actual nearby
specialization of the B058 tube and showing its full-support component is
nonzero. Only then test the equator/base-locus quotients and pairing.
