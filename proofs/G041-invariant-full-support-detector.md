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
dependencies: B022, B058, B063, B071-B077, G032, G040, G042-G043, NG050-NG054
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

B072 supplies the stack MHM and nearby-cycle operations. B074 proves that the
full-support pushdown contains a canonical invariant intermediate-extension
summand recovering the original local system. B073/NG050 prove that the
local \(A_2\) root-lattice constituent contributes no invariants, and NG051
shows that existence of the invariant object does not force the candidate
class to land in it. Therefore the remaining issue is class-level landing.

B075 proves that the invariant transfer of the B058 tube is nonzero and has
the correct normalized trace before collision. NG052 confines the remaining
loss to nearby specialization, strict support, and the two B022 kernels.

B076 proves the normalized trace remains a retract after nearby cycles.
NG053 shows that the cover cannot create missing original boundary
nonvanishing, so the residual class-level gate is G042/G032.

B077 supplies the strict-support decomposition; NG054/G043 isolate the
projection of the specialized class to its full-support summand.

## Smallest next calculation

Prove G042 by constructing the equivariant boundary vector of the B057-B058
non-equator thimble chain and separating:

1. the local \(A_2\) standard constituent;
2. global thimble-extension classes;
3. equator-extension and base-locus kernels; and
4. the target primitive ambient representation.

Then test its projection to B074's known trivial summand and the restricted
Saito pairing.

G075 later isolates the same nonzero invariant full-support landing for the
class-specific excess used by G074. It is a coordinate-level restatement of
this first obligation, not an independent route.
