---
brick_id: G023
status: PROVED
base_field: C
variety: the wonderful resolution of an arbitrary central representable nodal discriminant arrangement and all strata over its origin
smoothness: the parameter slice and wonderful resolution are smooth and the resolved boundary is simple normal crossing
projectivity: the wonderful morphism and every fiber stratum are projective
dimension: arbitrary parameter rank d at least 2; supports have arbitrary codimension at least 2
codimension: arbitrary building-flat and nested-set supports; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: rational perverse direct images, decomposition theorem, ordinary stalk cohomology, and polarizable mixed Hodge modules
hodge_type: any surviving ordinary-degree-one full-support group must be pure type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B039-B051, G019-G022, Saito S037, and Li S038
claim: In the proper direct image from every wonderful resolution, every non-full-support strict-support summand begins in ordinary stalk degree at least two, so B050's resolved degree-one group descends canonically to the downstairs IC stalk.
falsifier: a building-flat or nested-set support carrying a nonzero strict-support summand in ordinary stalk degree one after all dimension and perverse shifts are restored
---

# G023 - Universal strict-support bound

B050 closes the coefficient-sheaf calculation but not descent through the
wonderful morphism. For every proper support (S) in the origin fiber,
compute the normal wonderful fiber and its shifted hypercohomology, then prove
that the corresponding strict-support summands occur only in ordinary stalk
degrees at least two.

B051 proves the bound uniformly. On a normal codimension-\(c\) slice, B050
bounds the central-fiber hypercohomology by (2c-2); duality gives perverse
amplitude \([-(c-2),c-2]\). Undoing the ambient shift puts every proper
support first in ordinary degree (c-(c-2)=2). Thus no lower support alters
the degree-one group. The remaining G019 obligation is the global residue
hypercohomology, isolated next as G024.
