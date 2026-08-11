---
brick_id: G094
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a nonzero primitive rational middle Hodge class zeta, a high-power line bundle L, and a length-(n+1)N oriented half-double scheme Xi supported on N prospective nodes
smoothness: X and the support points are smooth; the final hypersurface must have isolated ordinary double points and the integrated simultaneous-node germ must be reduced and smooth
projectivity: X, Xi, and the linear system are projective; integration is local analytic in the projective parameter space
dimension: dim_C X=2n; Xi has length (n+1)N and support Z has length N
codimension: value rank R<N; Xi-evaluation rank at most R+n; coherent defect at least (n+1)N-R-n; final smoothing ideal height R
coefficient_field: C for schemes, coherent cohomology, jets, Hessians, and incidence germs; Q for zeta, vanishing cycles, and the terminal pairing
cohomology_theory: coherent sheaf cohomology, first principal parts, nodal deformation theory, rational vanishing-cycle homology, Saito local intersection cohomology, and rational Betti cohomology
hodge_type: the final local relation functional must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of zeta may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B134-B149, G092-G093, and NG118-NG120
claim: Construct from (X,zeta) an oriented half-double scheme Xi whose reduced support has uniform value rank R<N, whose length-(n+1)N evaluation rank is at most R+n, whose orientation planes are maximal inverse-Hessian isotropic and satisfy B146's common relation quadrics, and which integrates to a smooth height-R nodal germ with nonzero specified Saito pairing.
falsifier: Xi-evaluation rank greater than R+n, failure of Hessian compatibility or common isotropy, nonisolated singularities, failure of smooth integration, zero adjoint defect, zero primitive image, or zero pairing with zeta
---

# G094 — Construct the oriented half-double incidence

B149 turns G093's projected-gradient condition into one zero-dimensional
interpolation problem. For an arbitrary \((X,\zeta)\), construct an oriented
scheme

\[
 \Xi=\coprod_{i=1}^N
 \operatorname{Spec}\!\left(
 \mathcal O_{X,p_i}/
 (\mathfrak m_i^2+\widetilde{\Lambda}_i)
 \right)
\]

such that:

1. \(Z=\Xi_{\mathrm{red}}\) has uniform value matroid \(U_{R,N}\), \(R<N\),
   at B141's superlinear scale;
2. \(\operatorname{rank}(H^0(X,L)\to H^0(\Xi,L|_\Xi))\le R+n\);
3. every \(\Lambda_i\) is maximal isotropic for the inverse Hessian of the
   eventual node, and the full conditional-gradient image satisfies every
   B146 relation quadratic;
4. the finite jet data integrate to a reduced smooth height-\(R\)
   simultaneous-node germ;
5. the adjoint defect and primitive ambient image are nonzero, and the
   resulting rational type-\((0,0)\) Saito functional is nonzero on
   \(\zeta\).

Conditions 1-3 are falsifiable on a finite scheme before integration.
Condition 2 alone is a very large interpolation failure, quantified exactly
by B149. No carrier-free construction with all five properties is known.
