---
brick_id: G120
status: EXPLORATORY
base_field: C
variety: the full complete-linear-system ordered-node incidence of an arbitrary smooth projective complex 2n-fold with a specified primitive rational middle Hodge class
smoothness: the variety and tracked singularities are smooth/ODP; the desired rank and isotropy data must integrate to the class-directed incidence
projectivity: all node, section, value, and gradient data come from the full projective linear system
dimension: N nodes, value rank R<N, 2nN-dimensional gradient target, and required conditional-gradient rank at most nN
codimension: realize a full-support relation whose nondegenerate Hessian form contains the conditional-gradient image as a global isotropic subspace
coefficient_field: C for gradient and Hessian linear algebra; Q for the specified Hodge class, relation channel, and detector
cohomology_theory: ODP deformation theory, coherent first-jet evaluation, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the retained detector relation must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input Hodge class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B187, G013, G090-G119, NG106-NG151
claim: Construct from arbitrary (X,zeta) a full-incidence ordered ODP configuration with no-coloop value matroid and a full-support relation c such that the conditional-gradient image has rank at most nN and is totally isotropic for q_c, while retaining positive adjoint defect, primitive image, rational type, and specified nonzero Saito pairing.
falsifier: conditional-gradient rank greater than nN, nonzero q_c pairing, a coloop or zero relation coordinate, loss of full-system origin, or failure of any Hodge detector clause
---

# G120 — Realize the global Lagrangian shadow of G119

B187 gives the first unavoidable linear-algebra shadow of G119. For a
no-coloop value matroid, choose a full-support relation \(c\). Any
quadratically flat excess incidence must satisfy

\[
 \operatorname{im}D\subset(G,q_c)
 \quad\text{totally isotropically},\qquad
 \operatorname{rank}D\le nN. \tag{1}
\]

G120 asks for class-directed full-incidence data satisfying (1), together
with:

1. the uniform or otherwise audited no-coloop value matroid;
2. positive adjoint defect and nonzero primitive image;
3. a rational type-\((0,0)\) local relation channel;
4. nonzero specified pairing with \(\zeta\).

This is weaker than G119: it imposes isotropy only for one full-support
relation, whereas \(\kappa_2=0\) requires every relation. It is therefore a
necessary precursor, not a replacement.

The full-support \(c\) is a complex value relation used for the Hessian
rank bound. It is not automatically the rational vanishing-cycle relation
in items 3-4; the two channels must be constructed and compared without a
coefficient-field substitution.

NG151 prevents strengthening (1) to a nodewise split Lagrangian core
without additional geometry. A global maximal \(q_c\)-isotropic subspace
may mix all nodal blocks.
