---
brick_id: G131
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with very ample H, a specified primitive rational middle Hodge class, and G130's class-directed augmented node package
smoothness: X and Z are smooth, F has isolated ODPs, and reduced smoothness of the simultaneous-node germ remains downstream
projectivity: X, H^m, the full projective tangent system, doubled node scheme, third spatial jets, and detector family are projective
dimension: dim X=2n; U has dimension 2n; Kbar=H0(I_2Z H^m)/C F may be large; the cubic target is coker(E) tensor Sym^3(ker E)^*
codimension: kill both B201 cubic filters Theta on U^3 and Xi on Kbar tensor U^2 while retaining G130 and all detector clauses
coefficient_field: C for sections, jets, Hessians, and cubic tensors; Q for the Hodge class, detector, and specified pairing
cohomology_theory: coherent first through third spatial jets, ODP Kuranishi theory, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the detector must be rational type (0,0) with nonzero pairing against the specified class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B201, G013, G090-G130, NG106-NG163, and S065-S073
claim: Construct G130 for arbitrary (X,zeta) and prove both the pure cubic tensor Theta and the mixed lower-double Hessian map Xi vanish in the full projective tangent system, while retaining generator minimality, adjacent extinction, ODPs, the rational detector, and every previously closed condition.
falsifier: nonzero Theta, a double direction with Xi nonzero, use of a selected slice omitting Kbar, failure of G130's congruence or generator package, or failure of any detector clause
---

# G131 — Kill the pure and mixed cubic filters

Starting from G130, use the full projective tangent kernel

\[
 \ker E=U\oplus\overline K,\qquad
 \overline K=H^0(I_{2Z}H^m)/\mathbf CF.
\]

B201 proves that the next Kuranishi rung is zero exactly when

\[
 \Theta=0,\qquad
 \Xi:\overline K\to
 (\mathcal T/S)\otimes\operatorname{Sym}^2U^*=0. \tag{1}
\]

The first equality synchronizes the pure cubic critical-value tensors of
the \(2n\) jet-generator directions. The second requires the Hessian of
**every** degree-\(m\) section double on \(Z\), modulo \(F\), to produce a
node-value vector in \(S\) after contraction with two transported
jet directions.

Both conditions must hold in the full complete linear system. Deleting
\(\overline K\), passing to a \(2n\)-dimensional slice, or normalizing only
the central member does not prove (1). Success closes \(\kappa_3\) only;
the quartic through \(D_{\mathrm{car}}\) rungs and the terminal cycle remain
open.
