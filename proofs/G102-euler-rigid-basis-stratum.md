---
brick_id: G102
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a nonzero primitive rational middle Hodge class zeta, and the full hyperplane family restricted to a basis-node germ
smoothness: X is smooth; the central hyperplane has exactly N isolated ordinary double points; all nearby singularities must remain in the N tracked Morse charts
projectivity: the hypersurface family is the restriction of the full projective complete linear system
dimension: hyperplane-section dimension 2n-1; N tracked nodes; value rank R<N; basis germ codimension R
codimension: Euler rigidity on the basis germ must force all N-R extra node branches to contain it
coefficient_field: Z for Euler characteristics and Q for zeta, vanishing cycles, and the terminal pairing
cohomology_theory: proper hypersurface topology, Milnor fibers, rational vanishing-cycle homology, Saito local intersection cohomology, and rational Betti cohomology
hodge_type: the retained relation functional must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of zeta may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B134-B161, G090-G101, and NG118-NG127
claim: Construct carrier-free full-linear-system nodal data and a basis-node germ F_B on which the topological Euler characteristic of the projective hypersurface is locally constant, with all singularities confined to the N tracked Morse charts, while retaining the superlinear uniform matroid, positive adjoint defect, nonzero primitive ambient image, rational type, and nonzero specified Saito pairing.
falsifier: variation of Euler characteristic on F_B, an untracked or worse singularity, loss of full-linear-system scope, zero adjoint or ambient rank, or zero specified pairing
---

# G102 — Construct an Euler-rigid basis-node stratum

B160 supplies a scalar global certificate for G101. On a basis-node germ
\(F_B\), prove

\[
 \chi(Y_t)=\chi(Y_0)\qquad(t\in F_B), \tag{1}
\]

and verify that every possible singularity stays inside one of the \(N\)
tracked nondegenerate critical-point charts. Then the Euler–Milnor formula
forces all \(N\) critical values to remain zero. B158-B160 yield the
all-order factorization and saturated clean node germ.

The complete G102 obligation is to construct (1) without a preselected
algebraic carrier and simultaneously retain:

1. B141's superlinear uniform value matroid;
2. isolated multipart nodes and exhaustive singularity control;
3. positive adjoint defect and nonzero primitive ambient image;
4. rational type \((0,0)\) and nonzero pairing with the specified
   \(\zeta\).

B161/NG128 show that projectivity, flatness, and constant Hilbert polynomial
do not imply (1). A successful mechanism needs topological local triviality
of the singular hypersurfaces, constancy of an equivalent vanishing-cycle
rank, or another global conservation law strong enough to fix the total
Milnor number.
