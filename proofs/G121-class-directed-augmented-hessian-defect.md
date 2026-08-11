---
brick_id: G121
status: EXPLORATORY
base_field: C
variety: the full complete-linear-system ordered-node incidence of an arbitrary smooth projective complex 2n-fold with a specified primitive rational middle Hodge class
smoothness: the variety and tracked singularities are smooth/ODP; no excess smoothness is assumed
projectivity: every value, gradient, Hessian, and node datum comes from the full projective universal family
dimension: N-dimensional value target; value rank R<N; conditional-gradient image U; augmented map A_U of rank at most N-1
codimension: construct a nonzero no-coloop annihilator L_U of the augmented Hessian-value span
coefficient_field: C for the augmented defect and isotropic relation; Q for the specified Hodge class and detector channel
cohomology_theory: ODP second-order deformation theory, coherent jet evaluation, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the retained detector relation must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input Hodge class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B188, G013, G090-G120, NG106-NG152
claim: Construct from arbitrary (X,zeta) full-incidence ordered ODP data for which the augmented Hessian-value map A_U has rank less than N and its annihilator L_U has no identically zero coordinate, while retaining positive adjoint defect, nonzero primitive image, rational type, and specified nonzero Saito pairing.
falsifier: full augmented rank, a zero annihilator, a coordinate vanishing identically on L_U, use of non-full-system data, or failure of any Hodge detector clause
---

# G121 — Construct the augmented Hessian-value defect

B188 converts G120 into one finite rank condition. For the actual
conditional-gradient image \(U\), construct

\[
 A_U:
 \operatorname{im}E\oplus\operatorname{Sym}^2U
 \longrightarrow\mathcal T
\]

such that

\[
 \operatorname{rank}A_U<N, \tag{1}
\]

and such that no coordinate vanishes identically on

\[
 L_U=\ker A_U^*. \tag{2}
\]

Equations (1)-(2) produce a complex full-support relation \(c\) for which
\(U\) is \(q_c\)-isotropic. They are equivalent to G120's global
Lagrangian condition, but are directly falsifiable by a finite matrix
calculation.

The construction must also retain positive adjoint defect, nonzero
primitive image, a rational type-\((0,0)\) detector channel, and nonzero
specified pairing with \(\zeta\). The complex relation in (2) and the
rational detector are separate until a comparison is proved.

G121 remains weaker than G119: it produces one isotropic relation, not
vanishing of the full quadratic Kuranishi tensor for every relation. B189
forces an all-node isolated-jet defect in every candidate. B190/G122 give a
stronger sufficient attack by conformally synchronizing the full gradient
image; NG153 excludes obtaining it by restricting a high-power full system
to a chosen small family.
