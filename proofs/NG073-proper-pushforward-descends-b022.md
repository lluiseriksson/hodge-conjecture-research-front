---
brick_id: NG073
status: NO-GO
base_field: C with rational Hodge-module coefficients
variety: an arbitrary projective plane-net collision family mapping to the fixed smooth projective complex 2n-fold X
smoothness: X and generic hyperplane fibers smooth; special target clean nodal; total collision model proper
projectivity: all geometric maps projective/proper
dimension: ambient 2n; hyperplane fibers 2n-1; plane base 2; collision base 1
codimension: middle codimension n
coefficient_field: Q
cohomology_theory: proper pushforward, nearby cycles, relative thimble homology, B022 quotients, and primitive ambient homology
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B082-B083, B097, G060
claim: Proper-pushforward naturality before quotient automatically supplies the B097 special/nearby maps after the equator-extension and base-locus quotients and sends t_psi to the B058 class c.
falsifier: failure to realize t_psi in the source complex, or a raw pushforward whose kernel compatibility with either B022 quotient has not been proved
---

# NG073 — Proper pushforward does not automatically descend through B022

**Status:** NO-GO

Proper pushforward and nearby cycles are functorial for an already-defined
morphism of coefficient objects. G061 needs more: the B057 relative extension
must first be realized in that object, and both the equator-extension image
and base-locus kernel must map compatibly so that the morphism descends to the
primitive ambient target.

B022 and B082 show that these quotients have nontrivial kernels and only
forward maps. Properness alone neither identifies the chain-level source nor
proves $q_P(t_\psi)=c$ after quotient. Declaring the B097 square automatic
would assume the missing comparison.

The re-entry condition is G061: construct the exact quotient-compatible
morphism and verify its value on the specified detector.
