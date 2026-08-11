---
brick_id: B009
status: PROVED
base_field: C
variety: a local family of odd-dimensional hyperplane sections of a smooth projective 2n-fold, with a central fiber having finitely many ordinary double points and a quasi-local-normal-crossing discriminant model
smoothness: ambient X and nearby fibers smooth; central fiber nodal; local discriminant branches satisfy the stated transversality/independent-smoothing hypotheses
projectivity: ambient X projective and hyperplane family projective
dimension: dim X = 2n and dim X_s = 2n-1
codimension: middle codimension n on X
coefficient_field: Q
cohomology_theory: singular homology/cohomology, Picard-Lefschetz vanishing cycles, the local monodromy complex B^bullet, and local intersection cohomology
hodge_type: the input class is primitive (n,n); the channel statement itself is topological
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n)); no surjectivity is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: Green-Griffiths Section 4.2.3 and 4.2.4 (S021); BFNP Theorem 2.11 (S009); Saito equations (0.3)-(0.4) and Proposition 1.7 (S022); B134
claim: In the stated transverse nodal local model, the degree-one cohomological monodromy/intersection-cohomology channel is canonically dual to the Q-vector space of relations among the nodal vanishing cycles; a polarized coefficient-kernel model has the same rank and Tate type.
falsifier: a family satisfying the stated local hypotheses for which the degree-one cohomological channel is not canonically dual to the rational relation space, or their dimensions differ
---

# B009 - Nodal relation channel

Let \(X_{s_0}\) be a hyperplane section with ordinary double points
\(p_1,\ldots,p_r\). Assume locally that the nodes can be independently
smoothed and that the discriminant has the quasi-local-normal-crossing model
used in Green-Griffiths Section 4.1.1. Let

\[
 \delta_i\in H_{2n-1}(X_s,\mathbf Q)
\]

be the vanishing cycle of \(p_i\) in a nearby smooth fiber. In the elementary
normal-crossing case, the local monodromy complex has

\[
 B^0=V,\qquad B^1=\bigoplus_i N_iV,
\]

with its Koszul boundary. Green-Griffiths Section 4.2.4 computes the
homological relation model

\[
 H^1(B^\bullet)\simeq
 \ker\!\left(\mathbf Q^r\longrightarrow H_{2n-1}(X_s,\mathbf Q),
 (a_i)\longmapsto\sum_i a_i\delta_i\right).
\]

Their more general local statement permits a partition \(I=J\sqcup K\) for
which the nodes in each part are independent and obtains the same relation
space. Section 4.2.3 identifies this monodromy cohomology with the relevant
local intersection-cohomology channel under the local/quasi-local
normal-crossing hypotheses. Intrinsically, Saito equations (0.3)-(0.4) give

\[
 \mathcal H^{-d+1}(IC(V))_p\simeq R(Y_p)^\vee.
\]

The kernel displayed above is therefore the polarized homological model (or
dual) of the cohomological stalk. B134 fixes this convention at class level.

## Detection consequence

If the vanishing cycles are rationally independent, the relation space and
its dual channel are zero and no normal-function singularity can occur
through it. If relations exist, the target is merely nonzero: detection of a
specified class \(\zeta\) additionally requires its dual functional to
evaluate nontrivially on some relation.
The latter does not follow from the dimension of the relation space.

## Scope guard

This computation is local and conditional on the explicit nodal
transversality model. It is not asserted for arbitrary singularities or an
arbitrary non-normal-crossing germ. It constructs the possible receptacle for
a singularity, not an algebraic cycle representing \(\zeta\).
