---
brick_id: G056
status: EXPLORATORY
base_field: C with all sheaf and homology data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold, a prescribed primitive rational Hodge class, and the actual G055 one-parameter marked collision
smoothness: ambient and generic hyperplane fibers smooth; special hyperplane clean nodal; total space satisfies the hypotheses of the chosen rational Hodge-module model
projectivity: ambient family and collision projective
dimension: ambient 2n; hyperplane fibers 2n-1; collision base 1
codimension: middle codimension n; target nodal stratum of positive codimension
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, nearby and vanishing cycles, special-stalk intersection cohomology, local monodromy complex, perverse filtration, and B022 quotients
hodge_type: the selected local coordinate must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B022, B081-B084, B092, G046-G055, NG068
claim: For the actual G055 collision, construct a rational Hodge-module edge map from the special-lift group to B009/B052's local relation group, prove the B058 lift ambiguity lies in its pairing-null kernel, and show the resulting detector coordinate is nonzero and survives both B022 quotients with nonzero prescribed pairing.
falsifier: failure to define the edge map, lift-dependent coordinates, zero local coordinate, a B022-kernel image, wrong Hodge type, or loss of prescribed pairing
---

# G056 — Compute the special lift's local-relation coordinate

**Status:** EXPLORATORY

After G055 constructs the actual collision comparison and B083-B084 provide a
special lift $\beta$ of the nearby B058 class, construct the geometric map

\[
 \rho_H:H^q(i_p^*K)\longrightarrow
 H^1(C_H)\simeq R(H)_1.
\]

The gate requires three calculations:

1. every allowed change of $\beta$ maps under $\rho_H$ into the joint kernel
   of the two B022 projections and the prescribed pairing;
2. $\rho_H(\beta)$ is rational type $(0,0)$ and nonzero; and
3. its ambient image after both quotients pairs nontrivially with the fixed
   primitive Hodge class.

B092 proves that neither exactness nor type alone determines $\rho_H$ or its
value. It must come from the actual local-to-global Hodge-module comparison,
with degrees and support shifts checked explicitly.
