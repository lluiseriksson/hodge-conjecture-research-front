---
brick_id: B213
status: PROVED
base_field: C
variety: a smooth projective complex d-fold with very ample H, a finite reduced point scheme Z of length N, and G141's lower extinction and no-coloop degree-m value matroid
smoothness: X and Z are smooth; no divisor, ODP, or incidence germ is asserted smooth
projectivity: X, all powers H^k through m, the point evaluations, and their multiplication pairings are projective coherent data
dimension: dim X=d; E_k has rank h_Z(k); the degree-m relation has full support; the Hodge specialization has d=2n
codimension: multiplication transports one full-support degree-m relation injectively into every complementary lower relation space and forces N>=d+1+max(m,d+1)
coefficient_field: C for values, relations, multiplication, ranks, and tangent spans; Q remains required separately for the Hodge detector
cohomology_theory: coherent value evaluation, graded section multiplication, projective tangent-space duality, and finite-dimensional annihilators
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B187, B196-B197, B209-B212, G141
claim: Let E_k be the degree-k value image and R_k=E_k^perp. A full-support lambda in R_m induces, for every 1<=a<m, an injection E_a -> R_(m-a) by e maps to the functional x maps to lambda(ex). Hence N-h_Z(m-a)>=h_Z(a). Under G141, N>=h_Z(1)+h_Z(m-1)>=d+1+max(m,d+1); for d=2n this is N>=2n+1+max(m,2n+1). If the H-embedding has full order-two jet rank at one marked point, d+1 can be replaced in the first summand by binom(d+2,2).
falsifier: a nonzero value vector killed by a full-support relation multiplier, a transported functional outside R_(m-a), a G141 configuration violating any complementary-rank inequality, or a node count below the displayed floor
---

# B213 — A full-support relation propagates to lower degrees

For each \(k\), put

\[
 \mathcal T_k=\bigoplus_{i=1}^N H^k|_{p_i},\qquad
 E_k=\operatorname{im}\!\left[H^0(X,H^k)\to\mathcal T_k\right],
 \qquad
 \mathcal R_k=E_k^\perp. \tag{1}
\]

Multiplication of sections gives coordinatewise pairings

\[
 E_a\otimes E_b\longrightarrow E_{a+b}. \tag{2}
\]

G141's no-coloop degree-\(m\) value matroid has a full-support relation
\(\lambda\in\mathcal R_m\): B187's finite-union argument applies because
each coordinate occurs in some relation.

## Exact transport map

For \(1\le a<m\), define

\[
 M_{\lambda,a}:E_a\longrightarrow\mathcal T_{m-a}^*,\qquad
 M_{\lambda,a}(e)(x)=\lambda(ex). \tag{3}
\]

If \(x\in E_{m-a}\), then \(ex\in E_m\) by (2), so
\(\lambda(ex)=0\). Hence

\[
 M_{\lambda,a}(E_a)\subset\mathcal R_{m-a}. \tag{4}
\]

Every component \(\lambda_i\) is a nonzero functional on the
one-dimensional fiber \(H^m|_{p_i}\). If \(M_{\lambda,a}(e)=0\), then
\(\lambda_i(e_ix_i)=0\) for every \(i\) and every local fiber value
\(x_i\). Thus every \(e_i=0\), so \(e=0\) in \(E_a\). Therefore (3) is
injective and

\[
 N-h_Z(m-a)=\dim\mathcal R_{m-a}\ge h_Z(a)
 \qquad(1\le a<m). \tag{5}
\]

Equivalently,

\[
 h_Z(a)+h_Z(m-a)\le N. \tag{6}
\]

## Tangent absorption strengthens the node floor

Take \(a=1\), and write \(r=h_Z(m-1)\). G141's lower extinction gives
\(V_1=V_{m-1}=0\) by B197. Applying B196 to the embeddings by \(H\) and
\(H^{m-1}\), their point spans contain an affine embedded tangent space
of vector dimension \(d+1\). Consequently

\[
 h_Z(1)\ge d+1,\qquad r\ge d+1. \tag{7}
\]

B212 also gives \(r\ge m\). Equations (5) and (7) now yield

\[
 N\ge h_Z(1)+r
 \ge d+1+\max\{m,d+1\}. \tag{8}
\]

For the Hodge branch \(d=2n\),

\[
 N\ge 2n+1+\max\{m,2n+1\}. \tag{9}
\]

If the \(H\)-embedding has full order-two jet rank at one marked point,
lower second-profile extinction and B210 give
\(h_Z(1)\ge\binom{d+2}{2}\). In that conditional branch, (8) strengthens
to

\[
 N\ge\binom{d+2}{2}+\max\{m,d+1\}. \tag{10}
\]

B213 is a necessary rank obstruction. It constructs no special scheme,
profile, holonomy, detector, or algebraic cycle.
