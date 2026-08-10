---
brick_id: NG047
status: NO-GO
base_field: C
variety: arbitrary projective degenerations and the suspended A2 hyperplane family after an alteration
smoothness: weak semistability gives a smooth base but not necessarily a smooth total space
projectivity: the alteration and modification are projective
dimension: arbitrary, including every odd hyperplane-fiber dimension 2n-1
codimension: terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, nearby cycles, and primitive ambient homology
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative
dependencies: B022, B069, G037, and S044
claim: Weak semistable reduction alone cannot be counted as an S3-equivariant smooth model or as proof that the rational detector descends with nonzero pairing.
falsifier: an additional theorem making the Abramovich-Karu construction equivariant for the specified root cover, smoothing the total space without losing weak semistability, and identifying the full-support detector trace
---

# NG047 — Weak semistability is not detector-compatible descent

**Status:** NO-GO

## Rejected route

Invoke B069 and declare G037 solved because an all-dimensional weakly semistable model exists.

## Precise mismatches

The audited theorem supplies an unspecified alteration of the base and a modification with toroidal, equidimensional, reduced fibers. It does not assert:

1. that the alteration is the \(S_3\) root cover or carries a compatible group action;
2. that the total space is nonsingular;
3. that a subsequent resolution preserves weak semistability;
4. that the relevant rational Hodge module is strictly multispecialisable;
5. that proper pushdown separates a full-support detector from exceptional summands; or
6. that the B022 quotient class and its nonzero pairing survive trace to the original base.

These are exactly the data required for propagation toward G031.

## Re-entry condition

Prove G038: an equivariant refinement with a labeled support decomposition and a rational trace compatible with the detector maps.
