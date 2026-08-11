---
brick_id: B041
status: PROVED
base_field: C
variety: a two-dimensional nodal smoothing slice whose reduced central discriminant is the uniform arrangement U_(2,r) of r distinct lines, and its blow-up at the origin
smoothness: the parameter surface and blow-up are smooth; the resolved divisor is simple normal crossing; the central projective fiber has r ordinary double points and nearby fibers are smooth
projectivity: the blow-up and exceptional P^1 are projective; the parameter calculation is local analytic, while the motivating hyperplane-section family is projective
dimension: parameter surface dimension 2, exceptional curve dimension 1, ambient projective variety dimension 2n, and nearby fiber dimension 2n-1
codimension: the arrangement center has codimension 2, exceptional marked points have codimension 1 on the exceptional curve, and downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: Picard-Lefschetz vanishing cycles, rational intersection complexes, logarithmic residues, proper direct images, and polarizable rational mixed Hodge modules
hodge_type: after the Q(n) normalization, the downstairs degree-one IC stalk is pure of type (0,0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B035-B040, B134, Green-Griffiths S021, and Saito S022/S037
claim: For every r at least 3, the polarized homological model dual to the downstairs degree-one cohomological IC stalk of a U_(2,r) nodal arrangement is the full rational relation kernel, and both are pure type (0,0) after Q(n).
falsifier: an r at least 3 for which the exceptional residue transgression is not e_i -> delta_i, a point-supported direct-image term contributes in ordinary degree one, or the relation kernel has a non-(0,0) Hodge component after Q(n)
---

# B041 - Uniform rank-two multipart channel

The arguments B035-B040 do not depend on the number five. This brick records
their uniform rank-two consequence.

Let \(r\ge3\) distinct discriminant lines pass through the origin of a smooth
parameter surface \(B\). Blowing up the origin gives

\[
 E\simeq\mathbf P^1
\]

with \(r\) distinct marked crossings \(p_i=E\cap D_i\). For pairwise-disjoint
ordinary double points, Picard-Lefschetz gives

\[
 N_E=\sum_{i=1}^rN_i,
 \qquad N_iN_j=0,
 \qquad N_EN_i=0.
\]

Write \(W=\operatorname{span}_{\mathbf Q}\{\delta_1,\ldots,\delta_r\}\) and
\(K=\ker N_E\). The B036 crossing calculation is unchanged: every marked
point contributes one degree-one generator. The exceptional complex has
ordinary cohomology sheaves

\[
 \mathcal H^0=K_E,
 \qquad
 \mathcal H^1=\bigoplus_{i=1}^r\mathbf Q_{p_i}.
\]

Since \(E\) is a curve, the only differential affecting total degree one is

\[
 d_2:\mathbf Q^r\longrightarrow H^2(E,K_E)\simeq K.
\]

The logarithmic residue sequence for
\(P=p_1+\cdots+p_r\),

\[
 0\to\Omega_E^1\to\Omega_E^1(\log P)
 \xrightarrow{\operatorname{Res}}\bigoplus_i\mathbf C_{p_i}\to0,
\]

has connecting map \((c_i)\mapsto\sum_i c_i\). The local residue at \(p_i\)
is \(\delta_i\), exactly as in B038. Hence

\[
 d_2(a_1,\ldots,a_r)=\sum_{i=1}^r a_i\delta_i
\]

on the rational Betti side, and

\[
 \mathbb H^1(E,A|_E)
 =\ker\!\left(\mathbf Q^r\xrightarrow{e_i\mapsto\delta_i}W\right).
\]

The B039 amplitude argument also depends only on the fact that the base is a
surface and the exceptional fiber a curve. For \(P=A[2]\), \(R\pi_*P\) is
perverse, and strict-support decomposition gives

\[
 R\pi_*A\simeq IC_B(L_{\mathbf Q})\oplus i_{0*}H_0[-2].
\]

The point term is in ordinary degree two, so proper base change identifies
the displayed exceptional kernel canonically with the downstairs
\(H^1(IC_B(L_{\mathbf Q})_0)\).

Finally, after Saito's \(\mathbf Q(n)\) normalization, Proposition 1.7 makes
each of the \(r\) crossing generators \(\mathbf Q(0)\). The transgression is
a morphism of mixed Hodge structures, and therefore

\[
 H^1(IC_B(L_{\mathbf Q})_0)
 \simeq
 \ker(\mathbf Q(0)^r\to W)
 \simeq \mathbf Q(0)^{\,r-s},
 \qquad s=\dim_{\mathbf Q}W.
\]

Thus every uniform rank-two multipart arrangement has the full rational
type-\((0,0)\) relation channel.

## Propagation and limit

For a partition into independently smoothable blocks, rank two permits at
most two nodes per block. B041 therefore covers arbitrarily many blocks in
a two-dimensional smoothing slice. It does not cover higher-rank smoothing
matroids, whose resolutions have higher-dimensional exceptional strata and
additional incidence cohomology.

The next smallest unresolved uniform model is \(U_{3,7}\): two independent
rank-three blocks cover at most six elements, while seven elements require
at least three blocks. Blowing up its origin produces an exceptional
\(\mathbf P^2\) carrying seven lines and new pair-intersection strata. That
is the next falsifiable gate.

## Scope guard

B041 is a theorem for one class of local arrangements. It is not a reduction
of arbitrary multipart arrangements to rank two and is not global progress
toward algebraic cycles on arbitrary smooth projective varieties. The
standard rational Hodge Conjecture and G015 remain open.
