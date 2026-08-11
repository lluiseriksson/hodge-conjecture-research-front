---
brick_id: B211
status: PROVED
base_field: C
variety: a smooth projective complex d-fold with very ample H, a finite reduced point scheme Z of length N, and G139's adjacent osculating package
smoothness: X and Z are smooth; pointwise full order-two jet rank is stated separately when used for the node floor
projectivity: X, powers H^(m-1) and H^m, the schemes Z, 2Z, 3Z, and their restriction maps are projective coherent data
dimension: dim X=d; length Z=N; the fiber increments from Z to 2Z and from 2Z to 3Z are dN and d(d+1)N/2
codimension: G139 has adjacent Hilbert-rank increments (0,0) then (d,1), hence large defects from conditional jet independence
coefficient_field: C for sections, jets, ranks, and osculating spans; Q remains required separately for the detector
cohomology_theory: coherent restriction to zero-dimensional schemes, principal parts through order two, and finite-dimensional rank-nullity
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B197, B204, B209-B210, G139
claim: Writing h_(rZ)(k) for the restriction rank to rZ, G139 forces h_2Z(m-1)=h_Z(m-1), h_3Z(m-1)=h_2Z(m-1), h_2Z(m)-h_Z(m)=d, and h_3Z(m)-h_2Z(m)=1. Relative to maximal conditional ranks, the two degree-m defects are d(N-1) and d(d+1)N/2-1. If one marked order-two jet fiber has full rank binom(d+2,2), then N>=binom(d+2,2); in the full-span lower branch N>=h0(H^(m-1)).
falsifier: a different rank signature under G139, maximal conditional jet rank with the displayed small increments, or an order-two jet fiber of full dimension contained in a point span of smaller vector dimension
---

# B211 — The adjacent fat-point rank signature

For \(r=1,2,3\), write

\[
 h_{rZ}(k)=\operatorname{rank}\!\left[
 H^0(H^k)\longrightarrow H^0(H^k|_{rZ})
 \right]. \tag{1}
\]

Rank-nullity and the filtration \(T_k\subset K_k\subset J_k\) give

\[
 \dim V_k=h_{2Z}(k)-h_Z(k),\qquad
 \dim W_k=h_{3Z}(k)-h_{2Z}(k). \tag{2}
\]

Therefore G139's adjacent extinction and birth are exactly

\[
 \begin{aligned}
 h_{2Z}(m-1)-h_Z(m-1)&=0,\\
 h_{3Z}(m-1)-h_{2Z}(m-1)&=0,\\
 h_{2Z}(m)-h_Z(m)&=d,\\
 h_{3Z}(m)-h_{2Z}(m)&=1.
 \end{aligned} \tag{3}
\]

The local first- and second-order conormal fibers have dimensions

\[
 d,\qquad q_2=\binom{d+1}{2}=\frac{d(d+1)}2. \tag{4}
\]

Thus conditional jet independence at \(N\) nodes would give increments
\(dN\) and \(q_2N\). The G139 increments in (3) have exact defects

\[
 d(N-1),\qquad \binom{d+1}{2}N-1. \tag{5}
\]

In the Hodge setting \(d=2n\ge2\), the second defect is always positive.
Consequently a maximal-rank or independent-triple-point construction cannot
realize G139; the required configuration is strongly special.

## Necessary node floor

Suppose order-two jet evaluation at one marked point in degree \(m-1\) has
full fiber rank

\[
 c_d=\operatorname{length}(\mathcal O_{X,p}/\mathfrak m_p^3)
 =\binom{d+2}{2}. \tag{6}
\]

Its affine second osculating space has vector dimension \(c_d\). G139
places it inside the point span \(S_{m-1,Z}^{(0)}\), whose dimension is at
most \(N\). Hence

\[
 N\ge\binom{d+2}{2}; \tag{7}
\]

for \(d=2n\), this is \(N\ge(n+1)(2n+1)\). If the lower point span is the
whole ambient vector space, then instead directly

\[
 N\ge h^0(H^{m-1}). \tag{8}
\]

B211 gives necessary ranks and floors only. It constructs no special
scheme, nondegenerate profile, detector, or cycle.
