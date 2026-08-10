---
brick_id: G077
status: EXPLORATORY
base_field: C with collision and Hodge data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified primitive rational Hodge class zeta, its selected B058 detector, and an actual projective collision on the original plane-net base
smoothness: X and generic hyperplane fibers smooth; collision target singular; proper pushdown stratified by the discriminant
projectivity: X, high-power hyperplane family, plane net, collision, and pushdown projective
dimension: dim_C X = 2n; hyperplane fibers dimension 2n-1; plane base dimension 2
codimension: middle codimension n; competing proper support is a discriminant divisor in the plane base
coefficient_field: Q
cohomology_theory: original nearby and special mixed Hodge-module stalks, canonical perverse filtration, strict-support decomposition inside pH^0, divisor-support restriction, and full-support projection
hodge_type: selected relevant-grade class and its full-support component rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B057-B059, B077-B081, B083-B084, B110-B118, G043-G048, G076, G078-G080, NG054-NG060, NG086-NG094, S022, S037, S051-S052
claim: Construct G076's collision-certified ordinary lift beta, prove its E_infinity^(-1,0) class is nonzero, compute its strict-support decomposition inside pH^0, and prove every discriminant-divisor-supported coordinate is zero; the remaining full-support coordinate is then nonzero.
falsifier: undefined lift or grade, zero relevant-grade class, a nonzero divisor-supported coordinate, confinement to point support, wrong rational Hodge type, or zero residual full-support component
---

# G077 — Exclude divisor support for the selected specialization

**Status:** EXPLORATORY  
**Parent gate:** G076

After constructing the selected ordinary lift (eta), take its canonical
class in

\[
 E_\infty^{-1,0}(K,H).
\]

B080-B081 show that point support lies in the separate
(E_\infty^{0,-1}) grade, while full support and discriminant-divisor support
can both occur in (E_\infty^{-1,0}). Inside the canonical strict-support
decomposition of ({}^pH^0(K)), compute

\[
 [\beta]_{-1,0}
 =\beta_{\mathrm{fs}}+
   \sum_D\beta_D
\]

and prove

\[
 [\beta]_{-1,0}\ne0,
 \qquad
 \beta_D=0\quad\text{for every discriminant divisor }D.
\]

Then (eta_{\mathrm{fs}}\ne0), closing G076's landing condition. The proof
must compute the class coordinates or supply a theorem whose hypotheses hold
for this hyperplane family. B115/NG091 exclude importing Ngô's weak-abelian
support theorem. B116/NG092 also exclude using B008's vanishing at a smooth
discriminant point: that vanishing concerns the full-support intermediate
extension, not the divisor-supported strict-support summand. G078 is the
explicit transverse-disk calculation; B117 now executes its support part for
the original incidence pushdown.

G077 is the selected-class form of the divisor/full-support separation in
G045-G046. It is not counted as an independent reduction. B022 survival and
the final pairing remain downstream.

## Resolution of the divisor clause

B117 proves more than classwise vanishing for the original incidence
pushdown: its ${}^pH^0$ has no divisor strict support at all. The proof uses
both parts of S052's Lefschetz calculation. NG093 records the shift error in
using only the middle direct image. Thus the equations $\beta_D=0$ are now
structural for the original pushdown. The point grade also vanishes by B118,
but B121/NG097 correct the earlier conclusion: a nonzero ordinary lift may
still lie in the constant ambient $E_\infty^{-2,1}$ grade. B123/NG099 close
that filtered-lift route. G065 must construct the relation coordinate
directly as a marked relative boundary; then its divisor coordinates vanish
structurally by B117.
