---
brick_id: G079
status: NO-GO
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
dependencies: B057-B059, B081-B085, B092-B093, B107-B109, B110-B123, G047-G048, G071, G073-G078, G080-G083, NG059-NG060, NG086-NG099, S022, S037, S052
claim: The nearby-to-relation-filtered formulation is impossible for a nonzero selected disk class because B123 gives u(S_0)=0; direct relative-boundary landing remains possible through G064-G065.
falsifier: a nonzero clean-nodal nearby class in u(S_0)
---

# G079 — Make the selected original perverse grade nonzero

**Status:** NO-GO
**Parent gates:** G078 / G077 / G076

B123/NG099 close the nearby-lift formulation below. It is retained to audit
the failed direction; G064-G065 are a directionally valid but exact-target
replacement. B124 restores G031 as the narrower parent, and B125 isolates
active subgate G084.

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

These are the retired obligations; B123 proves item 3 impossible whenever
the selected nearby class is nonzero.

B121 corrects the total-degree list: besides the relation and point grades,
the constant ambient grade \(E_\infty^{-2,1}\) survives. Thus an ordinary
lift is insufficient. Membership in \(S_0\) excludes that higher grade.
B118 proves the remaining lower point grade zero, and B117 proves that every
nonzero \(E_\infty^{-1,0}\) class is already in the full-support
strict-support summand.

## Retired obstruction

No topology-changing construction can carry the distributed B057 chain into
one original disk-nearby object as a nonzero class with vanishing filtered
obstruction: B123 makes this impossible. A semistable cover cannot change
that conclusion. G065 retains the directionally valid relative-boundary
obligation.
