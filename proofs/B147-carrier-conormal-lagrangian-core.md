---
brick_id: B147
status: PROVED
base_field: C
variety: a smooth projective complex 2n-fold X, a smooth middle-dimensional subvariety W, a line bundle L, and a hypersurface Y=[s] containing W with isolated ordinary double points Z on W
smoothness: X and W are smooth; every point of Z is a transverse zero of the normal derivative of s and hence an ordinary double point of Y
projectivity: X, W, and Y are projective; the Hessian calculation is local analytic
dimension: dim_C X=2n, dim_C W=n, and each nodal cotangent space has dimension 2n
codimension: W has codimension n; its conormal space at every node is a maximal n-dimensional isotropic subspace for the inverse-Hessian quadratic form
coefficient_field: C for local equations, Hessians, deformation tangents, and isotropic subspaces; Q only in downstream Hodge applications
cohomology_theory: normal-jet deformation theory and local analytic ordinary-double-point deformation theory; downstream applications use rational Betti cohomology and nodal vanishing cycles
hodge_type: none asserted by the local theorem; downstream Saito relation classes are rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) in downstream applications; this brick starts from the algebraic carrier W and therefore is not a carrier-free cycle construction
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: S019 Theorem 4.2 local normal-derivative calculation, B142-B143, B146, and block-matrix inversion
claim: At every transverse normal-derivative node of a hypersurface containing W, the inverse nodal Hessian vanishes on the conormal space N^*_(W/X), and that conormal space is maximal isotropic. Consequently the gradients of all first-order hypersurface deformations that continue to contain the fixed W lie in a canonical nodewise Lagrangian core of B146's Hessian obstruction.
falsifier: a transverse normal-derivative node whose Hessian has a nonzero tangent-tangent block in coordinates adapted to W, a degenerate normal-tangent block, or a fixed-W deformation with nonzero tangent differential on W
---

# B147 — An algebraic carrier creates a conormal Lagrangian core

Let (z\in W) be a zero of the first normal derivative of (s). Choose
local coordinates

\[
 u=(u_1,\ldots,u_n),\qquad v=(v_1,\ldots,v_n),
 \qquad W=\{u=0\},
\]

and a local frame of (L). Since (s|_W=0), its quadratic expansion at
(z=(0,0)) has the form

\[
 s(u,v)=u^{\mathsf T}Jv+\tfrac12u^{\mathsf T}Au+O(3),
\]

where (A=A^{\mathsf T}). The zero of the normal derivative is transverse
exactly when (J) is invertible. In the ordered splitting
(T_zX=N_zW\oplus T_zW), the nodal Hessian and its inverse are

\[
 H_z=
 \begin{pmatrix}A&J\\J^{\mathsf T}&0\end{pmatrix},
 \qquad
 H_z^{-1}=
 \begin{pmatrix}
 0&J^{-\mathsf T}\\
 J^{-1}&-J^{-1}AJ^{-\mathsf T}
 \end{pmatrix}.
\]

The zero lower-right block of (H_z) is forced by the identity
(s|_W=0); the invertibility of (J) proves that (z) is an ordinary
double point. This is the local normal-derivative mechanism used in S019.

## Fixed-carrier deformation directions

Let (a) be a first-order deformation of (s) that still contains the
fixed (W). Then (a|_W=0), so

\[
 da_z=(\alpha,0)\in
 N_z^*W\oplus T_z^*W.
\]

The inverse-Hessian square appearing in B146 is therefore

\[
 da_z\bigl(H_z^{-1}da_z\bigr)
 = (\alpha,0)
 \begin{pmatrix}
 0&J^{-\mathsf T}\\
 J^{-1}&-J^{-1}AJ^{-\mathsf T}
 \end{pmatrix}
 \binom{\alpha}{0}=0.
\]

Thus

\[
 \Lambda_z:=N_z^*W\otimes L|_z
 \subset T_z^*X\otimes L|_z
\]

is isotropic for the nondegenerate inverse-Hessian form. It has dimension
(n), half the ambient dimension (2n), so it is maximal isotropic. For a
finite node set (Z), fixed-carrier gradients land in the split
Lagrangian space (igoplus_{z\in Z}\Lambda_z).

## What this explains—and what it does not

This gives a concrete source for the exceptional conditional-gradient
geometry in B142-B143. The moving-fiber incidence contains the fixed-fiber
directions above; carrier motion adds only the finite-dimensional normal
velocities of the fiber family. Its full Hessian-isotropy follows from the
actual smooth incidence as in B146.

The construction is not carrier-free. The subspaces (Lambda_z) are
conormals of a pre-existing algebraic middle-dimensional (W), and the
nonzero class-specific pairing in B142 is precisely supplied by ([W]).
Hence B147 is a mechanism audit for G092, not progress toward the general
Hodge Conjecture.
