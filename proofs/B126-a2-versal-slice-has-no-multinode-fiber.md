---
brick_id: B126
status: PROVED
base_field: C
variety: the suspended A2 miniversal hypersurface x^3+s*x+t+sum(z_i^2)=0 over the (s,t)-plane
smoothness: total space smooth; noncentral discriminant fibers have one ordinary double point; central fiber has one A2 singularity
projectivity: no; local analytic-algebraic model only
dimension: fiber dimension r for arbitrary r at least 1; base dimension 2
codimension: cusp discriminant codimension one; no multipart nodal stratum in the local base
coefficient_field: Q for downstream homology; the calculation is algebraic over C
cohomology_theory: critical-locus algebra, Milnor singularity type, and local vanishing cycles
hodge_type: none asserted; downstream nodal relations would be type (0,0) after Q(n)
cycle_class_map: none
cycle_equivalence: none
scope: relative and fiberwise
dependencies: B008, B025, B064, G032, G084, NG040
claim: In the suspended A2 miniversal two-parameter slice, every noncentral discriminant fiber has exactly one ordinary double point and the central fiber has one A2 singularity; no nearby fiber has two nodes, so local versal deformation cannot produce a multipart nodal relation target.
falsifier: a parameter in the local (s,t)-base whose fiber has two distinct ordinary double points
---

# B126 — The local A2 versal slice has no multinode fiber

**Status:** PROVED

Consider B064's smooth total space

\[
 x^3+sx+t+\sum_{i=1}^r z_i^2=0.
\]

A fiber critical point satisfies

\[
 3x^2+s=0,
 \qquad z_1=\cdots=z_r=0,
 \qquad x^3+sx+t=0.
\]

Eliminating \(s,t\) parametrizes the critical values by

\[
 x\longmapsto(s,t)=(-3x^2,2x^3).
\]

This parametrization is injective. Indeed, equal parameters for \(x,y\)
give \(x^2=y^2\) and \(x^3=y^3\). If \(y=-x\), the cubic equality forces
\(x=0\), hence \(x=y\); otherwise \(x=y\) directly. Therefore every
discriminant fiber has exactly one critical point.

For \(x\ne0\), the fiber Hessian has diagonal entries \(6x,2,\ldots,2\)
and is nondegenerate, so that point is an ordinary double point. At \(x=0\)
the fiber is the suspended \(A_2\) germ. Thus the local base contains no
fiber with two ordinary double points.

## Consequence

A nonzero Saito nodal relation requires a global dependence among at least
two local vanishing cycles. The local \(A_2\) versal slice has no multipart
nodal parameter at all. Hence a detecting class supported at its cusp cannot
be moved to G084's clean nodal locus by local versal adjacency alone; a
global topology-changing deformation is necessary.

## Scope guard

This does not exclude adding or recolliding nodes elsewhere in a global
hyperplane system. It excludes only a purely local cleanup theorem inside
the suspended \(A_2\) miniversal slice.
