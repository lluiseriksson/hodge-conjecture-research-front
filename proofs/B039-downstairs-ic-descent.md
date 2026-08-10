---
brick_id: B039
status: PROVED
base_field: C
variety: a two-dimensional local parameter slice B with central U_(2,5) discriminant, and its blow-up pi: tilde B -> B at the common point
smoothness: B and tilde B are smooth; the pulled-back discriminant is a simple-normal-crossing divisor; the motivating central projective fiber has five ordinary double points and nearby fibers are smooth
projectivity: pi is projective; the parameter calculation is local analytic, while the motivating hyperplane-section family is projective
dimension: parameter spaces have complex dimension 2, the exceptional fiber has dimension 1, the ambient projective variety has dimension 2n, and nearby fibers have dimension 2n-1
codimension: the blow-up center has codimension 2, exceptional marked points have codimension 1 on E, and downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: rational intersection complexes, perverse sheaves, proper base change, and polarizable rational Hodge modules
hodge_type: the direct-image splitting exists in the rational Hodge-module category, but the Hodge type of the degree-one relation kernel is not computed
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B035-B038 and Saito's projective direct-image and strict-support decomposition theorem (S037)
claim: For the U_(2,5) blow-up, the degree-one hypercohomology of the resolved exceptional restriction is canonically the degree-one stalk of the downstairs intermediate extension; every additional point-supported direct-image summand occurs in ordinary degree two and cannot change this group.
falsifier: a nonzero perverse direct-image cohomology sheaf outside degree zero, a non-full-support summand supported away from the blow-up center, or a point-supported summand contributing to ordinary degree one after the dimension-two shift
---

# B039 - Downstairs IC descent

B038 identifies the degree-one hypercohomology on the exceptional curve with
the rational relation kernel. This brick proves that the group is the
degree-one stalk of the downstairs intermediate extension, rather than a
contribution created by the resolution.

## Conventions

Let

\[
 \pi:\widetilde B\longrightarrow B
\]

be the blow-up of the smooth complex surface \(B\) at the origin, and write
\(E=\pi^{-1}(0)\simeq\mathbf P^1\). Let \(L_{\mathbf Q}\) be the geometric
polarizable rational variation on the complement of the discriminant. Put

\[
 A=IC_{\widetilde B}(\pi^*L_{\mathbf Q})
 \quad\text{and}\quad P=A[2].
\]

Thus \(A\) uses the unshifted convention, restricting to \(L_{\mathbf Q}\)
in degree zero on the open stratum, while \(P\) is perverse. Its Hodge-module
enhancement is pure and polarizable.

## The direct image is perverse

Away from \(0\), the map \(\pi\) is an isomorphism, so \(R\pi_*P\) is the
intermediate extension there. It remains to check the perverse stalk and
costalk conditions at \(0\).

Proper base change and B037 give

\[
 i_0^*R\pi_*P
 \simeq R\Gamma(E,A|_E)[2].
\]

The two-row description in B037 has a constant cohomology sheaf in ordinary
degree zero and point-supported cohomology in ordinary degree one. Since
\(E\) is a curve, its hypercohomology is zero outside ordinary degrees
\(0,1,2\). After shifting by two, the stalk therefore has cohomology only in
degrees \(-2,-1,0\), which is exactly the required upper bound at the
zero-dimensional stratum.

Apply the same argument to the Verdier dual variation. Properness gives

\[
 D(R\pi_*P)\simeq R\pi_*D(P).
\]

The dual exceptional complex has the same cohomological amplitude, so the
stalk condition for \(D(R\pi_*P)\) gives the costalk lower bound for
\(R\pi_*P\). Hence

\[
 R\pi_*P\in\operatorname{Perv}(B,\mathbf Q).
\]

This local amplitude argument is important: the proof does not assume an
unsourced assertion that every semismall direct image is \(t\)-exact for
arbitrary perverse coefficients.

## Strict-support decomposition

Saito's projective direct-image theorem sends the pure polarizable Hodge
module underlying \(P\) to pure polarizable perverse-cohomology Hodge
modules. The preceding amplitude calculation says that only perverse degree
zero occurs. Semisimplicity and strict-support decomposition therefore give

\[
 R\pi_*P\simeq IC_B(L_{\mathbf Q})[2]\oplus i_{0*}H_0,
\]

where \(H_0\) is some polarizable rational Hodge structure. There is exactly
one full-support summand: on \(B\setminus\{0\}\), the direct image is the
given intermediate extension of \(L_{\mathbf Q}\). Since \(\pi\) is an
isomorphism there, every other strict support must be the point \(0\).

Returning to the unshifted convention gives

\[
 R\pi_*A\simeq IC_B(L_{\mathbf Q})\oplus i_{0*}H_0[-2].
\]

The point-supported summand \(i_{0*}H_0[-2]\) has ordinary cohomology only
in degree two. It contributes nothing in degree one. Taking the stalk at
the origin and using proper base change yields the canonical identification

\[
 H^1\!\left(IC_B(L_{\mathbf Q})_0\right)
 \simeq
 \mathbb H^1(E,A|_E).
\]

Combining this with B038 proves

\[
 H^1\!\left(IC_B(L_{\mathbf Q})_0\right)
 \simeq
 \ker\!\left(
   \mathbf Q^5\xrightarrow{e_i\mapsto\delta_i}
   \operatorname{span}_{\mathbf Q}\{\delta_i\}
 \right).
\]

The isomorphism is rational and is induced in the Hodge-module category.
This last fact does not determine the weight or Hodge type of either side.

## Adversarial checks

- **Coefficient check.** The local system is a geometric polarizable
  rational variation, not a constant complex local system. Saito's
  coefficient-sensitive theorem is used; the constant-coefficient
  semismall theorem is only contextual.
- **Shift check.** A point perverse sheaf is in perverse degree zero.
  Undoing the surface shift places it in ordinary degree two, not degree
  one.
- **Support check.** The only exceptional image is \(0\), so there is no
  additional positive-dimensional strict support.
- **Canonicity check.** The strict-support summand is canonical. A splitting
  of the total direct image need not be canonical, but degree one is
  unaffected by the point summand, so the displayed degree-one
  identification is canonical.

## Remaining obligations

1. Determine the rational mixed/pure Hodge structure on the relation kernel
   and prove the precise Tate-twisted type-\((0,0)\) comparison required by
   B010.
2. Extend the calculation beyond the rank-two \(U_{2,5}\) arrangement to
   arbitrary multipart smoothing arrangements.

## Scope guard

B039 proves only the downstairs topological/intersection-cohomology
identification in the minimal multipart model. It proves no algebraicity,
constructs no cycle, and supplies no propagation from this special local
arrangement to arbitrary smooth projective varieties. The standard rational
Hodge Conjecture and G015 remain open.
