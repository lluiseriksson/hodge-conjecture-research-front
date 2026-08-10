---
brick_id: G067
status: EXPLORATORY
base_field: C with the chain comparison over Z before extension to Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, its B058 distributed detector in a plane net, and the actual isolated clean nodal collision with Saito good retraction
smoothness: X and detector fibers smooth; target nodal; nearby collision fiber Y_c smooth
projectivity: X, plane-net hyperplane family, and collision projective
dimension: ambient 2n; hyperplane fibers 2n-1; collision base 1
codimension: middle codimension n; special singular support finite
coefficient_field: Z for marked chains and Q for Hodge structures
cohomology_theory: relative thimble complexes, single-fiber relative homology H_(2n)(Y_c,Z_c), good retraction, B022 quotients, and primitive ambient homology
hodge_type: the resulting local relation and primitive ambient class must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B058, B081-B083, B093-B104, G047-G063, G068, NG069-NG080, S022, S049-S050
claim: Construct from the actual topology-changing collision a chain map that sends the specified B057 distributed thimble representative to gamma_t in H_(2n)(Y_c,Z_c;Z), sends its marked boundary to r_H(beta_sp), and makes Saito's good-retraction ambient realization of gamma_t equal B098's class c after extension to Q and primitive projection.
falsifier: no single-fiber realization, wrong marked boundary or orientation, failure of integrality/rationality, death in a B022 kernel, or mismatch of the two primitive ambient values
---

# G067 — Realize the distributed detector in one nearby-fiber pair

**Status:** EXPLORATORY

Let $C_{\mathrm{dist}}$ be G055's marked thimble complex for the actual B057
word. Construct a collision-induced chain map

\[
 \Lambda:C_{\mathrm{dist}}longrightarrow C_*(Y_c,Z_c;\mathbf Z)
\]

and prove that the chosen detector representative $t$ maps to

\[
 \gamma_t=[\Lambda(t)]
 \in H_{2n}(Y_c,Z_c;\mathbf Z).
\]

The construction must satisfy both class-specific identities

\[
 \partial\gamma_t=r_H(\beta_{\mathrm{sp}}),
 \qquad
 q_S(\gamma_t)=q_P(t)=c
\]

after rational extension and primitive projection, where $q_S$ uses B103's
already-global good retraction and $q_P$ is B098's nearby ambient map.

This is narrower than G066: no second construction of the local/exterior
collapse is needed. It is stronger than an abstract map on homology because
the marked boundary and the closed ambient realization must arise from the
same collision-induced chain map.

B104/NG080 show that even this full chain map is stronger than necessary.
G068 retains the minimal class-specific content: construct one collision
pair and kill the detector's lift-independent relative-bordism obstruction
coset.
