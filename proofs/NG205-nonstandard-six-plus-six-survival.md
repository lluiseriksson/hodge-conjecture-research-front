---
brick_id: NG205
status: NO-GO
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=8, primitive ruling difference zeta=a-b, nonstandard A=O_Q(k) with k>=2, and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; no central nodal divisor is constructed
projectivity: complete quadric embeddings, double-point restrictions, pair-line hyperplanes, and point spans are projective
dimension: dim X=d=2n>=8; G170 has s=6d+6, N=8d+8, and h_Z(1)=4d+4
codimension: records failure of the route that tries to attain the exact nonstandard rank floor while absorbing every marked tangent osculator
coefficient_field: Q for zeta and C for sections, jets, spans, graphs, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to finite double and reduced schemes
hodge_type: zeta is rational type (n,n); no rational type-(0,0) relation detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); no algebraicity inference is made
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B235, B246-B247, G170
claim: The route of surviving G170 with a nonstandard quadric polarization is impossible: four double neighborhoods already fill the allowed span for k=2,3 and an explicit pair-line four-cycle separates a fifth point, while B215 gives rank 4d+5 for k>=4.
falsifier: a valid nonstandard G170 quadric candidate or failure of one of B247's explicit separation steps
---

# NG205 — Nonstandard survival at \(6d+6\)

- **Label:** NO-GO
- **Route:** attain B244's exact nonstandard floor
  \(h_Z(1)=4d+4\) and absorb every marked tangent osculator.
- **Valid premise:** for \(k=2,3\), four double neighborhoods can have
  exactly the allowed total dimension \(4d+4\).
- **Invalid inference:** their full span can also absorb every further
  marked point.
- **Quartic/sextic obstruction:** after choosing four supports with no
  three collinear, the good pair-line graph relative to a fifth point
  has a four-cycle. The product of its four hyperplanes vanishes twice
  at the four supports and not at the fifth point. Two unit factors give
  the sextic version.
- **Higher-power obstruction:** B215 separates four doubles and one
  reduced point in exponent eight, giving rank \(4d+5\) for \(k\ge4\).
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge8\), is a
  valid input. No special-family success elsewhere can rescue G170.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G170 and both layers \(6d+6,6d+7\) are closed. G148
  and HC remain open.
- **Re-entry condition:** G171 begins at
  \(s=6d+8,\delta_1=3d+4,N=8d+10,h_Z(1)=4d+5\).
