---
brick_id: G018
status: PROVED
base_field: C
variety: a four-dimensional nodal smoothing slice whose central hyperplane arrangement has two nested dependent flats
smoothness: the parameter fourfold is smooth; the central projective fiber is nodal and nearby fibers are smooth; a wonderful resolution is required
projectivity: the wonderful blow-up morphisms and exceptional strata are projective over their centers, and the fiber over the origin is projective; the parameter calculation is local analytic, while the motivating hyperplane-section family is projective
dimension: parameter dimension 4, dependent flats of codimensions 2 and 3, ambient projective variety dimension 2n, and nearby fiber dimension 2n-1
codimension: nested arrangement flats have codimensions 2 and 3; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: Picard-Lefschetz vanishing cycles, rational intersection complexes, wonderful-model residues, perverse direct images, and mixed Hodge modules
hodge_type: the sought degree-one relation channel must be pure type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B043-B046 and G015-G017
claim: For a rank-four nodal arrangement with one dependent codimension-three flat contained in one dependent codimension-two flat, the wonderful-resolution degree-one IC channel remains the full rational type-(0,0) relation kernel.
falsifier: a nested exceptional-divisor incidence imposes an additional relation, creates a class, or contributes a non-full-support summand in ordinary degree one
---

# G018 - Nested-dependent-flat channel

This is the first gate not reduced to blowing up disjoint flat centers after
the origin. Fix branch sets \(S\subset T\) whose monodromy spans satisfy
\(W_S\subset W_T\subset W\), with dependent flats of codimensions two and
three nested in the arrangement lattice.

The falsifiable theorem is that, after the building-set blow-ups, every new
exceptional residue coefficient is uniquely forced to the corresponding
partial cycle sum and the remaining equation is exactly
\(\sum_i a_i\delta_i=0\). The proof must also audit strict supports on both
flats and their incidence; disjoint-center arguments from B045 do not apply.

B046 resolves the first nested case. For
\(Z=\operatorname{Bl}_{\widetilde\ell}\operatorname{Bl}_p\mathbf P^3\),
the divisor basis \(h,e_T,e_S\) gives the equations

\[
 \sum_i a_i\delta_i=0,
 \qquad
 w_T=\sum_{i\in T}a_i\delta_i,
 \qquad
 w_S=\sum_{i\in S}a_i\delta_i.
\]

The nested exceptional divisors therefore record the two partial sums but
impose no new relation. Flat- and point-supported direct-image summands start
in ordinary degree two, and the degree-one downstairs IC stalk is pure type
\((0,0)\). G018 constructs no algebraic cycle and does not establish the
corresponding theorem for arbitrary building sets.
