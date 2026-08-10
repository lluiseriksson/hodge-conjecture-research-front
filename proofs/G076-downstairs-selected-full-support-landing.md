---
brick_id: G076
status: EXPLORATORY
base_field: C with original collision and Hodge data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified nonzero primitive rational Hodge class zeta, its selected B058 detector, and an actual projective plane-net collision on the original base
smoothness: X and generic hyperplane fibers smooth; collision target singular; proper comparison model used only to define the original pushdown
projectivity: X, hyperplane family, plane net, collision, and proper pushdown projective
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; plane base dimension 2
codimension: middle codimension n; collision support positive base codimension
coefficient_field: Q
cohomology_theory: selected relative thimble chains, original nearby and special mixed Hodge-module stalks, canonical perverse filtration, strict support, and full-support projection
hodge_type: selected specialization and its full-support coordinate rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B057-B059, B077, B081-B084, B110-B118, G043, G047-G048, G073-G080, NG053-NG060, NG086-NG094, S022, S037, S052
claim: Construct on the original base a collision-certified nearby class and ordinary special lift for the selected B058 detector, and prove that its canonical relevant perverse-grade projection to the full-support strict-support summand is nonzero before the B022 quotient and pairing tests.
falsifier: undefined original specialization, nonzero vanishing-cycle obstruction, absence of an ordinary lift, confinement to the point grade or divisor/proper-support summand, zero full-support projection, or wrong rational Hodge type
---

# G076 — Land the selected original specialization in full support

**Status:** EXPLORATORY  
**Parent gates:** G075 / G074

Construct the selected nearby class (t_\psi) and ordinary special lift
(eta) on the original collision object, not first on the root cover.
Using B081's canonical perverse filtration and the strict-support
decomposition inside the relevant perverse cohomology object, prove

\[
 \operatorname{pr}_{\mathrm{fs}}
 [\beta]_{E_\infty^{-1,0}}\ne0.
\]

The proof must include the collision certificate linking (eta) to the
selected B057 chain. An ambient primitive class alone is inadmissible by
B110, and a chosen total decomposition splitting is inadmissible by NG058.

B114 then transports this established coordinate isomorphically to G075's
invariant covered full-support coordinate. It cannot be transported in the
opposite logical direction to manufacture nonvanishing.

B115/NG091 exclude Ngô's support theorem for this universal high-power
hyperplane family. B117 closes the divisor-support ambiguity by a mechanism
specific to the original incidence map: every generic transverse Lefschetz
slice has constant $R^{2n}$, so ${}^pH^0$ has no divisor support. G079 is
the grade parent, and B118 removes its point-grade alternative by relative
hard Lefschetz. B121/NG097 show that the constant ambient
$E_\infty^{-2,1}$ grade still competes with the relation grade. G083 is the
active subgate: construct the selected class and prove it has a lift in
$S_0$. Its nonzero relevant coordinate is then full-support by B117-B119.

## No double counting

G076 is the selected-excess/source-certified formulation of G043's original
full-support projection problem. It is not an independent reduction or a
second piece of progress. G083 incorporates the B022, filtered-lift, and
prescribed-pairing obligations on the selected class.
