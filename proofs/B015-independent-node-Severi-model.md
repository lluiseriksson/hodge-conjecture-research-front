---
brick_id: B015
status: PROVED
base_field: C
variety: a smooth projective X of dimension 2n embedded in projective space and a hyperplane section X_H with delta ordinary double points imposing independent conditions
smoothness: X is smooth; X_H is singular exactly at delta nodes; the relevant Severi strata are smooth near H
projectivity: X is projective with a fixed very ample hyperplane bundle
dimension: dim X = 2n; dim X_H = 2n-1; the dual parameter space has dimension N and the r-node stratum has local dimension N-r
codimension: middle codimension n on X; the r-node parameter stratum has codimension r
coefficient_field: Q
cohomology_theory: singular Betti cohomology, intersection cohomology, perverse filtration, local monodromy, and Picard-Lefschetz theory
hodge_type: primitive middle Hodge input in the application; the geometric normal-crossing and stalk computations are rational and not class-specific
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n)); no detecting algebraic cycle or hyperplane is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: Di Gennaro-Franco Theorem 3.2, Theorem 4.3, Corollary 4.5, and Remark 4.6 (S025)
claim: If the nodes of a nodal hyperplane section impose independent conditions, the local dual discriminant is normal crossing, every partial-smoothing Severi stratum is smooth of expected codimension, and the relevant local intersection complex is concentrated in degrees zero and one with degree one equal to the primitive local restriction channel.
falsifier: data satisfying H^1(I_Delta,X(1))=0 for which the local discriminant is not normal crossing, a partial node stratum has the wrong local dimension, or the cited intersection-complex exact sequence fails
---

# B015 - Independent-node Severi model

Let \(X^{2n}\subset\mathbf P^N\) be smooth projective and let \(X_H\) be a
hyperplane section with exactly \(\delta\) ordinary double points
\(\Delta\). Assume the nodes impose independent conditions:

\[
 H^1(I_{\Delta,X}(1))=0.
\]

Di Gennaro and Franco, Theorem 3.2, prove that in every sufficiently small
ball \(B\) about \(H\) in the dual projective space:

1. \(B\cap X^\vee\) is a normal-crossing divisor with \(\delta\) branches;
2. for each \(r\le\delta\), the locus of sections with exactly \(r\) nodes is
   nonempty, smooth, and pure of dimension \(N-r\).

Consequently, the \(\delta\) nodes can be smoothed independently, and the
simultaneous nodal member is an actual algebraic collision point for the
corresponding meridians.

Let \(V=R^{2n-1}\pi_*\mathbf Q\) on the smooth hyperplane locus. Theorem 4.3
computes the local intersection complex on a connected component \(C\) of
the \(\delta\)-node stratum. In the paper's shifted notation it is
concentrated in degrees zero and one, and there is an exact sequence of local
systems

\[
 0\longrightarrow
 \mathcal H^1(IC(V)[-N])|_C
 \longrightarrow R^{2n}\pi_*\mathbf Q|_C
 \longrightarrow \mathbf Q^{h^{2n-2}(X)}
 \longrightarrow0.
\]

Corollary 4.5 identifies the degree-one term with the primitive degree-\(2n\)
piece of \(H^{2n}(X_H,\mathbf Q)\). Hence, for a primitive Hodge class, its
restriction to \(X_H\) coincides with its local Green-Griffiths invariant in
this model. When \(X\) is projective space, Remark 4.6 identifies the
dimension of the degree-one term with the classical nodal defect.

## Consequence for G007/G008

The independent-node hypothesis supplies the missing local collision
geometry and computes its possible detection channel. It does not construct
\(H\) from a specified \(\zeta\), does not show that the degree-one term is
nonzero, and does not show that \(\zeta\) maps nontrivially when the term is
nonzero. Selecting such an \(H\) remains the class-specific, terminal-
equivalent obligation.
