---
brick_id: G062
status: EXPLORATORY
base_field: C with all coefficient objects and maps over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a prescribed primitive rational Hodge class, its B058 detector, and the actual G055 collision to a clean nodal target
smoothness: X and generic hyperplane fibers smooth; target clean nodal; semistable source regular where required
projectivity: plane-net family, collision, proper pushdown, and map to X projective
dimension: ambient 2n; hyperplane fibers 2n-1; plane base 2; collision base 1
codimension: middle codimension n; target nodal stratum of positive codimension
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, nearby cycles, special stalk, perverse filtration, strict support, B022 quotients, and primitive ambient homology
hodge_type: morphism and detector restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B022, B058, B081-B083, B093-B098, G047-G061, NG069-NG074
claim: After realizing t_psi as the B057 chain, prove that the canonical full-support relation coordinate r_H of every relevant special lift satisfies Phi_H(r_H(beta))=q_P(u(beta)), where Phi_H is B010's Saito ambient map and q_P is B098's nearby quotient map.
falsifier: landing outside the canonical full-support grade, noncommutativity of the displayed equality, or incompatibility between the topology-changing comparison and B010's Saito ambient map
---

# G062 — Compare the nearby ambient map with the special Saito map

**Status:** EXPLORATORY

B098 fixes $q_P$ and $q_P(t_\psi)=c$ once G047 realizes the nearby class.
B010 already supplies the special Saito ambient map

\[
 \Phi_H:R(H)_1^{(0,0)}\longrightarrow
 PH_{2n}(X,\mathbf Q(n))^{(0,0)}
\]

The remaining construction is the comparison, not either endpoint map. For
every relevant special lift $\beta$, first take B081/B093's canonical
full-support relation coordinate $r_H(\beta)$ and prove

\[
 \Phi_H(r_H(\beta))=q_P(u(\beta)).
\]

after passing through B081's canonical perverse grade and full-support
summand.

B097 then preserves the known nonzero pairing. The open content is comparison
across the topology-changing boundary between two already-defined ambient
maps, not the generic quotient arithmetic.
