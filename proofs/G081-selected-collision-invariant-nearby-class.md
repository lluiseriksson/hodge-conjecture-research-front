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
hodge_type: no type condition on the total nearby class or ordinary lift; conditional B119 makes a nonzero relation-filtered clean-nodal grade type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B059, B084-B085, B090-B093, B107-B109, B110-B122, G050-G051, G071, G073-G080, G082-G083, NG059-NG060, NG087, NG095-NG098, S022, S037
claim: Realize the selected B058 detector as a nonzero rational class t_Delta in one original collision-disk nearby object, preserve its B022 quotient and pairing certificates, and prove it has a lift in B107's relation filtration step S_0.
falsifier: undefined chain-to-disk-nearby map, zero image after a B022 quotient, loss of the selected nonzero pairing, nonzero filtered obstruction for every admissible disk, or substitution of a semistable exceptional class for the original downstairs class
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
2. its filtered obstruction \(\omega_{\mathrm{fil}}(t_\Delta)\) vanishes.

The second certificate puts \(t_\Delta\) in the image of B107's restricted
map \(u_\Delta:S_0\to P_\Delta\). B122 already gives an ordinary special
lift in the required plane-normalized stalk and

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
- the filtered special-to-nearby matrix and an explicit
  \(\beta_0\in S_0\) with \(u_\Delta(\beta_0)=t_\Delta\);
- the retained nonzero pairing with the specified \(\zeta\).

Failure of any one item falsifies the proposed G081 witness.

## Current obstruction

B122 proves every class in the actual nearby target degree is cyclically
invariant and ordinarily liftable; NG098 retires the raw G082 cocycle as an
overconstraint. B090-B091 still prove that a pure Hurwitz relabelling
produces no nonzero localized excess. G083 is therefore the exact remaining
calculation: map the distributed selected chain into one original disk and
kill its B108 filtered obstruction without changing the B022 quotient
pairing. A semistable cover
may be used as a calculation device, but its exceptional classes cannot
replace the required original class.
