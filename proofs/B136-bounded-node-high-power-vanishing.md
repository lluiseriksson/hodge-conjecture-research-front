---
brick_id: B136
status: PROVED
base_field: C
variety: a fixed polarized smooth projective complex 2n-fold X with ample line bundle L and nodal members in the systems |L^m|
smoothness: X is smooth; the tested hypersurface members have only ordinary double points with reduced node schemes
projectivity: X, its Hilbert schemes of points, and the hypersurface members are projective
dimension: dim_C X=2n with n at least 2; hypersurface dimension 2n-1
codimension: middle codimension n on X; every node has codimension 2n and the node count is bounded by a fixed integer N
coefficient_field: C for coherent evaluation and Q for vanishing-cycle relations, with Q(n) in the Hodge normalization
cohomology_theory: coherent cohomology, relative Serre vanishing on Hilbert schemes of points, nodal vanishing homology, and local intersection cohomology
hodge_type: every potential nodal relation would be rational type (0,0) after Q(n), but the proved relation space is zero
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B026-B027, S055 Hilbert schemes of points and relative Serre vanishing
claim: For every fixed N there is m_0(X,L,N) such that every B026-admissible nodal member of |L^m| with at most N nodes has zero adjoint defect, zero vanishing-cycle relation space, and zero degree-one local incidence channel for all m at least m_0.
falsifier: a fixed N and a sequence m tending to infinity of nodal members with at most N nodes and nonzero adjoint defect or a nonzero rational relation among their vanishing cycles
---

# B136 — Bounded node sets have no high-power relation

**Status:** PROVED

Fix \(N\ge1\). The key point is uniformity over the locations of the nodes,
not merely Serre vanishing for one previously chosen set.

## Uniform separation of bounded finite schemes

For \(1\le k\le N\), let

\[
 H_k=\operatorname{Hilb}^k(X)
\]

and let \(\mathcal Z_k\subset X\times H_k\) be the universal finite flat
subscheme, with ideal \(\mathcal I_k\). Write

\[
 p:X\times H_k\to H_k,\qquad q:X\times H_k\to X.
\]

The scheme \(H_k\) is proper and Noetherian. The line bundle \(q^\ast L\)
is \(p\)-ample. Relative Serre vanishing applied to the coherent sheaf
\(\mathcal I_k\) gives, uniformly on \(H_k\),

\[
 R^1p_\ast(\mathcal I_k\otimes q^\ast L^m)=0
 \qquad(m\ge m_k).
\]

For the same large \(m\), ordinary Serre vanishing on \(X\) and base change
identify

\[
 p_\ast q^\ast L^m
 =H^0(X,L^m)\otimes\mathcal O_{H_k}.
\]

Because \(\mathcal Z_k\to H_k\) is finite flat, the sheaf

\[
 p_\ast(\mathcal O_{\mathcal Z_k}\otimes q^\ast L^m)
\]

is locally free of rank \(k\) and commutes with base change. Pushing forward
the universal ideal sequence therefore gives a surjection

\[
 H^0(X,L^m)\otimes\mathcal O_{H_k}
 \twoheadrightarrow
 p_\ast(\mathcal O_{\mathcal Z_k}\otimes q^\ast L^m).
\]

Taking the fiber at any \(Z\in H_k\) proves

\[
 H^0(X,L^m)\twoheadrightarrow H^0(Z,L^m|_Z)
\]

for every length-\(k\) subscheme \(Z\). Taking the maximum of the finitely
many \(m_k\) gives one threshold valid for all \(k\le N\).

## Nodal consequence

Put \(A_m=L^m\). Increase the threshold so that

\[
 K_X\otimes A_m^{n-1}\ \text{is globally generated},\qquad
 H^1(X,K_X\otimes A_m^n)=0.
\]

This is possible because \(n\ge2\). Let \(Y_m\in|A_m|\) be nodal with
reduced node scheme \(\Delta_m\) of length at most \(N\). Uniform separation
and \(H^1(X,A_m)=0\) give

\[
 H^1(X,I_{\Delta_m}\otimes A_m)=0.
\]

All hypotheses of B027 now hold, so

\[
 H^1(X,I_{\Delta_m}\otimes K_X\otimes A_m^n)=0.
\]

In the B026 nodal scope this equals the dimension of the vanishing-cycle
relation space. Consequently

\[
 R(Y_m)=0,\qquad
 \mathcal H^{-d+1}(IC(V_m))_{[Y_m]}=0.
\]

## Consequences for the active route

Taking \(N=2\) closes the asymptotic G089 strategy: in every sufficiently
high power, a member with exactly two nodes has independent vanishing cycles,
so no proportional-pair residue quotient exists at all.

More generally, any sequence of high-power nodal detectors must have

\[
 |\Delta_m|\longrightarrow\infty.
\]

Thus the next scalable clean-nodal gate is not another bounded local model.
It is G013's multipart incidence, with node count growing enough to create
adjoint dependence while preserving isolated first jets and a nonzero B135
residue-cokernel coordinate. B137 subsequently sharpens this qualitative
growth requirement to the linear floor \(2(mn-c)+2\) for a fixed very ample
embedding.

## Scope guard

B136 does not exclude exceptional relations in finitely many low powers and
does not prove that any growing multipart configuration exists. It proves
that increasing positivity while keeping a bounded number of nodes cannot
close G088.
