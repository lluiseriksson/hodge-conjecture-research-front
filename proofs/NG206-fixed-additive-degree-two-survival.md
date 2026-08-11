---
brick_id: NG206
status: NO-GO
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with primitive ruling difference zeta=a-b, arbitrary A=O_Q(k), H=A^2, and any fixed additive excess j
smoothness: Q^d and the reduced marked scheme are smooth; no central nodal divisor is constructed
projectivity: complete quadric embeddings, mixed finite-scheme restrictions, bounded linear spans, and hyperplane-square separators are projective
dimension: dim X=d=2n tends through sufficiently large even values; h_Z(1)=4d+4+j and s=6d+6+2j for fixed j
codimension: records failure of every route that continues the degree-two balanced branch through only a dimension-independent additive number of ranks
coefficient_field: Q for zeta and C for sections, jets, spans, hyperplanes, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to finite double and reduced schemes
hodge_type: zeta is rational type (n,n); no rational type-(0,0) relation detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); no algebraicity inference is made
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B246-B248, G171
claim: No fixed additive excess j can make the balanced m=2 construction universal: high powers interpolate four doubles and j+1 points, bounded powers are defeated by successive hyperplane-square separators in a sufficiently large even dimension, and the standard polarization requires j>=d-7.
falsifier: a bounded-excess universal m=2 family surviving B248's explicit even-quadric inequalities
---

# NG206 — Fixed additive degree-two survival

- **Label:** NO-GO
- **Route:** continue the balanced \(m=2\) branch with
  \(h_Z(1)=4d+4+j\) for one fixed \(j\).
- **Valid premise:** each extra pair of slack units permits one more
  degree-one code dimension.
- **Invalid inference:** finitely many such dimensions can absorb all
  marked evaluations uniformly as the quadric dimension grows.
- **High-power obstruction:** if \(2k\ge8+j\), B215 separates four
  doubles and \(j+1\) reduced points, forcing rank \(h_Z(1)+1\).
- **Bounded-power obstruction:** if \(2k\le j+7\), the span of four
  double supports and at most \(j\) reduced supports has bounded
  degree-\(2k\) point rank. In sufficiently large dimension another
  marked point lies outside, and a squared hyperplane separates it.
- **Standard obstruction:** B246 requires \(j\ge d-7\).
- **Universal-quantifier guard:** a sufficiently large even quadric is
  a valid input for every fixed \(j\). No special-family success is
  promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G171 and every fixed-additive continuation are
  closed. G148 and HC remain open.
- **Re-entry condition:** G172 permits a dimension-growing excess
  \(j=j(X,\zeta)\) and retains every detector clause.
