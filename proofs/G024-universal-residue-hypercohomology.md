---
brick_id: G024
status: PROVED
base_field: C
variety: the central wonderful fiber of an arbitrary representable nodal discriminant arrangement
smoothness: the wonderful fiber is smooth projective and its branch/building boundary is simple normal crossing
projectivity: the fiber and every boundary divisor are projective
dimension: arbitrary arrangement rank d at least 2, with wonderful fiber dimension d-1
codimension: branch and building boundary divisors have codimension one on the fiber; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: rational logarithmic residue hypercohomology and Betti divisor classes
hodge_type: the desired degree-one kernel is required to be pure type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B038-B052, G019-G023, Green-Griffiths S021, Saito S022/S037, and Li S038
claim: The only differential affecting total degree one on every wonderful fiber is the divisor-class-weighted residue map from B050's coefficient sections, its equations are exactly B049's global and flat partial-sum rows, and its kernel is canonically the full vanishing-cycle relation space.
falsifier: a nonconstant global section of a coefficient support, an additional spectral-sequence differential entering total degree one, a residue extension class not equal to the corresponding divisor class, or a kernel different from the full relation space
---

# G024 - Universal residue hypercohomology

B049 fixes the divisor matrix, B050 fixes the coefficient sheaves, and B051
removes lower-support contamination. It remains to prove globally that

\[
 H^0\!\left(\mathcal H^1\right)
 \longrightarrow H^2(E_{\mathcal B},K)
\]

is the sole differential affecting total degree one and is the
divisor-class-weighted residue map. In the basis (h,(e_F)), it must be

\[
 h\otimes\sum_i a_i\delta_i+
 \sum_F e_F\otimes
 \left(w_F-\sum_{F\subset H_i}a_i\delta_i\right).
\]

The independent divisor basis forces each (w_F) to be the
corresponding partial sum and leave exactly
(\sum_i a_i\delta_i=0\). B052 proves that all coefficient supports are
connected, (H^1(E,K)=0), and no other spectral-sequence arrow affects total
degree one. The logarithmic residue extension is the divisor-class-weighted
map, so its kernel is exactly the full relation space.
