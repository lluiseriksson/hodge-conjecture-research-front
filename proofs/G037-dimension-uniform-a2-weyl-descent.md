---
brick_id: G037
status: EXPLORATORY
base_field: C, with a Q-structure on all Hodge-module and detector data
variety: the S3 root-covered suspended A2 family in every odd fiber dimension 2n-1 arising from a smooth projective 2n-fold
smoothness: the root-cover base is smooth; the raw total space is singular along B067's collision sections; the sought alteration must be smooth or semistable
projectivity: the local construction must algebraize inside the projective hyperplane family and remain proper over the base
dimension: arbitrary n at least 1, ambient dimension 2n, and singular hyperplane dimension 2n-1
codimension: terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, nearby cycles, proper direct image, and primitive ambient homology
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B063, B067-B068, G036, and NG046
claim: The S3 root-covered suspended A2 family admits a dimension-uniform proper semistable model whose rational MHM comparison descends and preserves the full-support detector pairing.
falsifier: failure of a semistable model in some odd dimension, nonregular S3 descent, an unavoidable exceptional-only detector, or loss of rational type or B022 quotient class
---

# G037 — Dimension-uniform \(A_2\) Weyl cover and detector descent

**Status:** EXPLORATORY  
**Parent gate:** G036

## Falsifiable theorem target

For every \(n\ge1\), start from B067's root-covered family
\[
(x-u)(x-v)(x+u+v)+\sum_{i=1}^{2n-1}z_i^2=0.
\]
Construct a proper algebraic modification, with any finite base change stated explicitly, satisfying:

1. smooth or semistable total space in all odd fiber dimensions \(2n-1\);
2. a rational mixed Hodge module that is strictly multispecialisable along the resolved reflection arrangement;
3. support-by-support proper pushdown to the original coefficient plane;
4. a defined \(S_3\)-trace or invariant descent on the relevant full-support object;
5. preservation of the B022 quotient class and nonzero Saito pairing with the prescribed Hodge class.

## Current audit

B067 proves the root-cover algebra and shows that the raw total space is still singular along three collision sections. B068 supplies simultaneous resolution only for surface rational double points. NG046 proves the dimension mismatch with every hyperplane fiber in the middle-degree reduction.

B069 supplies a dimension-uniform **weakly** semistable model after an
unspecified alteration and modification. This closes bare toroidal existence,
but not items 2-5: the total space may be singular, and equivariance, MHM
strictness, support decomposition, and detector trace are absent. NG047 and
G038 isolate the remaining bridge.

## Smallest next obligation

Determine whether functorial/equivariant resolution and toroidal refinement
can be combined with B069 while preserving weak semistability. Then construct
the rational MHM trace square in G038. A non-equivariant abstract resolution
is insufficient because the descent in item 4 would be undefined on a chosen
resolved object.
