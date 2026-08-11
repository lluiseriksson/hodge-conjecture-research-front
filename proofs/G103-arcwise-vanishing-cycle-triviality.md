---
brick_id: G103
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a nonzero primitive rational middle Hodge class zeta, and the full hyperplane family restricted to a basis-node germ
smoothness: X and the basis germ are smooth; the central hyperplane has exactly N ordinary double points; every nearby singularity must stay in the tracked Morse charts
projectivity: the family is the restriction of the full projective complete linear system
dimension: hyperplane dimension 2n-1; N tracked nodes; value rank R<N; analytic test arcs have dimension one
codimension: the basis germ has codimension R; zero arcwise specialization cones force all N-R extra branches to contain it
coefficient_field: Q for nearby and vanishing cycles and for zeta; C for analytic arcs
cohomology_theory: rational nearby and vanishing cycles, proper base change, Saito mixed Hodge modules, local intersection cohomology, and rational Betti cohomology
hodge_type: the retained local relation functional must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of zeta may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B134-B162, G090-G102, and NG118-NG128
claim: Construct carrier-free full-linear-system nodal data and a basis-node germ such that the relative vanishing-cycle complex is zero after pullback to every analytic arc in that germ, with exhaustive tracked-Morse singularity control, while retaining the superlinear uniform matroid, positive adjoint defect, nonzero primitive ambient image, rational type, and nonzero specified Saito pairing.
falsifier: one arc with a nonzero disappearing-node vanishing cycle, an untracked singularity, loss of full-linear-system scope, zero adjoint or ambient rank, or zero specified pairing
---

# G103 — Kill every arcwise node-escape vanishing cycle

B162 makes the Euler-rigidity part of G102 equivalent to the
sheaf-theoretic condition

\[
 \Phi_\gamma=0
 \qquad
 \text{for every analytic }
 \gamma:(\Delta,0)\to(F_B,0). \tag{1}
\]

Here \(\Phi_\gamma\) is the local specialization cone of the pulled-back
projective hypersurface family. In the tracked ODP model, it is a direct sum
of one rank-one middle group for each node that escapes along \(\gamma\).

G103 asks for (1) in the **full** complete-linear-system germ, together
with:

1. B141's superlinear uniform value matroid;
2. isolated multipart nodes and exhaustive singularity control;
3. positive adjoint defect and nonzero primitive ambient image;
4. rational type \((0,0)\) and nonzero pairing with the specified
   \(\zeta\).

By analytic curve selection, (1) kills the entire escape germ, not merely
its finite jets. B158-B162 then give the factorization and saturated clean
stratum.

NG129 prevents replacing (1) by local constancy of one ambient cohomology sheaf or
one selected cohomology class. The full disappearing-node specialization
cone must vanish; the specified detector must simultaneously remain
nonzero in its distinct relation channel.
