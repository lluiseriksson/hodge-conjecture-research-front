---
brick_id: NG053
status: NO-GO
base_field: C with rational Hodge data
variety: the original plane-net degeneration and its finite root-covered semistable stack
smoothness: smooth generic locus and semistable covered model
projectivity: finite cover and semistable modifications are projective
dimension: arbitrary ambient dimension 2n and odd singular-fiber dimension 2n-1
codimension: terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, iterated nearby cycles, finite trace, strict support, and B022 quotients
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B076
claim: Passing to the root cover, applying semistable nearby cycles, and averaging can create the missing nonzero original boundary detector without proving original specialization nonvanishing.
falsifier: the normalized nearby-cycle trace is a retraction and hence sends a pulled-back zero class to zero
---

# NG053 — Descent cannot create boundary nonvanishing

**Status:** NO-GO

## Route tested

Use the richer semistable boundary on the root cover and rational averaging
as a source of the nonzero local detector absent on the original family.

## Failure

B076 proves that finite-cover unit and normalized trace remain a split
unit/retraction pair after every nearby-cycle functor. This formalism
preserves an already nonzero original nearby class but cannot create one from
zero. Any covered class with nonzero trace already determines a nonzero class
downstairs.

Thus the finite cover and stack formalism remove technical obstructions; they
do not supply the terminal geometric nonvanishing. The remaining work is to
prove that the B057-B058 tube actually specializes to the required
full-support boundary class and avoids the two B022 kernels.

## Re-entry condition

Compute the original/canonical specialization morphism, its strict-support
projection, both B022 quotient maps, and the prescribed pairing. This is the
residual content of G042 and the original G032/G031 branch.
