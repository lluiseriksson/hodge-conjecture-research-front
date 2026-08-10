---
brick_id: NG061
status: NO-GO
base_field: C
variety: a B058 plane-net detector and a one-parameter deformation of plane-net data toward a collision
smoothness: detector-loop fibers and generic collision-parameter fibers smooth; endpoint singular
projectivity: hyperplane and collision families projective
dimension: ambient 2n, hyperplane fibers 2n-1, plane-net base 2, and collision parameter 1
codimension: middle codimension n; collision endpoint has positive parameter codimension
coefficient_field: Q
cohomology_theory: Picard-Lefschetz monodromy, nearby cycles, local invariant cycles, and relative homology
hodge_type: no Hodge type is inferred from either invariance statement
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B057-B058, B084, G047-G048
claim: The B057 condition g(alpha)=alpha for a loop in the hyperplane complement automatically implies that the resulting nearby collision class is fixed by monodromy around the collision parameter.
falsifier: the two monodromies act on different parameter directions and no comparison identifying their actions has been constructed
---

# NG061 — Detector-loop invariance is not collision invariance

**Status:** NO-GO

B057 starts with a loop $g$ in the smooth hyperplane-parameter complement
and a fiber class satisfying $g\alpha=\alpha$. G047 introduces a different
pointed curve $T$ that deforms the plane-net data toward a collision. Its
punctured parameter has its own monodromy $T_{\mathrm{coll}}$.

No formal implication gives

\[
 g\alpha=\alpha
 \quad\Longrightarrow\quad
 T_{\mathrm{coll}}t_\psi=t_\psi.
\]

The first equality closes the boundary of the B057 extension chain. The
second is the hypothesis needed to apply B084's local invariant-cycle
surjection. Relating them requires a two-parameter comparison that transports
the ordered thimble chain while the net itself degenerates.

The re-entry condition is G049: construct $t_\psi$ in a proper collision
model and compute the collision monodromy on that specified class.
