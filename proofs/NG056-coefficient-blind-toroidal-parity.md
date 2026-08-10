---
brick_id: NG056
status: NO-GO
base_field: C
variety: arbitrary smooth projective toroidal morphisms, including the explicit B079 product
smoothness: smooth source and target in the counterexample
projectivity: projective morphism and projective non-toric fiber factor
dimension: counterexample source dimension 3 and target dimension 2; proposed inference arbitrary-dimensional
codimension: counterexample support is a point of codimension 2
coefficient_field: Q
cohomology_theory: rational derived direct image, strict support, Kunneth formula, and Hodge structures
hodge_type: arbitrary global fiber Hodge structures; B079 uses non-Tate H^1 of a positive-genus curve
cycle_class_map: not used; downstream map is CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence in the downstream Hodge application
scope: relative and fiberwise
dependencies: B078-B079, G044
claim: Even normal toric support degree implies even total proper-support degree for every smooth projective toroidal family, independently of its global fiber coefficient cohomology.
falsifier: B079's nonzero H^1(C,Q)(-1)_0[-3] point-supported summand
---

# NG056 — Coefficient-blind toroidal parity is false

**Status:** NO-GO

## Invalid inference

Apply B078 in each toroidal normal chart, observe an even normal support
degree, and conclude that the global proper-support term is even without
tracking the coefficient Hodge module along the stratum.

## Counterexample

B079 takes the toric blowup of (mathbf A^2) at the origin and multiplies it
by a positive-genus projective curve. The even exceptional degree two tensored
with (H^1(C,mathbf Q)) gives the nonzero odd point-supported term

\[
 H^1(C,\mathbf Q)(-1)_0[-3].
\]

The source and target are smooth and the map is a projective toroidal
smooth-factor product. Hence toroidal local structure alone does not preserve
total parity.

## Re-entry condition

G044 must compute, not suppress, the coefficient index. It succeeds only if
the exact B057 detector degree is incompatible with

\[
 \text{normal support degree}+\text{global coefficient degree}
\]

for every proper support of the B071 pushdown. Otherwise the matching term is
an explicit exceptional component to subtract in G043.
