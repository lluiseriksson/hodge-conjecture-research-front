---
brick_id: NG223
status: NO-GO
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, cubic or quartic A=O_Q(k) with k=3 or 4, and H=A^2
smoothness: Q^d and the seven reduced marked supports are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: the residual P^2 through u, selected good secants, normalized hyperplanes, local unit jets, and annihilator graph planes are projective
dimension: dim X=d=2n>=14; no cubic or quartic candidate has h_Z(1)=7d+5; the resulting common floor is B265's M(d)
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the failed route is survival of B264's planar equality locus
coefficient_field: Q for zeta and C for plane equations, local units, tangent jets, graph intersections, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to the reduced and double marked schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B260-B265, G190, NG222, S081
claim: Cubic or quartic equality h_Z(1)=7d+5 cannot survive in B264's planar locus; two distinct selected secants have different normalized first jets and yield variable-edge images of combined rank d.
falsifier: a connected selected graph with only one geometric secant, two distinct normalized secants with identical first jet on the plane, or a planar combined edge rank below d
---

# NG223 — Planar cubic/quartic equality survival

- **Label:** NO-GO
- **Route:** retain cubic or quartic equality \(h_Z(1)=7d+5\) by placing
  the six independent-double supports in B264's \(\mathbf P^2\) through
  the seventh point.
- **Valid premise:** all endpoint tangent planes then coincide, so B264's
  projected-plane comparison alone is inconclusive.
- **Invalid inference:** the fixed unit jets for different variable
  edges define the same annihilator graph.
- **Secant obstruction:** connectivity and the no-collinear-triple
  condition provide two distinct selected pair lines in the plane.
- **Unit obstruction:** their normalized equations have different first
  jets; the two fixed products differ by exactly those factor jets.
- **Rank consequence:** the annihilator graph planes intersect in
  dimension one, so the two variable-edge images have combined rank
  \(d\) and force \(h_Z(1)\ge7d+6\).
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge14\), is a
  valid input. No special-family result is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G190 is closed as a universal gate; the surviving
  regimes pass to G191. G148 and HC remain open.
- **Re-entry condition:** G191 uses B265's \(M(d)\) and survivor table.
