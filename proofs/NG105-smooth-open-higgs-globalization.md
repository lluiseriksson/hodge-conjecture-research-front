---
brick_id: NG105
status: NO-GO
base_field: C
variety: an arbitrary polarized smooth projective complex 2r-fold and its universal high-power smooth hyperplane family over P_sm
smoothness: X and the family over P_sm are smooth
projectivity: X and the fibers are projective, but P_sm is the nonproper complement of the discriminant in projective P
dimension: dim_C X=2r with r at least 2; dim P=d
codimension: middle codimension r on X
coefficient_field: Q, complexified for filtered de Rham theory
cohomology_theory: Leray and Hodge-to-de-Rham spectral sequences, filtered D-modules, and decomposition-theorem splittings
hodge_type: primitive type (r,r), or (0,0) after Q(r)
cycle_class_map: CH^r(X)_Q -> H^(2r)(X,Q(r)); no cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B081, B130-B132, S037, S053
claim: One may identify the specified incidence class with Brogan's Higgs section by using the smooth-open Corollary 5.2 calculation or by choosing an arbitrary decomposition-theorem splitting.
falsifier: nonproper failure of the required filtered strictness, nonconstant global regular functions on P_sm, or dependence of the source-labelled map on the chosen derived splitting
---

# NG105 — Smooth-open Higgs globalization is not the comparison map

**Status:** NO-GO

- **Route:** use Brogan Corollary 5.2 on \(P^{\rm sm}\), or a chosen
  decomposition-theorem splitting, to declare that the primitive Higgs
  vector labelled by \(\zeta\) is the filtered realization of
  \(s_m(\zeta)\).
- **Valid input:** Corollary 4.1 computes on the full \(P\)
  
  \[
  \mathcal H^{-d+1}\operatorname{gr}_{-r}^F\operatorname{DR}(M)
  \simeq H^{r,r}_{\rm prim}(X)\otimes\mathcal O_P.
  \]

  The later Leray construction on \(P^{\rm sm}\) is canonical.
- **Invalid inference:** filtered hypercohomology on the nonproper smooth
  locus can be interchanged with hypercohomology of the associated graded,
  and its \(H^0\) is just the finite-dimensional primitive space.
- **Precise obstruction:** if the discriminant is the hypersurface
  \(F=0\), then for a homogeneous \(G\) of degree \(\deg F\) not proportional
  to \(F\), the ratio \(G/F\) is a nonconstant regular function on
  \(P\setminus V(F)\). Thus

  \[
  H^0(P^{\rm sm},H^{r,r}_{\rm prim}\otimes\mathcal O)
  \ne H^{r,r}_{\rm prim}
  \]

  in general. The displayed step from global sections of the Higgs sheaf to
  the finite primitive space in the proof of Corollary 5.2 is therefore not
  valid on \(P^{\rm sm}\). The filtered differentials may cancel these extra
  sections, exactly as B130 requires locally. Separately, B081/S037 show that
  the derived decomposition splitting is noncanonical; choosing one cannot
  label the image of a specified rational class invariantly.
- **Re-entry condition:** work on the full projective parameter space and
  start with the canonical class \(s_m(\zeta)\). Projective strictness and the
  canonical hypercohomology edge give its nonzero filtered realization in
  B132. The remaining issue is G088 boundary survival, not map labelling.

NG105 does not assert that the topological nonvanishing statement intended
by Corollary 5.2 is false; B131 proves the relevant rational first-Leray
nonvanishing independently. It rejects only the smooth-open filtered proof
and the arbitrary-splitting identification.
