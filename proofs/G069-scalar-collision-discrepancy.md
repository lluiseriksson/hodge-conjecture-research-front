---
brick_id: G069
status: EXPLORATORY
base_field: C with all collision, Hodge, and comparison data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified nonzero primitive rational Hodge class zeta, its B058 detector c, and a sought actual projective collision to an isolated clean nodal hyperplane section Y_0
smoothness: X and nearby hyperplane fibers smooth; Y_0 has finitely many ordinary double points
projectivity: X, plane-net hyperplane family, and collision projective
dimension: dim_C X = 2n; dim_C Y_0 = 2n-1
codimension: middle codimension n; target singular support finite
coefficient_field: Q
cohomology_theory: B057 thimble detector, nearby and vanishing cycles, the canonical full-support relation stalk, Saito's primitive ambient relation map, and the Hodge pairing
hodge_type: zeta, c, the local relation beta, and its ambient image rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B057-B058, B081, B093-B105, G047-G068, NG069-NG081, S022
claim: For the specified zeta and detector c, construct an actual isolated clean nodal collision and its canonical rational type-(0,0) local relation beta, compute D_zeta(c,beta)=<zeta,c-Phi_(Y_0)(beta)>, and prove D_zeta(c,beta) differs from <zeta,c>.
falsifier: failure to construct the collision or canonical relation, wrong coefficient field or Hodge type, an undefined Saito ambient image, or equality D_zeta(c,beta)=<zeta,c>
---

# G069 — Prove the exact scalar collision inequality

**Status:** EXPLORATORY

For every

\[
 0\ne\zeta\in
 H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))^{(0,0)},
\]

fix B058's detector $c$ with
$b_\zeta=\langle\zeta,c\rangle\ne0$. Construct from the actual
topology-changing plane-net collision:

1. an isolated clean nodal hyperplane section $Y_0$;
2. the canonical full-support relation
   $\beta\in R(Y_0)_1^{(0,0)}$ over $\mathbf Q$; and
3. Saito's ambient class $\Phi_{Y_0}(\beta)$.

Then compute the class-specific scalar

\[
 D_\zeta(c,\beta)
 =\left\langle\zeta,c-\Phi_{Y_0}(\beta)\right\rangle
\]

and prove

\[
 \boxed{D_\zeta(c,\beta)\ne b_\zeta.}
\]

By B105 this is equivalent to
$\langle\zeta,\Phi_{Y_0}(\beta)\rangle\ne0$, exactly S022's terminal
detector condition. Equality $D_\zeta=0$ is a useful sufficient target, but
must not be silently promoted to a necessary obligation.

A canonical collision pair as in G068 remains one possible construction.
If used, it is enough to compute the scalar pairing of the ambient image of
its B104 coset. The coset itself need not vanish.

This gate is falsifiable class by class and contains no assumption that the
desired Hodge class or relation is algebraic.
