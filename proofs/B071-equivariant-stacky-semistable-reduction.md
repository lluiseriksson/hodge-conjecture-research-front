---
brick_id: B071
status: PROVED
base_field: characteristic zero; the Hodge application is over C
variety: a finite-group-equivariant projective toroidal or fine log-smooth morphism, including a weakly semistable model after B069
smoothness: the input is log regular in the toroidal application; the output log stacks are semistable and have regular underlying spaces
projectivity: the monoidal alteration and source subdivision are projective
dimension: arbitrary source, base, and relative dimension
codimension: arbitrary boundary codimension; terminal cycles would have codimension n
coefficient_field: no coefficients enter the geometric theorem; the downstream detector problem uses Q
cohomology_theory: logarithmic and toroidal geometry; no mixed-Hodge-module comparison is claimed
hodge_type: no Hodge-type assertion; downstream target is rational type (0,0) after Q(n)
cycle_class_map: not used in this theorem; downstream map is CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence in the downstream Hodge application
scope: relative
dependencies: B069, S046
claim: Adiprasito-Liu-Temkin give a projective quasi-local semistable resolution in arbitrary dimension; for a finite group acting by strict automorphisms of the input log morphism, quasi-local compatibility canonically lifts the action to the stacky semistable resolution.
falsifier: failure of the cited quasi-local compatibility for a strict automorphism, or an assertion that the noncanonical scheme realization is automatically equivariant
---

# B071 — Equivariant stacky semistable reduction

**Status:** PROVED

## Imported theorem

Adiprasito–Liu–Temkin prove the Abramovich–Karu polyhedral conjecture in all
dimensions. Their Theorem 2.7 constructs a projective semistable resolution
of a map of conical complexes quasi-locally. Theorem 4.4 lifts this to a
projective monoidal resolution of fine log schemes compatible with
surjective strict morphisms, and Theorem 4.5 preserves log smoothness and
produces a semistable morphism.

For the toroidal weakly semistable input supplied by B069, the divisorial log
structures are log regular. Thus the resolved source and base have regular
underlying spaces and the local maps have the semistable monomial form.

## Finite-group equivariance

Let \(\Gamma\) act on \(f:Y\to B\) by strict automorphisms preserving the
boundary log structures. For each \(\gamma\in\Gamma\), the pair of
automorphisms of \(Y\) and \(B\) is a pair of surjective strict local
isomorphisms commuting with \(f\). The compatibility clause of Theorem 4.4
identifies the resolution pulled back by \(\gamma\) with the same canonical
resolution. Functoriality gives lifts satisfying the group law. Therefore
the projective monoidal alteration and subdivision are \(\Gamma\)-equivariant
at the logarithmic stack level.

This closes the arbitrary-dimensional relative smoothness,
equidimensionality, and reduced-fiber part of G039 in that category. It is a
strict improvement over B070: the resolution is built from the morphism of
fans, not from the absolute singular locus.

## Exact boundary

Remark 4.6 says that schemes can be recovered by Kawamata's trick, but the
base alteration is then noncanonical. The cited result does not assert that
this scheme realization preserves a preassigned \(\Gamma\)-action. It also
contains no theorem about rational mixed Hodge modules, strict support,
nearby-cycle comparison, the B022 quotients, or the detector pairing.

Accordingly, B071 is not a proof of G038, G031, or the Hodge Conjecture.
