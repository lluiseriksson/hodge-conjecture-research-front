---
brick_id: B194
status: PROVED
base_field: C
variety: a smooth projective complex variety with a very ample line bundle H, a set Z of at least two distinct points, and the full complete linear systems of powers H^k up to H^m
smoothness: the variety and point supports are smooth; in the intended application the degree-m central singularities are ODPs, but the extinction theorem concerns coherent first jets
projectivity: the variety, all powers of H, reduced point scheme Z, and doubled scheme 2Z are projective
dimension: arbitrary positive dimension; the Hodge application has dimension 2n and a degree-m conditional-gradient quotient of dimension at most 2n
codimension: one-node determination in degree m forces every lower-degree value-zero section to vanish to first order at all nodes
coefficient_field: C for sections, multiplication, values, and first jets; Q remains required separately for downstream Hodge detectors
cohomology_theory: coherent first-jet evaluation, multiplication of graded sections, and point separation by very ample powers
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B191-B193, G123-G124, and very ample separation of distinct points
claim: If the degree-m full conditional-gradient quotient is determined by the gradient at every one node, then for every k<m one has H0(I_Z H^k)=H0(I_2Z H^k). Thus no lower-degree section vanishing on Z has a nonzero node gradient; every nonzero conditional first jet in degree m is primitive with respect to multiplication from lower powers.
falsifier: a lower-degree section vanishing on Z with nonzero derivative at one node while every degree-m value-zero section with zero derivative at one node has zero derivatives at all nodes
---

# B194 — One-node determination forces primitive first-jet birth

Let \(H\) be very ample, let

\[
 Z=\{p_1,\ldots,p_N\},\qquad N>1,
\]

and fix \(m\ge1\). Assume the degree-\(m\) full system satisfies B191's
one-node determination:

\[
 H^0(X,I_{\Psi_j}\otimes H^m)
 =H^0(X,I_{2Z}\otimes H^m)
 \quad\text{for every }j. \tag{1}
\]

Equivalently, a section of \(I_Z\otimes H^m\) whose derivative vanishes at
one node has derivative zero at every node.

## Multiplication argument

Fix \(0\le k<m\) and take

\[
 s\in H^0(X,I_Z\otimes H^k). \tag{2}
\]

We prove \(ds(p_i)=0\) for every \(i\). Choose a second node \(p_j\ne p_i\).
The positive power \(H^{m-k}\) is very ample, so it separates these two
points. There is

\[
 h\in H^0(X,H^{m-k})
 \quad\text{with}\quad
 h(p_j)=0,\qquad h(p_i)\ne0. \tag{3}
\]

The product

\[
 hs\in H^0(X,I_Z\otimes H^m) \tag{4}
\]

has derivative at a node \(p\in Z\)

\[
 d(hs)(p)=h(p)\,ds(p)+s(p)\,dh(p)=h(p)\,ds(p), \tag{5}
\]

because \(s|_Z=0\). At \(p_j\), equations (3), (5) give
\(d(hs)(p_j)=0\). By (1), \(hs\) vanishes to first order at every node.
At \(p_i\),

\[
 0=d(hs)(p_i)=h(p_i)\,ds(p_i). \tag{6}
\]

Since \(h(p_i)\ne0\), \(ds(p_i)=0\). The node \(i\) was arbitrary, hence

\[
 s\in H^0(X,I_{2Z}\otimes H^k). \tag{7}
\]

The reverse inclusion is tautological, so for every \(k<m\),

\[
 H^0(X,I_Z\otimes H^k)
 =H^0(X,I_{2Z}\otimes H^k). \tag{8}
\]

## Consequence

Define the graded conditional-gradient quotients

\[
 V_k=H^0(X,I_Z\otimes H^k)/H^0(X,I_{2Z}\otimes H^k). \tag{9}
\]

Then

\[
 V_k=0\quad(0\le k<m). \tag{10}
\]

If \(V_m\ne0\), its first jets appear for the first time in degree \(m\).
They cannot be inherited by multiplying any lower-degree section vanishing
on \(Z\). This is a full-complete-system theorem: all products (4) are
already present in \(H^0(X,H^m)\).

B194 constructs neither the primitive birth \(V_m\), nor one-node
determination, Hessian holonomy, a detector, higher Kuranishi vanishing, or
an algebraic cycle.
