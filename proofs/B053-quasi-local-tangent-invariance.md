---
brick_id: B053
status: PROVED
base_field: C
variety: a Green-Griffiths quasi-local normal-crossing nodal smoothing germ, its blow-up along the common discriminant stratum, and the projectivized tangent arrangement on the exceptional normal fiber
smoothness: the base, common stratum, and discriminant branches are smooth; the quasi-local coordinate condition makes the reduced total transform simple normal crossing
projectivity: the motivating nodal family is projective and the blow-up is projective; the transverse calculation is local analytic
dimension: arbitrary base dimension; the common stratum has transverse codimension c at least 2 and exceptional normal fiber dimension c-1
codimension: the common discriminant stratum has codimension c and branch supports are divisors; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: rational Picard-Lefschetz intermediate extensions, logarithmic residues, Betti hypercohomology, and polarizable mixed Hodge modules
hodge_type: the degree-one channel and its tangent-arrangement comparison are pure type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B043, B050-B052, B134, G019, G025-G026, NG036, Green-Griffiths S021, and Saito S022/S037
claim: For every Green-Griffiths quasi-local normal-crossing nodal germ, blowing up the common stratum identifies its downstairs degree-one rational IC/MHS channel canonically with that of the uniform central tangent arrangement; its polarized homological model is the full vanishing-cycle relation kernel and the cohomological stalk is the dual kernel.
falsifier: failure of one-step SNC resolution, a nonuniform exceptional tangent arrangement, a residue depending on higher branch jets, a different exceptional degree-one complex, or lower-support contamination in degree one
---

# B053 - Quasi-local tangent invariance by common blow-up

This brick proves G026 without asserting the false analytic linearization in
G025/NG036.

## Quasi-local geometry

Let (S) be smooth, let (D_i=(s_i=0)) be the smooth local discriminant
branches, and put (C=\bigcap_iD_i), of codimension (c\ge2). The
Green-Griffiths condition says that on a slice normal to (C), every subset
of at most (c) of the (s_i) is part of a coordinate system. Consequently
the normal covectors

\[
 \ell_i=ds_i|_{N_{C/S}}
\]

realize the uniform matroid (U_{c,r}): every (c) are independent.

Blow up (C). The exceptional divisor is
(E=\mathbf P(N_{C/S})), and the strict transform of (D_i) meets each
normal fiber (E_x\simeq\mathbf P^{c-1}) in

\[
 L_i=\mathbf P(\ker\ell_i).
\]

No (c) of these hyperplanes meet and every smaller subset meets
transversally. Hence (E+\sum_i\widetilde D_i) is SNC along (E).
It is also SNC off (E) near (C): if a point lay on more than (c)
branches, any chosen (c) would cut out (C) locally and force the point
back into (C); for at most (c) branches, openness of differential
independence gives transversality. Thus the common blow-up is a one-step SNC
resolution.

## Independence from higher jets

The exceptional intersections \(L_i\) use only \(\ell_i\). A loop around
(widetilde D_i) has residue (N_i), while a loop around (E) has

\[
 N_E=\sum_iN_i.
\]

These statements are valuation-theoretic: every (s_i) vanishes to order
one along (C), so higher Taylor coefficients contribute neither to the
exceptional multiplicity nor to its monodromy. The exceptional normal-fiber
complex is therefore exactly B043's (U_{c,r}) complex:

\[
 \mathcal H^0=K_E,qquad
 \mathcal H^1=\bigoplus_i\mathbf Q_{L_i}\delta_i,qquad
 \mathcal H^{\ge2}=0.
\]

Every \(L_i\) has class \(h\), \(H^1(E,K)=0\), and the unique
total-degree-one transgression is

\[
 (a_i)\longmapsto h\otimes\sum_i a_i\delta_i.
\]

Thus the polarized homological exceptional hypercohomology is canonically
the full relation kernel, while the cohomological group is its dual. The
same normal-fiber amplitude as B043/B051 puts every proper
strict-support summand first in ordinary degree two, so proper base change
identifies this group with the downstairs degree-one IC stalk.

## Tangent comparison and Hodge type

The central tangent arrangement has the same (E,L_i,N_E,N_i) data.
Projection to the labelled branch coefficients canonically identifies both
dual homological models with

\[
 \ker\!\left(\mathbf Q^r\xrightarrow{e_i\mapsto\delta_i}
 \operatorname{span}\{\delta_i\}\right).
\]

The cohomological stalks are the duals of these kernels. All branch images
are \(\mathbf Q(0)\) after the \(\mathbf Q(n)\) twist and
the residue differential is a rational mixed-Hodge morphism. Hence this
comparison preserves the pure type-\((0,0)\) structure. No Whitney
trivialization or simultaneous analytic coordinate change is needed.

## Scope guard

B053 handles the exact Green-Griffiths quasi-local condition, whose tangent
matroid is uniform. G015's sought multipart analogue allows nonuniform
dependencies across separately independent blocks. Extending the common
blow-up argument to a nonlinear clean arrangement and its wonderful model is
G027. B053 constructs no class-paired degeneration and no algebraic cycle;
actual progress toward the general Hodge Conjecture remains zero.
