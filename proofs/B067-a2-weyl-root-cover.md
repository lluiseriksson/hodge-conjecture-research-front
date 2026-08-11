---
brick_id: B067
status: PROVED
base_field: C
variety: the S3 root cover of the miniversal A2 coefficient plane and the pulled-back suspended A2 family
smoothness: the root-cover base is smooth; its reduced discriminant is a three-line arrangement, while the pulled-back total family is singular along three collision sections
projectivity: no; this is a local affine model
dimension: the base has dimension two and the suspended fibers have arbitrary dimension r
codimension: each root hyperplane is a divisor; each total-space singular section lies over one root hyperplane
coefficient_field: Q for the finite-group descent bookkeeping and C for the polynomial calculation
cohomology_theory: none in the proof; later applications use vanishing cycles and rational mixed Hodge modules
hodge_type: none asserted
cycle_class_map: none
cycle_equivalence: none
scope: relative and fiberwise
dependencies: B064-B066 and verification/verify_B067_a2_weyl_cover.py
claim: The ordered-root map is a generically degree-six S3 quotient, pulls the cusp back to the square of the A2 reflection arrangement, and leaves the total family singular along the three pair-collision sections.
falsifier: failure of the invariant formulas, a non-arrangement discriminant pullback, or smoothness of the raw total family along a pair-collision section
---

# B067 — The \(S_3\) Weyl/root cover of the \(A_2\) deformation

**Status:** PROVED  
**Gate:** G036 / G037

## Root cover

Write the ordered roots as
\[
\lambda_1=u,\qquad \lambda_2=v,\qquad
\lambda_3=-u-v.
\]
Then
\[
(x-u)(x-v)(x+u+v)=x^3+s x+t
\]
with
\[
s=-(u^2+uv+v^2),\qquad t=uv(u+v).
\]
Permuting the three roots gives the Weyl group \(W(A_2)=S_3\). Away from the discriminant, a cubic has six orderings of its three distinct roots, so the coefficient map is generically degree six and is the elementary \(S_3\)-quotient map.

## Discriminant

The cusp equation pulls back as
\[
4s^3+27t^2
=-\bigl((u-v)(2u+v)(u+2v)\bigr)^2.
\]
Thus the reduced inverse image is the reflection arrangement
\[
L_{12}:u-v=0,qquad
L_{13}:2u+v=0,qquad
L_{23}:u+2v=0.
\]
One blowup of the origin separates the three strict transforms on an exceptional \(\mathbf P^1\). The pullback divisor has multiplicity two on each strict line and multiplicity six on the exceptional divisor.

## Raw total family

After the root cover the suspended family is
\[
P=(x-u)(x-v)(x+u+v)+\sum_{i=1}^{r}z_i^2=0.
\]
Its total-space singular locus is exactly the union of the three collision sections
\[
\begin{aligned}
S_{12}&:\ x=u=v,\ z=0,\\
S_{13}&:\ x=u,\ 2u+v=0,\ z=0,\\
S_{23}&:\ x=v,\ u+2v=0,\ z=0.
\end{aligned}
\]
Indeed, if exactly one of the three linear factors vanishes, differentiation with respect to the corresponding root variable gives the product of the two nonzero factors. All first derivatives vanish precisely when at least two factors vanish, which gives the three sections above.

## Consequence

The cover converts the cuspidal discriminant into a labeled reflection arrangement and exposes the correct finite group, but it is not itself a simultaneous resolution. A total-space resolution and its \(S_3\)-descent remain necessary.
