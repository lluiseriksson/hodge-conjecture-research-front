---
brick_id: NG181
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex 2n-fold re-embedded by powers A^k of a very ample line bundle A
smoothness: X is smooth; no central divisor or incidence smoothness follows from the re-embedding
projectivity: every complete A^k-embedding and its ordinary Gauss map are projective
dimension: dim X=2n; G146 requires at least D_(2n)(m)>=2(2n+1) points in one fiber, while every A^k fiber for k>=2 is a singleton
codimension: asymptotic positivity separates rather than collides embedded tangent spaces
coefficient_field: C for sections and Gauss maps; Q detector data remain separate
cohomology_theory: coherent first jets only; no primitive Hodge or vanishing-cycle conclusion is supplied
hodge_type: no rational type-(0,0) detector or specified pairing is produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not reached
cycle_equivalence: rational equivalence remains the terminal relation
scope: absolute
dependencies: B220, G146-G147
claim: Obtain G146 by replacing a very ample A with sufficiently high powers A^k and searching for a growing common-tangent Gauss fiber.
falsifier: B220 constructs, for every p!=q and k>=2, an A^k-section vanishing to first order at p and nonzero at q, so gamma_(A^k) is injective and every fiber is a singleton.
---

# NG181 — Powers separate the tangent spaces required by G146

- **Route:** raise the polarization power until a large common-tangent
  fiber and the remaining G146 clauses become available.
- **Valid input:** high powers improve ordinary section and jet
  generation.
- **Invalid inference:** this positivity creates the tangent-space
  collision forced by the extremal equality branch.

For every \(p\ne q\), B220 squares a separating A-section to obtain an
\(A^k\)-hyperplane containing \(T_pX\) but not \(q\). Thus
\(\gamma_{A^k}\) is injective for all \(k\ge2\), while G146 requires a
fiber with at least \(2(2n+1)\) points.

- **Precise obstruction:** asymptotic tangent separation.
- **Detector guard:** the result concerns the equality branch only and
  does not close G144's slack range \(N>D_{2n}(m)\).
- **Re-entry condition:** B221/NG182 subsequently close G147's
  exceptional-polarization escape; abandon equality and use G148's
  strict-slack branch.
