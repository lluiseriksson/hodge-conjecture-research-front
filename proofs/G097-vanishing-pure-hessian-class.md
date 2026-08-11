---
brick_id: G097
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a nonzero primitive rational middle Hodge class zeta, and a synchronized ordered N-node candidate with value rank R<N
smoothness: X and prospective supports are smooth; final nodes must be ordinary double points and the integrated excess germ reduced and smooth
projectivity: X, the nodal schemes, and the linear system are projective
dimension: synchronized quotient dimension n; pure Hessian obstruction dimension (N-R)n(n+1)/2
codimension: projected rank n; mixed conormal rank at most nR; pure quotient Hessian class must vanish; final smoothing height R
coefficient_field: C for jets, Hessians, quotient classes, and deformation germs; Q for zeta, vanishing cycles, and the terminal pairing
cohomology_theory: coherent first-jet interpolation, second-order nodal deformation theory, rational vanishing-cycle homology, Saito local intersection cohomology, and rational Betti cohomology
hodge_type: the final local relation functional must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of zeta may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B134-B153, G092-G096, and NG118-NG123
claim: Construct from (X,zeta), without an algebraic carrier, synchronized quotient gradients and B152-compatible conormal gradients for which B153's canonical pure Hessian class Omega_Q vanishes; then integrate the resulting second-order-flat smoothing data to a reduced smooth height-R nodal germ and prove its Saito functional pairs nontrivially with zeta.
falsifier: nonzero Omega_Q, dependence on a chosen quotient splitting, failure of higher-order integration, zero adjoint defect or primitive image, or zero specified pairing
---

# G097 — Kill the canonical pure Hessian class

B153 makes the final second-order obligation intrinsic:

\[
 \Omega_Q\in
 \operatorname{coker}(E)\otimes\operatorname{Sym}^2Q^*.
\]

For an arbitrary \((X,\zeta)\), construct the synchronized G096 data so
that:

1. the projected-gradient quotient has rank \(n\);
2. the common-kernel conormal image lies in B152's mixed-Hessian kernel;
3. \(\Omega_Q=0\);
4. the second-order-flat data integrate through every higher order to a
   reduced smooth simultaneous-node germ of height \(R\);
5. the resulting relation channel has positive adjoint defect, nonzero
   primitive image, rational type \((0,0)\), and nonzero pairing with
   \(\zeta\).

Items 1-3 are now a complete and splitting-independent characterization of
B146's second-order condition in the synchronized branch. Item 4 is the
next genuinely nonlinear obstruction. No carrier-free construction
satisfying the five items is known.
