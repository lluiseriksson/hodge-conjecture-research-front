---
brick_id: G114
status: EXPLORATORY
base_field: C
variety: the full algebraic critical-point incidence of an arbitrary smooth projective complex variety X and complete linear system, localized near a class-directed ordered multinodal member
smoothness: X and the parameter germ are smooth; all tracked critical points are distinct ODPs, so the critical-point incidence is étale at each label
projectivity: X and the universal hypersurface family are projective; every localization, primitive element, and denominator must be derived from the full incidence
dimension: arbitrary spatial and parameter dimensions; N labelled nodes with coincident critical value zero; effective splitting and degree bounds for every label
codimension: separate the critical-point labels before applying B180's finite conormal certificate
coefficient_field: C for étale algebras and elimination; Q for the specified Hodge class and detector
cohomology_theory: finite étale algebras, primitive elements, effective elimination, ODP critical values, conormal modules, primitive rational cohomology, and Saito pairing
hodge_type: the retained detector relation must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input Hodge class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B135-B181, G013, G088-G113, NG106-NG145
claim: Choose an algebraic separator of the distinct tracked critical points, construct effective idempotent or primitive-element splitting of the local étale critical algebra into labelled factors, and derive simple critical-value polynomials with fully tracked degrees before applying G113 and B180.
falsifier: a separator failing at the central points, ramification of a labelled factor, loss of labels under a value resultant or squarefree operation, uncontrolled denominators or degree growth, use of a nonlinear special base, or loss of any detector clause
---

# G114 — Effective labelled étale splitting

The critical values all equal zero at a multinodal member, so B181 shows
that the value resultant cannot label them. The critical points themselves
are distinct. G114 therefore asks for a separating algebraic coordinate
on the critical-point incidence before eliminating the spatial variables.

Required construction:

1. choose a regular function \(\lambda\) on an algebraic neighborhood of
   the tracked critical incidence such that
   \(\lambda(p_i)\ne\lambda(p_j)\) for \(i\ne j\);
2. use \(\lambda\) as an effective primitive element for the local finite
   étale critical algebra, or construct labelled idempotents directly;
3. split the critical-value function into the \(N\) labelled étale
   factors and obtain for each one a simple polynomial
   \(P_i(u,w)\) with \(\partial_wP_i(0,0)\ne0\);
4. track all localization denominators, separator discriminants,
   restrictions to \(F_B\), and total degrees to produce G113's common
   bound \(D\).

Only after this splitting may B180 reduce conormal vanishing to the
\((D-1)\)-jet calculation.

The construction must take place in the full complete-linear-system
incidence and retain every uniform-matroid, adjoint-defect,
primitive-image, rational-type, and specified-pairing clause. No effective
labelled splitting with those properties is currently proved.
