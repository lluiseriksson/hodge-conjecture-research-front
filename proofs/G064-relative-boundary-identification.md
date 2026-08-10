---
brick_id: G064
status: EXPLORATORY
base_field: C with all relative homology and Hodge data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a prescribed primitive rational Hodge class, its B057-B058 detector, and the actual isolated clean nodal collision
smoothness: X and nearby hyperplane fiber smooth; target has only ordinary double points; good retraction chosen
projectivity: ambient hyperplane family and collision projective
dimension: ambient 2n; hyperplane fibers 2n-1; collision base 1
codimension: middle codimension n; target singular locus finite
coefficient_field: Q
cohomology_theory: relative singular homology, nearby and vanishing cycles, good retraction, perverse full-support relation coordinate, and primitive ambient pushforward
hodge_type: local relation and primitive ambient image rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B057-B058, B081-B083, B093-B101, G047-G063, G065, NG069-NG077
claim: Construct a relative comparison sending the B057 detector to a class gamma_t in H_(2n)(Y_c,Z_c;Q(n)), prove its boundary equals the canonical full-support local relation coordinate r_H(beta_sp), and prove its primitive ambient pushforward is B058's class c.
falsifier: failure to define the relative comparison, a different local boundary, or incompatibility of primitive ambient pushforward with the B057 tube class
---

# G064 — Identify the B057 detector's local relative boundary

**Status:** EXPLORATORY

Construct from the actual collision a comparison

\[
 \kappa(t_\psi)=\gamma_t
 \in H_{2n}(Y_c,Z_c;\mathbf Q(n))
\]

for B057's specified nearby detector. Prove:

1. its relative boundary is the canonical full-support relation coordinate,

   \[
   \partial\gamma_t=r_H(\beta_{\mathrm{sp}});
   \]

2. its primitive pushforward to the fixed ambient $X$ is B058's class $c$.

The second condition is compatibility of the comparison map with ambient
pushforward, not equality of chosen relative representatives. Once these hold,
B100 allows Saito's §2.5 cycle to be any relative lift of the same boundary
and still gives

\[
 \gamma_{r_H(\beta_{\mathrm{sp}})}=c.
\]

This closes G063/G062 without auditing irrelevant representative choices.

B101 separates the remaining proof: both displayed equalities are formal
once G065 constructs a boundary-marked map of pairs and chain-homotopy-compatible
ambient realization maps. NG077 shows why the unmarked equation $\partial t_\psi=0$ cannot
replace that construction.
