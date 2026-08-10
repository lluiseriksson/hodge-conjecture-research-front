---
brick_id: G081
status: EXPLORATORY
base_field: C with all chain, monodromy, and cohomology data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified primitive rational Hodge class zeta, its selected B058 detector, the original plane-net incidence family, and one marked collision disk through a clean nodal target
smoothness: X and the incidence total space smooth; nearby hyperplane fibers smooth; target fiber clean nodal with finitely many ordinary double points
projectivity: X, the plane net, incidence family, and pushdown projective
dimension: dim_C X = 2n; hyperplane fibers dimension 2n-1; plane base dimension 2; collision test curve dimension 1
codimension: middle cycle codimension n; target is a base point
coefficient_field: Q
cohomology_theory: B022 relative thimble quotient, original disk nearby cycles, cyclic collision monodromy, local invariant cycles, and the canonical plane perverse filtration
hodge_type: no type condition on the total nearby class or total ordinary lift; B119 makes the nonzero relevant clean-nodal relation grade type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B059, B084-B085, B090-B091, B110-B120, G050-G051, G073-G080, G082, NG059-NG060, NG087, NG095-NG096, S022, S037
claim: Realize the selected B058 detector as a nonzero rational class t_Delta in the original incidence nearby object along one marked collision disk, and prove that its cyclic B085 monodromy obstruction vanishes.
falsifier: undefined chain-to-disk-nearby map, zero image after the B022 quotients, nonzero cyclic obstruction for every admissible disk, loss of the selected nonzero pairing, or substitution of a semistable exceptional class for the original downstairs class
---

# G081 — Construct the selected collision-invariant nearby class

**Status:** EXPLORATORY

**Parent gate:** G080

The exact remaining object is a rational class

\[
 0\ne t_\Delta\in H^0(i_p^*\Psi K_\Delta)
\]

in the *original* incidence pushdown, obtained from the selected B058
distributed thimble detector and accompanied by two certificates:

1. its image survives the equator-extension and base-locus quotients of
   B022 and retains the prescribed nonzero pairing with \(\zeta\);
2. the generator of the marked disk's cyclic local monodromy fixes
   \(t_\Delta\).

The second certificate puts \(t_\Delta\) in the disk local-invariant
subspace. B120 applies B084 after the original curve base change and gives a
rational ordinary special lift in the required plane-normalized stalk and,
equivalently,

\[
 \operatorname{can}(t_\Delta)=0.
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
- the matrix or geometric formula for the marked disk monodromy and an
  explicit kernel adjustment proving \((M_\Delta-I)t_\Delta=0\);
- the retained nonzero pairing with the specified \(\zeta\).

Failure of any one item falsifies the proposed G081 witness.

## Current obstruction

B057 supplies detector-loop invariance, not invariance under the marked
collision disk. B120/NG096 show that no simultaneous plane-local invariant
is needed. B090-B091 prove that a pure Hurwitz relabelling produces no
nonzero localized excess. G082 is therefore the exact remaining
calculation: map the distributed selected chain into one original disk,
compute its cyclic B085 defect in the combined B022 kernel, and kill that
class without changing the prescribed quotient pairing. A semistable cover
may be used as a calculation device, but its exceptional classes cannot
replace the required original class.
