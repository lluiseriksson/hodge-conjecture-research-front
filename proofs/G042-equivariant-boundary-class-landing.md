---
brick_id: G042
status: EXPLORATORY
base_field: C with all finite-group and Hodge data defined over Q
variety: the root-covered plane-net family, its B071 semistable log-stack, and the original projective family
smoothness: smooth over the dense discriminant complement and semistable on the compactified stack
projectivity: finite root cover and all semistable modifications and pushdowns are projective
dimension: arbitrary ambient dimension 2n and odd fiber dimension 2n-1
codimension: terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational stack mixed Hodge modules, intermediate extension, nearby cycles, proper pushforward, finite-group invariants, and the B022 exact quotients
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B058, B063, B071-B074, G041, NG050-NG051
claim: The equivariant boundary image of the lifted B058 non-equator thimble class has nonzero projection to B074's invariant full-support intermediate-extension summand after the equator-extension and base-locus quotients, and its trace retains nonzero Saito pairing with the prescribed Hodge class.
falsifier: boundary image confined to the A2 standard constituent, projection into either B022 kernel, support on a proper stabilizer stratum, or vanishing prescribed pairing
---

# G042 — Equivariant boundary-class landing

**Status:** EXPLORATORY  
**Parent gate:** G041

## Falsifiable theorem target

Write \(t\) for the B058 non-equator thimble class before the A2 collision,
and let

\[
\partial_{\mathrm{ss}}(t)
\]

be its boundary/nearby-cycle image on the B071 semistable stack. Under the
B074 decomposition of finite pushdown, prove that

\[
e_{S_3}\partial_{\mathrm{ss}}(t)\ne0
\]

in the quotient by equator extensions and then in the quotient by the pencil
base-locus kernel. Finally prove that its Saito ambient image pairs
nontrivially with the prescribed primitive rational Hodge class.

## What is closed

- B072 defines every stack MHM, nearby-cycle, and proper-pushdown operation.
- B074 identifies the invariant full-support object with the original
  intermediate extension.
- B073/NG050 compute and exclude the purely local root-lattice trace.
- NG051 shows why object-level invariant descent is not class-level survival.

## Smallest next calculation

Express the B057 ordered thimble-extension chain in the six sheets of the
root cover, compute its equivariant boundary vector, and project it onto the
trivial and standard isotypic parts before and after the two B022 kernel
maps. The calculation must use the actual non-equator coefficients; the
total-equator vector is already zero by NG038.
