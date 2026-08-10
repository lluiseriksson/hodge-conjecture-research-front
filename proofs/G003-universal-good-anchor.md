---
brick_id: G003
status: EXPLORATORY
base_field: C
variety: arbitrary anchored smooth projective family over a Hodge-locus component
smoothness: family and base smooth after restriction; desired Hilbert point smooth
projectivity: projective family
dimension: even relative dimension 2m
codimension: m
coefficient_field: Q
cohomology_theory: relative singular Betti cohomology R^{2m}f_*Q
hodge_type: flat section fiberwise of type (m,m)
cycle_class_map: CH^m(Y_t)_Q -> H^{2m}(Y_t,Q(m))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: G001 anchor; B002 criterion; semiregularity/deformation theory
claim: Every algebraic anchor class admits a cycle representative satisfying B002 smoothness and tangent-surjectivity conditions over its full Hodge-locus component.
falsifier: an anchored class for which every representative is obstructed or every relative Hilbert tangent image is a proper subspace of the Hodge-locus tangent space
---

# G003 - Universal good-anchor representative

## Attempt

Bloch-style semiregularity is the natural mechanism: for suitable embedded
cycles it relates deformation obstructions to Hodge-theoretic variation. If it
made an anchor's relative Hilbert point smooth and its tangent image equal the
Hodge-locus tangent space, B002 would force the desired dominance.

The universal claim is not proved. The source theorem has hypotheses on the
cycle, while an arbitrary rational algebraic class may have no known smooth,
lci, or semiregular representative. Replacing a cycle by a rational linear
combination also does not automatically produce a single unobstructed Hilbert
point. Treating semiregularity as automatic is NG-004.

## Next falsifiable sub-brick

Extract the exact tangent and obstruction maps for a smooth lci
codimension-\(m\) anchor \(Z\subset Y_t\), then test whether injectivity of the
semiregularity map implies both B002 hypotheses along the Hodge locus. This
must remain a special-geometric conditional result until a universal
representative theorem is independently proved.

