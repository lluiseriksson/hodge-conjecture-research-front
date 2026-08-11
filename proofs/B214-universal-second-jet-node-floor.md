---
brick_id: B214
status: PROVED
base_field: C
variety: a smooth projective complex d-fold with very ample H, a finite reduced point scheme Z, and G142's lower two-layer extinction and full-support degree-m relation
smoothness: X and Z are smooth, so regular parameters and principal parts through order two have their expected dimensions; no divisor or incidence smoothness is inferred
projectivity: X, all powers H^k through m, the H-embedding, point and second-osculating spans, and value multiplication are projective
dimension: dim X=d; c_d=binom(d+2,2) is the full order-two jet length; the Hodge case has d=2n
codimension: H^k is order-two jet spanned for every k>=2, so B213 yields the piecewise node floor C_d(2)=2(d+1), C_d(3)=c_d+d+1, and C_d(m)=c_d+max(c_d,m-1) for m>=4
coefficient_field: C for local parameters, sections, jets, spans, relations, and ranks; Q remains required separately for the Hodge detector
cohomology_theory: principal parts through order two, projective embeddings, graded section multiplication, and finite-dimensional annihilator duality
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196-B197, B209-B213, G142
claim: For every k>=2, H^k has surjective order-two jet evaluation at every point. Under lower extinction, h_Z(1)>=d+1 and h_Z(k)>=max(k+1,c_d) for 2<=k<m. B213 then forces N>=C_d(m), where C_d(2)=2(d+1), C_d(3)=c_d+d+1, and C_d(m)=c_d+max(c_d,m-1) for m>=4. In particular B211's full lower order-two jet hypothesis is automatic when m>=3.
falsifier: a missing order-two jet of H^k for k>=2, a lower point span smaller than a full second osculator under extinction, or G142 data with N below the displayed piecewise floor
---

# B214 — Universal second-jet generation raises the node floor

Put

\[
 c_d=\operatorname{length}(\mathcal O_{X,p}/\mathfrak m_p^3)
 =\binom{d+2}{2}. \tag{1}
\]

## Every \(H^k\), \(k\ge2\), generates full two-jets

Fix \(p\in X\). Choose \(s_0\in H^0(X,H)\) nonzero at \(p\). Because the
map defined by \(H\) is an immersion, choose sections
\(s_1,\ldots,s_d\), each vanishing at \(p\), such that

\[
 x_j=s_j/s_0\qquad(1\le j\le d) \tag{2}
\]

form a regular system of parameters at \(p\). For every \(k\ge2\), the
global sections

\[
 s_0^k,\qquad s_js_0^{k-1},\qquad
 s_is_js_0^{k-2}\quad(1\le i\le j\le d) \tag{3}
\]

have local representatives

\[
 1,\qquad x_j,\qquad x_ix_j. \tag{4}
\]

These form a basis of
\(\mathcal O_{X,p}/\mathfrak m_p^3\). Hence

\[
 H^0(X,H^k)\longrightarrow
 H^k|_p\otimes\mathcal O_{X,p}/\mathfrak m_p^3
 \quad\text{is surjective for every }k\ge2. \tag{5}
\]

No projective-normality or global jet-ampleness theorem is used.

## Consequence of lower second-osculating absorption

G142's adjacent extinction propagates by B209 to every \(1\le k<m\).
For \(k\ge2\), B210 and (5) place a \(c_d\)-dimensional affine second
osculator inside the degree-\(k\) point span. B212 independently gives
the Veronese separation bound \(h_Z(k)\ge k+1\). Therefore

\[
 h_Z(1)\ge d+1,\qquad
 h_Z(k)\ge\max\{c_d,k+1\}\quad(2\le k<m). \tag{6}
\]

In particular, when \(m\ge3\), the full order-two hypothesis used
conditionally in B211 at degree \(m-1\) is automatic.

## Optimize B213's complementary-degree inequality

B213 gives

\[
 h_Z(a)+h_Z(m-a)\le N\qquad(1\le a<m). \tag{7}
\]

- If \(m=2\), use \(a=1\) and (6):

  \[
  N\ge2(d+1). \tag{8}
  \]

- If \(m=3\), use the pair \(1,2\):

  \[
  N\ge c_d+d+1. \tag{9}
  \]

- If \(m\ge4\), use the pair \(2,m-2\):

  \[
  N\ge c_d+\max\{c_d,m-1\}. \tag{10}
  \]

For \(2\le a\le m-2\), the lower-bound sum from (6) is symmetric and
piecewise convex in \(a\), hence is maximal at \(a=2\) or \(m-2\).
The pair \(1,m-1\) gives
\(d+1+\max\{c_d,m\}\), which is no larger than (10) because
\(c_d\ge d+2\). Thus the displayed pairs maximize the universal lower
bound supplied by (6), so define

\[
 C_d(m)=
 \begin{cases}
 2(d+1),&m=2,\\
 c_d+d+1,&m=3,\\
 c_d+\max\{c_d,m-1\},&m\ge4.
 \end{cases} \tag{11}
\]

Every G142 configuration satisfies \(N\ge C_d(m)\). B214 constructs no
configuration, ODP profile, holonomy, detector, or algebraic cycle.
