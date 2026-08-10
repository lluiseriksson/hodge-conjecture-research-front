---
brick_id: G073
status: EXPLORATORY
base_field: C with collision, chain, and mixed-Hodge-module data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified nonzero primitive rational Hodge class zeta, its B058 distributed detector t, and an actual projective plane-net collision to a clean nodal target H
smoothness: X and generic hyperplane fibers smooth; target has finitely many ordinary double points; proper total space and a regular semistable source where required
projectivity: X, hyperplane family, plane net, collision, and proper pushdown projective
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; plane base dimension 2; collision parameter dimension 1
codimension: middle codimension n; H is a point of the plane base with finite nodal singular support
coefficient_field: Q
cohomology_theory: relative thimble complexes, B022 quotient homology, nearby and vanishing rational mixed Hodge-module stalks, local invariant cycles, and primitive ambient homology
hodge_type: the source class, nearby class, ordinary lift, and ambient image rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B059, B081-B084, B088-B091, B110, G047-G055, NG059-NG067, NG086, S023
claim: Construct an actual collision-induced source realization rho carrying the selected B057 distributed class t to a nearby class t_psi in the proper IC model, prove can(t_psi)=0 and choose a rational ordinary lift s, and prove the induced ambient image still pairs nontrivially with the prescribed zeta through both B022 quotients.
falsifier: no collision-induced source map, t_psi outside ker(can), loss in either B022 quotient, wrong rational Hodge type, or zero prescribed pairing for every admissible topology-changing comparison
---

# G073 — Source-realized ordinary collision lift

**Status:** EXPLORATORY

For B058's selected distributed detector $t$, construct an actual projective
collision and a morphism on the relevant chain/cohomology objects inducing

\[
 \rho:H(C_{\mathrm{dist}})^{(0,0)}
 \longrightarrow
 P_\psi=H^{-1}(i_H^*\Psi_fK)^{(0,0)},
 \qquad t_\psi=\rho(t).
\]

The construction must then prove all of the following on the same class:

1. $\operatorname{can}(t_\psi)=0$ in the shifted vanishing-cycle term;
2. there is $s\in S=H^{-1}(i_H^*K)^{(0,0)}$ with $u(s)=t_\psi$;
3. the source, nearby class, and lift are rational and of type $(0,0)$ after
   $\mathbf Q(n)$;
4. the comparison survives the equator-extension and base-locus kernels of
   B022; and
5. its primitive ambient realization has nonzero pairing with the prescribed
   $\zeta$.

Exact recovery of B058's chosen ambient class $c$ is sufficient but not
required by B059; nonzero prescribed pairing is the minimal retained datum.

## Attempt: marked pure-Hurwitz return

G052 proposes a marking that returns $(g,\alpha)$, and B088 would then make
the geometric extension word monodromy invariant. This attempt does not
close the gate. It begins after the word has already been placed in the
collision coefficient object, so it does not construct $\rho$. Even if that
typing gap were supplied, B091 proves that the pure-Hurwitz positive
local-boundary realization of the nonzero B058 detector is zero. The route
therefore loses the required detector channel.

This failed attempt is NG086. The next admissible construction must compute
the genuinely topology-changing excess map isolated in G055; it cannot be a
pure change of Hurwitz basis.

## Propagation

Once G073 is proved, G072 becomes defined for this actual $s$ and may compute
$[s]\in S/(S_0+\ker u)$. Vanishing then closes G071's filtered-lift condition
and permits G070's restricted dual certificate. G073 itself constructs no
algebraic cycle and does not resolve the terminal conjecture.
