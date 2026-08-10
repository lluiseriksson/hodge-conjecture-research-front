---
brick_id: NG049
status: NO-GO
base_field: C
variety: the finite-group-equivariant stacky semistable resolution of B071 and its original projective family
smoothness: the stacky model is semistable; a group-equivariant scheme presentation is not supplied
projectivity: the stacky monoidal operations are projective; the scheme alteration is noncanonical
dimension: arbitrary ambient dimension 2n and fiber dimension 2n-1
codimension: terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, nearby cycles, proper direct image, and trace
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B071, S046
claim: A canonical equivariant semistable log-stack resolution may be treated without further proof as an equivariant smooth scheme resolution carrying the required rational full-support detector trace.
falsifier: the explicit noncanonicity of scheme realization or absence of the required MHM descent and pairing square
---

# NG049 — Stacky semistability does not close detector descent

**Status:** NO-GO

## Route tested

Apply B071 and immediately regard the result as the smooth equivariant scheme
model and rational detector descent required by G038.

## Failure

The geometric theorem is canonical and equivariant at the log-stack level.
Adiprasito–Liu–Temkin Remark 4.6 explicitly separates this from the scheme
realization: Kawamata's trick gives schemes, but the alteration is
noncanonical. No cited statement makes that choice compatible with the
preassigned finite group.

Even an equivariant scheme realization would settle only the geometry. The
paper does not define the rational nearby-cycle mixed Hodge module on the
stacky model, identify a full-support invariant summand under proper
pushdown, compare the B022 quotients, or prove survival of the prescribed
pairing.

## Re-entry condition

Prove G040 by either:

1. constructing a projective \(\Gamma\)-equivariant scheme realization of
   the stacky semistable model and then its rational MHM trace square; or
2. developing the required rational MHM nearby-cycle and proper-pushdown
   formalism directly on the finite Deligne–Mumford stack and proving that
   passage to invariants/coarse space preserves the full-support detector and
   nonzero pairing.
