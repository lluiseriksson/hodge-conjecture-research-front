---
brick_id: B050
status: PROVED
base_field: C
variety: the central wonderful fiber of an arbitrary representable nodal discriminant arrangement, stratified by its simple-normal-crossing branch and building-flat divisors
smoothness: the smoothing base and wonderful resolution are smooth and the resolved boundary is simple normal crossing
projectivity: the wonderful morphism is projective and the central wonderful fiber is smooth projective
dimension: arbitrary parameter rank d at least 2, with central wonderful fiber dimension d-1
codimension: arbitrary building flats of arrangement codimension at least 2; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: rational Picard-Lefschetz local systems, Saito's normal-crossing intermediate-extension complex, and ordinary cohomology sheaves on the wonderful fiber
hodge_type: after Q(n), every degree-one coefficient space is a direct sum of Q(0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B040-B049, G019-G022, Li S038, and Saito Section 1.4 Proposition 1.7 (S022)
claim: On every central wonderful fiber, the unshifted intermediate-extension restriction has constant degree-zero sheaf K, degree-one sheaf equal to the direct sum of the branch lines and intrinsic building-flat coefficient spaces W_F, and no cohomology sheaves in degree at least two; the identification is rational, generization compatible, order independent, and pure type (0,0) after Q(n).
falsifier: failure of the kernel identity for the origin residue, a wonderful boundary residue not equal to its intrinsic branch-subset sum, a nonzero product of two incident residues, a stalk quotient not split by the anchor residue, or an incompatible generization map
---

# B050 - Universal wonderful coefficient sheaf

This brick proves G022. It is a local coefficient theorem; it does not prove
the strict-support or global residue conclusions still required by G019.

## Picard-Lefschetz kernel identity

Let (V) be the rational nearby-fiber cohomology and let
(delta_1,ldots,delta_r) be the vanishing cycles of distinct nodes. With
one common Picard-Lefschetz sign,

\[
 N_i(v)=\epsilon\langle v,\delta_i\rangle\delta_i,
 \qquad N_E=\sum_iN_i,
 \qquad W=\operatorname{span}_{\mathbf Q}\{\delta_i\}.
\]

Distinct-node vanishing spheres are disjoint, so
(langledelta_i,delta_jangle=0) and every (N_iN_j), including
(N_i^2), is zero. Moreover

\[
 K:=\ker N_E=\bigcap_i\ker N_i.
\]

Indeed, if (a_i=langle v,delta_iangle) and (N_Ev=0), pairing with
(v) gives, up to the fixed nonzero sign, (sum_i a_i^2=0). The
coefficients are rational, hence real, so every (a_i=0). The reverse
inclusion is immediate. This argument allows arbitrary rational linear
relations among the (delta_i); it does not assume node independence.

For a flat (F), put

\[
 N_F=\sum_{F\subset H_i}N_i,
 \qquad W_F=\operatorname{Im}N_F
      =\operatorname{span}\{\delta_i:F\subset H_i\}.
\]

The same sum-of-squares argument proves the displayed image equality.
Also (K\subseteq\ker N_F), so there is a unique linear map
(overline N_F:W\to W_F) with
(N_F=overline N_F N_E). The analogous factorization holds for each
(N_i).

## Intrinsic residues on the wonderful model

The residue around the origin divisor is (N_E). At the generic point of
the strict branch (M_i), it is (N_i). At the generic point of the
boundary divisor (D_F), its center lies with multiplicity one precisely in
the branches containing (F), so its residue is (N_F). This is invariant
under permissible order: the boundary valuation is intrinsically labelled
by (F), exactly as its divisor is in B049 and Li Theorems 1.2-1.3.

Thus every residue incident to a point of the central wonderful fiber is one
of (N_E,N_i,N_F). All pairwise products vanish because their images lie in
(W), which every (N_i) annihilates.

## Anchored SNC quotient lemma

At a stratum incident to the origin divisor and to additional components
with residues (M_1,ldots,M_s), Saito's normal-crossing
intermediate-extension complex is

\[
 V\xrightarrow{(N_E,M_1,\ldots,M_s)}
 W\oplus\bigoplus_{a=1}^s\operatorname{Im}M_a\longrightarrow0,
\]

because every product of two residues is zero. Its degree zero is (K).
For each (a), the inclusion (K\subseteq\ker M_a) gives the unique
factor (overline M_a:W\to\operatorname{Im}M_a). The map

\[
 [(w,u_1,\ldots,u_s)]\longmapsto
 (u_a-\overline M_a(w))_{a=1}^s
\]

is a canonical isomorphism from the degree-one cokernel to
(igoplus_a\operatorname{Im}M_a). Its kernel is exactly the graph of the
map from (V/K\simeq W), and it is visibly surjective. When one generizes
to a larger stratum, this isomorphism merely forgets the coefficient spaces
of the components no longer incident. Hence the identifications glue.

Writing (i_i:M_i\hookrightarrow E_{\mathcal B}) and
(i_F:D_F\hookrightarrow E_{\mathcal B}), the ordinary cohomology sheaves
of the unshifted restriction (A|_{E_{\mathcal B}}) are therefore

\[
 \mathcal H^0=K_{E_{\mathcal B}},\qquad
 \mathcal H^1=
 \bigoplus_i(i_i)_*\mathbf Q\delta_i
 \oplus\bigoplus_F(i_F)_*W_F,\qquad
 \mathcal H^{\ge2}=0.
\]

## Rationality, Hodge type, and order

Every map used above is defined over \(\mathbf Q\). Saito's Proposition 1.7
applies because the residue products vanish. Each nodal image is
\(\mathbf Q(-n)\); after the stipulated \(\mathbf Q(n)\) normalization, every
branch line and every \(W_F\) is a sum of \(\mathbf Q(0)\). Consequently
\(\mathcal H^1\) is pure type \((0,0)\) coefficientwise.

Li's canonical model and the intrinsic valuations (D_F) identify the same
residues and supports in every permissible order. NG035's raw divisor basis
change causes no ambiguity here.

## Scope guard

B050 computes only the local cohomology sheaves. Their global
hypercohomology still has residue differentials, and the proper direct image
may contain lower strict-support summands. G019 additionally requires a
uniform proof that none of those summands contributes in ordinary degree
one. No algebraic cycle is constructed, so actual progress toward the
general rational Hodge Conjecture remains zero.
