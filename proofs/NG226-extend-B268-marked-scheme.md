---
brick_id: NG226
status: NO-GO
base_field: C
variety: the smooth split even-dimensional quadric X=Q^d with d=2n>=22, B268's seven planar supports, cubic A=O_Q(3), and H=O_Q(6)
smoothness: Q^d, the isotropic plane, and all reduced supports are smooth; no ODP divisor or incidence germ is constructed
projectivity: the complete sextic embedding and restrictions to double finite schemes are projective
dimension: dim X=d=2n>=22; B268 has rank 7d+5 on seven doubles, whereas G190 requires N=2(7d+5) marked points
codimension: the failed route is to retain B268's rank while adjoining the remaining reduced marked supports required by G190
coefficient_field: Q for explicit planar data and the ruling difference, and C for sections and first jets
cohomology_theory: rational singular cohomology and coherent restriction to double finite schemes
hodge_type: the ruling difference is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); no arbitrary Hodge class is assumed algebraic
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B268-B269, G190, NG225, S081
claim: B268's exact seven-support equality witness cannot be promoted to a G190 marked scheme without raising h_Z(1), because every eighth distinct double neighborhood contributes a nonzero new restriction coordinate.
falsifier: an eighth distinct point whose complete sextic double neighborhood is absorbed by the span of 2P7, or an extension of B268 to N=2(7d+5) reduced marked points at unchanged rank
---

# NG226 — The B268 witness cannot be extended to the marked scheme

- **Label:** NO-GO
- **Route:** keep B268's exact rank \(7d+5\) while adjoining the
  remaining marked supports required by G190.
- **Obstruction:** B269 constructs, for every \(x\notin P_7\), a
  sextic vanishing on \(2P_7\) but not on \(2x\).
- **Rank consequence:** every eighth distinct double neighborhood
  raises the rank above \(7d+5\).
- **Cardinality mismatch:** G190 requires \(N=2(7d+5)>7\), and tangent
  absorption requires every marked double neighborhood to lie in the
  same degree-one span.
- **Scope guard:** this excludes only the explicit B268 configuration,
  not every planar cubic equality configuration.
- **Detector guard:** no relation, ODP package, Kuranishi vanishing,
  rational detector, specified pairing, cycle, proof, or disproof of
  HC is produced.
- **Re-entry condition:** classify all planar equality configurations
  and their first-jet base schemes, or attack the quartic branch.
