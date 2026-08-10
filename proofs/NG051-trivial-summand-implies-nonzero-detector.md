---
brick_id: NG051
status: NO-GO
base_field: C with rational Hodge data
variety: the finite-Galois full-support pushdown of B074 and its boundary detector class
smoothness: smooth dense locus and semistable stack compactification
projectivity: finite cover and proper semistable pushdown
dimension: arbitrary ambient dimension 2n and odd fiber dimension 2n-1
codimension: terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, strict support, nearby cycles, and S3 representations
hodge_type: rational type (0,0) after Q(n) is required for the detector
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B073-B074
claim: The existence of B074's invariant full-support summand forces every nonzero lifted boundary detector to have nonzero normalized trace.
falsifier: a nonzero class contained entirely in a nontrivial isotypic summand
---

# NG051 — A trivial summand does not force nonzero detector trace

**Status:** NO-GO

## Route tested

Use B074 to identify a trivial full-support constituent and infer that the
nonzero boundary class under study projects nontrivially to it.

## Failure

This is false already in the semisimple rational representation

\[
\mathbf 1\oplus V_{\mathrm{std}}.
\]

The invariant summand \(\mathbf 1\) exists, but every nonzero vector in
\(V_{\mathrm{std}}\) has zero normalized trace. B073 identifies precisely
this standard constituent in the local \(A_2\) vanishing lattice. Existence
of the target summand is an object-level statement; nonzero projection of the
candidate is a separate class-level statement.

## Re-entry condition

Prove G042 by computing the equivariant boundary/nearby-cycle map of the B058
thimble class and showing its image has a nonzero component in B074's
invariant intermediate-extension summand after both B022 quotients.
