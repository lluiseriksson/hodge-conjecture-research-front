---
brick_id: G126
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with very ample H, a specified primitive rational middle Hodge class, and one full degree-m ODP incidence satisfying G125
smoothness: the ambient variety, labeled critical incidences, and basis carrier are smooth at the marked configuration; the final simultaneous-node germ must be reduced and smooth
projectivity: all equations, powers, node schemes, carrier data, and detector data come from the same degree-m full projective universal family
dimension: N nodes, value rank R<N, primitive conditional-gradient birth q_m=2n, and B185 finite certificate order D_car=E^(M+1)
codimension: kill every Kuranishi tensor kappa_2 through kappa_D_car at the same primitive birth degree m
coefficient_field: C for coherent jets, Hessian holonomy, and Kuranishi tensors; Q for the Hodge class, detector, and specified pairing
cohomology_theory: graded coherent jets, ODP Kuranishi theory, finite conormal certificates, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the retained detector must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B195, G013, G090-G125, and NG106-NG158
claim: Construct G125's primitive degree-m birth and, without changing the polarization degree or node scheme, compute B185's certificate order and prove kappa_2=...=kappa_D_car=0 while retaining every detector clause.
falsifier: moving to a higher degree, changing the node scheme without a new class-directed proof, a nonzero Kuranishi tensor within the certificate range, loss of primitive birth or holonomy, or failure of any rational detector clause
---

# G126 — Close the finite Kuranishi ladder at the birth degree

B195 shows that G125's one-node-determined holonomy is isolated at its
primitive birth degree \(m\). Raising the power while keeping \(Z\) fixed
increases the conditional-gradient rank and eventually makes it full.

Therefore the finite all-order obligation of G118 must be closed in the
same degree-\(m\) full incidence. Starting from arbitrary \((X,\zeta)\),
construct all G125 data and then:

1. build B185's labelled algebraic basis carrier for that exact incidence;
2. compute its finite certificate order
   \[
   D_{\mathrm{car}}=E^{M+1};
   \]
3. prove, on the same carrier and without polarization transport,
   \[
   \kappa_2=\kappa_3=\cdots=\kappa_{D_{\mathrm{car}}}=0; \tag{1}
   \]
4. retain the uniform/no-coloop value data, positive adjoint defect,
   nonzero primitive image, rational type-\((0,0)\), and specified nonzero
   Saito pairing.

B186 makes (1) equivalent to the finite conormal certificate and hence to
the desired all-order critical-value syzygies on the basis carrier. G125
targets only \(\kappa_2\); NG150 already proves that the cubic and later
rungs do not follow from it.

G126 is stronger than the current operational gate G125. If constructed,
it would close G118 for the selected class-directed incidence. It still
does not itself turn the resulting rational detector into an algebraic
cycle without the remaining upstream comparison steps.
