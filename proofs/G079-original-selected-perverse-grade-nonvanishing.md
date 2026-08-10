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
hodge_type: no type condition on the total nearby class or lift; the nonzero E_infinity^(-1,0) clean-nodal coordinate is rational type (0,0) after Q(n) by B119
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B057-B059, B081-B085, B092-B093, B107-B109, B110-B122, G047-G048, G071, G073-G078, G080-G083, NG059-NG060, NG086-NG098, S022, S037, S052
claim: Construct the collision-certified selected disk-nearby class and prove it has a lift in B107's relation filtration step S_0; B117-B119 then make its nonzero E_infinity^(-1,0) coordinate full-support and type (0,0).
falsifier: undefined original disk-nearby class, death in either B022 quotient, zero prescribed pairing, nonzero filtered obstruction for every admissible disk, zero E_infinity^(-1,0) coordinate after a filtered lift, or non-clean-nodal target
---

# G079 — Make the selected original perverse grade nonzero

**Status:** EXPLORATORY  
**Parent gates:** G078 / G077 / G076

B117 removes the divisor/full-support ambiguity for the original incidence
pushdown. The remaining class-specific obligation is therefore:

1. realize B058's selected detector as a nearby class \(t_\psi\) in the
   original collision object;
2. use B122's automatic ordinary liftability in degree \(d+1\);
3. prove B108's filtered obstruction vanishes and choose
   \(\beta_0\in S_0\), then prove

   \[
   [\beta_0]_{E_\infty^{-1,0}}\ne0;
   \]

4. use B119 to obtain type \((0,0)\) after \(\mathbf Q(n)\) on this
   coordinate, while retaining the marked collision provenance needed by
   the B022 and pairing tests.

B121 corrects the total-degree list: besides the relation and point grades,
the constant ambient grade \(E_\infty^{-2,1}\) survives. Thus an ordinary
lift is insufficient. Membership in \(S_0\) excludes that higher grade.
B118 proves the remaining lower point grade zero, and B117 proves that every
nonzero \(E_\infty^{-1,0}\) class is already in the full-support
strict-support summand.

## Current obstruction

No topology-changing construction yet carries the distributed B057 chain
into one original disk-nearby object as a nonzero class with vanishing
filtered obstruction. The semistable cover can help compute this map,
but its exceptional support must not be substituted for the original class.
G083 is the exact remaining construction inside G081/G080; G073-G075 retain its
source and descent obligations.
