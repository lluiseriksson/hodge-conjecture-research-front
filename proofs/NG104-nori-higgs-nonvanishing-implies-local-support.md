---
brick_id: NG104
status: NO-GO
base_field: C
variety: arbitrary smooth projective complex 2r-folds with r at least 2 and their universal high-power hyperplane families
smoothness: ambient variety smooth; comparison first occurs over the smooth parameter locus
projectivity: ambient and full parameter space projective
dimension: ambient dimension 2r; hyperplane dimension 2r-1; parameter dimension d
codimension: middle codimension r; desired local support codimension at least two
coefficient_field: Q, complexified for filtered de Rham theory
cohomology_theory: Nori relative connectivity, filtered regular holonomic D-modules, Higgs and de Rham complexes, and rational intersection cohomology
hodge_type: primitive rational type (r,r), normalized to (0,0)
cycle_class_map: CH^r(X)_Q -> H^(2r)(X,Q(r))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B012, B128-B130, G086-G087, S053
claim: Nori connectivity and nonvanishing of Brogan's primitive Hodge component in H^(-d+1)gr_F DR(M) automatically produce a nonzero class in H^(-d+1)DR(M), hence a local Green-Griffiths singularity.
falsifier: vanishing of H^(-d+1)DR(M) on P_sm while the corresponding Higgs-graded cohomology sheaf is nonzero
---

# NG104 — Nori-Brogan Higgs nonvanishing is not local support

**Status:** NO-GO

- **Route:** use Nori connectivity and Brogan Corollary 4.1 to obtain the
  primitive \((r,r)\) class in
  \(\mathcal H^{-d+1}\operatorname{gr}_F^{-r}\operatorname{DR}(M)\), then
  read it as a nonzero local Betti class.
- **Valid input:** B130 verifies the indices and the primitive Higgs-graded
  class for every \(r\ge2\) and sufficiently high power.
- **Invalid inference:** cohomology of the associated graded filtered de
  Rham complex equals the associated graded of ordinary de Rham cohomology.
- **Precise obstruction:** on \(P^{\rm sm}\),
  \(\operatorname{DR}(M)\simeq V_{\mathbf C}[d]\), so
  \(\mathcal H^{-d+1}\operatorname{DR}(M)=0\), while Brogan's
  \(\mathcal H^{-d+1}\operatorname{gr}_F^{-r}\operatorname{DR}(M)\) can be
  the nonzero bundle \(H^{r,r}_{\rm prim}(X)\otimes\mathcal O\). Filtered
  differentials cancel the Higgs class. Brogan p. 14 also leaves the
  incidence-map identification unchecked.
- **Re-entry condition:** prove G087: identify the canonical incidence
  section and show that its cancellation fails at at least one discriminant
  stalk, with rational realization and strict support verified.
