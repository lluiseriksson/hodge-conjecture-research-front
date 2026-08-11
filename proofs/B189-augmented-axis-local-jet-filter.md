---
brick_id: B189
status: PROVED
base_field: C
variety: finite first-jet data of an ordered ODP configuration in the full complete linear system of a smooth projective complex 2n-fold
smoothness: the ambient variety and all tracked singularities are smooth/ordinary double points; no smoothness of the excess incidence is inferred
projectivity: the jet maps arise from a projective line bundle and the full projective linear system; the proof is finite-dimensional and coherent-local
dimension: N one-dimensional value summands, N gradient blocks of dimension 2n, and one isolated-gradient subspace at every node
codimension: a full-support augmented annihilator forces every isolated-gradient image to be inverse-Hessian totally isotropic and hence of dimension at most n
coefficient_field: C for jets, Hessians, ranks, and annihilators; Q remains required separately for the Hodge detector
cohomology_theory: coherent first-jet evaluation, ODP Hessian deformation theory, and finite-dimensional bilinear algebra
hodge_type: none asserted; a rational type-(0,0) detector with specified nonzero pairing remains a separate obligation
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream; no algebraic cycle or class detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B145-B188, G119-G121, and the ideal-sheaf description of first jets
claim: For W=im(E)+H(U), the i-th coordinate vanishes identically on W-perp exactly when the i-th value line lies in W. Hence a full-support isotropic relation forces the conditional gradients supported only at node i to form an inverse-Hessian totally isotropic space of dimension at most n. This space is exactly the image at p_i of sections vanishing to first order at every other node and in value at p_i.
falsifier: a coordinate vanishing identically while its value line is not in W, a full-support isotropic relation with a non-isotropic isolated-gradient image, dimension greater than n for such an image, or failure of the coherent isolated-jet identification
---

# B189 — Axis avoidance forces an all-node local jet defect

Retain B188's notation

\[
 \mathcal T=\bigoplus_{i=1}^N\mathcal T_i,\qquad
 W=S+H(U),\qquad L_U=W^\perp,
\]

where every value summand \(\mathcal T_i=L|_{p_i}\) is a line and
\(G_i=T_{p_i}^*X\otimes L|_{p_i}\) has dimension \(2n\). The inverse
nodal Hessian is a nondegenerate symmetric pairing

\[
 B_i:G_i\times G_i\longrightarrow\mathcal T_i.
\]

## Primal form of the support condition

The \(i\)-th coordinate vanishes identically on \(L_U\) precisely when
every \(c\in L_U\) annihilates \(\mathcal T_i\). In finite dimension,

\[
 \left(L_U|_{\mathcal T_i}=0\right)
 \quad\Longleftrightarrow\quad
 \mathcal T_i\subset L_U^\perp=W. \tag{1}
\]

Consequently B188's full-support condition is equivalently

\[
 \mathcal T_i\not\subset S+H(U)
 \quad\text{for every }i. \tag{2}
\]

This is frame-free: it refers to the intrinsic value line, not a chosen
coordinate vector.

## Gradients isolated at one node

Embed \(G_i\) as the \(i\)-th summand of \(G=\bigoplus_jG_j\), and put

\[
 U_i^{\mathrm{iso}}:=U\cap G_i. \tag{3}
\]

If \(u,v\in U_i^{\mathrm{iso}}\), then B188's Hessian-pairing map gives

\[
 h_U(u\odot v)=(0,\ldots,B_i(u,v),\ldots,0). \tag{4}
\]

If the restriction of \(B_i\) to \(U_i^{\mathrm{iso}}\) is nonzero,
(4) spans \(\mathcal T_i\). Thus \(\mathcal T_i\subset H(U)\subset W\),
contradicting (2). Therefore every full-support relation
\(c\in L_U\) forces

\[
 B_i|_{U_i^{\mathrm{iso}}\times U_i^{\mathrm{iso}}}=0
 \quad\text{for every }i. \tag{5}
\]

A totally isotropic subspace of a nondegenerate symmetric space of
dimension \(2n\) has dimension at most \(n\). Hence

\[
 \dim U_i^{\mathrm{iso}}\le n \quad(1\le i\le N). \tag{6}
\]

This is a nodewise obstruction independent of B187's global bound
\(\dim U\le nN\).

## Coherent interpolation form

Let \(Z=\{p_1,\ldots,p_N\}\). For each \(i\), define the zero-dimensional
scheme \(\Theta_i\) by the local ideals

\[
 I_{\Theta_i,p_i}=\mathfrak m_{p_i},\qquad
 I_{\Theta_i,p_j}=\mathfrak m_{p_j}^2\quad(j\ne i). \tag{7}
\]

A section of \(I_{\Theta_i}\otimes L\) has zero value at every node and
zero first derivative at every node other than \(p_i\). Its derivative at
\(p_i\) therefore defines

\[
 \delta_i:H^0(X,I_{\Theta_i}\otimes L)\longrightarrow G_i. \tag{8}
\]

If \(D:\ker E\to\bigoplus_jG_j\) is the conditional-gradient map, then

\[
 \operatorname{im}\delta_i=U\cap G_i=U_i^{\mathrm{iso}}. \tag{9}
\]

Indeed, both sides consist exactly of gradients of value-zero deformations
whose other node gradients vanish. Combining (5), (6), and (9), G121
requires every isolated-jet map (8) to have inverse-Hessian isotropic image
of rank at most \(n\).

The converse is false: nodewise isotropy alone does not control cross-node
Hessian pairings or make \(S+H(U)\) proper. B189 is a necessary filter,
not a construction of G121 or a Hodge detector.
