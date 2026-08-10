---
brick_id: B079
status: PROVED
base_field: C
variety: Bl_0(A^2) times a smooth projective curve C of positive genus, mapped properly to A^2
smoothness: source and target are smooth; the map is a smooth-factor product of a toric blowup and is toroidal for the pulled-back toric boundary
projectivity: the morphism is projective; C is projective
dimension: source dimension 3 and target dimension 2
codimension: the exceptional strict support is the origin of codimension 2
coefficient_field: Q
cohomology_theory: rational derived direct image, proper base change, decomposition theorem, Kunneth formula, and pure Hodge structures
hodge_type: the odd proper-support coefficient is H^1(C,Q)(-1), with types (2,1) and (1,2) before normalization
cycle_class_map: not used; downstream map is CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence in the downstream Hodge application
scope: relative and fiberwise
dependencies: B077-B078 and the rational Kunneth formula
claim: A smooth projective toroidal morphism with a non-toric smooth fiber factor can have an odd-degree proper-support summand, even though its toric normal modification has only even support degrees.
falsifier: absence of the point-supported H^1(C,Q)(-1)[-3] summand in the stated derived direct image
---

# B079 — Non-toric coefficients break global toric parity

**Status:** PROVED

Let

\[
 \pi:\widetilde B=\operatorname{Bl}_0(\mathbf A^2)\longrightarrow
 B=\mathbf A^2
\]

and let (C) be a smooth projective curve of genus (g>0). Put
(X=\widetilde B\times C) and
(f=\pi\circ\operatorname{pr}_{\widetilde B}:X\to B). This is a projective
morphism between smooth varieties. With the toric boundary pulled back from
(B), it is the smooth-factor product of a toric blowup and is toroidal.

Purity and the decomposition theorem split the blowup direct image as

\[
 R\pi_*\mathbf Q_{\widetilde B}
 \simeq
 \mathbf Q_B\oplus \mathbf Q_{0}(-1)[-2].
\]

Indeed, the map is an isomorphism off the origin, while the exceptional fiber
is (mathbf P^1); its additional rational cohomology is the one-dimensional
(H^2(\mathbf P^1,\mathbf Q)=\mathbf Q(-1)).

The rational Kunneth formula gives

\[
 Rf_*\mathbf Q_X
 \simeq
 R\pi_*\mathbf Q_{\widetilde B}\otimes R\Gamma(C,\mathbf Q).
\]

Since

\[
 R\Gamma(C,\mathbf Q)
 \simeq
 \mathbf Q
 \oplus H^1(C,\mathbf Q)[-1]
 \oplus \mathbf Q(-1)[-2],
\]

the proper-support part contains

\[
 \mathbf Q_0(-1)[-2],\qquad
 H^1(C,\mathbf Q)(-1)_0[-3],\qquad
 \mathbf Q_0(-2)[-4].
\]

Thus a nonzero point-supported summand occurs in ordinary degree three. Its
coefficient is not Hodge-Tate when (g>0). The normal toric degrees remain
even, but convolution with global fiber cohomology changes total parity.

## Consequence and boundary

Any extension of B078 from globally toric maps to arbitrary toroidal
families must retain the coefficient degree. Local toric parity alone is
false as a statement about total proper-support degrees. This example does
not show that a proper-support term occurs in the exact B057 detector degree;
that coefficient-index equality is the remaining calculation in G044.
