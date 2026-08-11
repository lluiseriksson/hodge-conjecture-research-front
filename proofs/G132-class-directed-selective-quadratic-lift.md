---
brick_id: G132
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with very ample H, a specified primitive rational middle Hodge class, and G129's class-directed augmented point scheme Z
smoothness: X and Z are smooth; the lifted F must have isolated ODPs and be smooth away from the tracked nodes in the relevant incidence
projectivity: X, H^m, the ideal powers I_Z^2 and I_Z^3, the connecting map, generator spaces, and detector family are projective
dimension: dim X=2n; N>1; dim V_m=2n; q_(t,Q) is a nondegenerate section of a rank n(2n+1)N conormal-quadratic layer
codimension: construct a special nondegenerate q_(t,Q) in ker(partial_Z) while H1(I_Z^3 H^m) remains nonzero and all G129 rank defects persist
coefficient_field: C for sections, quadratic profiles, and coherent cohomology; Q for the Hodge class, detector, and specified pairing
cohomology_theory: coherent ideal-power lifting, ODP jets, graded minimal generators, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the detector must be rational type (0,0) with nonzero pairing against the specified class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B202, G013, G090-G131, NG106-NG164, and S065-S073
claim: Construct from arbitrary (X,zeta) G129's adjacent minimal-generator data, t outside J_m with nowhere-zero values, and nondegenerate Q such that q_(t,Q) lies in the kernel of the nonzero connecting map H0((I_Z^2/I_Z^3)H^m)->H1(I_Z^3 H^m); choose a lift F that is a new double generator with isolated ODPs and retain every detector clause.
falsifier: zero H1(I_Z^3 H^m), q_(t,Q) outside the kernel, a degenerate profile, every lift decomposable or singular away from Z, loss of R<N or dim V_m=2n, or failure of any detector clause
---

# G132 — Construct the selective quadratic lift

G132 isolates the construction step inside G130. Starting from arbitrary
\((X,\zeta)\), construct \(Z,m,U,t,Q\) satisfying all adjacent-rank and
detector obligations of G129, with

\[
 t|_Z\ne0,\qquad Q\in\operatorname{Sym}^2U
 \text{ nondegenerate}.
\]

Form B202's prescribed quadratic profile

\[
 q_{t,Q}\in H^0((I_Z^2/I_Z^3)H^m).
\]

The required selective superabundance is

\[
 H^1(I_Z^3H^m)\ne0,\qquad
 \partial_Z(q_{t,Q})=0. \tag{1}
\]

Choose a lift \(F\in H^0(I_Z^2H^m)\) of \(q_{t,Q}\) such that:

1. its class spans G129's new double-generator line;
2. its only tracked singularities are isolated ODPs at \(Z\);
3. \(tF-\mu_2(Q)\in H^0(I_Z^3H^{2m})\);
4. the no-coloop value relation, rational detector, and specified pairing
   survive.

Equation (1) is narrower than G130 but is not sufficient by itself: lift
minimality, global nodality, G131's cubic filters, every later Kuranishi
rung, and the terminal cycle remain separate.
B203 separates lift existence from minimal-generator novelty. G133 records
the clean quadratic-new line, while NG165 prevents counting an arbitrary
lift before quotienting by decomposable lower products.
