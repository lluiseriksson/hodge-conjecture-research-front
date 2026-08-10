---
brick_id: NG072
status: NO-GO
base_field: C with rational type-(0,0) Hodge structures
variety: an arbitrary projective collision carrying a liftable nearby B058 detector
smoothness: generic fiber smooth; special target clean nodal
projectivity: collision projective
dimension: ambient 2n; hyperplane fibers 2n-1
codimension: middle codimension n
coefficient_field: Q
cohomology_theory: nearby/vanishing-cycle long exact sequence, dual Hodge structures, perverse grade, B022 quotients, and pairing
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B083, B096, G059
claim: The equation can(t_psi)=0, equivalently existence of a special lift, forces the detector functional to annihilate the preceding ambiguity-boundary image.
falsifier: an exact type-(0,0) sequence with liftable t_psi and F composed with d nonzero
---

# NG072 — Liftability does not kill the ambiguity-boundary functional

**Status:** NO-GO

The equation $\mathrm{can}(t_\psi)=0$ places the specified nearby vector in
$\operatorname{im}u$. It imposes no condition on the independent covector
$F$ restricted to $\ker u=\operatorname{im}d$.

For a strict type-$(0,0)$ countermodel, take

\[
 W=\mathbf Q,
 \quad S=\mathbf Q^2,
 \quad P=\mathbf Q,
 \quad d(w)=(0,w),
 \quad u(x,y)=x.
\]

Then $t_\psi=1$ is liftable, while $F(x,y)=y$ satisfies
$F\circ d=\mathrm{id}\ne0$. The first B096 branch holds.

The re-entry condition is G060: compute $F\circ d$ rather than assuming it
vanishes; construct the descended pairing square only in the zero branch.
