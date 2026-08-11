---
brick_id: G016
status: PROVED
base_field: C
variety: a three-dimensional nodal smoothing slice with seven central discriminant hyperplanes whose matroid has exactly one dependent triple, together with its wonderful resolution
smoothness: the parameter threefold is smooth; the central projective fiber has seven ordinary double points and nearby fibers are smooth; the unresolved projectivized divisor has one triple point
projectivity: the blow-ups and exceptional strata are projective; the parameter calculation is local analytic, while the motivating hyperplane-section family is projective
dimension: parameter dimension 3, first exceptional divisor dimension 2, dependent flat dimension 1, ambient projective variety dimension 2n, and nearby fiber dimension 2n-1
codimension: the origin has codimension 3, the unique dependent flat has codimension 2, and downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: Picard-Lefschetz vanishing cycles, rational intersection complexes, wonderful-model logarithmic residues, perverse direct images, and mixed Hodge modules
hodge_type: the sought downstairs degree-one relation channel must be pure of type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B035-B044, B134, and G015
claim: For the stated one-dependent-triple arrangement, the polarized homological model dual to the downstairs cohomological IC channel is the full rational relation kernel, and both are pure type (0,0) after Q(n).
falsifier: a wonderful exceptional-flat stratum that kills a rational relation, creates a spurious degree-one class, contributes a degree-one proper-direct-image summand, or changes the Tate type
---

# G016 - Single-dependent-flat channel

## Falsifiable theorem sought

Let \(H_1,\ldots,H_7\subset\mathbf C^3\) be central hyperplanes such that
\(\{1,2,3\}\) is the unique dependent triple and every other triple is
independent. Equivalently, the projective lines \(L_1,L_2,L_3\subset
\mathbf P^2\) have one common point and there are no other triple points.
Assume the seven node-smoothing directions admit the required independent
block partition.

Resolve first the origin and then the strict transform of the common
codimension-two flat \(H_1\cap H_2\cap H_3\). Prove that

\[
 H^1\!\left(IC_B(L_{\mathbf Q})_0\right)
 \simeq
 \ker\!\left(
   \mathbf Q^7\xrightarrow{e_i\mapsto\delta_i}
   \operatorname{span}_{\mathbf Q}\{\delta_i\}
 \right)
\]

as a rational type-\((0,0)\) Hodge structure after \(\mathbf Q(n)\).

## Why B043 does not apply

After blowing up only the origin, \(L_1,L_2,L_3\) meet at one point of the
exceptional \(\mathbf P^2\). Together with the first exceptional divisor,
four boundary components meet in a threefold, so the divisor is not SNC.
The second blow-up creates an exceptional divisor over the dependent flat
and changes both the incidence complex and the support decomposition of the
composite proper direct image.

Uniform deletion or perturbation is not a proof. It changes the arrangement
matroid and can change the intermediate extension at the dependent stratum.

## First concrete obligation

Compute the local degree-one sheaf on the second exceptional divisor and
its gluing to the proper transforms of \(L_1,L_2,L_3\). Determine whether
the new residue differential is merely the redundant relation among those
three branch residues or imposes an additional quotient on the global
seven-cycle relation kernel. Then audit the perverse shifts for the
two-stage proper map.

## Resolution of the gate

B044 performs this calculation. The fiber over the origin is
\(Z=\operatorname{Bl}_p\mathbf P^2\). If \(C\) is its exceptional curve,
the degree-one sheaf is

\[
 (W_F)_C\oplus\bigoplus_{i=1}^7\mathbf Q_{M_i},
 \qquad W_F=\operatorname{span}\{\delta_1,\delta_2,\delta_3\}.
\]

In the divisor-class basis \(h,e\), the residue equations are

\[
 \sum_{i=1}^7a_i\delta_i=0,
 \qquad
 w=\sum_{i=1}^3a_i\delta_i.
\]

Thus projection to \((a_i)\) identifies the resolved kernel with the full
seven-cycle relation space. The composite direct image can have strict
support on the dependent flat, but its curve-supported and point-supported
summands begin in ordinary degree two. Degree one is the downstairs
full-support IC stalk, and Saito's normalization makes it pure type
\((0,0)\).

## Propagation

G016 is the first proved nonuniform-flat test of G015. It justifies moving
to several flats only after proving compatibility for overlapping or nested
building-set centers.

## Scope guard

G016 assumes no desired algebraic cycle and makes no claim about arbitrary
arrangements or the general Hodge Conjecture.
