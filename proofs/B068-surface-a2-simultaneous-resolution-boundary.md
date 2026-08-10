---
brick_id: B068
status: PROVED
base_field: C
variety: affine surfaces with rational double point singularities, specialized to the surface A2 singularity and its Artin deformation component
smoothness: the singular central surface has an A2 rational double point; the simultaneous resolution has smooth resolved fibers
projectivity: the local resolution morphism is proper; no global projective Hodge family is supplied
dimension: complex surface fibers only
codimension: the exceptional locus is a configuration of curves; this is not a terminal cycle-codimension statement
coefficient_field: integral geometric theorem; later Hodge use would require Q
cohomology_theory: none in the theorem statement used here
hodge_type: none asserted
cycle_class_map: none
cycle_equivalence: none
scope: relative and fiberwise
dependencies: Shepherd-Barron Theorem 1.1/Theorem 2.10 audited as S043 and B067
claim: For a surface A2 rational double point, the simultaneous-resolution cover of the Artin component is Galois with Weyl group S3; the result is explicitly a surface theorem.
falsifier: failure of Theorem 2.10 for a characteristic-zero surface A2 rational double point
---

# B068 — Exact scope of the Weyl simultaneous-resolution theorem

**Status:** PROVED (imported theorem boundary)  
**Gate:** G036 / G037  
**Primary source:** S043

## Imported result

Shepherd-Barron's Theorem 1.1, equivalently Theorem 2.10(1), proves the Burns–Rapoport description of the cover parametrizing simultaneous resolutions of a rational surface singularity: its Galois group is the Weyl group determined by the \((-2)\)-curve configuration. For a surface singularity of type \(A_2\), this group is \(W(A_2)=S_3\), matching B067's ordered-root cover.

Theorem 2.10(2) identifies the cover as the smooth base of a versal deformation of the minimal resolution, while part (3) identifies reflection fixed divisors with loci where roots survive as effective curves.

## Exact scope record

The cited theorem begins with a **surface** \(X_s\) having rational singularities. Its exceptional roots are classes of \((-2)\)-curves on the minimal surface resolution. It therefore proves the simultaneous-resolution mechanism for the two-dimensional rational-double-point case.

## Non-claims

- It does not state a simultaneous resolution for arbitrary higher-dimensional quadratic suspensions of \(A_2\).
- It does not provide an \(S_3\)-equivariant algebraic cycle realizing a prescribed detector.
- It does not prove that averaging or taking invariants after resolution preserves the B022 quotient class or Saito pairing.
- It does not imply the rational Hodge Conjecture.

