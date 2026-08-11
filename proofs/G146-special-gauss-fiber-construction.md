---
brick_id: G146
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with very ample H, a specified nonzero primitive rational middle Hodge class, and a class-directed marked scheme Z
smoothness: X and Z are smooth; the Gauss image may be singular, while every central ODP and incidence smoothness condition remains as in G143-G145
projectivity: the H-embedding, finite birational Gauss morphism, powers H^k, nodal linear system, and detector family are projective
dimension: dim X=2n; the special Gauss fiber must contain N=D_(2n)(m) distinct marked points
codimension: construct the complete G145 package in one non-injective special fiber of the ordinary Gauss normalization map
coefficient_field: C for Gauss, jet, profile, holonomy, and relation data; Q for the Hodge class, detector, and specified pairing
cohomology_theory: coherent principal parts, finite-scheme restrictions, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the detector must be rational type (0,0) and pair nontrivially with the arbitrary specified class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B218, G013, G090-G145, NG106-NG178
claim: For every arbitrary (X,zeta), choose H, m, and a point Lambda of the Gauss image whose normalization fiber contains a reduced subset Z of cardinality D_(2n)(m), and on that same Z realize every G145 central-profile, transport, holonomy, congruence, full-system, rational-detector, specified-pairing, pure-cubic-closure, and later-rung clause.
falsifier: one pair (X,zeta) for which every very ample H and every special Gauss fiber either has fewer than D_(2n)(m) points for all usable m or fails any retained G145 clause
---

# G146 — Construct the detector inside one special Gauss fiber

For a nonzero primitive input class, the H-embedding is not the excluded
linear \(\mathbf P^{2n}\). By B218 its ordinary Gauss map

\[
 \gamma_H:X\longrightarrow\gamma_H(X) \tag{1}
\]

is the finite birational normalization of its image. B217 rewrites the
extremal equality condition as

\[
 Z\subset\gamma_H^{-1}(\Lambda),\qquad
 |Z|=D_{2n}(m), \tag{2}
\]

for one special point \(\Lambda\in\gamma_H(X)\), with every point of
\(Z\) mapping to the same embedded tangent \(2n\)-plane.

G146 asks for (2) together with the *entire* G145 package. A large
normalization fiber alone is not progress toward the Hodge Conjecture:
the central nondegenerate nodal profile, full-support relation, holonomy,
congruence, rational type-\((0,0)\), specified nonzero pairing, and all
later rungs must be constructed on the same marked fiber.
