---
brick_id: G099
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a nonzero primitive rational middle Hodge class zeta, and an ordered N-node critical-value germ with value rank R<N
smoothness: X and central nodes are smooth/ordinary double points; the desired simultaneous-node germ must be reduced and smooth
projectivity: X and the hypersurface linear system are projective; the factorization is local analytic on that algebraic parameter space
dimension: critical-value target dimension N; factor target dimension R; tangent kernel has the desired excess dimension
codimension: the factor submersion has codimension R and its zero ideal must equal the N-branch smoothing ideal
coefficient_field: C for analytic factorization and deformations; Q for zeta, vanishing cycles, and the terminal pairing
cohomology_theory: analytic critical-value deformation theory, rational vanishing-cycle homology, Saito local intersection cohomology, and rational Betti cohomology
hodge_type: the final local relation functional must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of zeta may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B134-B155, G090-G098, and NG118-NG125
claim: Construct from (X,zeta), without a preselected algebraic carrier, an ordered nodal critical-value germ tau together with an analytic submersion f to C^R and an analytic rank-R matrix A such that tau=A f; retain the uniform value matroid, positive adjoint defect, nonzero primitive image, rational type, and nonzero specified Saito pairing.
falsifier: failure of rank A(0)=R, failure of ideal equality between tau and f, a singular or nonreduced zero germ, zero adjoint defect or primitive image, or zero specified pairing
---

# G099 — Construct an all-order factorization without a carrier

B155 shows that finite Kuranishi calculations cannot close G098. The
smallest auditable all-order certificate is

\[
 \tau=A\,f,
\]

where

\[
 f:(|L|,[s])\longrightarrow(\mathbf C^R,0)
\]

is an analytic submersion and
\(A:(|L|,[s])\to\operatorname{Mat}_{N\times R}\) has rank \(R\) at the
origin. This forces

\[
 (\tau_1,\ldots,\tau_N)=(f_1,\ldots,f_R)
\]

and supplies the reduced smooth saturated germ required by G090.

For an arbitrary \((X,\zeta)\), G099 must construct this factorization
together with:

1. a uniform rank-\(R\) node-value matroid at B141's superlinear scale;
2. isolated ordinary double points and the required multipart partition;
3. positive adjoint defect and nonzero primitive ambient image;
4. a rational type-\((0,0)\) Saito functional nonzero on \(\zeta\).

The moving-carrier incidence gives such a factorization because its smooth
ideal is already known. NG118 prevents using that carrier for an arbitrary
specified class. No carrier-free structural factorization is known.
