---
brick_id: B043
status: PROVED
base_field: C
variety: a d-dimensional nodal smoothing slice whose reduced central discriminant is a simple uniform arrangement U_(d,r), and its blow-up at the origin
smoothness: the parameter space and blow-up are smooth; the projectivized uniform arrangement is simple normal crossing; the central projective fiber has r ordinary double points and nearby fibers are smooth
projectivity: the blow-up and exceptional P^(d-1) are projective; the parameter calculation is local analytic, while the motivating hyperplane-section family is projective
dimension: parameter dimension d at least 2, exceptional divisor dimension d-1, ambient projective variety dimension 2n, and nearby fiber dimension 2n-1
codimension: the arrangement center has codimension d, k-fold exceptional incidence strata have codimension k in P^(d-1), and downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: Picard-Lefschetz vanishing cycles, rational intersection complexes, logarithmic residues, perverse direct images, and polarizable rational mixed Hodge modules
hodge_type: after the Q(n) normalization, the downstairs degree-one IC stalk is pure of type (0,0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B035-B042, Green-Griffiths S021, and Saito S022/S037
claim: For every d at least 2 and every r at least d, the downstairs degree-one IC stalk of a simple uniform U_(d,r) Picard-Lefschetz nodal arrangement is canonically the full rational vanishing-cycle relation kernel and is pure of type (0,0) after Q(n).
falsifier: a uniform incidence stratum producing cohomology beyond the direct sum of its incident branch generators, a residue transgression different from e_i -> delta_i, a point-supported blow-up summand in ordinary degree one, or a non-(0,0) kernel component after Q(n)
---

# B043 - Uniform arbitrary-rank multipart channel

B041-B042 are the cases \(d=2,3\) of a uniform statement.

## One blow-up is an SNC resolution

Let \(H_1,\ldots,H_r\subset\mathbf C^d\) realize \(U_{d,r}\): every subset
of at most \(d\) defining forms is independent. Blow up the common origin.
The exceptional divisor is \(E=\mathbf P^{d-1}\), and
\(L_i=E\cap\widetilde H_i\) is a projective hyperplane.

For \(|S|=k<d\), the intersection \(\bigcap_{i\in S}L_i\) has codimension
\(k\); no \(d\) of the \(L_i\) meet. Hence the projectivized arrangement and
the total transform are SNC. No additional wonderful-model center is needed
for a uniform arrangement.

## Uniform exceptional cohomology sheaves

As before,

\[
 N_E=\sum_iN_i,
 \qquad N_iN_j=N_EN_i=0,
 \qquad
 K=\ker N_E=\bigcap_i\ker N_i.
\]

At the stratum indexed by \(S\), where \(|S|\le d-1\), the local complex has
only degrees zero and one. Its degree-one group is

\[
 F_S=\operatorname{coker}\!\left[
 V\longrightarrow
 W\oplus\bigoplus_{i\in S}\mathbf Q\delta_i
 \right],
 \qquad W=\operatorname{Im}N_E.
\]

The lift construction from B042 gives a canonical, generization-compatible
isomorphism

\[
 F_S\simeq\bigoplus_{i\in S}\mathbf Q\delta_i.
\]

Therefore, for the unshifted exceptional restriction \(A|_E\),

\[
 \mathcal H^0(A|_E)=K_E,
 \qquad
 \mathcal H^1(A|_E)=\bigoplus_{i=1}^r\mathbf Q_{L_i},
 \qquad
 \mathcal H^{\ge2}(A|_E)=0.
\]

All higher incidence strata merely record simultaneous stalks of these
hyperplane sheaves; they add no new quotient.

## Residue and the relation kernel

For the SNC divisor \(D=\sum_iL_i\) on \(E\),

\[
 0\to\Omega_E^1\to\Omega_E^1(\log D)
 \xrightarrow{\operatorname{Res}}\bigoplus_i\mathcal O_{L_i}\to0.
\]

Every \(L_i\) has hyperplane class \(h\), so the connecting map on global
sections is \((c_i)\mapsto(\sum_i c_i)h\). Pushing the \(i\)-th residue
generator through the Picard-Lefschetz coefficient map gives \(\delta_i\).
Thus the sole differential affecting total degree one is

\[
 d_2:\mathbf Q^r\longrightarrow H^2(E,K_E),
 \qquad
 d_2(a_i)=\sum_i a_i\delta_i.
\]

Consequently

\[
 \mathbb H^1(E,A|_E)
 =\ker\!\left(\mathbf Q^r\xrightarrow{e_i\mapsto\delta_i}W\right).
\]

## Dimension-uniform direct-image bound

Put \(P=A[d]\). The constant row on \(E=\mathbf P^{d-1}\) has ordinary
cohomology through degree \(2d-2\). Each hyperplane row is shifted by one
and has cohomology through degree \(1+2(d-2)=2d-3\). Hence

\[
 H^j\!\left(R\Gamma(E,A|_E)[d]\right)=0
 \quad\text{for }j>d-2.
\]

Since the blow-up is an isomorphism off the origin,

\[
 R\pi_*P\in{}^pD^{\le d-2}.
\]

The Verdier-dual calculation gives the lower bound
\(R\pi_*P\in{}^pD^{\ge-(d-2)}\). Saito decomposition therefore allows only
point-supported perverse summands in degrees
\(j=-(d-2),\ldots,d-2\), in addition to the full-support
\(IC_B(L_{\mathbf Q})[d]\) summand at \(j=0\).

After undoing the dimension-\(d\) shift, a point summand of perverse degree
\(j\) occurs in ordinary degree \(d+j\). The possible point degrees are

\[
 2,3,\ldots,2d-2.
\]

In particular, no exceptional point summand contributes to ordinary degree
one. Proper base change canonically identifies the resolved group with

\[
 H^1\!\left(IC_B(L_{\mathbf Q})_0\right).
\]

## Hodge type

At every SNC stratum, Saito Proposition 1.7 applies because all pairwise
products of logarithms vanish and all their images are Tate after the
\(\mathbf Q(n)\) normalization. The degree-one hyperplane sheaves are
\(\mathbf Q(0)_{L_i}\), and the residue transgression is a morphism of mixed
Hodge structures. Hence

\[
 H^1\!\left(IC_B(L_{\mathbf Q})_0\right)
 \simeq\mathbf Q(0)^{\,r-s},
 \qquad s=\dim_{\mathbf Q}W.
\]

## Boundary of the theorem

Uniformity is essential to this one-blow-up proof. A nonuniform arrangement
can have too many hyperplanes through a positive-dimensional flat. Its
projectivization is not SNC, and a wonderful resolution introduces
exceptional divisors over several nested flats. B043 supplies no theorem
that their incidence complex preserves the relation kernel.

## Scope guard

B043 proves G015's desired local channel only for simple uniform smoothing
matroids. It neither reduces arbitrary representable matroids to uniform
ones nor constructs a class-paired nodal member on an arbitrary projective
variety. The standard rational Hodge Conjecture remains open, and actual
general-case progress remains zero.
