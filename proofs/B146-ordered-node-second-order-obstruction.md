---
brick_id: B146
status: PROVED
base_field: C
variety: a smooth projective complex 2n-fold X, a line bundle L, a hypersurface Y=[s] in |L| with N ordered isolated ordinary double points, and the local ordered-node incidence
smoothness: X is smooth and the selected singularities are ordinary double points; smoothness of the excess incidence is an explicit hypothesis only for the obstruction consequence
projectivity: X and |L| are projective; the calculation is local analytic over the ordered configuration space
dimension: dim_C X=2n; the value-evaluation rank is 1<=R<N and the conditional gradient target has dimension 2nN
codimension: a smooth excess incidence would have codimension 2nN+R in |L| x Conf_N(X); uniformity forces conditional-gradient corank at least n(R+1)
coefficient_field: C for analytic deformations, Hessians, relations, and quadratic forms; Q only in downstream Hodge applications
cohomology_theory: local first- and second-jet deformation theory, analytic critical-point elimination, evaluation matroids, and downstream adjoint and vanishing-cycle cohomology
hodge_type: none asserted by the obstruction theorem; downstream relation classes are normalized to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) in downstream applications; no algebraic cycle is constructed or assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B145, the analytic implicit-function theorem, polarization of quadratic forms, and the Witt-index bound over C
claim: Smooth rank-deficient ordered-node incidence forces every value relation to annihilate the Hessian quadratic form on the conditional gradient image. For a uniform U_(R,N) value matroid this image has codimension at least n(R+1); in particular conditional gradient surjectivity is incompatible with smooth excess.
falsifier: a smooth rank-deficient ordered-node incidence with a tangent direction whose Hessian obstruction has nonzero value under a value relation, or a uniform example whose conditional-gradient corank is smaller than n(R+1)
---

# B146 — Second-order obstruction for ordered-node excess

Keep the notation of B145 and write \(d=2n\). Put

\[
 W=T_{[s]}|L|=H^0(X,L)/\langle s\rangle,
 \qquad
 E:W\longrightarrow\bigoplus_i L|_{p_i}.
\]

Choose local coordinates and a local frame of \(L\) at every node. For the
nodal Hessian write

\[
 H_i:T_{p_i}X\xrightarrow{\sim}
 T_{p_i}^*X\otimes L|_{p_i}.
\]

## The local smoothing map

For \(t\) close to \(s\), the critical-point equation in the chosen frame
has a unique solution \(x_i(t)\) close to \(p_i\). This is the analytic
implicit-function theorem applied to the invertible Hessian. Define

\[
 \tau_i(t)=t(x_i(t)),\qquad
 \tau=(\tau_1,\ldots,\tau_N).
\]

The projected ordered-node incidence germ is exactly
\(\tau^{-1}(0)\). Choose a linear affine slice through \([s]\). For
\(a,b\in W\), differentiation at \(s\) gives

\[
 d\tau_i(a)=a(p_i)
\]

and

\[
 d^2\tau_i(a,b)=
 -\,da_{p_i}\bigl(H_i^{-1}(db_{p_i})\bigr).
\]

The displayed bilinear form is symmetric because \(H_i\) is symmetric.
It is independent of the representatives of \(a,b\) modulo \(s\), since
\(s(p_i)=ds_{p_i}=0\). A change of local frame multiplies the smoothing
function by a unit; the relation obstruction below on \(\ker E\) is
unchanged up to the same nonzero block scalars.

## The obstruction equation

Let

\[
 K=\ker(E^*)\subset
 \left(\bigoplus_iL|_{p_i}\right)^*
\]

be the space of value relations. For \(c=(c_i)\in K\), define on

\[
 G=\bigoplus_i(T_{p_i}^*X\otimes L|_{p_i})
\]

the quadratic form

\[
 q_c(\lambda)=
 \sum_i c_i\!\left(
 \lambda_i(H_i^{-1}\lambda_i)
 \right).
\]

Also define the conditional gradient map

\[
 D:\ker E\longrightarrow G,
 \qquad a\longmapsto(da_{p_i})_i.
\]

Assume that the ordered-node incidence is smooth at \(([s],\Delta)\) with
the tangent dimension computed in B145. Every \(a\in\ker E\) is then the
velocity of an analytic arc

\[
 t(u)=s+ua+\tfrac12u^2b+O(u^3)
 \quad\text{inside }\tau^{-1}(0).
\]

Twice differentiating \(\tau(t(u))=0\) yields

\[
 E(b)_i=
 da_{p_i}\bigl(H_i^{-1}(da_{p_i})\bigr).
\]

Applying any \(c\in K\) kills the left side. Hence

\[
 q_c(Da)=0
 \qquad(c\in K,\ a\in\ker E).
\]

By polarization, \(U:=\operatorname{im}D\) is a totally isotropic linear
subspace for every quadratic form \(q_c\).

## Uniform-matroid corank floor

Let the value matroid be \(U_{R,N}\), with \(R<N\). Every nonzero relation
\(c\in K\) then has support of size at least \(R+1\). If its support has
size \(s_c\), the direct-sum form \(q_c\) has rank

\[
 \operatorname{rank}q_c=2n s_c.
\]

On a complex vector space of dimension \(2nN\), a quadratic form of rank
\(2ns_c\) has totally isotropic subspaces of dimension at most

\[
 2nN-ns_c.
\]

Consequently

\[
 \operatorname{codim}_{G}(\operatorname{im}D)
 \ge ns_c\ge n(R+1).
\]

In particular \(D\) cannot be surjective. Thus value-rank drop alone is
not a smooth-excess mechanism: smooth excess requires a second, large and
Hessian-compatible failure of conditional gradient interpolation.

This is only a necessary second-order condition. It neither integrates
the isotropic tangent data through all higher orders nor produces the
class-specific rational relation required by G091.
