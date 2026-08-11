---
brick_id: B188
status: PROVED
base_field: C
variety: the finite second-order value and conditional-gradient data of an ordered ODP configuration in a full projective linear system
smoothness: the ambient variety and central singularities are smooth/ODP; no smoothness of the excess incidence is inferred
projectivity: inherited from the intended full projective incidence; the theorem itself is finite-dimensional linear algebra
dimension: value target dimension N, value rank R, conditional-gradient image U of arbitrary dimension, and augmented Hessian-value rank at most N
codimension: isotropic value relations form the annihilator of the sum of the value image and the nodewise Hessian-pairing span
coefficient_field: C for value relations and Hessian forms; Q remains required separately for Hodge detectors
cohomology_theory: second-order ODP deformation theory, symmetric bilinear algebra, value matroids, and finite rank
hodge_type: none asserted; a rational type (0,0) detector with specified nonzero pairing remains separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is only downstream; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B146-B153, B186-B187, G119-G120
claim: For a conditional-gradient image U, let H(U) be the span in the N-dimensional value target of all tuples of nodewise inverse-Hessian pairings. The relations c in ker(E^*) for which U is q_c-isotropic are exactly (im(E)+H(U))^perp. Such a relation exists exactly when the augmented Hessian-value map has rank less than N, and a full-support one exists exactly when this annihilator is not contained in any coordinate hyperplane.
falsifier: an isotropic relation outside the augmented annihilator, an annihilator element whose relation form is nonzero on U, rank deficiency with zero annihilator, or a full-support element when one coordinate vanishes identically on the annihilator
---

# B188 — Isotropic relations are an augmented evaluation defect

Let

\[
 \mathcal T=\bigoplus_{i=1}^N L|_{p_i},\qquad
 S=\operatorname{im}E\subset\mathcal T,
\]

and let \(U\subset G=\bigoplus_iG_i\) be the conditional-gradient image.
After choosing local frames, write \(B_i\) for the nondegenerate
inverse-Hessian symmetric form on \(G_i\).

Define the Hessian-pairing map

\[
 h_U:\operatorname{Sym}^2U\longrightarrow\mathcal T,
 \qquad
 h_U(u\odot v)
 =\bigl(B_i(u_i,v_i)\bigr)_{i=1}^N, \tag{1}
\]

and put

\[
 H(U)=\operatorname{im}h_U.
\]

The augmented Hessian-value map is

\[
 A_U:S\oplus\operatorname{Sym}^2U\longrightarrow\mathcal T,
 \qquad
 A_U(s,\xi)=s+h_U(\xi). \tag{2}
\]

Its image is \(S+H(U)\).

## Exact annihilator identity

For \(c\in\mathcal T^*\), the following are equivalent:

1. \(c\in\ker E^*\) and \(q_c|_{U\times U}=0\);
2. \(c(S)=0\) and \(c(H(U))=0\);
3. \(c\in\ker A_U^*=(S+H(U))^\perp\).

Indeed,

\[
 c\bigl(h_U(u\odot v)\bigr)
 =\sum_i c_iB_i(u_i,v_i)
 =q_c(u,v). \tag{3}
\]

Thus the complete space of value relations making \(U\) isotropic is

\[
 L_U:=\ker A_U^*. \tag{4}
\]

In particular,

\[
 L_U\ne0
 \quad\Longleftrightarrow\quad
 \operatorname{rank}A_U<N. \tag{5}
\]

This is the exact rank form of G120's existential quadratic condition.

## Full-support criterion

Choose frames so \(L_U\subset(\mathbf C^N)^*\). A full-support relation
exists in \(L_U\) exactly when no coordinate \(c_i\) vanishes identically
on \(L_U\). If this condition holds, each

\[
 \{c\in L_U:c_i=0\}
\]

is a proper hyperplane, and their finite union cannot cover \(L_U\) over
\(\mathbf C\). Conversely, if one coordinate vanishes identically, no
element can have full support.

Hence B187's nondegenerate global Lagrangian witness exists precisely when
the augmented defect space \(L_U\) is nonzero and has no identically zero
coordinate.

## Coefficient and scope guards

The map \(A_U\) and its annihilator are complex. A full-support
\(c\in L_U\) is not automatically a rational vanishing-cycle relation or
the specified Saito detector.

B188 is an exact finite criterion only. It does not construct a deficient
augmented map, force isotropy for every value relation, prove
\(\kappa_2=0\), or supply any Hodge pairing. B189 gives its nodewise
axis-avoidance consequence, while B190 gives a stronger conformal-
synchronization condition sufficient for every quadratic relation.
