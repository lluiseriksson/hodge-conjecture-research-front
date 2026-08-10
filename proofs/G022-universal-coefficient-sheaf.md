---
brick_id: G022
status: EXPLORATORY
base_field: C
variety: the SNC boundary on the wonderful resolution of an arbitrary central representable nodal discriminant arrangement
smoothness: the parameter slice and wonderful resolution are smooth, and the resolved boundary is simple normal crossing
projectivity: the wonderful morphism is projective and the central exceptional fiber is smooth projective
dimension: arbitrary arrangement rank d at least 2, with central exceptional fiber dimension d-1
codimension: arbitrary building-set flats of arrangement codimension at least 2; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: rational Picard-Lefschetz intermediate extensions, local monodromy complexes, and ordinary cohomology sheaves on the wonderful fiber
hodge_type: after Q(n), every proposed degree-one branch or exceptional coefficient is required to be Q(0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B042-B049, G019-G021, Green-Griffiths S021, and Saito S022
claim: On every wonderful fiber, the unshifted intermediate-extension complex has constant degree-zero sheaf K, degree-one sheaf equal to the generization-compatible sum of the branch coefficient lines and exceptional W_F sheaves, and no higher cohomology sheaves.
falsifier: an SNC incidence stratum whose local intermediate-extension complex has an additional degree-one quotient, a nonzero cohomology sheaf in degree at least two, or a generization map not induced by the evident inclusions among W_F and branch lines
---

# G022 - Universal coefficient-sheaf incidence

B049 removes all divisor-class ambiguity from G019. The remaining first
local obligation is now coefficient-theoretic.

Let \(N_i\) be the Picard-Lefschetz logarithms, let
\(N_F=\sum_{F\subset H_i}N_i\), and put
\(W_F=\operatorname{Im}N_F\). At a stratum incident to branch transforms
\(M_i\) and exceptional divisors \(D_F\), prove that the local lift map from
the common nearby-fiber space identifies degree one with exactly

\[
 \bigoplus_i\mathbf Q\delta_i\oplus\bigoplus_F W_F,
\]

subject only to the evident generization identifications. These stalks must
glue to

\[
 \mathcal H^0=K,qquad
 \mathcal H^1=
 \bigoplus_i(\mathbf Q\delta_i)_{M_i}
 \oplus\bigoplus_F(W_F)_{D_F},qquad
 \mathcal H^{\ge2}=0.
\]

The tested chain and fork arrangements satisfy this formula, but they do not
prove it for arbitrary nested-set incidence. A proof must work over
\(\mathbf Q\), not merely in the complex face-quiver category excluded by
NG-034, and must verify compatibility at intersections of arbitrarily many
boundary divisors.

G022 controls neither global cohomology of these sheaves nor lower strict
supports under the proper direct image. Even if proved, G019 would still
require those two audits before G015 could be promoted.
