---
brick_id: G100
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a nonzero primitive rational middle Hodge class zeta, and the full ordered-node critical-value germ in a complete linear system
smoothness: X is smooth and projective; the selected hypersurface has isolated ordinary double points; the desired node germ is reduced and smooth
projectivity: the ambient deformation is the full projective complete linear system, not an arbitrary nonlinear analytic pullback
dimension: N ordered nodes; critical-value differential rank R<N; relation space dimension N-R
codimension: the simultaneous-node ideal must have exactly R minimal generators and codimension R
coefficient_field: C for analytic syzygies and deformations; Q for zeta, vanishing cycles, and the terminal pairing
cohomology_theory: analytic local algebra of the discriminant, rational vanishing-cycle homology, Saito local intersection cohomology, and rational Betti cohomology
hodge_type: the retained local relation functional must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of zeta may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B134-B157, G090-G099, and NG118-NG125
claim: Construct carrier-free nodal data for which the hidden-generator module H_tau vanishes, equivalently every linear node-value relation lifts to an analytic syzygy of the full critical-value germ, while retaining the uniform value matroid, positive adjoint defect, nonzero primitive ambient image, rational type, and nonzero specified Saito pairing.
falsifier: a nonzero hidden-generator class, failure of any lifted syzygy identity to all analytic orders, loss of full-linear-system scope, zero adjoint or ambient rank, or zero specified pairing
---

# G100 — Kill the hidden generators in the full linear system

B156 replaces G099's matrix factorization by the exact finite-dimensional
obstruction

\[
 H_\tau=\ker\left(I_\tau/\mathfrak m I_\tau
          \longrightarrow\mathfrak m/\mathfrak m^2\right).
\]

The factorization part of G099 is equivalent to \(H_\tau=0\). Equivalently,
if

\[
 L=\ker\left(\mathbf C^N\longrightarrow
              \mathfrak m/\mathfrak m^2\right)
\]

is the space of linear relations among the node-value differentials, every
element of \(L\) must lift to an analytic identity

\[
 \sum_i a_i(s)\tau_i(s)=0
\quad\text{with}\quad
 (a_1(0),\ldots,a_N(0))\in L.
\]

It is enough to lift one basis of \(L\). Their coefficient rows form
B156's matrix \(S\), whose analytic kernel gives \(\tau=A f\).

G100 asks for those lifts in the **full** complete-linear-system germ and
simultaneously retains:

1. B141's superlinear uniform value matroid;
2. isolated multipart ordinary double points;
3. positive adjoint defect and nonzero primitive ambient image;
4. a rational type-\((0,0)\) Saito functional nonzero on the specified
   \(\zeta\).

B157 shows why local Morse and Picard--Lefschetz data cannot supply the
lifts: those data remain fixed while an arbitrary \(H_\tau\) is inserted
by nonlinear projective pullback. A successful proof must use a genuinely
global constraint of the full linear-system incidence together with the
class-specific detector.
