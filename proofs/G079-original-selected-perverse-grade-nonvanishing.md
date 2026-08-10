---
brick_id: G079
status: EXPLORATORY
base_field: C with collision and Hodge data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified primitive rational Hodge class zeta, its selected B058 detector, and the original smooth plane-net incidence pushdown
smoothness: X and the incidence total space smooth; generic hyperplane fibers smooth; target fiber clean nodal or A2-collision as specified; generic discriminant points Lefschetz
projectivity: X, the plane net, original incidence family, and pushdown projective
dimension: dim_C X = 2n; hyperplane fibers dimension 2n-1; plane base dimension 2
codimension: middle cycle codimension n; the former competing point support has base codimension two and is excluded by B118
coefficient_field: Q
cohomology_theory: selected relative thimble chains, original nearby and special mixed Hodge-module stalks, canonical perverse filtration, strict support, and the local invariant-cycle triangle
hodge_type: selected nearby class, special lift, and E_infinity^(-1,0) coordinate rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B057-B059, B081-B084, B110-B118, G047-G048, G073-G078, G080, NG059-NG060, NG086-NG094, S022, S037, S052
claim: Construct the collision-certified selected nearby class and ordinary special lift directly in the original incidence pushdown and prove that the lift has a nonzero canonical E_infinity^(-1,0) coordinate; B117 then makes this coordinate full-support automatically.
falsifier: undefined original nearby class, nonzero vanishing-cycle obstruction, absence of an ordinary lift, zero E_infinity^(-1,0) coordinate, confinement to E_infinity^(0,-1), wrong rational Hodge type, or loss of the prescribed detector provenance
---

# G079 — Make the selected original perverse grade nonzero

**Status:** EXPLORATORY  
**Parent gates:** G078 / G077 / G076

B117 removes the divisor/full-support ambiguity for the original incidence
pushdown. The remaining class-specific obligation is therefore:

1. realize B058's selected detector as a nearby class \(t_\psi\) in the
   original collision object;
2. prove \(\operatorname{can}(t_\psi)=0\) and choose an ordinary rational
   special lift \(\beta\);
3. place \(\beta\) in the canonical perverse filtration and prove

   \[
   [\beta]_{E_\infty^{-1,0}}\ne0;
   \]

4. verify type \((0,0)\) after \(\mathbf Q(n)\) and retain the marked
   collision provenance needed by the B022 and pairing tests.

The only remaining support alternative at detector total degree \(-1\) is
the point-supported grade \(E_\infty^{0,-1}\). B118 now proves that this
grade is zero in the original incidence pushdown: relative hard Lefschetz
would reflect any point support into a constant high direct image. B117
proves that every nonzero \(E_\infty^{-1,0}\) class there is already in the
full-support strict-support summand.

## Current obstruction

No topology-changing construction yet carries the distributed B057 chain
into the original nearby-cycle object as a nonzero class with an ordinary
lift. The semistable cover can help compute this map, but its exceptional
support must not be substituted for the original class. G080 is the exact
remaining construction; G073-G075 retain its source and descent obligations.
