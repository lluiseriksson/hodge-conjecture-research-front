---
brick_id: B042
status: PROVED
base_field: C
variety: a three-dimensional nodal smoothing slice whose reduced central discriminant is the uniform arrangement U_(3,r) of r central hyperplanes, and its blow-up at the origin
smoothness: the parameter threefold and blow-up are smooth; the projectivized arrangement has no triple line concurrence, so the resolved divisor is simple normal crossing; the central projective fiber has r ordinary double points and nearby fibers are smooth
projectivity: the blow-up and exceptional P^2 are projective; the parameter calculation is local analytic, while the motivating hyperplane-section family is projective
dimension: parameter space dimension 3, exceptional divisor dimension 2, ambient projective variety dimension 2n, and nearby fiber dimension 2n-1
codimension: the arrangement center has codimension 3, exceptional lines have codimension 1 and their pair intersections codimension 2 in the exceptional P^2, and downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: Picard-Lefschetz vanishing cycles, rational intersection complexes, logarithmic residues, perverse direct images, and polarizable rational mixed Hodge modules
hodge_type: after the Q(n) normalization, the downstairs degree-one IC stalk is pure of type (0,0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B035-B041, B134, Green-Griffiths S021, and Saito S022/S037
claim: For every r at least 3, the polarized homological model dual to the downstairs degree-one cohomological IC stalk of a U_(3,r) nodal arrangement is the full rational relation kernel, and both are pure type (0,0) after Q(n).
falsifier: a line-pair stratum producing an additional degree-one quotient, a residue transgression different from e_i -> delta_i, a point-supported direct-image summand in ordinary degree one, or a non-(0,0) component after Q(n)
---

# B042 - Uniform rank-three multipart channel

This brick computes the first higher-rank gate \(U_{3,7}\), uniformly for
\(U_{3,r}\).

## Blow-up and incidence strata

Let \(H_1,\ldots,H_r\subset\mathbf C^3\) be the central hyperplanes of a
simple realization of \(U_{3,r}\). Any three defining linear forms are
independent. After blowing up the origin, the exceptional divisor is

\[
 E\simeq\mathbf P^2,
\]

and \(L_i=E\cap\widetilde H_i\) is a projective line. No three \(L_i\) meet:
a triple point would give a nonzero common kernel for three defining forms.
Thus the total transform is SNC. At a general point of \(L_i\), the local
components are \(E,\widetilde H_i\); at
\(p_{ij}=L_i\cap L_j\), they are
\(E,\widetilde H_i,\widetilde H_j\).

## Cohomology sheaves on the exceptional plane

For distinct ordinary double points, the vanishing cycles have zero mutual
intersection. Hence

\[
 N_E=\sum_iN_i,
 \qquad N_iN_j=N_EN_i=0.
\]

Put \(W=\operatorname{Im}N_E=\operatorname{span}\{\delta_i\}\) and
\(K=\ker N_E=\bigcap_i\ker N_i\). Because every product of two logarithms
vanishes, the local intermediate-extension complex has no term beyond
degree one.

For \(S\subseteq\{1,\ldots,r\}\) with \(|S|\le2\), its degree-one stalk on
the stratum contained in the \(L_i\), \(i\in S\), is

\[
 F_S=\operatorname{coker}\!\left[
 V\longrightarrow W\oplus\bigoplus_{i\in S}\mathbf Q\delta_i
 \right].
\]

There is a canonical isomorphism

\[
 F_S\xrightarrow{\sim}\bigoplus_{i\in S}\mathbf Q\delta_i.
\]

Indeed, for \((w,(u_i))\), choose \(v\in V\) with \(N_Ev=w\) and send its
class to \((u_i-N_iv)_i\). A different lift differs by an element of \(K\),
on which every \(N_i\) vanishes. The kernel is exactly the image of \(V\).
These isomorphisms commute with generization from \(p_{ij}\) to the two
lines. Consequently the ordinary cohomology sheaves of the exceptional
restriction \(A|_E\) are

\[
 \mathcal H^0(A|_E)=K_E,
 \qquad
 \mathcal H^1(A|_E)=\bigoplus_{i=1}^r\mathbf Q_{L_i},
 \qquad
 \mathcal H^{\ge2}(A|_E)=0.
\]

The pair-intersection strata create no extra skyscraper quotient.

## Exceptional transgression

The only differential that can affect total degree one in the
local-to-global spectral sequence is

\[
 d_2:\bigoplus_iH^0(L_i,\mathbf Q)
 \longrightarrow H^2(E,K_E).
\]

For the SNC divisor \(D=\sum_iL_i\), the residue sequence is

\[
 0\longrightarrow\Omega_E^1
 \longrightarrow\Omega_E^1(\log D)
 \xrightarrow{\operatorname{Res}}
 \bigoplus_i\mathcal O_{L_i}\longrightarrow0.
\]

The connecting homomorphism sends constants \((c_i)\) to

\[
 \sum_i c_i[L_i]
 =\left(\sum_i c_i\right)h
 \in H^1(E,\Omega_E^1),
\]

where \(h\) is the hyperplane class. Pushing the \(i\)-th residue through
the local Picard-Lefschetz map sends its generator to \(\delta_i\in K\).
Naturality of the connecting morphism therefore gives, on the rational
Betti side,

\[
 d_2(a_1,\ldots,a_r)=\sum_i a_i\delta_i.
\]

It follows that

\[
 \mathbb H^1(E,A|_E)
 =\ker\!\left(
 \mathbf Q^r\xrightarrow{e_i\mapsto\delta_i}W
 \right).
\]

## Non-semismall direct-image audit

The blow-up of a threefold at a point is not semismall: its defect is one.
Thus B039's perverse argument cannot be copied verbatim.

Set \(P=A[3]\). The preceding two-row description and
\(E=\mathbf P^2\) show that
\(R\Gamma(E,A|_E)[3]\) has no cohomology above degree \(1\). Away from the
origin, the blow-up is an isomorphism. Hence

\[
 R\pi_*P\in{}^pD^{\le1}.
\]

Applying the same argument to the Verdier dual gives
\(R\pi_*P\in{}^pD^{\ge-1}\). Saito's projective decomposition and
strict-support theorem therefore yield

\[
 R\pi_*P\simeq
 IC_B(L_{\mathbf Q})[3]
 \oplus H_{-1}[1]\oplus H_0\oplus H_1[-1],
\]

where the \(H_j\) are point-supported polarizable Hodge modules; a zero
summand is allowed. Undoing the dimension-three shift gives point terms in
ordinary degrees \(2,3,4\):

\[
 R\pi_*A\simeq IC_B(L_{\mathbf Q})
 \oplus H_{-1}[-2]\oplus H_0[-3]\oplus H_1[-4].
\]

None contributes to ordinary degree one. Proper base change consequently
identifies the exceptional relation kernel canonically with

\[
 H^1\!\left(IC_B(L_{\mathbf Q})_0\right).
\]

## Hodge type

After Saito's \(\mathbf Q(n)\) normalization, Proposition 1.7 applies at the
two- and three-component SNC strata because all pairwise logarithm products
vanish. It makes every line-supported degree-one generator a copy of
\(\mathbf Q(0)\), compatibly at \(p_{ij}\). The transgression is a morphism
of rational mixed Hodge structures. Its kernel, and hence the downstairs IC
stalk, is therefore

\[
 \mathbf Q(0)^{\,r-s},
 \qquad s=\dim_{\mathbf Q}W.
\]

## Scope guard

B042 proves the full relation-channel statement for uniform rank-three
arrangements, including the first three-block case \(U_{3,7}\). It does not
cover nonuniform arrangements, rank at least four, or construct an algebraic
cycle. It is not counted as progress toward the general Hodge Conjecture.
