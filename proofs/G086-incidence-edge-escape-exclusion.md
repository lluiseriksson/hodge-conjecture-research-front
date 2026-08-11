---
brick_id: G086
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X and its universal hyperplane families for powers mL
smoothness: X is smooth; the universal family is smooth away from its discriminant
projectivity: X and every parameter space P_m are projective
dimension: dim_C X=2n; hyperplane fibers have dimension 2n-1; dim P_m=d_m
codimension: middle cycle codimension n; local support has parameter codimension at least two
coefficient_field: Q
cohomology_theory: singular and intersection cohomology, the hypercohomology edge sequence, polarizable Hodge modules, and universal-incidence pullback
hodge_type: primitive rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007, B012, B128-B132, G008, G087-G088, NG103-NG105, S024, S037, S053-S054
claim: For every nonzero primitive rational Hodge class zeta, for some sufficiently high m the canonical incidence class s_m(zeta) does not lie in the escape image H^1(P_m,H^(-d_m)K_m) inside IH^1(P_m,K_m), where K_m=IC(R^(2n-1)pi_(m,*)Q(n)).
falsifier: an arbitrary smooth projective complex 2n-fold and nonzero primitive rational Hodge class whose incidence class lies in the escape image for every sufficiently high m
---

# G086 — Exclude incidence classes from the escape row

**Status:** EXPLORATORY — active operational form of G008, not a smaller
terminal reduction

For

\[
 K_m=IC_{P_m}(R^{2n-1}\pi_{m,*}\mathbf Q(n)),
\]

B128 gives an edge map

\[
 e_m:IH^1(P_m,K_m)\longrightarrow
 H^0(P_m,\mathcal H^{-d_m+1}K_m).
\]

Prove, without an algebraic representative of \(\zeta\), that for some
sufficiently high \(m\),

\[
 \boxed{s_m(\zeta)\notin
 \operatorname{im}H^1(P_m,\mathcal H^{-d_m}K_m)}.
\]

Equivalently, prove \(e_m(s_m(\zeta))\ne0\). Its nonzero stalk is the G008
support point.

## Attempt audit

1. **Projective base:** insufficient. B129 constructs the same global/local
   separation on every \(\mathbf P^d\).
2. **Purity, polarizability, geometric origin, and hard Lefschetz:**
   insufficient. B129 satisfies all of them.
3. **Rational type \((0,0)\):** insufficient. The B129 escape class is a
   rational \((0,0)\) tensor.
4. **Universal incidence origin:** not yet discharged. The surviving datum is
   that \(s_m(\zeta)\) is the canonical \([q_m^*\zeta]_{00}\) component for
   the universal hyperplane incidence, not an arbitrary \(IH^1\) Hodge
   class.
5. **Nori connectivity and the primitive Higgs class:** insufficient.
   B130/NG104 show that Brogan's incidence-specific
   \(\mathcal H^{-d+1}\operatorname{gr}_F\operatorname{DR}(M)\) class can
   be nonzero while \(\mathcal H^{-d+1}\operatorname{DR}(M)\) is zero on
   the smooth locus. The source also leaves the Leray-map identification
   unchecked. B131-B132 now solve that identification canonically on full
   projective \(P\); NG105 closes the smooth-open comparison.
6. **Canonical projective filtered realization:** still insufficient.
   B131 proves the rational first-Leray transgression is nonzero, and B132
   canonically realizes \(s_m(\zeta)\) as the nonzero projective filtered
   section \(h_m(\zeta)\). NG105 removes the noncanonical smooth-open map
   comparison. The sole remaining issue is G088: the specified section may
   still be killed by filtered differentials at every boundary stalk.

Thus the next proof must calculate the composite

\[
 H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))^{(0,0)}
 \xrightarrow{\;[q_m^*(-)]_{00}\;}
 IH^1(P_m,K_m)
 \longrightarrow
 IH^1(P_m,K_m)/H^1(P_m,\mathcal H^{-d_m}K_m)
\]

and prove that a specified nonzero class survives for some \(m\). B128 shows
that this is exactly G008, so G086 must not be counted as partial closure of
HC.
