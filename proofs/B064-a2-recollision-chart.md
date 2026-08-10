---
brick_id: B064
status: PROVED
base_field: C
variety: the smooth local hypersurface Y_r given by x^3+s*x+t+sum(z_i^2)=0, projected to the (s,t)-plane
smoothness: the total space is smooth; generic discriminant fibers have one ordinary double point and the origin fiber has an A2 singularity
projectivity: no; this is a local analytic-algebraic chart, and no global projective realization is asserted
dimension: Y_r has dimension r+2 and its fibers have dimension r
codimension: the discriminant is a codimension-one cusp in the two-dimensional base
coefficient_field: Q for the constant Hodge module and C for the differential calculation
cohomology_theory: local singularity theory, vanishing cycles, and mixed Hodge modules
hodge_type: none asserted; no detector class is selected
cycle_class_map: none
cycle_equivalence: none
scope: relative and fiberwise
dependencies: B062, B063, and S042
claim: The A2 collision chart has cusp discriminant 4s^3+27t^2=0 and its critical locus is not contained in the coordinate boundary st=0, so the raw morphism is not a geometric without-slopes morphism and the graph-pair theorem cannot be invoked without a separate b-function check.
falsifier: containment of the computed critical locus in the inverse image of st=0 or a smooth normal-crossing discriminant at the origin
---

# B064 — The raw \(A_2\) recollision chart is not without slopes

**Status:** PROVED  
**Gate:** G033 / G034

## Local chart

For \(r\ge1\), let
\[
Y_r=\left\{x^3+s x+t+\sum_{i=1}^{r}z_i^2=0\right\}
\subset\mathbf C_x\times\mathbf C_z^r\times\mathbf C_s\times\mathbf C_t
\]
and let \(g:Y_r\to\mathbf C^2\) be projection to \((s,t)\). Since the derivative of the defining equation with respect to \(t\) is one, \(Y_r\) is smooth.

Solving for \(t\) presents the map as
\[
(x,z,s)\longmapsto
\left(s,-x^3-sx-\sum z_i^2\right).
\]
Its differential has rank less than two exactly when
\[
s=-3x^2,\qquad z_1=\cdots=z_r=0.
\]
On this critical locus, \(t=2x^3\). Eliminating \(x\) gives the discriminant
\[
4s^3+27t^2=0.
\]

For \(x\ne0\), the fiber Hessian is nondegenerate, so the discriminant's smooth points parametrize ordinary double points. At \(x=0\), the fiber germ is
\(x^3+\sum z_i^2=0\), the suspended \(A_2\) singularity where the two Morse critical values coalesce.

## Without-slopes test

Kochersperger S042 recalls a necessary geometric feature of a morphism without slopes: its critical locus lies over the union of the chosen coordinate hyperplanes. Here critical points with \(x\ne0\) have
\[
s=-3x^2\ne0,\qquad t=2x^3\ne0.
\]
Thus
\[
\operatorname{Crit}(g)\not\subset g^{-1}(\{st=0\}),
\]
and the raw pair of coordinate functions \((s,t)\) is not a geometric without-slopes morphism. Consequently B063 cannot be applied merely by citing that geometric condition. A direct application to the graph-pushed constant Hodge module would still require the separate \(V\)-multifiltration/Bernstein-Sato definition for that exact pair; no such check is presently available.

## Geometric obstruction

The discriminant is an irreducible cusp, not a smooth or simple-normal-crossing boundary at the collision. It therefore lies outside the raw Li-clean arrangement geometry already controlled by B054. A target blow-up can resolve the cusp, but descent of the resulting comparison and exclusion of exceptional-only detector terms are additional obligations.

## Non-claims

- Failure of this sufficient hypothesis does not prove that the two particular iterated nearby-cycle objects are nonisomorphic.
- No global projective recollision or class-specific detector is constructed.
- No Hodge class is proved algebraic.
