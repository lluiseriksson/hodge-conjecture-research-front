---
brick_id: G071
status: EXPLORATORY
base_field: C with all collision, perverse-filtration, and Hodge data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified B058 nearby detector t_psi, and an actual projective plane-net collision to a clean nodal hyperplane target H
smoothness: X and generic hyperplane fibers smooth; target has finitely many ordinary double points; semistable source regular where required
projectivity: X, hyperplane family, collision, and proper pushdown projective
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; plane base dimension 2
codimension: middle codimension n; H is a point of the plane base with finite nodal singular support
coefficient_field: Q
cohomology_theory: nearby and special rational mixed Hodge-module stalks, perverse filtration, local invariant cycles, and quotient obstruction homology
hodge_type: S, S_0, P_psi, t_psi, and u restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B058, B081-B084, B107-B108, G048-G070, NG059-NG084, S023, S037
claim: For the actual class-specific collision, construct the canonical relation-grade step S_0 and the ordinarily liftable t_psi, compute omega_fil(t_psi)=[t_psi] in im(u)/u(S_0), and prove omega_fil(t_psi)=0.
falsifier: undefined collision map or filtration step, t_psi not in im(u), nonzero quotient class, wrong rational Hodge type, or reliance on unproved perverse strictness
---

# G071 — Kill the filtered-lift obstruction

**Status:** EXPLORATORY

For the actual collision construct

\[
 u:S=H^{-1}(i_H^*K)^{(0,0)}
 \longrightarrow P_\psi
\]

and B107's canonical relation-grade filtration step $S_0\subseteq S$.
Realize B057's selected detector as

\[
 t_\psi\in\operatorname{im}u
\]

using the audited ordinary-lift conditions of G048/B084. Then form B108's
canonical obstruction

\[
 \omega_{\mathrm{fil}}(t_\psi)
 =[t_\psi]\in\operatorname{im}u/u(S_0).
\]

Prove

\[
 \boxed{\omega_{\mathrm{fil}}(t_\psi)=0.}
\]

An acceptable proof may:

1. construct an explicit special lift already lying in $S_0$; or
2. prove, from a cited theorem with all hypotheses checked, that the actual
   special-to-nearby map is strict at the relevant perverse step.

Purity, decomposition, local invariant-cycle surjectivity, or strictness for
the Hodge filtration alone do not prove the box by NG084.

Vanishing supplies the filtered lift required by G070. Only then should the
restricted dual-cokernel/evaluation certificate be computed. G071 is the
smallest current geometric gate.

