---
brick_id: NG225
status: NO-GO
base_field: C
variety: the smooth split even-dimensional quadric X=Q^d with d=2n>=22, primitive ruling difference zeta=a-b, cubic A=O_Q(3), H=O_Q(6), and B268's seven planar supports
smoothness: Q^d, the isotropic plane, and the seven reduced supports are smooth; no central ODP package is asserted
projectivity: the complete sextic embedding, two generator lines, isotropic plane, and restrictions to double finite schemes are projective
dimension: dim X=d=2n>=22; the full residual sextic restriction to 2u has rank exactly d-1, so the seven-double rank is exactly 7d+5
codimension: the primitive codimension-n ruling difference supplies a valid universal test input; the failed route is closing G190 by finding an additional sextic first jet on B268's planar 3+3 configuration
coefficient_field: Q for explicit coordinates and exact matrices, Q for zeta, and C for sections and tangent jets
cohomology_theory: rational singular cohomology and coherent restriction to the seven double neighborhoods
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B261, B264-B268, G190, NG222-NG223, S081
claim: No additional sextic interpolation argument can raise the residual rank above d-1 on B268's planar 3+3 configuration: the plane jet image has rank one and the normal image has rank d-2. Therefore this route cannot exclude cubic equality h_Z(1)=7d+5 or close G190.
falsifier: a sextic double at the six supports whose plane first jet is independent of its value, more than d-2 independent normal directions, or residual rank at least d
---

# NG225 — More sextic interpolation cannot escape the planar witness

- **Label:** NO-GO
- **Route:** close G190 by finding one more first jet in the full sextic
  system vanishing on B268's six double supports.
- **Plane obstruction:** restriction to each generator line has degree
  six and three prescribed double zeros, exhausting the degree. Both
  line derivatives at \(u\) are fixed by the common value.
- **Normal obstruction:** only the \(d-2\) directions normal to the
  isotropic plane remain free.
- **Exact rank:** the plane image has rank one, the normal image rank
  \(d-2\), and the full residual image rank \(d-1\).
- **Sharpness:** the six doubles are independent, so the seven-double
  rank is exactly \(7d+5\), not merely bounded above by it.
- **Universal-quantifier guard:** the explicit split quadrics are valid
  test inputs, but the rank witness is not promoted to a full G190
  package.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** cubic equality survives every coherent sextic-rank
  obstruction used so far. G190 remains open.
- **Re-entry condition:** test the relation transport, ODP incidence,
  Kuranishi, rational-type, and specified-pairing clauses on or beyond
  the B268 witness rather than seeking another sextic jet.
