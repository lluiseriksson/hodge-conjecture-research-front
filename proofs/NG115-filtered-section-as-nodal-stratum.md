---
brick_id: NG115
status: NO-GO
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X and its universal high-power hyperplane parameter space P_m
smoothness: X is smooth; no nodal stratum is produced by the attempted route
projectivity: X and P_m are projective
dimension: dim_C X=2n with n at least 2; dim P_m=d_m
codimension: the desired support has codimension at least two, while the nonzero filtered section has empty zero locus
coefficient_field: Q for the canonical incidence class, complexified for the filtered D-module section
cohomology_theory: rational intersection cohomology, filtered D-modules, the filtered stalk spectral sequence, and the B128 local-to-global edge map
hodge_type: primitive rational type (n,n), normalized to (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B128-B132, G008, G086, G088, G090, and NG103
claim: The nonzero canonical filtered section h_m(zeta) can be treated as an equation whose zero or support locus supplies G090's smooth saturated nodal stratum.
falsifier: B132 identifies h_m(zeta) with a constant nonzero section, while B128-B130 and NG103 allow complete cancellation in every ordinary local target
---

# NG115 — The filtered incidence section is not a nodal-stratum equation

**Status:** NO-GO

- **Route:** take B132's canonical nonzero filtered section
  \(h_m(\zeta)\), define a geometric locus from it, and use that locus as
  G090's saturated simultaneous-node germ.
- **Valid input:** \(h_m(\zeta)\) is canonically constructed on the full
  projective parameter space from the universal incidence class, without an
  algebraic representative of \(\zeta\).
- **Invalid inference:** its zero locus or ordinary support is an
  unconditionally nonempty smooth nodal stratum of the required
  codimension.
- **Precise obstruction:** B132 identifies the target sheaf with

  \[
  H_{\mathrm{prim}}^{n,n}(X)\otimes\mathcal O_{P_m}
  \]

  and \(h_m(\zeta)\) with the constant nonzero section \(\zeta\). Its zero
  locus is empty. The relevant ordinary support is not the support of this
  coherent section; it is the locus where the section survives the filtered
  stalk differentials to
  \(\mathcal H^{-d_m+1}(IC(V_m))\). G088 asks precisely for one such
  survivor. B129/NG103 show that global nonzero Hodge data with the full
  formal package can have zero local target everywhere.
- **Further gap:** even a proved survivor would give a support point, not a
  smooth codimension-\(R\) germ contained in all branches, a uniform
  smoothing matroid, or isolated nodality.
- **Re-entry condition:** use the specific universal-hyperplane incidence
  geometry to construct an actual simultaneous-node stratum and verify its
  codimension and conormal matroid before applying B144. Do not define the
  stratum by the terminal-equivalent survival condition itself.
