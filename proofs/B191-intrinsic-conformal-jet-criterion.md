---
brick_id: B191
status: PROVED
base_field: C
variety: a smooth projective complex 2n-fold, a projective line bundle, and the full complete-linear-system first-jet data at N ordered ODPs
smoothness: the ambient variety and node supports are smooth and every central singularity is an ODP; no excess-incidence smoothness is inferred
projectivity: the line bundle, complete linear system, reduced node scheme, and first infinitesimal node scheme are projective
dimension: the full conditional-gradient quotient V has dimension q; every node gradient block has dimension 2n; the full double-point scheme has length (2n+1)N
codimension: conformal synchronization is equivalent to one-node determination plus tensor rank one of the intrinsic pulled-back Hessian tensor
coefficient_field: C for coherent jets, Hessians, tensor rank, and value matroids; Q remains required separately for the Hodge detector
cohomology_theory: coherent first-jet evaluation, ODP inverse-Hessian deformation theory, symmetric tensors, and finite-dimensional linear algebra
hodge_type: none asserted; downstream detector data must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream; no algebraic cycle or class detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B145-B153, B188-B190, G119-G122
claim: The auxiliary conformal-synchronization data of B190 are equivalent in the full system to injectivity of every node gradient map on V=H0(I_Z L)/H0(I_2Z L), equality of each one-node first-jet kernel with H0(I_2Z L), and tensor rank one of the intrinsic tuple of pulled-back inverse-Hessian forms. The multiplier lies in im(E) exactly when the tensor's value factor lies there. If H1(X,L)=0, the full first-jet defect is (2n+1)N-R-q and one-node determination forces q<=2n.
falsifier: disagreement between the conditional-gradient image and V, an injective node map with a larger one-node kernel, conformal synchronization with tensor rank greater than one, a rank-one tensor whose value factor test fails, or a different coherent defect formula under H1(X,L)=0
---

# B191 — Intrinsic coherent criterion for conformal synchronization

Let \(Z=\{p_1,\ldots,p_N\}\) be the reduced node scheme and let \(2Z\)
denote its first infinitesimal neighborhood, with local ideal
\(\mathfrak m_{p_i}^2\). Put

\[
 V:=H^0(X,I_Z\otimes L)/H^0(X,I_{2Z}\otimes L),
 \qquad q=\dim V. \tag{1}
\]

The derivative maps at the nodes descend to

\[
 d_i:V\longrightarrow G_i=T_{p_i}^*X\otimes L|_{p_i}. \tag{2}
\]

## The full conditional-gradient quotient

A value-zero section has zero gradient at every node exactly when it lies
in \(H^0(X,I_{2Z}\otimes L)\). Therefore the direct-sum map

\[
 d=(d_1,\ldots,d_N):V\longrightarrow\bigoplus_iG_i \tag{3}
\]

is injective, and its image is precisely B188's full conditional-gradient
image \(U\). Thus \(V\simeq U\) intrinsically; no selected parameter
subfamily enters (1). The central nodal section itself belongs to
\(H^0(X,I_{2Z}\otimes L)\), so passing from the affine section space to the
projective tangent space does not change this quotient.

For each \(i\), let \(\Psi_i\) be double at \(p_i\) and reduced at every
other node:

\[
 I_{\Psi_i,p_i}=\mathfrak m_{p_i}^2,
 \qquad I_{\Psi_i,p_j}=\mathfrak m_{p_j}\quad(j\ne i). \tag{4}
\]

The kernel of \(d_i\) is

\[
 \ker d_i=
 H^0(X,I_{\Psi_i}\otimes L)/H^0(X,I_{2Z}\otimes L). \tag{5}
\]

Consequently

\[
 d_i\text{ injective}
 \quad\Longleftrightarrow\quad
 H^0(X,I_{\Psi_i}\otimes L)
 =H^0(X,I_{2Z}\otimes L). \tag{6}
\]

All maps \(d_i\) are injective exactly when the full image \(U\) is the
graph of one common space with injective projections to every node, as in
B190. In that case a first jet at any one node determines all node gradients
modulo sections vanishing to first order on all of \(Z\). In particular,

\[
 q\le\dim G_i=2n. \tag{7}
\]

## Intrinsic Hessian tensor

Let

\[
 B_i:G_i\times G_i\longrightarrow\mathcal T_i=L|_{p_i}
\]

be the inverse-Hessian pairing. Pulling back along \(d_i\) gives the
intrinsic tensor

\[
 \Gamma_Z:=\bigl(d_i^*B_i\bigr)_{i=1}^N
 \in
 \mathcal T\otimes\operatorname{Sym}^2V^*,
 \qquad \mathcal T=\bigoplus_i\mathcal T_i. \tag{8}
\]

After local frames are chosen, flatten (8) as a linear map

\[
 \mathcal T^*\longrightarrow\operatorname{Sym}^2V^*. \tag{9}
\]

It has rank one and is nonzero exactly when

\[
 \Gamma_Z=\lambda\otimes B_V \tag{10}
\]

for a nonzero value vector \(\lambda\in\mathcal T\) and a nonzero symmetric
form \(B_V\). Equation (10) says precisely

\[
 B_i(d_iv,d_iw)=\lambda_iB_V(v,w), \tag{11}
\]

which is B190's conformal-Hessian condition with \(Q=V\) and
\(\phi_i=d_i\). Tensor rank is frame-independent, and changing the factor
scales \(\lambda\) and \(B_V\) inversely.

If \(S=\operatorname{im}E\subset\mathcal T\), the multiplier condition is

\[
 \lambda\in S
 \quad\Longleftrightarrow\quad
 \Gamma_Z\in S\otimes\operatorname{Sym}^2V^* \tag{12}
\]

under the nonzero rank-one hypothesis. Equivalently, the image line of the
transpose flattening of (9) lies in \(S\). Equations (6), the vanishing of
all \(2\times2\) minors of (9), nonvanishing of (9), and (12) are finite,
intrinsic, and falsifiable.

## Coherent defect forced by one-node determination

Assume \(H^1(X,L)=0\), and write \(R=\operatorname{rank}E\). Evaluation on
\(2Z\) has rank

\[
 R+q, \tag{13}
\]

because values contribute \(R\) and the conditional gradients contribute
\(q\). Since \(\operatorname{length}(2Z)=(2n+1)N\), the ideal-sheaf exact
sequence gives

\[
 h^1(X,I_{2Z}\otimes L)
 =(2n+1)N-R-q. \tag{14}
\]

Under one-node determination, (7) sharpens this to

\[
 h^1(X,I_{2Z}\otimes L)
 \ge (2n+1)N-R-2n. \tag{15}
\]

This is an equality and a necessary lower bound, not an existence argument.
B191 constructs no node scheme, detector, higher Kuranishi vanishing, or
cycle.
