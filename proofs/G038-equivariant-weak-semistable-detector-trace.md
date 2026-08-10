---
brick_id: G038
status: EXPLORATORY
base_field: C with all descent and Hodge data defined over Q
variety: the projective algebraization of B067's S3 root-covered suspended A2 family and an equivariant weakly semistable alteration
smoothness: the base is smooth; the sought refinement must either have smooth total space or prove mixed-Hodge comparison on its stated quotient singularities
projectivity: all alterations, modifications, and pushdowns must be projective
dimension: arbitrary ambient dimension 2n and odd fiber dimension 2n-1
codimension: terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, toroidal nearby cycles, decomposition theorem, trace, and primitive ambient homology
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B063, B067, B069, G037, and NG047
claim: Weak semistable reduction can be refined equivariantly over the S3 root cover so that the rational full-support detector admits a trace to the original family preserving the B022 class and nonzero pairing.
falsifier: unavoidable non-equivariance, loss of weak semistability under resolution, detector support confined to exceptional strata, or trace annihilation of the nonzero pairing
---

# G038 — Equivariant weak semistability and detector trace

**Status:** EXPLORATORY  
**Parent gates:** G037 / G036

## Falsifiable theorem target

For a projective algebraization of B067's family, prove all of the following:

1. choose the Abramovich–Karu alteration compatibly with the \(S_3\) root cover, or dominate both by an explicitly Galois alteration with group \(\Gamma\);
2. produce a \(\Gamma\)-equivariant weakly semistable model and either a smooth equivariant refinement preserving the toroidal reduced-fiber structure or a direct MHM theorem for its quotient singularities;
3. prove strict multispecialisability of the rational coefficient Hodge module along the toroidal boundary;
4. decompose proper pushdown by strict support and identify a full-support summand carrying the original detector;
5. define the rational trace/invariant morphism and prove it intertwines both B022 quotients and the Saito ambient map;
6. prove the resulting pairing with the prescribed \(\zeta\) remains nonzero.

## Current result

B069 supplies only the non-equivariant weakly semistable existence theorem. NG047 shows why this is insufficient. No step above is inferred merely from rational coefficients: dividing a defined trace by \(|\Gamma|\) is legitimate, but it does not prove that the relevant class lies in the invariant full-support summand or has nonzero trace.

## Smallest next audit

Audit functorial/equivariant resolution and toroidal alteration theorems for whether they preserve the weakly semistable morphism, not merely the abstract total space. Then formulate the exact trace square on rational MHM objects before making any pairing claim.

