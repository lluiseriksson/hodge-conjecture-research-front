---
brick_id: G093
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a nonzero primitive rational middle Hodge class zeta, a high-power line bundle L, and an ordered nodal member with node set Z
smoothness: X is smooth and the target singularities are isolated ordinary double points; smoothness and reducedness of the integrated excess incidence are obligations
projectivity: X and the hyperplane linear system are projective; the jet constraints and integration problem are local analytic inside that system
dimension: dim_C X=2n; every nodal cotangent space has dimension 2n and every desired split isotropic factor has dimension n
codimension: the node-value rank is R<N; the projected conditional-gradient rank must be at most n, the full conditional-gradient corank must be at least n(R+1), and the final smoothing ideal must have height exactly R
coefficient_field: C for jets, Hessians, and deformation germs; Q for the Hodge class, vanishing-cycle relations, and the terminal pairing
cohomology_theory: local nodal deformation theory, evaluation matroids, rational vanishing-cycle homology, Saito local intersection cohomology, and rational Betti cohomology
hodge_type: the final local relation functional must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of zeta may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B134-B148, G090-G092, and NG115-NG119
claim: Construct from (X,zeta), without an algebraic middle-dimensional carrier, a uniform rank-deficient node set and nodewise maximal inverse-Hessian-isotropic subspaces such that the conditional-gradient map projected modulo their split sum has rank at most n and its full image satisfies B146's common relation-weighted Hessian isotropy; integrate the resulting constraints to a reduced smooth height-R simultaneous-node germ and prove its Saito functional pairs nontrivially with zeta.
falsifier: projected-gradient rank greater than n, failure of the B146 common Hessian-isotropy condition, a nonreduced or singular smoothing ideal, zero adjoint defect, zero primitive ambient image, or zero pairing with zeta
---

# G093 — Construct the carrier-free split Lagrangian jet core

B147-B148 show exactly how the anchored examples obtain much of B146's
large isotropic gradient failure: conormal spaces of an algebraic carrier
provide one maximal isotropic \(n\)-plane at every node, while all quotient
gradients factor through the \(n\)-dimensional carrier-motion space. The
narrowest constructive test is whether the same **jet package** can be
produced without such a carrier.

For an arbitrary pair \((X,\zeta)\), seek:

1. an ordered node set \(Z=\{p_1,\ldots,p_N\}\) with uniform value matroid
   \(U_{R,N}\), \(R<N\), at the dimension-scaled size required by B141;
2. maximal isotropic subspaces
   \(\Lambda_i\subset T_{p_i}^*X\otimes L|_{p_i}\) for the inverse nodal
   Hessians;
3. projected conditional-gradient rank

   \[
   \operatorname{rank}\left(
   \ker E_Z\xrightarrow{D}\bigoplus_iT_{p_i}^*X\otimes L|_{p_i}
   \longrightarrow\bigoplus_i
   (T_{p_i}^*X\otimes L|_{p_i})/\Lambda_i
   \right)\le n.
   \]

   Equivalently, the kernel is a split-Lagrangian gradient core of
   codimension at most \(n\) in \(\ker E_Z\). This rules out the vacuous
   choice consisting only of sections vanishing to first order;
4. B146's common condition
   \(q_c(Da)=0\) for every \(a\in\ker E_Z\) and every value relation
   \(c\in\ker E_Z^*\), including the corank floor \(n(R+1)\);
5. higher-order integrability to a reduced smooth simultaneous-node germ
   of codimension \(R\);
6. positive adjoint defect, nonzero primitive ambient image, and a Saito
   relation functional nonzero on \(\zeta\).

Items 1-4 are finite jet conditions and are falsifiable before attempting
the nonlinear integration in item 5. Item 6 prevents a class-blind
isotropic construction from being counted as progress. A solution of G093
would solve the stronger G092 package, but no such carrier-free construction
is known. B148 proves that the anchored product-fiber construction satisfies
the rank bound; NG119 proves that choosing the Lagrangians after a generic
surjective jet map cannot satisfy it.
