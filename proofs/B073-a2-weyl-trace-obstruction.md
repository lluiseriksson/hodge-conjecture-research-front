---
brick_id: B073
status: PROVED
base_field: Q for the representation; C for the A2 geometric realization
variety: the local A2 vanishing lattice on the ordered-root S3 cover
smoothness: local Milnor fibers are smooth; no global smooth family is asserted
projectivity: local representation calculation; projective globalization is not asserted
dimension: rank-two vanishing lattice, arising inside arbitrary odd-dimensional quadratic suspensions
codimension: local vanishing channel; terminal cycles would have codimension n
coefficient_field: Q
cohomology_theory: rational vanishing homology and finite-group representation theory
hodge_type: no Hodge-type assertion; the calculation is representation-theoretic
cycle_class_map: not used; downstream map is CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence in the downstream Hodge application
scope: fiberwise
dependencies: B067-B068, B072
claim: The rational A2 root or vanishing lattice is the two-dimensional standard S3 representation, has zero S3-invariant subspace, and its normalized group-average projector is the zero map.
falsifier: a nonzero vector fixed by both simple reflections or a nonzero average matrix
---

# B073 — The local A2 Weyl trace vanishes

**Status:** PROVED

Let

\[
V=\{(x_1,x_2,x_3)\in\mathbf Q^3:x_1+x_2+x_3=0\}
\]

with basis \(\alpha_1=e_1-e_2\), \(\alpha_2=e_2-e_3\). This is the
rational \(A_2\) root lattice and the rational vanishing lattice in the Weyl
description audited in B068. The simple transpositions act by

\[
s_1=\begin{pmatrix}-1&1\\0&1\end{pmatrix},\qquad
s_2=\begin{pmatrix}1&0\\1&-1\end{pmatrix}.
\]

Solving \((s_1-I)v=(s_2-I)v=0\) gives \(v=0\). Equivalently,

\[
V^{S_3}=0,
\qquad
e_{S_3}:=\frac1{6}\sum_{g\in S_3}g=0\quad\text{on }V.
\]

The exact matrix calculation is reproduced by
`verification/verify_B073_a2_weyl_trace.py`.

## Consequence and boundary

A single detector candidate that lives only in the local \(A_2\) vanishing
lattice cannot descend by normalized \(S_3\)-averaging: its trace is zero.
This does not prove that the full detector in B072's proper pushdown vanishes.
It may acquire an invariant component from global thimbles, boundary terms,
or a larger full-support representation. G041 isolates exactly that remaining
question.
