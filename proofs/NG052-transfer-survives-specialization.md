---
brick_id: NG052
status: NO-GO
base_field: C with rational Hodge data
variety: the finite-cover plane-net family before collision and its B071 semistable collision model
smoothness: smooth along the transferred tube; semistable after collision
projectivity: all finite covers, modifications, and pushdowns are projective
dimension: arbitrary ambient dimension 2n and odd singular-fiber dimension 2n-1
codimension: terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: finite-cover transfer, nearby cycles, rational mixed Hodge modules, strict support, and B022 quotients
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B075
claim: Nonzero invariant finite-cover transfer of the smooth-locus tube automatically specializes to a nonzero full-support local detector surviving both B022 quotients.
falsifier: specialization into an equator-extension kernel, base-locus kernel, proper-support summand, or zero local boundary class
---

# NG052 — Global transfer need not survive specialization

**Status:** NO-GO

## Route tested

Use B075's nonzero invariant transfer before collision and declare its nearby
boundary to be the required descended local detector.

## Failure

Transfer controls finite-cover pushforward on the smooth locus. It does not
identify the specialization morphism or its kernel. B022 already exhibits
two independent ways for a zero-boundary thimble combination to disappear:
equator extensions and the pencil base-locus kernel. Proper semistable
pushdown can also place a boundary class in a lower-support summand. None of
these possibilities is excluded by \(p_*p^!=d\).

## Re-entry condition

Complete G042 by constructing the nearby specialization of the invariant
transfer and proving, support by support, that its invariant full-support
component avoids both B022 kernels and retains the prescribed pairing.
