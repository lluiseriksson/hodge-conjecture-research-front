---
brick_id: NG189
status: NO-GO
base_field: C
variety: arbitrary smooth projective complex 2n-folds, tested on smooth even quadrics Q^(2n) with primitive ruling difference a-b
smoothness: every test quadric and reduced marked scheme is smooth; no central ODP construction is asserted
projectivity: all quadric polarizations, finite jet restrictions, osculating spans, secant lines, and isotropic spaces are projective
dimension: unbounded even dimension d=2n>=4; any proposed dimension-independent finite slack bound is defeated by choosing 2d+2 larger than that bound
codimension: the test class a-b has codimension n; the obstruction concerns only the node excess above the B215 floor
coefficient_field: Q for the Hodge input and C for ranks, jets, and quadric geometry
cohomology_theory: rational singular cohomology and coherent finite-jet restriction
hodge_type: a-b is primitive rational type (n,n); no unknown class is assumed algebraic
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the known ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221-B231, G145-G154
claim: Prove the universal G148 strict-slack theorem while keeping s=N-D_(2n)(m) bounded by one finite constant independent of n.
falsifier: B231 excludes every degree on a sufficiently high-dimensional valid even-quadric input for any such fixed bound
---

# NG189 — Dimension-independent slack cannot realize G148

- **Route:** choose one finite excess bound \(S\) and allow degree and
  polarization to vary while keeping \(s\le S\) on every primitive target.
- **Valid premise:** strict slack avoids equality saturation, and each fixed
  dimension has finite rank thresholds.
- **Invalid inference:** one finite number of extra nodes works uniformly in
  the dimension.
- **Precise obstruction:** B231 proves on \(Q^d\) that degree two requires
  \(s\ge2d+2\), while every degree \(m\ge3\) requires
  \(s\ge\binom{d+2}{2}\). Given \(S\), choose even \(d\) with
  \(S<2d+2\); then no degree or polarization realizes the candidate.
- **Detector guard:** the algebraic ruling difference only supplies a valid
  universal-quantifier input. No unknown Hodge class, detector, pairing, or
  cycle is produced.
- **Conclusion:** G154 and every dimension-independent bounded-slack
  specialization are **NO-GO**. G148 and the rational Hodge Conjecture remain
  open.
- **Re-entry condition:** let the slack grow with dimension; B232 later
  excludes the first two degree-two layers, so move to G156.
