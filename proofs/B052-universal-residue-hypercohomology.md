---
brick_id: B052
status: PROVED
base_field: C
variety: the central wonderful fiber of an arbitrary representable nodal discriminant arrangement with any building set
smoothness: the wonderful fiber and every branch/building divisor are smooth and the boundary is simple normal crossing
projectivity: the wonderful fiber and all coefficient supports are projective
dimension: arbitrary arrangement rank d at least 2, with wonderful fiber dimension d-1
codimension: coefficient supports are divisors on the fiber; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: rational logarithmic residue hypercohomology, Betti divisor classes, intermediate extensions, and mixed Hodge structures
hodge_type: the resulting degree-one group is pure type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B038-B051, G019-G024, Green-Griffiths S021, Saito S022/S037, and Li S038
claim: The degree-one wonderful-fiber hypercohomology, and hence the downstairs IC stalk, is canonically the full rational vanishing-cycle relation kernel for every representable central nodal arrangement and every building set, and it is pure type (0,0) after Q(n).
falsifier: nonzero H^1 of the constant row, a disconnected coefficient divisor, another spectral-sequence arrow affecting total degree one, a residue extension not represented by its divisor class, failure of the triangular kernel calculation, or lower-support contamination
---

# B052 - Universal residue hypercohomology

This brick proves G024 and completes G019's arbitrary-building-set relation
channel. It combines, rather than repeats, B049-B051.

## The only total-degree-one term

Let (E=E_{\mathcal B}) be the wonderful fiber and (A|_E) the unshifted
complex. B050 gives only two ordinary cohomology sheaves:

\[
 \mathcal H^0=K_E,
 \qquad
 \mathcal H^1=
 \bigoplus_i(i_i)_*\mathbf Q\delta_i
 \oplus\bigoplus_F(i_F)_*W_F.
\]

The variety (E) is obtained from projective space by blow-ups along smooth
connected centers. The degree-one blow-up formula leaves (H^1) unchanged,
so (H^1(E,\mathbf Q)=0), and hence (H^1(E,K)=0). Every strict branch and
every boundary divisor is connected: each begins as a connected projective
linear space or a projective bundle over a connected center, and subsequent
blow-ups preserve connectedness. Therefore

\[
 H^0(E,\mathcal H^1)=
 \bigoplus_i\mathbf Q\delta_i\oplus\bigoplus_FW_F.
\]

In the hypercohomology spectral sequence
(E_2^{p,q}=H^p(E,\mathcal H^q)\), total degree one has no
((1,0)) term. The only surviving candidate is (E_2^{0,1}), and the only
possible differential from it is

\[
 d_2:E_2^{0,1}\longrightarrow E_2^{2,0}=H^2(E,K).
\]

There is no incoming differential and every (d_r) for (r\ge3) lands in
a negative coefficient-sheaf degree. Thus
(mathbb H^1(E,A|_E)=\ker d_2).

## Identification of the transgression

Green-Griffiths' logarithmic model and its residue morphism identify the
Postnikov transgression with the connecting class of the logarithmic residue
sequence. For a smooth divisor (D), the connecting image of its constant
residue section is (c_1(\mathcal O_E(D))=[D]). Tensoring with its rational
Picard-Lefschetz coefficient gives the divisor-class-weighted map. This
argument is local along each SNC component and additive, so arbitrary nested
intersections introduce no further degree-one term.

By B049, in the intrinsic basis (h,(e_F)), the map is exactly

\[
 (a_i,w_F)\longmapsto
 h\otimes\sum_i a_i\delta_i+
 \sum_F e_F\otimes
 \left(w_F-\sum_{F\subset H_i}a_i\delta_i\right).
\]

The divisor classes are independent. Hence every kernel vector satisfies

\[
 \sum_i a_i\delta_i=0,
 \qquad
 w_F=\sum_{F\subset H_i}a_i\delta_i,
\]

and every relation ((a_i)) has one unique such lift. Projection to branch
coordinates therefore gives the canonical isomorphism

\[
 \mathbb H^1(E,A|_E)
 \simeq
 \ker\!\left(\mathbf Q^r\xrightarrow{e_i\mapsto\delta_i}W\right).
\]

## Descent, Hodge type, and scope

B051 proves that no lower strict support contributes in ordinary degree one,
so this is canonically \(H^1(IC_B(L_{\mathbf Q})_0)\). All coefficient
spaces are sums of \(\mathbf Q(0)\) after \(\mathbf Q(n)\), and the residue
map is a morphism of rational mixed Hodge structures. Its kernel is therefore
pure type ((0,0)).

This closes the local theorem for central representable arrangements. It
does not yet prove that every analytic multipart model in G015 is reduced to
such a linear arrangement without changing the IC stalk, and it constructs
no class-paired degeneration or algebraic cycle. Actual progress toward the
general rational Hodge Conjecture remains zero.
