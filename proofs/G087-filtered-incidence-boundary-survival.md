---
brick_id: G087
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2r-fold X with r at least 2 and its universal sufficiently high hyperplane family
smoothness: X smooth; coefficient variation smooth on P_sm; target point lies on the discriminant
projectivity: X and P are projective
dimension: dim_C X=2r; hyperplane fibers dimension 2r-1; dim P=d
codimension: middle codimension r on X; sought boundary support has parameter codimension at least two
coefficient_field: Q with complexification for filtered de Rham calculations
cohomology_theory: rational intersection cohomology, mixed Hodge modules, filtered D-modules, de Rham/Higgs spectral sequences, and universal-incidence Leray filtration
hodge_type: primitive rational type (r,r), normalized to (0,0) after Q(r)
cycle_class_map: CH^r(X)_Q -> H^(2r)(X,Q(r)); no algebraic representative may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B012, B026-B027, B128-B134, G008, G086, G088, NG103-NG107, S009, S021-S024, S037, S053-S054
claim: For every nonzero primitive rational Hodge class zeta, its canonical incidence class has the nonzero projective filtered realization h_m(zeta) of B132, and for some sufficiently high power that specified section survives at a discriminant stalk to a nonzero rational class in H^(-d+1)(IC(V))_p.
falsifier: a smooth projective complex 2r-fold and nonzero primitive rational Hodge class for which the canonical map identification fails or every corresponding Higgs class is killed at every discriminant stalk for all high powers
---

# G087 — Filtered incidence boundary survival

**Status:** EXPLORATORY — incidence-specific sufficient mechanism for G086

Let \(M_m\) be the minimal-extension Hodge module of the high-power
vanishing-cohomology variation. B130 supplies the primitive Hodge component

\[
 H^{r,r}_{\rm prim}(X)\otimes\mathcal O_{P_m}
 \simeq
 \mathcal H^{-d_m+1}\operatorname{gr}^{F}_{-r}
 \operatorname{DR}(M_m).
\]

For a specified rational \(0\ne\zeta\), the two original obligations were:

1. **Map identification.** The section corresponding to \(\zeta\) is the
   filtered de Rham realization of the canonical incidence component
   \(s_m(\zeta)=[q_m^*\zeta]_{00}\), not merely an abstract primitive summand.
2. **Boundary survival.** At some discriminant point \(p\), that section is
   not killed in the filtered stalk spectral sequence and gives

   \[
   0\ne s_m(\zeta)_p\in
   \mathcal H^{-d_m+1}(IC(V_m))_p.
   \]

## First obligation discharged

B131 proves the canonical rational first-Leray transgression is nonzero.
B132 works on the full projective parameter space, applies projective
strictness to the already-canonical class \(s_m(\zeta)\), and constructs its
nonzero section \(h_m(\zeta)\). This avoids any need to equate the canonical
map with a source-labelled map obtained from a noncanonical decomposition
splitting. NG105 records why the smooth-open proof cannot supply that
comparison.

The remaining boundary-survival obligation is now G088. The rational
structure, Tate twist, and strict support must be checked after the complex
filtered stalk calculation. Survival gives G086 by B128 and hence G008.

## Falsifiable failure modes

- the relevant filtered differential kills the section at every boundary
  stalk;
- a complex survivor does not lie in the rational realization;
- the survivor belongs to a different strict-support component.

On \(P_m^{\rm sm}\), B130 proves that cancellation is mandatory. Therefore a
proof must calculate how the minimal extension changes the filtered
differentials at the discriminant; smooth-locus connectivity and projective
global strictness alone cannot close G087/G088.
