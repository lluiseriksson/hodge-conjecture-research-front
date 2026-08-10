---
brick_id: G074
status: EXPLORATORY
base_field: C with collision chains, nearby-cycle data, and Hodge structures over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified nonzero primitive rational Hodge class zeta, its selected B058 detector t, and an actual projective marked collision to a clean nodal target
smoothness: X and generic hyperplane fibers smooth; target has finitely many ordinary double points; proper or semistable comparison model regular where required
projectivity: X, hyperplane family, plane net, collision, and comparison model projective
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; comparison chains degree 2n; collision parameter dimension 1
codimension: middle codimension n; target is a point of the plane base with finite nodal singular support
coefficient_field: Q
cohomology_theory: selected relative thimble chains, marked relative target chains, nearby and vanishing cycles, B022 quotient homology, and primitive ambient pairing
hodge_type: the selected excess and induced nearby class rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B059, B083-B084, B088-B091, B110-B112, G055, G073, NG086-NG088, S023
claim: For the selected detector t, construct an actual topology-changing comparison chain gamma_sp and a marked pure-Hurwitz reference gamma_H with the same boundary, compute the excess class [gamma_sp-gamma_H], and prove that it induces an ordinarily liftable rational type-(0,0) nearby class surviving both B022 quotients with nonzero prescribed pairing.
falsifier: inability to construct either selected chain with a common marked boundary, zero or undefined excess, wrong Hodge type, nonzero vanishing-cycle obstruction, death in a B022 kernel, or zero pairing for every admissible collision
---

# G074 — Compute the selected topology-changing excess

**Status:** EXPLORATORY  
**Parent gate:** G073

Track only B058's selected representative $t$. In an actual marked
topology-changing collision, construct:

\[
 \gamma_{\mathrm{sp}},\gamma_H\in C_{2n}(C_H;\mathbf Q(n)),
 \qquad
 \partial\gamma_{\mathrm{sp}}=\partial\gamma_H,
\]

where $\gamma_H$ is the pure-Hurwitz reference and
$\gamma_{\mathrm{sp}}$ is the actual collision realization. Form B112's
well-defined selected excess

\[
 e_t=\gamma_{\mathrm{sp}}-\gamma_H,
 \qquad
 [e_t]\in H_{2n}(C_H;\mathbf Q(n)).
\]

The gate is passed only by proving on this exact class:

1. $[e_t]$ is rational type $(0,0)$ after $\mathbf Q(n)$;
2. its induced nearby class $t_\psi$ satisfies
   $\operatorname{can}(t_\psi)=0$ and hence has an ordinary rational lift;
3. it survives the equator-extension and base-locus kernels of B022; and
4. its primitive ambient image pairs nontrivially with the prescribed
   $\zeta$.

B091 shows that the pure-Hurwitz reference alone cannot carry the detector.
B112/NG088 show that the common marked boundary does not compute the excess:
the actual collision chain must be constructed and its homology coordinate
evaluated. A map on unrelated thimble classes is not required by B111.

G074 is the class-specific core of G055 and the current smallest geometric
subgate of G073. It does not assume that the desired Hodge class is
algebraic.
