---
brick_id: G078
status: EXPLORATORY
base_field: C with collision and Hodge data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified primitive rational Hodge class zeta, its selected B058 detector, and the actual projective collision over the original plane-net base
smoothness: X and generic hyperplane fibers smooth; each transverse disk meets the smooth generic locus of one discriminant divisor and avoids all other strata
projectivity: X, high-power hyperplane family, plane net, collision, and proper pushdown projective; transverse disks are local analytic tests
dimension: dim_C X = 2n; hyperplane fibers dimension 2n-1; plane base dimension 2; transverse slice dimension 1
codimension: middle codimension n; tested discriminant support has base codimension one and becomes point support on the slice
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, noncharacteristic pullback, perverse cohomology, canonical strict-support decomposition, nearby/special stalks, and punctual projection on a transverse disk
hodge_type: selected class and every tested coordinate rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B008, B077, B080-B081, B116-B117, G045-G047, G073-G077, G079, NG092-NG093, S052
claim: Construct G077's selected nonzero E_infinity^(-1,0) class and, for every discriminant divisor D, choose a generic noncharacteristic transverse disk; identify the D-strict-support coordinate with the punctual summand on that disk and prove the selected punctual projection is zero. The residual full-support coordinate is then nonzero.
falsifier: failure to construct the selected class, a characteristic slice, an unidentified perverse shift, a nonzero punctual projection for some D, or a zero residual full-support coordinate
---

# G078 — Compute divisor coordinates on transverse disks

**Status:** EXPLORATORY  
**Parent gate:** G077

Let \(K\) be the actual proper Hodge-module pushdown on the plane-net base
and let \([\beta]_{-1,0}\) be G077's selected nonzero canonical graded
class. For each irreducible discriminant divisor \(D\):

1. choose a general smooth point \(p\in D\), away from every other support
   stratum, and a disk \(\Delta_D\) transverse to \(D\) at \(p\);
2. prove that the appropriately shifted pullback to \(\Delta_D\) is
   noncharacteristic and perverse-exact on the relevant strict-support
   constituents;
3. identify the pullback of the \(D\)-strict-support summand with the
   canonical punctual summand supported at \(p\), while the full-support
   constituent remains the intermediate extension from
   \(\Delta_D\setminus\{p\}\);
4. compute the punctual projection of the selected class and prove it is
   zero.

Repeating this for every \(D\) proves \(\beta_D=0\). Since B081 has already
separated point supports into \(E_\infty^{0,-1}\), nonvanishing of the
selected \(E_\infty^{-1,0}\) class then forces a nonzero full-support
coordinate.

## Required output

Closure requires an explicit morphism or local normal-form computation for
the actual coefficient Hodge module, including the pullback shift and the
image of \(\beta\). A dimension count, the one-node relation vanishing of
B008, or a statement about multiplicities without the selected class does
not close the gate.

## Current obstruction

B117 executes the transverse calculation for the original smooth incidence
pushdown and proves that every punctual divisor-support multiplicity is
zero. It uses constancy of $R^{d+1}$; NG093 explains why the shifted-IC
statement for $R^d$ alone would not suffice. Thus no selected punctual
coordinate remains on the original object. What remains is G079: no
construction yet realizes $\beta$ there with a nonzero
$E_\infty^{-1,0}$ coordinate.
