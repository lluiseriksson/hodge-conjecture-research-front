---
brick_id: NG152
status: NO-GO
base_field: C
variety: two abstract ODP Hessian blocks with uniform rank-one value image and a half-dimensional conditional-gradient subspace supported on one node
smoothness: both Hessian blocks are nondegenerate; this is finite second-order linear algebra
projectivity: not used; projective finite-jet interpolation may realize the data, but no Hodge detector is asserted
dimension: N=2, R=1, gradient blocks of dimension 2n, and conditional-gradient dimension 2n=nN
codimension: B187's dimension ceiling is satisfied while the augmented Hessian-value map has full rank two
coefficient_field: C; Q remains required only for downstream Hodge detectors
cohomology_theory: symmetric bilinear forms, augmented Hessian-value evaluation, and conditional-gradient ranks
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B146, B187-B188, G120-G121
claim: The numerical inequality dim(U)<=nN alone guarantees a nonzero value relation c for which U is q_c-isotropic.
falsifier: with S=span(1,1) and U=G_1 direct_sum 0, the Hessian span is span(1,0), so S+H(U)=C^2 and no nonzero relation annihilates both
---

# NG152 — The half-dimensional rank bound does not create isotropy

Let \(G_1=G_2=H\), where \(H\) has dimension \(2n\) and carries a
nondegenerate symmetric form \(B\). Take

\[
 S=\operatorname{im}E=\mathbf C(1,1)\subset\mathbf C^2,
\qquad
 U=G_1\oplus0\subset G_1\oplus G_2.
\]

Then

\[
 \dim U=2n=nN,
\]

so B187's numerical ceiling is saturated. But the nodewise Hessian
pairings on \(U\) have span

\[
 H(U)=\mathbf C(1,0),
\]

because \(B\) is nondegenerate. Consequently

\[
 S+H(U)=\mathbf C^2,
\qquad
 L_U=(S+H(U))^\perp=0. \tag{1}
\]

Equivalently, the unique value relation \(c=(1,-1)\) restricts to the
nondegenerate form \(B\) on \(U\), not to zero.

## Consequence

Rank at most \(nN\) is necessary after a full-support isotropic relation
has already been found; it is not sufficient to produce that relation.
G121 must construct the augmented defect (1), not merely the numerical
gradient corank.
