---
brick_id: G063
status: EXPLORATORY
base_field: C with all relative homology and Hodge data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a prescribed primitive rational Hodge class, its B057-B058 detector, and the actual collision to an isolated clean nodal target
smoothness: X and nearby hyperplane fiber smooth; target has only ordinary double points; Saito good retraction chosen
projectivity: ambient hyperplane family and collision projective
dimension: ambient 2n; hyperplane fibers 2n-1; collision base 1
codimension: middle codimension n; target singular locus finite
coefficient_field: Q
cohomology_theory: relative singular homology, good retraction, nearby and vanishing cycles, perverse full-support relation coordinate, B022 quotients, and Saito ambient map
hodge_type: local relation and ambient image rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B022, B057-B058, B081-B083, B093-B099, G047-G062, NG069-NG075
claim: Construct Saito's good-retraction relative class gamma' for the canonical full-support relation coordinate of a special lift, prove its boundary is that coordinate, and identify gamma' with the B057 detector chain after both B022 quotients.
falsifier: failure of the relative comparison map, a different boundary relation, discrepancy by an equator or base-locus class affecting the ambient image, or failure to identify the B057 chain
---

# G063 — Identify Saito's relative cycle with the B057 chain

**Status:** EXPLORATORY

For the isolated clean nodal target, choose Saito's good retraction
$\rho:Y_c\to Y_0$ and vanishing neighborhood $Z_c$. For a relevant special
lift $\beta_{mathrm{sp}}$, let $r_H(\beta_{mathrm{sp}})$ be its canonical
full-support relation coordinate. Construct

\[
 \gamma'\in H_{2n}(Y_c,Z_c;\mathbf Q(n))
\]

and prove all four identities:

1. $\partial\gamma'=r_H(\beta_{mathrm{sp}})$;
2. under the collision comparison, $\gamma'$ is the B057 relative extension
   $\tau_g(\alpha)$;
3. the comparison respects the equator-extension quotient; and
4. it respects the base-locus quotient.

B099 then gives
$\gamma_{r_H(\beta_{mathrm{sp}})}=c$ and the prescribed pairing is nonzero.
The gate asks for equality of actual relative classes, not merely equality of
dimensions, monodromy invariance, or existence of some lift.
