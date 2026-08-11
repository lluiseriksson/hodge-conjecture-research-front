---
brick_id: NG187
status: NO-GO
base_field: C
variety: arbitrary smooth projective complex 2n-folds, tested on Q^4 with zeta=a-b
smoothness: Q^4 is smooth; marked schemes are reduced; no ODP family is produced
projectivity: every very ample quadric polarization and all jet, secant, and point-span data are projective
dimension: the test has dim Q^4=4, c_4=15, and required first-slack A^4 rank 16
codimension: powers have no defect pairs and the standard polarization confines every defect clique to a P^2 of quartic rank at most 15
coefficient_field: Q for the primitive Hodge input and C for the geometric obstruction
cohomology_theory: rational singular cohomology and coherent finite-jet restriction
hodge_type: the test class is primitive rational type (2,2); no algebraicity inference for an unknown class is used
cycle_class_map: CH^2(Q^4)_Q -> H^4(Q^4,Q(2)); the known ruling difference only certifies a legitimate universal input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221, B226-B228, G149-G152
claim: After powered polarizations fail, choose an exceptional very ample polarization on every primitive target and thereby realize the G149-G152 first-slack package.
falsifier: on Q^4 every very ample A=O_Q(k) is excluded by B228
---

# NG187 — Exceptional polarization does not universally rescue first slack

- **Route:** allow the polarization to vary and expect one exceptional
  low embedding to support the first-slack defect clique.
- **Valid correction:** B226 proves that high powers are the wrong
  direction, so a low exceptional polarization is necessary.
- **Invalid inference:** every primitive target has such an exceptional
  polarization with the required rank.
- **Precise obstruction:** B228 exhausts all \(A=O_{Q^4}(k)\). Powers
  have no defect pairs; \(O(1)\) confines a clique to an isotropic
  plane of quartic rank 15 instead of 16.
- **Detector guard:** the test class \(a-b\) is already algebraic only
  to certify a valid input. No unknown Hodge class is assumed algebraic.
- **Conclusion:** G152 and the entire first-slack specialization are
  **NO-GO**. G148 and the rational Hodge Conjecture remain open.
- **Re-entry condition:** none for universal first slack; move to the
  second-slack rank layer.
