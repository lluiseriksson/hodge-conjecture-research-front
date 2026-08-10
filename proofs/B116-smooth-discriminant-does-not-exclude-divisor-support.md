---
brick_id: B116
status: PROVED
base_field: C
variety: the smooth projective base B = P^2_C, a smooth divisor D = P^1_C, and a local model for the perverse direct-image object of an arbitrary polarized smooth projective complex 2n-fold
smoothness: B and D smooth; the model is evaluated at a smooth point of D
projectivity: B and D projective; the model consists of polarizable pure Hodge modules
dimension: dim_C B = 2 and dim_C D = 1; downstream hyperplane fibers have dimension 2n-1
codimension: D has base codimension one; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: rational polarizable pure Hodge modules, perverse sheaves, intermediate extension, strict support, and stalk cohomology
hodge_type: the model is pure Tate; downstream selected relation classes must have rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); the model constructs no cycle and assumes no algebraic representative
cycle_equivalence: rational equivalence
scope: relative
dependencies: B008, B077, B080-B081, G045-G046, G077
claim: Vanishing of the smooth-discriminant local intersection-cohomology group H^(-1)(i_p^* j_!*L[2]) does not imply that the total perverse direct-image object has no divisor-supported strict-support summand in the same detector grade.
falsifier: a theorem in the stated semisimple Hodge-module category forcing every divisor-supported strict-support summand to vanish whenever the full-support intermediate-extension stalk has zero H^(-1)
---

# B116 — Smooth-discriminant vanishing does not remove divisor support

**Status:** PROVED

Let

\[
 B=\mathbf P^2_{\mathbf C},\qquad D\subset B
\]

be a line, let \(i:D\hookrightarrow B\), and let
\(j:B\setminus D\hookrightarrow B\). In the category of rational
polarizable pure Hodge modules set

\[
 P=\mathbf Q_B^H[2]=j_{!*}\mathbf Q_{B\setminus D}^H[2],
 \qquad
 Q=i_*\mathbf Q_D^H[1],
 \qquad
 K=P\oplus Q.
\]

Both summands are semisimple perverse Hodge modules. The strict support of
\(P\) is all of \(B\), while the strict support of \(Q\) is \(D\).
For every \(p\in D\),

\[
 H^{-1}(i_p^*P)=0,
 \qquad
 H^{-1}(i_p^*Q)=\mathbf Q,
 \qquad
 H^{-1}(i_p^*K)=\mathbf Q.
\]

Thus the degree used by B080 cleanly distinguishes two facts:

1. the full-support intermediate-extension channel can vanish at a smooth
   discriminant point, exactly as in B008; and
2. the total perverse object can nevertheless contain a nonzero
   divisor-supported coordinate in that same ordinary stalk degree.

The direct sum is already the canonical strict-support decomposition, so
the example does not exploit a noncanonical splitting across perverse
degrees. It is also pure Tate, so no integral/rational or Hodge-type mismatch
is involved.

## Consequence for G077

B008 cannot be used to prove \(\beta_D=0\). It computes the local
intersection-cohomology channel of the full-support variation, not the
multiplicity or selected-class coordinate of \(IC_D(M_D)\) inside the total
proper pushdown. Those divisor coordinates require a separate calculation.
G078 records the canonical transverse-slice calculation that would do so.

## Scope guard

This is a logical countermodel, not a claim that the actual hyperplane
pushdown contains a divisor summand. It proves only that the proposed
inference from B008 is invalid. It produces no Hodge class and no algebraic
cycle.
