---
brick_id: NG167
status: NO-GO
base_field: C
variety: a smooth projective complex 2n-fold with G134's one-dimensional primitive quadratic-profile quotient
smoothness: X and Z are smooth and the central profile is nondegenerate; mixed cubic closure is not implied
projectivity: X, graded profile spaces, value spaces, and the full projective tangent system are projective
dimension: the primitive quotient has dimension one, while the decomposable profile subspace may have arbitrary positive dimension
codimension: B201's mixed cubic map can be nonzero on decomposable profiles even though it kills the primitive central line
coefficient_field: C for profiles, contractions, and quotient tensors; Q detector data are absent
cohomology_theory: graded coherent quadratic profiles and cubic Kuranishi tensors
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B201-B205, G131-G135
claim: Infer Xi=0 solely from the fact that W_m/(sum E_a W_(m-a)) is the one-dimensional central profile line.
falsifier: Xihat_m kills q_F but may be nonzero on the decomposable denominator, so the quotient dimension does not control the full mixed map
---

# NG167 — A primitive profile line does not kill the mixed cubic block

- **Route:** prove G134's one-dimensional primitive quotient and conclude
  \(\Xi=0\).
- **Valid input:** B205 proves
  \(\widehat\Xi_m(q_F)=0\).
- **Invalid inference:** \(\widehat\Xi_m\) also vanishes on the
  decomposable profile subspace.

Under G134,

\[
 W_m=\mathbf Cq_F+D_m^{\mathrm{prof}},\qquad
 D_m^{\mathrm{prof}}=\sum_{a=1}^mE_aW_{m-a}.
\]

The induced quotient \(W_m/D_m^{\mathrm{prof}}\) being one-dimensional
says nothing about
\(\widehat\Xi_m|_{D_m^{\mathrm{prof}}}\). A decomposable profile can have a
contracted node vector outside \(S_m\), producing a nonzero mixed cubic
class while the primitive quotient remains exactly \(\mathbf Cq_F\).

- **Precise obstruction:** primitive generation and cubic contraction
  closure are independent linear conditions.
- **Re-entry condition:** prove every lower-product containment in G135,
  then kill the pure cubic tensor and every later rung separately.
