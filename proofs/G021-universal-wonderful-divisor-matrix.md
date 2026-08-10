---
brick_id: G021
status: PROVED
base_field: C
variety: the projectivized exceptional fiber of a wonderful resolution of an arbitrary central representable hyperplane arrangement, for an arbitrary building set of flats
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
dependencies: B044-B049, G019-G020, NG035, and Li S038
claim: For every representable central arrangement and every permissible wonderful blow-up order, H^2 of the central exceptional fiber has basis h and the exceptional classes e_F, every strict branch has class h minus the sum of e_F over building flats contained in that branch, and the resulting divisor-class residue matrix is order independent and triangular.
falsifier: failure of the inclusion-compatible Picard decomposition, multiplicity greater than one along a contained linear branch, failure of Li's canonical comparison to preserve the labelled boundary divisors and strict branches, or a permissible order violating the intrinsic formula
---

# G021 - Universal wonderful divisor matrix

Let \(\mathcal G\) be an arbitrary building set of nontrivial flats of a
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

The tempting direct induction through every permissible order is false in
raw exceptional coordinates: if a curve is blown up before a point contained
in it, the dominant transform of the point lies inside the first exceptional
divisor. NG035 records the counterexample. B049 repairs the argument by
proving the formula in an inclusion-compatible order and transporting the
intrinsic labelled boundary divisors through Li's canonical wonderful-model
comparison. Raw exceptional coordinates may change by an integral triangular
basis transformation; the intrinsic classes \(e_F=[D_F]\) do not.

If the formula holds, the divisor-class part of the G019 residue map is
forced to be

\[
 h\otimes\sum_i a_i\delta_i
 +\sum_F e_F\otimes
 \left(w_F-\sum_{F\subset H_i}a_i\delta_i\right).
\]

This proves triangularity of the geometric matrix only. G021 does not
assert that the degree-one coefficient sheaf contains exactly the rows
\(W_F\), exclude additional incidence cohomology, perform the perverse
strict-support audit, or construct an algebraic cycle. Those remain separate
obligations in G019. Those are isolated next as G022.
