---
brick_id: G002
status: CONDITIONAL
base_field: C
variety: smooth projective family f:Y->T
smoothness: f smooth; T connected and smooth after permitted alteration
projectivity: f projective
dimension: relative dimension 2m
codimension: m
coefficient_field: Q
cohomology_theory: relative singular Betti cohomology R^{2m}f_*Q
hodge_type: flat section fiberwise of type (m,m)
cycle_class_map: relative codimension-m Chow cycles to fiberwise H^{2m}(-,Q(m))
cycle_equivalence: rational equivalence on fibers
scope: relative and fiberwise
dependencies: existence of an algebraic anchor; dominance of a relative Chow/Hilbert component
claim: If a relative cycle component with the prescribed class dominates the Hodge locus after surjective proper base change, the class is algebraic on every fiber reached by that base change.
falsifier: a fiber over the dominated locus at which specialization/refined pullback of the relative cycle lacks the prescribed Betti class
---

# G002 - Cycle-space dominance gate

## Conditional theorem

Let \(f:\mathcal Y\to T\) and \(\widetilde\alpha\) be as in the metadata. Assume
there is a surjective proper map \(T'\to T\) and a relative
codimension-\(m\) rational cycle \(\mathcal Z\) on
\(\mathcal Y\times_T T'\) whose fiberwise Betti class equals the pullback of
\(\widetilde\alpha\). Then every fiber class covered by \(T'\to T\) is
algebraic. This conclusion is immediate from refined fiber pullback and
compatibility of the cycle-class map.

## Attempt to discharge dominance

1. CDK makes the Hodge locus algebraic.
2. Relative Chow/Hilbert schemes parameterize actual cycles.
3. An anchor cycle supplies one point over the Hodge locus.
4. **Failure:** one point does not imply that its cycle-space component
   dominates the Hodge-locus component. Obstructions to deforming the cycle
   can keep the image proper even while the cohomology class remains Hodge.

Therefore the conditional theorem is valid, but its decisive dominance
hypothesis is not proved. The invalid CDK-only route is NG-001.
