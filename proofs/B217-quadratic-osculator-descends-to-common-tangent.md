---
brick_id: B217
status: PROVED
base_field: C
variety: a smooth projective complex d-fold with very ample H and a reduced marked scheme Z satisfying B216's common full second-osculator conclusion
smoothness: X and Z are smooth; only embedded tangent and second-principal-part spaces are used
projectivity: the H-embedding, its quadratic multiplication subsystem inside H^2, the marked point span, and all affine osculating spaces are projective data
dimension: dim X=d; every affine tangent space has dimension d+1 and every full affine second osculator of H^2 has dimension c_d=binom(d+2,2)
codimension: a common full H^2 second osculator plus lower first-layer absorption forces all marked H-tangent spaces and the H-point span to be the same d+1 dimensional vector space
coefficient_field: C for section multiplication, symmetric tensors, tangent spaces, and point evaluations; Q detector data remain separate
cohomology_theory: coherent first and second principal parts, dual section multiplication, and finite-dimensional symmetric linear algebra
hodge_type: none asserted; rational type (0,0) and the specified Hodge pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196, B214-B216, G143
claim: In every minimal-window G143 configuration with m>=3, if all full affine second osculators of the H^2 embedding equal S_(2,Z)^(0), then the degree-one point span equals every affine tangent space: S_(1,Z)^(0)=T_hat_(p_i)X for all p_i in Z. Hence h_Z(1)=d+1, and the H-images of all marked points lie in one projective d-plane Lambda that is tangent to X at every marked point.
falsifier: two marked points p,q with equal full H^2 second osculators but v_q outside T_hat_p X, or a lower-absorbed tangent space strictly smaller or larger than the degree-one marked point span
---

# B217 — The quadratic osculator descends to a common tangent plane

Let

\[
 V=H^0(X,H)^*,\qquad W=H^0(X,H^2)^*.
\]

Multiplication of sections and its dual are

\[
 \mu:\operatorname{Sym}^2H^0(X,H)\longrightarrow H^0(X,H^2),
 \qquad
 \mu^*:W\longrightarrow\operatorname{Sym}^2V. \tag{1}
\]

For a marked point \(p\), choose a nonzero evaluation vector
\(v_p\in V\), and put

\[
 U_p=\widehat T_pX\subset V. \tag{2}
\]

## Image of the second osculator

In local coordinates, a lift of the H-embedding has expansion

\[
 v(t)=v_p+\sum_i t_i v_i+
 \frac12\sum_{i,j}t_it_jv_{ij}+O(t^3), \tag{3}
\]

where \(U_p=\langle v_p,v_1,\ldots,v_d\rangle\). The terms through
order two in \(v(t)^2\) are spanned by

\[
 v_p^2,\qquad v_pv_i,\qquad v_iv_j+v_pv_{ij}. \tag{4}
\]

Every tensor in (4) has at least one factor in \(U_p\). Therefore

\[
 \mu^*\bigl(\widehat O_p^{(2)}(H^2)\bigr)
 \subset U_p\cdot V
 =\ker\!\left(\operatorname{Sym}^2V
 \longrightarrow\operatorname{Sym}^2(V/U_p)\right). \tag{5}
\]

No surjectivity of \(\mu\), and hence no projective normality, is used.

## Recover the tangent plane

Assume B216's equality

\[
 \widehat O_p^{(2)}(H^2)=S_{2,Z}^{(0)}
 \quad(p\in Z). \tag{6}
\]

For any \(q\in Z\), its H^2 evaluation line lies in the left side of
(6), and its image by \(\mu^*\) is \(v_q^2\). Equations (5)-(6) give

\[
 (v_q\bmod U_p)^2=0\quad\text{in }\operatorname{Sym}^2(V/U_p). \tag{7}
\]

The symmetric algebra of a complex vector space is a polynomial ring,
so (7) implies \(v_q\in U_p\). Hence

\[
 S_{1,Z}^{(0)}=\langle v_q:q\in Z\rangle\subset U_p. \tag{8}
\]

G143's lower first-layer extinction and B196 give the reverse inclusion
\(U_p\subset S_{1,Z}^{(0)}\). Thus, simultaneously for every marked
point,

\[
 S_{1,Z}^{(0)}=U_p,\qquad h_Z(1)=d+1. \tag{9}
\]

Projectivizing (9) produces one \(d\)-plane
\(\Lambda=\mathbf P(S_{1,Z}^{(0)})\) containing \(Z\) and satisfying
\(\Lambda=T_pX\) for every \(p\in Z\). This constructs no such marked
fiber and no Hodge detector or algebraic cycle.
