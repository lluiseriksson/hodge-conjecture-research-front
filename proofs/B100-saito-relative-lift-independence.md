---
brick_id: B100
status: PROVED
base_field: C with rational homology and Hodge structures
variety: a one-parameter projective degeneration of hyperplane sections of a smooth projective complex 2n-fold, with isolated singular special fiber
smoothness: ambient X and nearby fiber Y_c smooth; special fiber has isolated singularities and a good retraction
projectivity: X and degeneration projective
dimension: ambient 2n; hyperplane fibers 2n-1
codimension: middle codimension n; special singular locus finite
coefficient_field: Q
cohomology_theory: relative singular homology, limit homology, good retraction, Lefschetz primitive decomposition, and Saito ambient classes
hodge_type: relation and primitive ambient class rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence in the terminal application
scope: relative and fiberwise
dependencies: B010, B099, S022 Sections 2.4-2.5
claim: In Saito's isolated-singularity model, any two nearby relative cycles with the same local vanishing-cycle boundary define the same primitive ambient class; their difference comes from nearby-fiber homology whose image in X is nonprimitive.
falsifier: two relative lifts of one relation whose difference comes from nearby-fiber homology but has nonzero primitive image in X under Saito's hypotheses
---

# B100 — Saito's primitive class is independent of the relative lift

**Status:** PROVED

Let

\[
 \partial:H_{2n}(Y_c,Z_c;\mathbf Q(n))
 \longrightarrow H_{2n-1}(Z_c;\mathbf Q(n))
\]

be Saito's relative boundary map. If
$\partial\gamma'_1=\partial\gamma'_2=\beta$, exactness gives

\[
 \gamma'_1-\gamma'_2
 \in\operatorname{im}H_{2n}(Y_c,\mathbf Q(n)).
\]

S022 §2.4 states that the image of the corresponding nearby/limit group in
$H_{2n}(X,\mathbf Q(n))$ is contained in the nonprimitive part. Therefore
the primitive projection of the difference vanishes. Saito's §2.5
good-retraction construction consequently gives

\[
 \gamma_{\partial\gamma'_1}
 =\gamma_{\partial\gamma'_2}
 \in PH_{2n}(X,\mathbf Q(n)).
\]

Thus B099 does not require literal identity of relative representatives. It
is enough to place B057's detector in Saito's relative group and identify its
boundary with the canonical local relation.

## Boundary

B100 does not construct the comparison from B057's moving-hyperplane
extension to $H_{2n}(Y_c,Z_c)$ or identify its boundary. G064 is that minimal
comparison gate; B101/NG077 reduce its genuinely geometric content to G065's
boundary-marked map of pairs.
