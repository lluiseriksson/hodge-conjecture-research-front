---
brick_id: NG082
status: NO-GO
base_field: C with rational Hodge structures and collision stalks
variety: an arbitrary polarized smooth projective complex 2n-fold with a specified primitive rational Hodge class, a B058 global tube detector, and a sought clean nodal collision
smoothness: ambient and generic hyperplane fibers smooth; target clean nodal
projectivity: ambient variety, plane net, and collision projective
dimension: ambient 2n; hyperplane fibers 2n-1
codimension: middle codimension n; nodal singular support finite
coefficient_field: Q
cohomology_theory: primitive Hodge pairing, global tube homology, Saito local relation map, and nearby/special stalk exactness
hodge_type: all detector and relation classes rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B010, B058, B095, B105-B106, G059, G069, S022-S023
claim: Writing Saito's terminal nonzero pairing as D_zeta(c,beta) != <zeta,c> using a B058 detector c makes it a genuine reduced collision gate or proves that beta is descended from c.
falsifier: B106's algebraic cancellation of c and the absence in S022-S023 of a comparison from an arbitrary global tube detector to a chosen local relation
---

# NG082 — An auxiliary detector does not create collision provenance

**Status:** NO-GO

- **Route:** insert B058's global tube detector $c$ into the discrepancy
  $D_\zeta(c,\beta)$ and count the inequality
  $D_\zeta(c,\beta)\ne\langle\zeta,c\rangle$ as a reduced collision theorem.
- **Valid input:** B058 gives a global $c$ with nonzero pairing, and B105's
  inequality is equivalent to detection by the chosen local relation.
- **Invalid inference:** the occurrence of $c$ in the notation links
  $\beta$ to the global detector or makes the condition easier than B010.
- **Precise obstruction:** B106 cancels $c$ identically, leaving
  $\langle\zeta,\Phi_{Y_0}(\beta)\rangle\ne0$. This is exactly the terminal
  Saito condition. S022 constructs $\Phi_{Y_0}$ from a local relation, while
  S023 constructs global tube classes; neither source supplies the missing
  topology-changing comparison between them.
- **Re-entry condition:** use G070's filtration-restricted
  special-to-nearby map $u_0$, detector class $t_\psi$, and canonical
  functional $F_0$. Prove either the cokernel branch $[F_0]\ne0$ or, after
  proving $[F_0]=0$, the nonzero descended evaluation
  $\lambda(t_\psi)\ne0$.
