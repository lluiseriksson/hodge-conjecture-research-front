---
brick_id: B210
status: PROVED
base_field: C
variety: a smooth projective complex variety embedded by a very ample line bundle A, with a finite set Z of distinct smooth points
smoothness: X and Z are smooth so the first and second principal-part fibers have the expected intrinsic jet interpretation; no divisor smoothness follows
projectivity: the embedding, point lines, affine tangent spaces, second osculating spaces, and their spans are projective linear data
dimension: dim X=d; V_A is dual to the first-osculating span modulo the point span and W_A is dual to the second-osculating span modulo the first
codimension: simultaneous first- and second-jet extinction is exactly absorption of every second osculating space by the point span
coefficient_field: C for embeddings, jets, annihilators, and osculating spaces; Q remains required separately for the detector
cohomology_theory: principal parts through order two, coherent ideal powers, and finite-dimensional projective duality
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196, B204, B209, and the principal-parts interpretation of a very ample embedding
claim: Let S_Z^(j) be the span in H0(A)^* of the images dual to order-j jet evaluation at all points of Z, for j=0,1,2. Then V_A^* is S_Z^(1)/S_Z^(0), W_A^* is S_Z^(2)/S_Z^(1), and V_A=W_A=0 exactly when S_Z^(0)=S_Z^(1)=S_Z^(2). In the proper branch, the projective point span contains every second osculating space at Z.
falsifier: a section-space annihilator different from the corresponding jet span, a mismatch between either quotient dimension and its osculating increment, or simultaneous quotient vanishing with a second osculating direction outside the point span
---

# B210 — Quadratic-profile extinction is second-osculating absorption

Let \(A\) be very ample, \(\mathcal W=H^0(X,A)\), and

\[
 j_{i}^{(r)}:\mathcal W\longrightarrow
 A_{p_i}\otimes\mathcal O_{X,p_i}/\mathfrak m_{p_i}^{r+1}
 \qquad(r=0,1,2)
\]

be jet evaluation. Define

\[
 \widehat O_i^{(r)}=\operatorname{im}\bigl((j_i^{(r)})^*\bigr)
 \subset \mathcal W^*,\qquad
 S_Z^{(r)}=\sum_i\widehat O_i^{(r)}. \tag{1}
\]

These are respectively the embedded point line, affine tangent space, and
affine second osculating space, summed over \(Z\). They form a flag

\[
 S_Z^{(0)}\subset S_Z^{(1)}\subset S_Z^{(2)}. \tag{2}
\]

The kernels of the three jet evaluations are the annihilators

\[
 H^0(I_ZA)=(S_Z^{(0)})^\perp,\quad
 H^0(I_Z^2A)=(S_Z^{(1)})^\perp,\quad
 H^0(I_Z^3A)=(S_Z^{(2)})^\perp. \tag{3}
\]

Finite-dimensional duality applied to (2)--(3) gives canonical
identifications

\[
 V_A^*\cong S_Z^{(1)}/S_Z^{(0)},\qquad
 W_A^*\cong S_Z^{(2)}/S_Z^{(1)}. \tag{4}
\]

Therefore

\[
 V_A=W_A=0
 \quad\Longleftrightarrow\quad
 S_Z^{(0)}=S_Z^{(1)}=S_Z^{(2)}. \tag{5}
\]

If the point span \(\mathbf P(S_Z^{(0)})\) is proper, (5) says it contains
the second osculating space of \(X\) at every marked point. If it is the
whole ambient space, the condition is vacuous.

At a G138 birth, (4) also gives

\[
 \dim S_Z^{(1)}/S_Z^{(0)}=d,\qquad
 \dim S_Z^{(2)}/S_Z^{(1)}=1. \tag{6}
\]

B210 is exact projective duality. It constructs no absorbing span, adjacent
jump, ODP, detector, or cycle.
