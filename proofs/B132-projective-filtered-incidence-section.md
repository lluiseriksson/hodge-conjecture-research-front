---
brick_id: B132
status: PROVED
base_field: C
variety: an arbitrary polarized smooth projective complex 2r-fold X with r at least 2 and its universal sufficiently high hyperplane incidence over the full projective parameter space P
smoothness: X is smooth; the coefficient variation is smooth on P_sm and minimally extended across the discriminant
projectivity: X and P are projective; the incidence morphism is projective
dimension: dim_C X=2r; hyperplane dimension 2r-1; dim P=d
codimension: middle codimension r on X; possible local support has parameter codimension at least two
coefficient_field: Q, complexified only for the filtered D-module calculation
cohomology_theory: rational intersection cohomology, pure Hodge modules, filtered D-modules, projective strictness, and hypercohomology
hodge_type: primitive rational type (r,r), equivalently type (0,0) after Q(r); left-D-module filtration index -r before twisting
cycle_class_map: CH^r(X)_Q -> H^(2r)(X,Q(r)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B012, B128, B130-B131, S024, S037, S053
claim: Every nonzero primitive rational Hodge class has a canonical nonzero projective filtered-de-Rham section h_m(zeta), obtained from its canonical incidence class s_m(zeta), in H^0(P,H^(-d+1)gr_F^(-r)DR(M_m)); this avoids both a noncanonical decomposition splitting and the invalid smooth-open globalization.
falsifier: failure of projective filtered direct-image strictness, a nonzero type-(r,r) incidence class with zero grade-minus-r image, or an additional hypercohomology term contributing to total degree -d+1
---

# B132 — Projective filtered realization of the incidence class

**Status:** PROVED

Let \(P=P_m\) be the full projective parameter space, let \(M_m\) be the
filtered \(D\)-module underlying the minimal-extension Hodge module of the
vanishing-cohomology variation, and let

\[
 0\ne s_m(\zeta)=[q_m^*\zeta]_{00}
 \in IH^1(P,V_{m,\mathbf Q})
\]

be the canonical global incidence class of S024/B012. If \(\zeta\) is a
primitive rational \((r,r)\) class, strict support and the canonical perverse
grade make \(s_m(\zeta)\) a rational \((r,r)\) class as well. No derived
decomposition splitting is used in this statement.

## Projective strictness

For the projective map \(P\to\mathrm{pt}\), strictness of the filtered direct
image gives

\[
 \operatorname{gr}_{-r}^F
 IH^1(P,V_{m,\mathbf C})
 \simeq
 \mathbb H^{-d+1}
 \left(P,\operatorname{gr}_{-r}^F\operatorname{DR}(M_m)\right).
\]

Consider the ordinary hypercohomology spectral sequence for the complex on
the right. In total degree \(-d+1\), a term with sheaf-cohomology degree
\(a\ge1\) uses

\[
 \mathcal H^{-d+1-a}
 \operatorname{gr}_{-r}^F\operatorname{DR}(M_m).
\]

In Brogan's indices this is \(k=(2r-1)+1-a=2r-a\). Corollary 4.1 has no
primitive summand for \(k<2r\), so all such terms vanish. The possible
outgoing differentials from \(a=0\) land in the same vanishing range. Hence
the edge morphism is an isomorphism

\[
 \mathbb H^{-d+1}
 \left(P,\operatorname{gr}_{-r}^F\operatorname{DR}(M_m)\right)
 \xrightarrow{\sim}
 H^0\!\left(P,
 \mathcal H^{-d+1}\operatorname{gr}_{-r}^F\operatorname{DR}(M_m)
 \right).
\]

Brogan Corollary 4.1 computes the target sheaf as

\[
 H^{r,r}_{\rm prim}(X)\otimes\mathcal O_P.
\]

Because \(P\) is projective and connected, \(H^0(P,\mathcal O_P)=\mathbf C\).
The type-\((r,r)\) class \(s_m(\zeta)\) therefore has a canonical, nonzero
image

\[
 h_m(\zeta)\in
 H^0\!\left(P,
 \mathcal H^{-d+1}\operatorname{gr}_{-r}^F\operatorname{DR}(M_m)
 \right).
\]

This \(h_m(\zeta)\), rather than a vector labelled using a chosen
decomposition-theorem splitting, is the correctly typed primitive Higgs
section attached to the specified rational incidence class.

## What remains

The section \(h_m(\zeta)\) is nonzero in every associated-graded stalk, but
B130 shows that it is cancelled in ordinary de Rham cohomology on
\(P^{\rm sm}\). B132 does not prevent the same cancellation at all boundary
stalks. G088 is the exact residual theorem: prove that at some discriminant
point the canonical section survives to the rational ordinary IC stalk.
