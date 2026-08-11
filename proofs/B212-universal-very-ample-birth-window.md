---
brick_id: B212
status: PROVED
base_field: C
variety: a smooth projective complex d-fold X with a very ample line bundle H, a nonempty finite reduced point scheme Z of length N, and G140's adjacent fat-point data
smoothness: X and Z are smooth; no nodal divisor or incidence germ is asserted smooth
projectivity: X, its embedding by H, all powers H^k, and the schemes Z, 2Z, and 3Z are projective
dimension: dim X=d; length Z=N; length 3Z=binom(d+2,2)N; the proposed birth degree is m
codimension: lower two-layer extinction plus a nonzero no-coloop degree-m value relation forces N>=m+2 and bounds the adjacent Hilbert ranks
coefficient_field: C for sections, restrictions, ranks, and value matroids; Q remains required separately for the Hodge detector
cohomology_theory: coherent restriction to zero-dimensional schemes, Castelnuovo-Mumford regularity, Hilbert functions, and finite-dimensional duality
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B197, B209-B211, G140, S076, and Gotzmann regularity
claim: Every H^k separates every zero-dimensional subscheme of length at most k+1. Hence G140 forces N>=m+2. If r=h_Z(m-1) and R=h_Z(m), then m<=r<=R, m+1<=R<=N-1, h_2Z(m-1)=h_3Z(m-1)=r, h_2Z(m)=R+d, and h_3Z(m)=R+d+1. Every nonzero degree-m value relation has support at least m+2. With B211's pointwise full order-two hypothesis, N>=max(m+2,binom(d+2,2)).
falsifier: a length-at-most-k+1 scheme not separated by H^k, G140 data with N<=m+1, a degree-m relation supported on at most m+1 nodes, or any rank outside the displayed window
---

# B212 — Universal very-ample window for the adjacent birth

Embed \(X\hookrightarrow\mathbf P^s\) by \(H\). Let
\(\xi\subset X\) be zero-dimensional of length \(\ell\le k+1\). S076's
zero-dimensional case of Gotzmann regularity says that
\(I_{\xi/\mathbf P^s}\) is \(\ell\)-regular. Therefore

\[
 H^1(\mathbf P^s,I_\xi(k))=0\qquad(k\ge\ell-1), \tag{1}
\]

so degree-\(k\) polynomials restrict surjectively to \(\xi\). Their
restrictions to \(X\) are global sections of \(H^k\). Consequently

\[
 H^0(X,H^k)\longrightarrow H^0(\xi,H^k|_\xi)
 \quad\text{is surjective whenever }\operatorname{length}\xi\le k+1.
 \tag{2}
\]

Thus \(H^k\) is \(k\)-very ample. This uses only the embedding by \(H\),
not projective normality of \(X\).

## Apply (2) below the birth

Put \(k=m-1\). An Artinian composition series (all residue fields are
\(\mathbf C\)) gives subschemes of every smaller length inside \(3Z\).
Thus (2) gives

\[
 h_{3Z}(m-1)\ge
 \min\!\left\{m,\binom{d+2}{2}N\right\}. \tag{3}
\]

G140's lower extinction and the reduced target give

\[
 h_{3Z}(m-1)=h_Z(m-1)\le N. \tag{4}
\]

Since \(d\ge1\), equations (3)--(4) exclude \(m>N\). Hence

\[
 m\le N. \tag{5}
\]

Write

\[
 r=h_Z(m-1),\qquad R=h_Z(m). \tag{6}
\]

Applying (2) to \(m\) reduced points and using monotonicity gives

\[
 m\le r\le R. \tag{7}
\]

## The value relation makes the window strict

G140 retains a nonzero degree-\(m\) value-relation space with no coloop.
If \(N\le m+1\), equation (2) applied to \(Z\) in degree \(m\) would make
the value evaluation surjective, leaving no relation. Therefore

\[
 N\ge m+2,\qquad m+1\le R\le N-1. \tag{8}
\]

More precisely, every subset of at most \(m+1\) reduced marked points is
independent in degree \(m\). Thus every nonzero degree-\(m\) value relation
has support at least \(m+2\).

Combining (6)--(8) with B211 gives the complete adjacent rank window

\[
 \begin{array}{c|ccc}
 &h_Z&h_{2Z}&h_{3Z}\\ \hline
 m-1&r&r&r\\
 m&R&R+d&R+d+1
 \end{array},
 \qquad
 m\le r\le R,\quad m+1\le R\le N-1. \tag{9}
\]

If B211's pointwise full order-two jet hypothesis holds in degree
\(m-1\), its node floor combines with (8) to give

\[
 N\ge\max\!\left\{m+2,\binom{d+2}{2}\right\}. \tag{10}
\]

B212 is necessary only. It constructs no point scheme, central profile,
holonomy, detector, or algebraic cycle.
