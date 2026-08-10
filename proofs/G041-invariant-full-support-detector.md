---
brick_id: G041
status: EXPLORATORY
base_field: C with all equivariant and Hodge data defined over Q
variety: the S3-equivariant semistable log-stack dominating the ordered-root A2 family and the original projective family
smoothness: semistable regular source and base from B071
projectivity: projective monoidal alteration, source subdivision, and proper pushdown
dimension: arbitrary ambient dimension 2n and odd fiber dimension 2n-1
codimension: terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: stack-valued rational mixed Hodge modules, nearby cycles, strict support, proper pushforward, invariants, and trace
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B058, B063, B071-B073, G040, NG050
claim: The full-support nearby-cycle detector associated with the B058 non-equator tube has a nonzero S3-invariant projection whose trace survives both B022 quotients and has nonzero Saito pairing with the prescribed Hodge class.
falsifier: the full-support representation contains no trivial constituent, the average lies in an equator or base-locus kernel, or the traced class is orthogonal to the prescribed Hodge class
---

# G041 — Invariant full-support detector

**Status:** EXPLORATORY  
**Parent gate:** G040

## Falsifiable theorem target

Let \(M_{\mathrm{fs}}\) be the full-support rational nearby-cycle summand on
the B071 semistable log-stack that receives the lifted B058 non-equator tube
class \(t\). Prove

\[
e_{S_3}t\ne0
\]

after the equator-extension quotient and after the base-locus quotient of
B022, and prove that its proper trace has nonzero Saito pairing with the
specified primitive rational Hodge class.

## Current obstruction

B072 supplies the stack MHM and nearby-cycle operations, but not the
representation carried by \(M_{\mathrm{fs}}\). B073/NG050 prove that the
local \(A_2\) root-lattice constituent contributes no invariants. Therefore
any positive result must identify an additional trivial constituent coming
from the global thimble-extension or boundary/full-support data and must
track it through both quotients.

## Smallest next calculation

Construct the \(S_3\)-character of the full-support summand in the explicit
root-covered plane-net model, separating:

1. the local \(A_2\) standard constituent;
2. global thimble-extension classes;
3. equator-extension and base-locus kernels; and
4. the target primitive ambient representation.

Then test the trivial-isotypic multiplicity and the restricted Saito pairing.
