---
brick_id: G096
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a nonzero primitive rational middle Hodge class zeta, and a synchronized ordered N-node candidate with value rank R<N
smoothness: X and prospective supports are smooth; final singularities must be ordinary double points and the integrated excess germ reduced and smooth
projectivity: X, the full double-point scheme 2Z, and the linear system are projective
dimension: dim_C X=2n; synchronized quotient dimension n; relation dimension N-R; full double scheme length (2n+1)N
codimension: projected-gradient rank n; common-kernel conormal rank at most nR; full first-jet rank at most (n+1)R+n; final smoothing height R
coefficient_field: C for jets, Hessians, schemes, and deformation germs; Q for zeta, vanishing cycles, and the terminal pairing
cohomology_theory: coherent first-jet interpolation, second-order nodal deformation theory, rational vanishing-cycle homology, Saito local intersection cohomology, and rational Betti cohomology
hodge_type: the final local relation functional must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of zeta may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B134-B152, G092-G095, and NG118-NG122
claim: Construct from (X,zeta), without an algebraic carrier, synchronized quotient gradients of rank n whose common-kernel conormal gradients lie in B152's mixed-Hessian kernel of dimension nR, whose pure quotient Hessian quadrics also land in the value-evaluation image, and whose full data integrate to a smooth height-R nodal germ with nonzero specified Saito pairing.
falsifier: conormal rank greater than nR, violation of a mixed or pure B146 relation identity, full first-jet rank greater than (n+1)R+n, failed integration, zero adjoint defect or primitive image, or zero specified pairing
---

# G096 — Realize the synchronized second defect

In G095's synchronized branch, B152 adds a second finite obstruction. A
candidate must simultaneously provide:

1. value rank \(R<N\) and synchronized projected-gradient rank \(n\);
2. a common-kernel conormal-gradient map

   \[
   A:C\longrightarrow\bigoplus_i\Lambda_i
   \]

   whose image lies in B152's canonical mixed-Hessian kernel of dimension
   \(nR\);
3. the remaining pure-\(Q\) quadratic terms of every B146 relation in the
   value-evaluation image;
4. full double-point evaluation rank at most \((n+1)R+n\);
5. nonlinear integration to a reduced smooth simultaneous-node germ of
   height \(R\);
6. positive adjoint defect, nonzero primitive ambient image, and a rational
   type-\((0,0)\) Saito functional nonzero on \(\zeta\).

The product-fiber carrier satisfies and saturates the mixed linear bound,
but its common quotient and conormal kernel come from the known algebraic
fiber. No carrier-free construction from an arbitrary \((X,\zeta)\) is
known.
