---
brick_id: NG166
status: NO-GO
base_field: C
variety: a smooth projective complex variety with very ample H, reduced point scheme Z, and a lower-degree liftable quadratic profile
smoothness: X and Z are smooth; profile multiplication does not construct a new ODP generator
projectivity: X, powers of H, value spaces, and quadratic-profile spaces are projective
dimension: arbitrary dim X; multiplication injects profiles under a nowhere-zero value but sends them into the decomposable degree-m subspace
codimension: a multiplied lower profile is zero in the indecomposable quotient required by G134
coefficient_field: C for sections, values, and profiles; Q detector data are absent
cohomology_theory: graded coherent quadratic jets and section multiplication
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B194-B204, G133-G134
claim: Multiply a nonzero lower-degree quadratic profile by a value section and count the resulting degree-m profile as G134's primitive new generator.
falsifier: B204 places every such product in sum_(a=1)^m E_a W_(m-a), so its class in the indecomposable quotient is zero
---

# NG166 — Multiplication cannot create the primitive profile

- **Route:** take \(w\in W_{m-a}\), multiply by a value
  \(e\in E_a\), and use \(ew\in W_m\) as \(q_{t,Q}\).
- **Valid input:** if \(e\) is nowhere zero on \(Z\), multiplication
  preserves nonzero profiles and can preserve fiberwise nondegeneracy.
- **Invalid inference:** the product is a new degree-\(m\) profile
  generator.

B204 gives

\[
 ew\in E_aW_{m-a}\subset
 \sum_{b=1}^mE_bW_{m-b}.
\]

Therefore

\[
 [ew]=0\in
 W_m\Big/\sum_{b=1}^mE_bW_{m-b}.
\]

- **Precise obstruction:** multiplication transports a lower profile but
  places it in the decomposable submodule by definition.
- **Re-entry condition:** construct G134's genuinely primitive,
  nondegenerate degree-\(m\) profile line and retain the triple-hidden,
  ODP, rank, and detector conditions.
