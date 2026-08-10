---
brick_id: G039
status: EXPLORATORY
base_field: C with rational Hodge and trace data
variety: a Galois-equivariant weakly semistable model dominating the A2 root-covered projective family
smoothness: the source is initially toroidal and may have quotient singularities; the sought refined source is smooth
projectivity: all subdivisions, blowups, alterations, and pushdowns must be projective
dimension: arbitrary ambient dimension 2n and odd fiber dimension 2n-1
codimension: boundary strata vary; terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: toroidal geometry, rational mixed Hodge modules, nearby cycles, and proper direct image
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B063, B069-B071, G038, NG048, and NG049
claim: The equivariant weakly semistable morphism admits a projective group-equivariant toroidal refinement with smooth source that preserves equidimensional reduced fibers and the rational nearby-cycle trace square.
falsifier: a required subdivision that breaks equidimensionality or saturation, failure of equivariance/projectivity, or incompatibility of the resulting MHM comparison with pushdown
---

# G039 — Equivariant relative toroidal resolution

**Status:** EXPLORATORY  
**Parent gate:** G038

## Falsifiable theorem target

Starting with a finite-Galois weakly semistable model \(Y\to B'\), construct a projective \(\Gamma\)-equivariant toroidal subdivision such that:

1. the refined source and base are smooth;
2. the morphism remains toroidal and equidimensional;
3. all fibers remain reduced, equivalently the relevant monoid maps remain saturated;
4. local boundary coordinates satisfy the strict-multispecialisability hypotheses used in B063;
5. the refinement and proper pushdown are compatible with the rational trace square of G038.

## Current audit

B070 supplies equivariant absolute resolution because functoriality includes automorphisms. NG048 shows that this does not verify items 2-5. A positive proof must work with the cone complexes and lattice maps of the toroidal morphism, not merely with the singular locus of \(Y\).

B071 now supplies exactly that relative construction at the logarithmic
stack level: the Adiprasito–Liu–Temkin quasi-local semistable resolution is
projective, arbitrary-dimensional, and compatible with finite-group strict
automorphisms. Thus items 1-3 are closed in the stacky category. NG049 keeps
the gate open because the scheme realization is noncanonical and items 4-5
are not statements of the source theorem.

## Smallest next obligation

Prove G040: construct the rational mixed-Hodge nearby-cycle, strict-support,
and detector-trace square on the equivariant semistable log-stack, or first
give an equivariant projective scheme realization and prove the same square
there.
