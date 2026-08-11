---
brick_id: B133
status: PROVED
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X and a nodal universal-hyperplane fiber over a quasi-local normal-crossing discriminant point
smoothness: X and nearby fibers are smooth; the central fiber has r ordinary double points with independently smoothable local branches
projectivity: X and the hyperplane family are projective
dimension: dim_C X=2n; fiber dimension 2n-1; the minimal case has a codimension-two parameter stratum and r=2
codimension: middle codimension n on X; the local parameter support has codimension r in the transverse normal-crossing model
coefficient_field: Q, with Q(n) in the Hodge application
cohomology_theory: rational local intersection cohomology, Picard-Lefschetz monodromy, the normal-crossing monodromy complex, and filtered de Rham survival
hodge_type: the relation channel is rational type (0,0) after Q(n); no nonzero class coordinate is inferred
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B008-B010, B026, B128, B132, B134, G088, S009, S021-S022, S024
claim: At a quasi-local normal-crossing nodal point p, the intrinsic ordinary cohomological target of the canonical filtered section is the dual of the rational relation kernel ker(Q^r -> H_(2n-1)(X_s,Q)); hence independent vanishing cycles force every B132 associated-graded stalk class to die, and for r=2 a nonzero target requires the two nonzero cycles to be proportional.
falsifier: a transverse nodal point whose vanishing cycles are independent but whose degree-minus-d-plus-one full-support IC stalk is nonzero, or two nonzero independent cycles with nonzero relation kernel
---

# B133 — Two-branch boundary relation criterion

**Status:** PROVED

Let \(p\) parametrize a nodal hyperplane section with independently
smoothable nodes and quasi-local normal-crossing discriminant branches. Let

\[
 \delta_1,\ldots,\delta_r\in
 H_{2n-1}(X_s,\mathbf Q(n))
\]

be the Picard-Lefschetz vanishing cycles in a nearby smooth fiber. B009
computes the polarized homological model of the full-support degree-one
local IC channel as

\[
 R_p=
 \ker\!\left(
 \mathbf Q^r\xrightarrow{\partial}
 H_{2n-1}(X_s,\mathbf Q(n))\right),
 \qquad
 \partial(e_i)=\delta_i.
\]

B134 supplies the intrinsic typing

\[
 \mathcal H^{-d+1}(IC(V))_p\simeq R_p^\vee.
\]

B128 identifies this ordinary stalk with the target in which a local
incidence edge class \(s_m(\zeta)_p\) must land. Consequently any filtered
stalk representative of the canonical B132 section that survives to
ordinary cohomology is a functional on \(R_p\), not a selected vector of
\(R_p\).

## Minimal codimension-two case

For \(r=1\), the map sends \(1\) to a nonzero nodal vanishing cycle and its
kernel is zero, recovering B008's smooth-discriminant exclusion.

For \(r=2\),

\[
 R_p=\ker\!\left(
 \mathbf Q^2\longrightarrow
 \langle\delta_1,\delta_2\rangle_{\mathbf Q}\right).
\]

Thus the dual target has the same dimension, and:

- if \(\delta_1,\delta_2\) are independent, \(R_p=0\);
- if both are nonzero and proportional, then \(\dim_{\mathbf Q}R_p=1\);
- writing \(\delta_2=c\delta_1\), a generator is
  \(c e_1-e_2\), while the cohomological coordinate is evaluation on this
  generator.

Therefore a transverse double-node point can support G088 only when its two
vanishing cycles form a rational matching relation. Merely having a
codimension-two intersection of discriminant branches is insufficient.

## Scope guard

B133 gives a necessary local receptacle and its exact rank. B134 identifies
the specified functional on it. B133 does not
construct a proportional two-node fiber, does not show that
\(s_m(\zeta)_p\) has nonzero coordinate in the one-dimensional kernel, and
does not prove the canonical filtered section survives. Those are
class-specific parts of G088.
