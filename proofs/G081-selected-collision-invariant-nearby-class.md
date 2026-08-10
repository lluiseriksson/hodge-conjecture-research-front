---
brick_id: G081
status: EXPLORATORY
base_field: C with all chain, monodromy, and cohomology data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified primitive rational Hodge class zeta, its selected B058 detector, and the original plane-net incidence family near a clean nodal collision
smoothness: X and the incidence total space smooth; nearby hyperplane fibers smooth; target fiber clean nodal with finitely many ordinary double points
projectivity: X, the plane net, incidence family, and pushdown projective
dimension: dim_C X = 2n; hyperplane fibers dimension 2n-1; plane base dimension 2; collision test curve dimension 1
codimension: middle cycle codimension n; target is a base point
coefficient_field: Q
cohomology_theory: B022 relative thimble quotient, original nearby cycles, local collision monodromy, local invariant cycles, and the canonical perverse filtration
hodge_type: no type condition on the total nearby class or total ordinary lift; B119 makes the nonzero relevant clean-nodal relation grade type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B059, B084, B090-B091, B110-B111, B117-B119, G073-G080, NG059-NG060, NG087, NG095, S022, S037
claim: Realize the selected B058 detector as a nonzero rational class t_psi in the original incidence nearby object along a specified collision curve, with an explicit certificate that t_psi is fixed by the full local collision monodromy.
falsifier: undefined chain-to-nearby map, zero image after the B022 quotients, failure of invariance under any generator of the local collision fundamental group, loss of the selected nonzero pairing, or substitution of a semistable exceptional class for the original downstairs class
---

# G081 — Construct the selected collision-invariant nearby class

**Status:** EXPLORATORY

**Parent gate:** G080

The exact remaining object is a rational class

\[
 0\ne t_\psi\in H^{-1}(i_p^*\Psi K)
\]

in the *original* incidence pushdown, obtained from the selected B058
distributed thimble detector and accompanied by two certificates:

1. its image survives the equator-extension and base-locus quotients of
   B022 and retains the prescribed nonzero pairing with \(\zeta\);
2. every generator of the local collision fundamental group fixes
   \(t_\psi\).

The second certificate puts \(t_\psi\) in the local invariant subspace.
B084 then gives a rational ordinary special lift and, equivalently,

\[
 \operatorname{can}(t_\psi)=0.
\]

No type-\((0,0)\) condition is required on the total nearby vector or the
total lift: B119 proves that any such nonzero rational lift has a nonzero
full-support clean-nodal relation coordinate, automatically of type
\((0,0)\) after \(\mathbf Q(n)\).

## Falsifiable construction obligation

A proposed construction must print:

- the relative chain representing the selected B058 class;
- the exact map to the original nearby-cycle stalk;
- the induced class after both B022 quotients;
- matrices or geometric formulas for a generating set of collision
  monodromy, and the equality \((T_i-I)t_\psi=0\) for every generator;
- the retained nonzero pairing with the specified \(\zeta\).

Failure of any one item falsifies the proposed G081 witness.

## Current obstruction

B057 supplies detector-loop invariance, not collision-monodromy invariance.
B090-B091 prove that a pure Hurwitz relabelling produces no nonzero
localized excess. The missing input is therefore a topology-changing
comparison that maps the distributed selected chain nontrivially into the
original downstairs nearby object while allowing the collision generators
to be computed. A semistable cover may be used as a calculation device, but
its exceptional classes cannot replace the required original class.
