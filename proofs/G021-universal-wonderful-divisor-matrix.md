---
brick_id: G021
status: EXPLORATORY
base_field: C
variety: the projectivized exceptional fiber of a wonderful resolution of an arbitrary central representable hyperplane arrangement, for a building set of connected flats
smoothness: every iterated blow-up center and the resulting wonderful fiber are smooth; the boundary is simple normal crossing
projectivity: every blow-up is projective and the iterated blow-up of projective space is projective
dimension: arbitrary arrangement rank d at least 2, with exceptional fiber dimension d-1
codimension: building-set flats have arrangement codimension at least 2; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: rational divisor classes in Betti cohomology and the divisor-class component of the logarithmic residue complex
hodge_type: divisor classes have type (1,1); after coefficient normalization the induced degree-one residue equations are sought in type (0,0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no downstream algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B044-B048, G019-G020, and Li S038
claim: For every representable central arrangement and every permissible wonderful blow-up order, H^2 of the central exceptional fiber has basis h and the exceptional classes e_F, every strict branch has class h minus the sum of e_F over building flats contained in that branch, and the resulting divisor-class residue matrix is order independent and triangular.
falsifier: a permissible center that fails to add an independent exceptional Picard generator, a later center contained in an earlier exceptional divisor and changing its class, a strict branch with multiplicity other than one along some building flat, or two permissible orders producing inequivalent named divisor matrices
---

# G021 - Universal wonderful divisor matrix

Let \(\mathcal G\) be the nontrivial connected-flat building set of a
central representable arrangement in \(\mathbf C^d\). After the origin
blow-up, its fiber is \(E_0=\mathbf P^{d-1}\). Resolve the projectivized
arrangement by any Li-permissible order of the dominant transforms of
\(\mathbf P(F)\), \(F\in\mathcal G\setminus\{0\}\).

The sought theorem is the simultaneous formula

\[
 H^2(E_{\mathcal G},\mathbf Q)
 =\mathbf Qh\oplus\bigoplus_{F\in\mathcal G\setminus\{0\}}\mathbf Qe_F,
 \qquad
 [\widetilde H_i]=h-\sum_{F\subset H_i}e_F.
\]

It must be proved by induction through arbitrary comparable and incomparable
centers. At each step one must check that the dominant transform of a later
center is not contained in an earlier exceptional divisor, that a linear
branch containing the center has multiplicity exactly one, and that blow-ups
of the separated incomparable centers commute. The names \(e_F\) must be
intrinsic to their maps onto \(F\), not chosen after comparing Picard groups.

If the formula holds, the divisor-class part of the G019 residue map is
forced to be

\[
 h\otimes\sum_i a_i\delta_i
 +\sum_F e_F\otimes
 \left(w_F-\sum_{F\subset H_i}a_i\delta_i\right).
\]

This would prove triangularity of the geometric matrix only. G021 does not
assert that the degree-one coefficient sheaf contains exactly the rows
\(W_F\), exclude additional incidence cohomology, perform the perverse
strict-support audit, or construct an algebraic cycle. Those remain separate
obligations in G019.
