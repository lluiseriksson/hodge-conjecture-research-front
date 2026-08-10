---
brick_id: G001
status: EXPLORATORY
base_field: C
variety: arbitrary smooth projective Y and smooth projective families containing it
smoothness: smooth total family morphism; smooth fibers
projectivity: projective family
dimension: even relative dimension 2m
codimension: m
coefficient_field: Q
cohomology_theory: relative singular Betti cohomology R^{2m}f_*Q
hodge_type: fiberwise (m,m)
cycle_class_map: CH^m(Y_t)_Q -> H^{2m}(Y_t,Q(m))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: algebraic Hodge loci; existence of a suitable deformation family
claim: Every middle rational Hodge pair can be connected inside its Hodge locus to a fiber where the transported class is algebraic.
falsifier: a middle rational Hodge pair whose every connected Hodge-locus realization has no distinct algebraic anchor
---

# G001 - Algebraic-anchor access

This is a falsifiable sufficient gate, not a theorem. For each pair
\((Y,\alpha)\) in MHC it asks for a connected algebraic base \(T\), smooth
projective family \(f:\mathcal Y\to T\), point \(t\), and flat rational class
\(\widetilde\alpha\) with \((Y_t,\widetilde\alpha_t)=(Y,\alpha)\), such that
\(\widetilde\alpha\) remains of type \((m,m)\) and is algebraic at some anchor
\(t_0\in T\).

No general construction is known. Taking \(T=\{t\}\) and calling \(t\) the
anchor is circular unless \(\alpha\) was independently proved algebraic.
Cattani-Deligne-Kaplan proves the Hodge locus is algebraic but does not show it
contains an algebraic anchor.

