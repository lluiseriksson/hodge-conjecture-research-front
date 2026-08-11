---
brick_id: NG237
status: NO-GO
base_field: C
variety: the smooth split even-dimensional quadric Q^d with d=2n>=14, primitive ruling difference zeta=a-b, cubic or quartic A=O_Q(k) for k=3,4, H=A^2, and a hypothetical G200 marked scheme
smoothness: Q^d and all reduced marked supports are smooth; no central ODP package is constructed
projectivity: the complete sextic or octic embedding, tangent osculators, variable-edge product spaces, and first-jet targets are projective
dimension: dim X=d=2n>=14; the attempted next equality is h_Z(1)=7d+6, six independent doubles have rank 6d+6, and the allowed residual rank is exactly d
codimension: the failed route tries to apply the planar B271-B272 classifications at the next G200 cubic/quartic boundary without first eliminating B264's nonplanar exact-rank branch
coefficient_field: Q for zeta and C for sections, tangent jets, graph incidence, endpoint planes, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); no arbitrary Hodge class is assumed algebraic
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196, B260-B272, B278, G200-G201, S081, S084
claim: The B271-B272 planar mechanisms do not by themselves exclude cubic or quartic rank 7d+6: B264 permits a nonplanar branch whose two variable-edge images have combined rank exactly d, equal to the full residual budget.
falsifier: a proof from the cited bricks that rank 7d+6 still forces all six supports into a plane through the seventh point, or an exclusion of every exact-rank-d nonplanar branch
---

# NG237 — The planar equality argument stops one rank too early

- **Label:** NO-GO
- **Route:** apply the B271 cubic and B272 quartic planar arguments
  unchanged at the next boundary \(h_Z(1)=7d+6\).
- **Exact obstruction:** six independent doubles contribute \(6d+6\),
  so the seventh residual budget is

  \[
  (7d+6)-(6d+6)=d. \tag{1}
  \]

  B264 proves only that a nonplanar selected-edge configuration has
  residual rank at least \(d\). Equality is therefore allowed rather
  than contradictory.
- **Linear-algebra locus:** for tangent selected edges \(e,f\), B264
  writes their jet images as \(R_e,R_f\subset A\), \(\dim A=d+1\).
  The next-rank equality case is precisely compatible with

  \[
  \dim(R_e+R_f)=d,
  \qquad
  \dim(R_e^\perp\cap R_f^\perp)=1. \tag{2}
  \]

  The orthogonal planes are multiplier-dependent graphs over distinct
  endpoint planes, so endpoint incidence alone does not exclude (2).
  A nontangent edge can likewise have image rank exactly \(d\).
- **Why B271-B272 do not apply:** their weak-del-Pezzo and four-point
  analyses begin only after planar reduction. Using them here would
  silently discard the exact-rank nonplanar branch.
- **Boundary consequence:** G200 remains EXPLORATORY. G201 isolates the
  required nonplanar absorbed-support theorem.
- **Detector guard:** no relation, ODP package, Kuranishi vanishing,
  rational detector, specified pairing, cycle, proof, or disproof of HC
  is produced.
- **Re-entry condition:** prove G201, or supply a different theorem that
  excludes every exact-rank-\(d\) nonplanar residual branch.
