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
dependencies: B022, B057-B059, B071-B077, B081-B084, B088-B091, B110-B118, G041-G055, G074-G080, NG050-NG067, NG080, NG086-NG094, S022-S023, S037, S052
claim: Construct an actual class-specific collision certificate carrying the selected B057 distributed class t to a nearby class t_psi in the proper IC model, prove can(t_psi)=0 and choose a rational ordinary lift s, and prove the induced ambient image still pairs nontrivially with the prescribed zeta through both B022 quotients; no map on unrelated distributed classes is required.
falsifier: no collision-certified realization of the selected class, t_psi outside ker(can), loss in either B022 quotient, wrong rational Hodge type, or zero prescribed pairing for every admissible topology-changing comparison
---

# G073 — Source-realized ordinary collision lift

**Status:** EXPLORATORY

For B058's selected distributed detector $t$, construct an actual projective
collision and a class-specific marked comparison, chain, or relative bordism
certifying

\[
 t\rightsquigarrow
 t_\psi\in
 P_\psi=H^{-1}(i_H^*\Psi_fK)^{(0,0)}.
\]

B111/NG087 show that this certificate need not extend to a map on the entire
distributed complex.

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
collision coefficient object, so it does not construct the selected
realization certificate. Even if that
typing gap were supplied, B091 proves that the pure-Hurwitz positive
local-boundary realization of the nonzero B058 detector is zero. The route
therefore loses the required detector channel.

This failed attempt is NG086. B112/NG088 show that even equality of every
marked boundary does not determine the missing excess class. G074 is the
current subgate: construct and compute the selected topology-changing excess
isolated in G055; it cannot be a pure change of Hurwitz basis.

## Propagation

Once G073 is proved, G072 becomes defined for this actual $s$ and may compute
$[s]\in S/(S_0+\ker u)$. Vanishing then closes G071's filtered-lift condition
and permits G070's restricted dual certificate. G080 is the original-object
nearby-class-and-lift portion of G073. B121/NG097 correct the next step:
ordinary nonzeroness does not remove the constant ambient grade. B123/NG099
then prove filtered liftability is impossible for a nonzero nearby class.
G065 is the directionally valid replacement mechanism: construct the
relation as the marked boundary of the selected relative class; B117-B119
then control its support and type. B124/NG100 show that its exact ambient
target is stronger than active gate G008.
G073 itself constructs no
algebraic cycle and does not resolve the terminal conjecture.
