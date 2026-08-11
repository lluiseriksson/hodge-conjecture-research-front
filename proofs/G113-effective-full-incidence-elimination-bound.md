---
brick_id: G113
status: EXPLORATORY
base_field: C
variety: the full complete-linear-system critical incidence on an arbitrary smooth projective complex variety X, with a class-directed ordered nodal member and basis-node germ F_B
smoothness: X, the parameter germ, and F_B are smooth; the critical incidence is étale over the parameter germ at each tracked ODP
projectivity: X and the universal hypersurface family are projective; all algebraic presentations must come from the full incidence, not a nonlinear special pullback
dimension: arbitrary projective dimension and polarization power; parameter dimension d; N nodes; critical-value rank R; effective degree bound D(X,L,N,B)
codimension: use a computed degree bound to reduce all-order conormal vanishing to jets through order D-1
coefficient_field: C for elimination and analytic branches; Q for the specified rational Hodge class and detector
cohomology_theory: algebraic critical incidence, étale local algebra, effective elimination, conormal modules, ODP vanishing cycles, primitive rational cohomology, and Saito pairing
hodge_type: the retained detector relation must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input Hodge class may not be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B135-B180, G013, G088-G112, NG106-NG144
claim: Produce a common étale algebraic coordinate chart on F_B and simple implicit polynomials for every escape generator with an explicit degree bound D derived from the full critical incidence; then prove the conormal defect vanishes through order D-1 and retain every detector clause.
falsifier: ramification of a claimed simple branch, an untracked increase of degree under elimination or restriction, a bound depending on an unspecified analytic coordinate change, use of a special nonlinear base, failure of a required jet, or loss of any detector clause
---

# G113 — Effective elimination bound for the full incidence

At a tracked ODP, the spatial critical equations have invertible Hessian,
so the algebraic critical incidence is étale over the parameter space at
that point. The critical value is regular on this incidence. G113 asks for
an effective version of this observation after all \(N\) branches are
placed over the smooth basis-node germ \(F_B\).

Construct:

1. a common étale algebraic coordinate chart
   \(u=(u_1,\ldots,u_{d-R})\) on \(F_B\);
2. for every nonbasis branch, a polynomial
   \(P_i(u,z)\) with
   \(P_i(u,\epsilon_{B,i}(u))=0\) and
   \(\partial_zP_i(0,0)\ne0\);
3. a computable common total-degree bound
   \(\deg P_i\le D(X,L,N,B)\), including every elimination and coordinate
   substitution cost;
4. vanishing of \(j^{D-1}\beta_{K_B}\) for the actual full-system germ.

B180 then promotes item 4 to \(\beta_{K_B}=0\), hence to \(H_\tau=0\).

The degree bound may depend on the polarization power and the complete
nodal configuration. It must be explicit enough to make the required jet
verification finite and reproducible. Any computation exceeding the local
resource policy belongs in the pinned Colab Pro+ workflow.

All uniform-matroid, adjoint-defect, primitive-image, rational-type, and
specified-pairing clauses remain attached. No such elimination bound or
jet vanishing theorem is currently proved.
