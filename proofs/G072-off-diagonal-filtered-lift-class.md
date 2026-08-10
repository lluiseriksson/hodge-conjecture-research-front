---
brick_id: G072
status: EXPLORATORY
base_field: C with all collision, filtered Hodge-module, and chain data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified B058 detector t_psi, and an actual projective plane-net collision to a clean nodal hyperplane target H
smoothness: X and generic hyperplane fibers smooth; target has finitely many ordinary double points; semistable source regular where required
projectivity: X, hyperplane family, collision, and proper pushdown projective
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; plane base dimension 2
codimension: middle codimension n; H is a point of the plane base with finite nodal singular support
coefficient_field: Q
cohomology_theory: nearby/special mixed Hodge-module stalks, perverse filtration, chain-level lift, quotient by S_0 plus ker(u), and dual separation
hodge_type: S, S_0, t_psi, the ordinary lift, and all maps restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B058, B071-B084, B107-B114, G041-G071, G073-G076, NG050-NG090, S023, S037
claim: For the actual collision, construct an ordinary lift s of t_psi with its full perverse extension data and prove [s]=0 in S/(S_0+ker u), equivalently construct a corrected lift in S_0; associated-graded calculations alone are not admissible.
falsifier: undefined ordinary lift or filtration, nonzero quotient class, a separating dual functional, wrong rational Hodge type, or use only of associated-graded ranks without the off-diagonal extension
---

# G072 — Compute the off-diagonal filtered-lift class

**Status:** EXPLORATORY

For the actual collision, realize the selected nearby detector
$t_\psi\in\operatorname{im}u$ and choose any ordinary lift

\[
 s\in S,
 \qquad u(s)=t_\psi.
\]

Retain the filtered extension data of $s$, not merely its classes in the
associated grades. Compute B109's lift-side obstruction

\[
 \widetilde\omega_{\mathrm{fil}}(t_\psi)
 =[s]\in S/(S_0+\ker u)
\]

and prove

\[
 \boxed{[s]=0.}
\]

Equivalently, exhibit $k\in\ker u$ such that $s+k\in S_0$. A dual attack may
instead prove that every functional on $\operatorname{im}u$ annihilating
$u(S_0)$ also annihilates $t_\psi$.

B109/NG085 prohibit replacing this calculation by dimensions, support ranks,
or maps on $E_\infty$: the off-diagonal extension between grades changes the
answer while all such data remain fixed.

The box closes G071 and supplies G070's filtered lift. B110/NG086 show that
the box is not defined for the selected detector until G073 constructs the
actual nearby realization and an ordinary lift. G072 is therefore the next
filtered calculation after G073, not the current first attackable geometric
brick.
