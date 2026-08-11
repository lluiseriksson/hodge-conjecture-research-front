---
brick_id: NG193
status: NO-GO
base_field: C
variety: arbitrary smooth projective complex 2n-folds, tested on Q^(2n) with primitive ruling difference a-b
smoothness: the quadric and reduced marked scheme are smooth; no central ODP construction is asserted
projectivity: tangent osculators, three-double restrictions, and collinear point spans are projective
dimension: dim X=d=2n>=4; every m=2 candidate with slack s<4d is excluded on the valid even-quadric input
codimension: the ruling difference supplies a legitimate primitive codimension-n universal input
coefficient_field: Q for the Hodge input and C for sections, tangent tensors, and ranks
cohomology_theory: rational singular cohomology and coherent finite-scheme restriction
hodge_type: a-b is primitive rational type (n,n); no unknown class is assumed algebraic
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the known class only certifies the test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221-B235, G158
claim: Realize universal G148 through any m=2 specialization whose slack grows strictly slower than the B235 floor 4d, including G158's s=2d+8 signature.
falsifier: B235 proves s>=4d on every valid even-quadric input; for G158 choose any even d>=6, where 2d+8<4d
---

# NG193 — Sub-slope-four degree-two cores cannot realize G148

- **Route:** keep increasing the additive number of dimensions beyond two
  tangent osculators while retaining a slack formula below \(4d\).
- **Valid premise:** each added pair of slack layers increases the point
  span by one.
- **Invalid inference:** a fixed additive excess eventually absorbs the
  third tangent osculator uniformly in dimension.
- **Precise obstruction:** B235 proves that the standard quadric
  polarization needs quotient dimension at least \(d-1\), hence
  \(s\ge4d\). Square and higher polarizations satisfy the stronger
  \(s\ge4d+4\).
- **G158 falsifier:** for every even \(d\ge6\),
  \(2d+8<4d\), so the valid input \((Q^d,a-b)\) excludes G158.
- **Detector guard:** no ODP profile, rational detector, specified pairing,
  algebraic cycle, proof, or disproof of HC is produced.
- **Conclusion:** G158 and every sub-\(4d\) degree-two specialization are
  **NO-GO**. G148 and HC remain open.
- **Re-entry condition:** B236 later excludes the exact boundary and its
  odd neighbor; move to G160.
