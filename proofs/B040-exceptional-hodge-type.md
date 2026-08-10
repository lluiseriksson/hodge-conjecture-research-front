---
brick_id: B040
status: PROVED
base_field: C
variety: the blow-up of a two-dimensional U_(2,5) nodal smoothing slice and the five-marked exceptional P^1
smoothness: the parameter surface and its blow-up are smooth; the pulled-back discriminant is simple normal crossing; the central projective fiber has five ordinary double points and nearby fibers are smooth
projectivity: the blow-up and exceptional curve are projective; the parameter calculation is local analytic, while the motivating hyperplane-section family is projective
dimension: parameter surface dimension 2, exceptional curve dimension 1, ambient projective variety dimension 2n, and nearby fiber dimension 2n-1
codimension: the original arrangement center has codimension 2, marked crossings have codimension 1 on the exceptional curve, and downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: polarizable rational variations and mixed Hodge modules, Picard-Lefschetz vanishing cycles, local intersection cohomology, and exceptional hypercohomology
hodge_type: after Saito's standard Q(n) vanishing-homology normalization, the downstairs degree-one relation kernel is pure of type (0,0), equivalently a direct sum of Q(0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B010, B035-B039, Saito Section 1.4 Proposition 1.7 and Theorem 3 (S022), and Hodge-module functoriality (S037)
claim: In the minimal U_(2,5) multipart model, the rational Hodge structure on the downstairs degree-one IC stalk identified in B039 is the full vanishing-cycle relation kernel with pure Tate type (0,0) after the Q(n) normalization.
falsifier: a resolved crossing group with a non-(0,0) Hodge component after Q(n), a transgression that is not a morphism of mixed Hodge structures, or a B039 descent map that fails to preserve the Hodge-module structure
---

# B040 - Exceptional relation Hodge type

B039 identifies the downstairs degree-one IC stalk with the rational
relation kernel in the minimal \(U_{2,5}\) model. This brick computes the
Hodge type carried by that identification.

## Tate normalization

Use Saito's normalization

\[
 \mathcal H=R^{2n-1}f_*\mathbf Q(n),
\]

which is a variation of weight \(-1\) on the smooth locus. For an ordinary
double point, Saito Theorem 3 identifies its vanishing cohomology before the
twist as \(\mathbf Q(-n)\). Equivalently, the corresponding generator in the
twisted vanishing-cycle relation complex has type \((0,0)\).

This is the same normalization used in B010. No factor \(2\pi i\) is
discarded: the Tate twist is part of the rational Hodge structure, while the
de Rham residue normalization in B038 only fixes the comparison with the
integral Betti boundary map.

## The five crossing groups

At the crossing \(p_i=E\cap D_i\), the two logarithms are

\[
 N_E=\sum_{j=1}^5N_j,\qquad N_i,
\]

and B035 gives \(N_EN_i=N_iN_E=0\). Each
\(\operatorname{Im}N_i\) is a one-dimensional Tate Hodge structure of type
\((0,0)\) in Saito's twisted complex. Moreover,

\[
 \operatorname{Im}N_E
 =\operatorname{span}_{\mathbf Q}
   \{\operatorname{Im}N_1,\ldots,\operatorname{Im}N_5\}
\]

is itself a direct sum of copies of \(\mathbf Q(0)\).

Saito Proposition 1.7 applies to this normal-crossing pair: when the products
of the nilpotent logarithms vanish and their images are sums of
one-dimensional mixed Hodge structures, the degree-one intermediate-
extension group has as many \((0,0)\) Hodge classes as its total dimension.
B036 computes that dimension as one. Hence each of the five skyscraper
groups in B037 is canonically a copy of \(\mathbf Q(0)\), up to the common
orientation convention already fixed in B038.

## The exceptional kernel

The local monodromy/intermediate-extension complexes in Saito Section 1.4
are constructed in the derived category of mixed Hodge modules. Restriction
to \(E\), the truncation triangle used in B038, and projective direct image
from \(E\) to a point therefore induce a spectral sequence in rational mixed
Hodge structures. In particular, B038's transgression is a morphism of mixed
Hodge structures

\[
 d_2:\mathbf Q(0)^5\longrightarrow H^2(E,K_E).
\]

Its underlying rational map is

\[
 d_2(a_1,\ldots,a_5)=\sum_i a_i\delta_i.
\]

Consequently

\[
 \ker d_2
 \subseteq \mathbf Q(0)^5
\]

is a rational sub-Hodge structure of a pure Tate structure. Therefore

\[
 \ker d_2\simeq \mathbf Q(0)^{\,5-s},
 \qquad
 s=\dim_{\mathbf Q}\operatorname{span}\{\delta_i\}.
\]

B039's strict-support decomposition and degree-one descent take place in the
rational Hodge-module category. They identify this kernel with

\[
 H^1\!\left(IC_B(\mathcal H)_0\right)
\]

as a rational Hodge structure, not only as a vector space. The downstairs
group is therefore pure of type \((0,0)\) after the specified Tate twist.

## Adversarial checks

- **Rational/integral guard.** The claim is rational. It does not promote an
  integral lattice statement.
- **Twist guard.** Type \((0,0)\) is asserted only after the explicit
  \(\mathbf Q(n)\) normalization used by Saito and B010.
- **Multiparameter guard.** The Hodge structure comes from the resolved
  mixed-Hodge-module complex and its proper direct image; it is not imported
  from a dimension equality for a separately chosen one-parameter slice.
- **Subspace guard.** A rational sub-Hodge structure of
  \(\mathbf Q(0)^5\) is again Tate of type \((0,0)\); no claim is made about
  the Hodge type of the target \(H^2(E,K_E)\).

## Remaining obligation

The full G015 theorem still requires the corresponding residue, support,
and Hodge-type argument for arbitrary multipart smoothing arrangements.
Higher-rank arrangements have higher-dimensional exceptional strata and
additional differentials; the \(U_{2,5}\) calculation does not control them.

## Scope guard

B040 completes the rational topological and Hodge-theoretic calculation only
for the minimal three-block local arrangement. It constructs no algebraic
cycle and proves no reduction from arbitrary varieties to this arrangement.
The standard rational Hodge Conjecture and G015 remain open.
