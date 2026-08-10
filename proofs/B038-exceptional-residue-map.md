---
brick_id: B038
status: PROVED
base_field: C
variety: the exceptional P^1 resolving the U_(2,5) central discriminant arrangement in a local slice of a projective nodal hyperplane-section family
smoothness: the exceptional curve is smooth with five distinct simple-normal-crossing marked points; the central projective fiber has five ordinary double points and nearby fibers are smooth
projectivity: the exceptional curve and motivating hyperplane-section family are projective; the parameter calculation is local analytic
dimension: exceptional curve dimension 1, parameter surface dimension 2, ambient projective variety dimension 2n, and nearby fiber dimension 2n-1
codimension: marked points have codimension 1 on the exceptional curve, the original common stratum has codimension 2 in the parameter surface, and downstream cycles have middle codimension n
coefficient_field: Q, with C used for the logarithmic de Rham comparison
cohomology_theory: Picard-Lefschetz vanishing homology, logarithmic de Rham residues, the resolved monodromy complex, and hypercohomology
hodge_type: the residue map is defined over Q, but no type-(0,0) mixed-Hodge comparison or Tate-twist normalization is asserted
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009, B035-B037, Green-Griffiths Section 4.3.2 (S021), and the logarithmic residue sequence on P^1
claim: With the common Picard-Lefschetz orientation, the sole B037 transgression for the resolved U_(2,5) exceptional complex is d_2(a_i)=sum_i a_i delta_i; consequently its degree-one hypercohomology is exactly the rational relation kernel among the five vanishing cycles.
falsifier: a compatible Green-Griffiths logarithmic-residue model on the five-marked exceptional P^1 in which the i-th crossing generator has residue other than delta_i up to the common orientation, or in which the connecting map is not the sum-of-residues map
---

# B038 - Exceptional residue map

B037 reduces the resolved \(U_{2,5}\) calculation to one transgression

\[
 d_2:\mathbf Q^5\longrightarrow H^2(\mathbf P^1,K)\simeq K,
 \qquad K=\ker N_E.
\]

This brick computes that transgression. It does not yet identify the
downstairs IC summand in the proper direct image.

## Logarithmic model

Green–Griffiths Section 4.3.2 constructs, under the quasi-local
normal-crossing hypotheses, a logarithmic subcomplex whose differential is

\[
 \nabla_{\log}=d+\sum_j\frac{df_j}{f_j}N_j,
\]

and a residue morphism from that complex to the monodromy complex

\[
 V\longrightarrow\bigoplus_jN_jV
 \longrightarrow\bigoplus_{j<k}N_jN_kV.
\]

After the B035 blow-up, one boundary component is the exceptional curve
\(E\), with logarithm \(N_E=\sum_iN_i\), and the five other components meet
\(E\) at \(p_i\). The tangential logarithmic residues along \(E\) are the
five \(N_i\).

## Residue sequence on the exceptional curve

For \(P=p_1+\cdots+p_5\), the logarithmic residue sequence is

\[
 0\longrightarrow\Omega_E^1
 \longrightarrow\Omega_E^1(\log P)
 \xrightarrow{\operatorname{Res}}
 \bigoplus_{i=1}^5\mathbf C_{p_i}
 \longrightarrow0.
\]

Its connecting homomorphism is

\[
 \partial:\bigoplus_{i=1}^5\mathbf C_{p_i}
 \longrightarrow H^1(E,\Omega_E^1)\simeq\mathbf C,
 \qquad (c_i)\longmapsto\sum_i c_i.
\]

Indeed, the image is the obstruction to a meromorphic differential on
\(\mathbf P^1\) having the prescribed simple residues, and the global
residue theorem says that the only relation is \(\sum_i c_i=0\). Equivalently,
this is an immediate Čech computation on the standard two-chart cover.

Tensoring with the constant rational space \(K\), and using de Rham
comparison, gives

\[
 \partial_K:\bigoplus_{i=1}^5K_{p_i}\longrightarrow
 H^2(E,K_E)\simeq K,
 \qquad (k_i)\longmapsto\sum_i k_i.
\]

The formula has integral coefficients and therefore descends from the
complex logarithmic calculation to \(\mathbf Q\).

Under algebraic de Rham/Betti comparison, the conventional logarithmic
residue and a positively oriented topological meridian differ by the
universal \(2\pi i\) normalization. Here \(d_2\) is normalized on the Betti
side, where the boundary map has integral coefficient one. The same common
factor on the de Rham side does not change the kernel. No Hodge-type claim is
deduced from suppressing that factor.

## Identification of the five local residues

At \(p_i\), B036 identifies the local degree-one cokernel of

\[
 V\xrightarrow{(N_E,N_i)}W\oplus\mathbf Q\delta_i
\]

with one rational generator. Under the Green–Griffiths residue morphism, the
generator represented by the \(N_i\)-summand has residue \(\delta_i\). A
change of orientation of a vanishing sphere changes its labeled generator
and \(\delta_i\) together; the Picard-Lefschetz operator itself is unchanged.
After one common convention, the five inclusions into \(K\) are therefore

\[
 e_i\longmapsto\delta_i.
\]

To identify the spectral-sequence map, filter the total logarithmic residue
complex by its two cohomology sheaves. Its truncation triangle is

\[
 K_E\longrightarrow\mathcal B_E^\bullet
 \longrightarrow\bigoplus_i\mathbf Q_{p_i}[-1]
 \xrightarrow{\kappa}K_E[1].
\]

Equivalently, \(\kappa\) is a class in
\(\operatorname{Ext}^2(\bigoplus_i\mathbf Q_{p_i},K_E)\). It induces
B037's \(d_2\). The
Green–Griffiths residue morphism identifies this triangle with the pushout
of the logarithmic residue sequence along the five local maps
\(e_i\mapsto\delta_i\). Naturality of connecting homomorphisms therefore
identifies \(d_2\) with \(\partial_K\) applied to those local residues. Hence

\[
 d_2(a_1,\ldots,a_5)=\sum_{i=1}^5a_i\delta_i.
\]

It follows immediately that

\[
 \mathbb H^1(E,\mathcal B_E^\bullet)
 =\ker d_2
 =\ker\!\left(
   \mathbf Q^5\xrightarrow{e_i\mapsto\delta_i}W
  \right).
\]

Thus the resolved exceptional contribution retains the full rational
vanishing-cycle relation space in the first genuinely three-block model.

## Remaining obligations

1. Prove that this resolved group is precisely the downstairs
   intermediate-extension stalk rather than a mixture with point-supported
   decomposition-theorem summands.
2. Match its rational mixed Hodge structure and Tate twist to B010's
   type-\((0,0)\) detector class; NG-034 forbids inferring this from a complex
   arrangement quiver.
3. Generalize the residue calculation from the rank-two \(U_{2,5}\) model to
   arbitrary multipart smoothing arrangements and their wonderful
   resolutions.

## Scope guard

B038 proves no algebraicity statement and no global projective realization
of the \(U_{2,5}\) slice. It closes only the resolved local topological
relation calculation. The rational Hodge Conjecture and G015 remain open.
