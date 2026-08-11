---
brick_id: B197
status: PROVED
base_field: C
variety: a smooth projective complex variety with a very ample line bundle H and a nonempty finite reduced point scheme Z
smoothness: X and the supports of Z are smooth; no divisor, node-incidence germ, or deformation space is asserted smooth
projectivity: X, the powers H^k, Z, and its first infinitesimal neighborhood 2Z are projective
dimension: dim X=d; length Z=N; the conditional first-jet quotient V_k has dimension q_k between 0 and dN
codimension: q_k is the difference between the first-jet and value Hilbert functions; multiplication makes q_k nondecreasing
coefficient_field: C for sections, jets, Hilbert functions, and multiplication; Q remains required separately for the Hodge detector
cohomology_theory: coherent first jets, restriction maps to zero-dimensional schemes, and graded section multiplication
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B191-B196 and global generation of positive powers of a very ample line bundle
claim: The dimensions q_k=dim H0(I_Z H^k)/H0(I_2Z H^k) are nondecreasing. Precisely, multiplication by any section of H^a nonzero at every point of Z injects V_k into V_(k+a). Moreover q_k=h_2Z(k)-h_Z(k), and for m>=2 all lower V_k vanish exactly when V_(m-1)=0.
falsifier: a nonzero conditional first jet killed after multiplication by a section nonzero on Z, a decrease q_(k+a)<q_k, failure of the Hilbert-function difference formula, or V_(m-1)=0 with some lower V_k nonzero
---

# B197 — Conditional first-jet defect is monotone

Put

\[
 J_k=H^0(X,I_Z\otimes H^k),\qquad
 K_k=H^0(X,I_{2Z}\otimes H^k),\qquad
 V_k=J_k/K_k. \tag{1}
\]

For a finite scheme \(T\subset X\), write

\[
 h_T(k)=\operatorname{rank}\left(
 H^0(X,H^k)\longrightarrow H^0(T,H^k|_T)
 \right). \tag{2}
\]

Because \(K_k\subset J_k\) are the kernels of restriction to \(2Z\) and
\(Z\), respectively, rank-nullity gives the exact identity

\[
 q_k:=\dim V_k=h_{2Z}(k)-h_Z(k). \tag{3}
\]

## Multiplicative injection

Fix \(a\ge1\). Since \(H^a\) is globally generated and the base field is
infinite, there is a section

\[
 t\in H^0(X,H^a),\qquad t(p)\ne0\quad(p\in Z). \tag{4}
\]

Indeed, the sections vanishing at any fixed point form a proper hyperplane,
and finitely many proper hyperplanes do not cover the section space.
Multiplication defines

\[
 \mu_t:V_k\longrightarrow V_{k+a},\qquad [s]\longmapsto[ts]. \tag{5}
\]

It is well-defined because \(tK_k\subset K_{k+a}\). If \([ts]=0\), then at
every \(p\in Z\)

\[
 d(ts)(p)=t(p)\,ds(p)+s(p)\,dt(p)=t(p)\,ds(p)=0. \tag{6}
\]

Equation (4) forces \(ds(p)=0\) at every marked point, so \(s\in K_k\).
Thus (5) is injective and

\[
 q_k\le q_{k+a}. \tag{7}
\]

## Collapse of all lower-degree obligations

For \(m\ge2\), (7) implies

\[
 q_{m-1}=0
 \quad\Longleftrightarrow\quad
 q_k=0\quad(0\le k<m). \tag{8}
\]

Consequently G127 does not require independent constructions in every
lower embedding. By B196 it is enough to make the \(H^{m-1}\)-point span
full or tangent-absorbing; every earlier extinction then follows
algebraically. This does not construct the adjacent jump \(q_m=2n\), its
one-node Hessian holonomy, any rational detector, or an algebraic cycle.
