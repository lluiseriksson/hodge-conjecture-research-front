---
brick_id: G112
status: EXPLORATORY
base_field: C
variety: the full complete-linear-system germ on an arbitrary smooth projective complex variety X, with a class-directed ordered nodal member, rank-R basis-node germ F_B, and escape ideal K_B
smoothness: X, the parameter germ, and F_B are smooth; no smoothness of the full simultaneous-node germ is assumed
projectivity: X and the universal hypersurface family are projective; the conormal morphism is analytic on F_B
dimension: parameter dimension d; basis-node dimension d-R; arbitrary N-R escape generators and arbitrary middle Hodge dimension downstream
codimension: prove the all-order conormal morphism beta_K_B is zero, forcing smooth reduced codimension-R persistence
coefficient_field: C for analytic conormal modules and connections; Q for the specified Hodge class and detector
cohomology_theory: Kähler differentials, Gauss-Manin connection, variation of Hodge structure, ODP vanishing cycles, primitive rational cohomology, and Saito pairing
hodge_type: the retained detector relation must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of the input Hodge class may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B135-B179, G013, G088-G111, NG106-NG143
claim: Use a canonical full-family geometric or connection comparison to prove the complete analytic conormal escape morphism beta_K_B vanishes identically, while retaining the uniform superlinear node matroid, positive adjoint defect, primitive ambient image, rational type (0,0), and specified nonzero Saito pairing.
falsifier: vanishing only after tensoring with the central residue field, vanishing to a fixed finite jet order, a comparison defined only on cohomology with no map to K_B/K_B^2, or loss of any detector clause
---

# G112 — Kill the all-order conormal escape defect

For the actual full-system basis-node germ, construct a canonical proof
that

\[
 \beta_{K_B}:K_B/K_B^2\longrightarrow
 \Omega^1_{F_B}\otimes\mathcal O_{F_B}/K_B
\]

vanishes as a morphism of analytic modules.

B179 proves that this is equivalent to \(K_B=0\), hence to \(H_\tau=0\)
and the G100/G109 analytic persistence clause. G112 refines G111 by naming
the exact target of any proposed Gauss--Manin, correspondence, or
incidence comparison.

The required statement is all-order. It is not enough to show:

1. \(\beta_{K_B}\otimes\mathbf C=0\) at the central point;
2. the first \(q\) jets vanish for one fixed \(q\);
3. an associated-graded or characteristic-cycle shadow vanishes;
4. a cohomological connection is flat without an intertwining map to the
   conormal module.

The same nodal configuration must still retain the superlinear uniform
matroid, positive adjoint defect, nonzero primitive ambient image, rational
type \((0,0)\), and specified nonzero pairing. No proof of the required
vanishing is currently known.
