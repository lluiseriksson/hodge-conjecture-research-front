---
brick_id: B123
status: PROVED
base_field: C with rational coefficients
variety: the original plane-net incidence family restricted to a transverse disk through a clean nodal hyperplane Y_p, with nearby smooth fiber Y_t
smoothness: ambient X, disk total space, and nearby fiber smooth; central fiber has finitely many ordinary double points
projectivity: X and the disk degeneration projective/proper
dimension: dim_C X=2n; hyperplane fibers d=2n-1; disk base dimension 1
codimension: middle cycle codimension n; singular support finite
coefficient_field: Q
cohomology_theory: special and limit Betti cohomology, vanishing-cycle exact sequence, perverse filtration, local intersection cohomology, and Saito relation/extra duality
hodge_type: the nodal relation/extra grade is type (0,0) after Q(n); the vanishing conclusion is rational
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed or constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B026, B081, B093, B107-B109, B117-B122, S022, S037
claim: In the clean nodal original disk, B107's relation filtration step S_0 is the extra-cohomology kernel of specialization H^(d+1)(Y_p)->H^(d+1)(Y_t); hence u_Delta(S_0)=0 and every nonzero nearby class has nonzero filtered obstruction.
falsifier: a class in the clean-nodal relation grade with nonzero specialization, or a nonzero nearby class lying in u_Delta(S_0)
---

# B123 — The relation grade is killed by specialization

**Status:** PROVED

For B120's transverse disk, Saito's isolated-singularity exact sequence in
S022 Proposition 1 contains

\[
 H^d(Y_t,\mathbf Q)
 \longrightarrow
 \bigoplus_{y\in\operatorname{Sing}Y_p}H^d(Z_{y,t},\mathbf Q)
 \longrightarrow
 H^{d+1}(Y_p,\mathbf Q)
 \xrightarrow{u_\Delta}
 H^{d+1}(Y_t,\mathbf Q)
 \longrightarrow0.
\]

Define the extra cohomology

\[
 E(Y_p)=\ker u_\Delta.
\]

Saito identifies its dual with the relation kernel among the local vanishing
cycles. B009/B093 identify that same relation channel with the full-support
\(E_\infty^{-1,0}\) stalk grade. Thus the relation grade in the special
group is precisely the extra-cohomology subspace killed by specialization.

B118 proves that the lower point grade \(E_\infty^{0,-1}\) vanishes in the
original incidence pushdown. Therefore B107's filtration step \(S_0\), whose
associated quotient is the relation grade and whose only possible lower
piece was that point grade, identifies canonically with \(E(Y_p)\). Hence

\[
 \boxed{u_\Delta(S_0)=0.}
\]

By B122, \(u_\Delta:S\to P_\Delta\) is surjective. For every nonzero
\(t_\Delta\in P_\Delta\), B108's filtered obstruction is consequently

\[
 \omega_{\mathrm{fil}}(t_\Delta)
 =[t_\Delta]
 \in P_\Delta/u_\Delta(S_0)
 =P_\Delta,
\]

and is nonzero.

## Directional consequence

A Saito relation cannot be obtained by lifting a nonzero ordinary nearby
cohomology class into the relation filtration step. It appears in the
opposite exact-sequence direction: as the local boundary of a relative class

\[
 \partial:H_{2n}(Y_t,Z_t;\mathbf Q(n))
 \longrightarrow H_{2n-1}(Z_t;\mathbf Q(n)).
\]

This is the direction already encoded by B099-B101 and G064-G065.

## Scope guard

B123 does not say the relation group is zero. It says it maps to zero under
specialization. A nonzero relation can still have a nonzero primitive
ambient image and detect \(\zeta\); constructing its selected relative
boundary is the active geometric problem. The theorem applies to the clean
nodal isolated-singularity disk and does not assert the same filtration
identity for arbitrary non-isolated degenerations.
