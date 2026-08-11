---
brick_id: G101
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a nonzero primitive rational middle Hodge class zeta, and the full ordered-node discriminant germ in a complete linear system
smoothness: X is smooth; the selected hypersurface has isolated ordinary double points; every basis-node germ is smooth by the uniform value matroid
projectivity: the ambient deformation is the full projective complete linear system, not a nonlinear analytic pullback
dimension: N ordered nodes; value rank R<N; a basis-node persistence germ has codimension R
codimension: the R basis branches cut a smooth codimension-R germ that must be contained in all N-R remaining branches
coefficient_field: C for analytic discriminant branches; Q for zeta, vanishing cycles, and the terminal pairing
cohomology_theory: analytic discriminant incidence, rational vanishing-cycle homology, Saito local intersection cohomology, and rational Betti cohomology
hodge_type: the retained relation functional must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of zeta may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B134-B159, G090-G100, and NG118-NG126
claim: Construct carrier-free full-linear-system nodal data and a basis B of the uniform value matroid such that every remaining labeled node persists identically along the smooth basis-node germ F_B, while retaining the superlinear node count, positive adjoint defect, nonzero primitive ambient image, rational type, and nonzero specified Saito pairing.
falsifier: one escaping node on F_B, reliance on a nonlinear pullback rather than the full linear system, loss of the uniform matroid or isolated nodes, zero adjoint or ambient rank, or zero specified pairing
---

# G101 — Force all nodes to persist along one basis-node germ

Choose \(R\) labeled branches with independent critical-value
differentials and let

\[
 F_B=\bigcap_{b\in B}\{\tau_b=0\}.
\]

B158 proves that the analytic factorization part of G100 is exactly the
geometric statement

\[
 F_B\subseteq\{\tau_i=0\}
 \qquad\text{for every }i\notin B. \tag{1}
\]

Thus G101 asks for a carrier-free construction of (1) in the **full**
complete-linear-system germ, while retaining:

1. B141's superlinear uniform value matroid;
2. isolated multipart ordinary double points;
3. positive adjoint defect and nonzero primitive ambient image;
4. rational type \((0,0)\) and nonzero pairing with the specified
   \(\zeta\).

Once (1) is proved, the Hadamard formula in B158 gives the analytic
syzygies, B156 kills \(H_\tau\), and B144 supplies the saturated clean
arrangement. No separate infinite Kuranishi calculation remains.

B159 shows that neither the uniform matroid nor any finite jet
strengthening proves (1). The missing mechanism must constrain the entire
global incidence germ and must do so without installing an algebraic
carrier for \(\zeta\).
