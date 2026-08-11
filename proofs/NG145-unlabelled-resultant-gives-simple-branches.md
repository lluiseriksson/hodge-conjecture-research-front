---
brick_id: NG145
status: NO-GO
base_field: C
variety: a polynomial Morse family with at least two distinct tracked critical points having common critical value zero
smoothness: every critical point is Morse and the critical-point cover is étale; the failure comes solely from collision in the value coordinate
projectivity: not needed for the resultant obstruction; arbitrary-projective transfer requires the labelled full-incidence construction of G114
dimension: failure already occurs for one spatial variable, two tracked nodes, and one auxiliary critical point
codimension: the global value resultant has a multiple root and cannot provide simple implicit equations for labelled escape branches
coefficient_field: C; Q enters only in downstream Hodge detectors
cohomology_theory: univariate resultants, critical values, finite étale covers, and conormal escape ideals
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B172, B179-B181, G113-G114
claim: The unlabelled critical-value resultant, or its squarefree specialization, automatically supplies B180's simple polynomial for every individual tracked branch through a multinodal collision.
falsifier: f=(z^2-1)^2 has two distinct Morse critical points of value zero but resultant 256 w^2(w-1), while the squarefree factor w forgets which of the two labels it represents
---

# NG145 — The value resultant does not split the labels

For \(f=(z^2-1)^2\), B181 computes

\[
 \operatorname{Res}_z(f'(z),w-f(z))=256w^2(w-1). \tag{1}
\]

The roots \(z=-1\) and \(z=1\) are distinct Morse critical points, but
both have critical value zero. Hence

\[
 \partial_w\operatorname{Res}_z(f',w-f)|_{w=0}=0,
\]

contrary to B180's simple-root hypothesis.

Replacing (1) by its squarefree specialization \(w(w-1)\) does not solve
the problem. The single factor \(w\) forgets the two labels and supplies
no individual analytic functions \(\tau_1,\tau_2\), no labelled escape
ideal, and no syzygy comparison through nearby parameters.

## Re-entry condition

G114 must separate the critical points by an additional algebraic
coordinate, split the finite étale critical algebra into labelled factors,
and track the effective degree and denominators of every factor. The
required conormal jets and all Hodge detector clauses remain separate.
