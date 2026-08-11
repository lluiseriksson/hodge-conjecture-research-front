---
brick_id: G147
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with a specified nonzero primitive rational middle Hodge class and a very ample H having no factorization into two line bundles that each separate every ordered pair of points
smoothness: X and the marked scheme Z are smooth; all central ODP and incidence smoothness clauses remain those of G146
projectivity: the exceptional low-polarization H-embedding, its finite birational Gauss map, the nodal system, and detector family are projective
dimension: dim X=2n; one special Gauss fiber must contain N=D_(2n)(m)>1 marked points
codimension: realize G146 using an exceptional very ample polarization with no two point-separating factors, since every such product has injective Gauss map
coefficient_field: C for polarization, Gauss, jet, profile, and relation data; Q for the specified Hodge class and detector
cohomology_theory: coherent first and second principal parts, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the detector must be rational type (0,0) and have nonzero specified pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B220, G013, G090-G146, NG106-NG180
claim: For every arbitrary (X,zeta), find an exceptional very ample H with no two point-separating factors whose ordinary Gauss map has a D_(2n)(m)-point fiber and realize on that fiber every G146 central-profile, transport, holonomy, congruence, full-system, rational-detector, specified-pairing, pure-cubic-closure, and later-rung clause.
falsifier: one pair (X,zeta) for which every very ample H without two point-separating factors has only smaller Gauss fibers or fails any retained detector clause
---

# G147 — The equality branch is confined to exceptional polarizations

B220 removes every polarization of the form

\[
 H=A\otimes B\qquad(A,B\text{ each separate point pairs}) \tag{1}
\]

from G146: its Gauss fibers are singletons, whereas
\(D_{2n}(m)\ge2(2n+1)>1\).

G147 is the residual equality gate. For every fixed arbitrary
\((X,\zeta)\), find a very ample H outside (1), a birth degree \(m\),
and one special Gauss fiber of cardinality \(D_{2n}(m)\), while retaining
the complete G146 profile and detector package.

In particular, replacing a chosen very ample \(A\) by \(A^k\),
\(k\ge2\), can never approach this gate. G147 is an exceptional
low-polarization construction problem, not an asymptotic-positivity
problem.
