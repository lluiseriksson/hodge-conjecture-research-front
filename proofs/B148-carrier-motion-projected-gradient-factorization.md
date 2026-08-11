---
brick_id: B148
status: PROVED
base_field: C
variety: a smooth projective complex 2n-fold X, a smooth h-dimensional family of smooth middle-dimensional subvarieties W_b, a line bundle L, and a hypersurface Y=[s] containing W_b with transverse normal-derivative nodes Z
smoothness: X, the carrier family, and W_b are smooth; the nodes are ordinary double points; equality with the full conditional tangent space is an explicit saturated-incidence hypothesis
projectivity: X, the carriers, and the hypersurface are projective; the tangent factorization is local analytic
dimension: dim_C X=2n, dim_C W_b=n, dim_C B=h, and the projected gradient target over N nodes has dimension nN
codimension: the kernel of the projected conditional-gradient map has codimension at most h in ker E; for the B142 fiber family h=n
coefficient_field: C for tangent spaces, normal derivatives, Hessians, and rank; Q only in downstream Hodge applications
cohomology_theory: first normal jets, tangent deformation theory of subvarieties, local nodal deformation theory, and downstream rational vanishing-cycle homology
hodge_type: none asserted; downstream relation functionals must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) in downstream applications; the theorem assumes an algebraic carrier family and constructs no carrier-free cycle
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B143, B145-B147, the linearized containment equation, and rank-nullity
claim: Tangential node gradients of deformations preserving a moving carrier factor through the h-dimensional carrier-motion tangent space. If this incidence supplies the full conditional tangent ker E, then after quotienting each nodal cotangent space by the carrier conormal, the conditional-gradient map has rank at most h; equivalently it has a fixed-carrier Lagrangian kernel of codimension at most h.
falsifier: a tangent pair preserving the moving carrier that violates the differentiated containment equation, or a saturated carrier incidence whose projected conditional-gradient rank exceeds dim B
---

# B148 — Carrier motion is the low-rank quotient of the Lagrangian core

Let \(\mathcal W\to B\) be a smooth local family of smooth
middle-dimensional subvarieties of \(X\), and fix \(b\in B\). Write
\(W=W_b\), and suppose \(s|_W=0\). Its first normal derivative is

\[
 \sigma\in H^0(W,N_{W/X}^*\otimes L|_W).
\]

Assume its zero set \(Z=\{z_1,\ldots,z_N\}\) is transverse. By B147 these
are ordinary double points and

\[
 \Lambda_i=N_{z_i}^*W\otimes L|_{z_i}
\]

is maximal isotropic for the inverse nodal Hessian.

## Differentiate the containment equation

A tangent pair \((a,w)\), with \(a\) a hypersurface deformation and
\(w\in T_bB\to H^0(W,N_{W/X})\) the carrier velocity, preserves containment
exactly when

\[
 a|_W+\langle\sigma,w\rangle=0.
\]

At a zero \(z_i\) of \(\sigma\), differentiation along \(W\) gives

\[
 d_W(a|_W)_{z_i}
 =-\langle d_W\sigma_{z_i},w(z_i)\rangle.
\]

Let

\[
 \pi_i:T_{z_i}^*X\otimes L|_{z_i}
 \longrightarrow T_{z_i}^*W\otimes L|_{z_i}
\]

be the quotient by \(\Lambda_i\). The displayed identity proves that the
stacked tangential-gradient map on the moving-carrier incidence factors as

\[
 T_{(s,b)}\mathcal F\longrightarrow T_bB
 \longrightarrow\bigoplus_i T_{z_i}^*W\otimes L|_{z_i}.
\]

It therefore has rank at most \(h=\dim B\).

## Saturated consequence

If projection of the carrier incidence to \(|L|\) has tangent space exactly
\(\ker E_Z\), as in the saturated B143 situation, then for B146's
conditional gradient map \(D\),

\[
 P:=\left(\bigoplus_i\pi_i\right)D:\ker E_Z
 \longrightarrow\bigoplus_iT_{z_i}^*W\otimes L|_{z_i}
\]

has rank at most \(h\). Hence \(C=\ker P\) has codimension at most \(h\) in
\(\ker E_Z\), and

\[
 D(C)\subset\bigoplus_i\Lambda_i.
\]

For the moving fibers of \(\mathbf P^n\times\mathbf P^n\to\mathbf P^n\),
\(h=n\). Thus the anchored example does not merely contain some isotropic
directions: all tangential node gradients are controlled by the same \(n\)
carrier-motion parameters. This rank-\(n\) factorization is the precise
finite-jet shadow that G093 must reproduce without a carrier.
