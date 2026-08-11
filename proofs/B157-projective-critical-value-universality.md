---
brick_id: B157
status: PROVED
base_field: C
variety: a smooth projective complex d-fold X, a sufficiently high power of an ample line bundle, N distinct points, and an arbitrary analytic base germ B with an ordered critical-value germ tau:B->C^N
smoothness: X is smooth; the central hypersurface can be chosen smooth away from the N prescribed ordinary double points; the node Hessians remain nondegenerate in the constructed family
projectivity: X and the hypersurfaces are projective; the realizing map from B to the complete linear system is generally nonlinear analytic
dimension: dim X=d; N prescribed nodes; base dimension arbitrary finite; critical-value target dimension N
codimension: each node branch is tau_i=0 on B; no expected-codimension or smooth-excess conclusion is asserted
coefficient_field: C for jets and analytic families; Q for the unchanged local A1 Milnor lattices
cohomology_theory: coherent jet evaluation, Serre vanishing, Bertini, parameterized holomorphic Morse lemma, and local vanishing homology
hodge_type: no global Hodge type or specified detector class is produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used; no algebraic representative of a specified Hodge class is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: S055, S065, Bertini, and the parameterized holomorphic Morse lemma
claim: After replacing an ample line bundle by a sufficiently high power, every analytic germ tau:B->C^N with tau(0)=0 is realized as the ordered critical-value germ at N fixed projective ordinary-double-point charts, with fixed nondegenerate quadratic 2-jets. Consequently nodewise A1 Hessians, local Milnor lattices, and individual Picard-Lefschetz operators impose no higher analytic relation among the tau_i. The realizing base map is generally nonlinear, so the theorem does not remove the full-linear-system incidence gate.
falsifier: an analytic tau that cannot be realized after surjective two-jet evaluation, movement of a prescribed critical point, degeneration of a fixed Hessian, or an inference here about the full universal linear-system germ rather than the constructed nonlinear pullback
---

# B157 — Projective ODP charts realize arbitrary critical-value germs

Let \(X\) be a smooth projective complex variety, \(L\) ample, and
\(p_1,\ldots,p_N\) distinct closed points. Fix local trivializations of
\(L\) and nondegenerate quadratic forms \(q_i\) on \(T_{p_i}X\). Let

\[
 \tau=(\tau_1,\ldots,\tau_N):(B,0)\longrightarrow(\mathbf C^N,0)
\]

be any analytic germ.

## Jet construction

Put

\[
 Z=\coprod_i\operatorname{Spec}(\mathcal O_{X,p_i}/\mathfrak m_{p_i}^3).
\]

For \(k\gg0\), Serre vanishing applied to
\(\mathcal I_Z\otimes L^k\) makes

\[
 H^0(X,L^k)\longrightarrow H^0(Z,L^k|_Z) \tag{1}
\]

surjective. Choose a section \(s_0\) whose two-jet at \(p_i\) is exactly
\(q_i\): zero value, zero linear part, and prescribed nondegenerate
quadratic part. Choose sections \(u_j\) with two-jets

\[
 j^2_{p_i}(u_j)=\delta_{ij};
\]

that is, constant term \(\delta_{ij}\) and zero linear and quadratic parts.
After increasing \(k\), \(\mathcal I_Z\otimes L^k\) is generated away from
the prescribed points. Bertini therefore permits \(s_0\) to be chosen
smooth away from them while retaining its fixed jets.

Define the projective hypersurface family by the analytic map

\[
 s(t)=s_0+\sum_{j=1}^N\tau_j(t)u_j. \tag{2}
\]

At \(p_i\), equation (2) has value \(\tau_i(t)\), zero spatial gradient,
and Hessian \(q_i\). Hence \(p_i\) is a fixed nondegenerate critical point
and its critical value is exactly \(\tau_i(t)\). In particular, the
ordered simultaneous-node ideal on \(B\) is
\((\tau_1,\ldots,\tau_N)\).

The parameterized holomorphic Morse lemma identifies each local chart with

\[
 q_i(z)+\tau_i(t).
\]

Thus its local \(A_1\) Milnor lattice, Hessian class, and individual
Picard--Lefschetz reflection are independent of every higher coefficient of
\(\tau\).

## Exact scope

This is a projective realization, but \(t\mapsto[s(t)]\) is generally a
nonlinear analytic map into \(|L^k|\). Restricting a smooth universal
incidence germ to a nontransverse nonlinear base can create arbitrary
nilpotents. Therefore B157 proves only the following no-go statement:
nodewise ODP and local Picard--Lefschetz data do not force B156's syzygy
lifts. It does **not** prove that the full complete-linear-system germ has
arbitrary critical values, and it does not address the class-specific
Saito pairing.
