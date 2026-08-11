---
brick_id: G116
status: EXPLORATORY
base_field: C
variety: the full labelled finite étale critical incidence on an arbitrary smooth projective complex variety, restricted to a class-directed basis-node germ
smoothness: the parameter and basis-node germs are smooth; tracked critical points are ODPs and separator denominators are units
projectivity: every numerator and unit certificate must come from the full projective critical incidence, not a nonlinear special base
dimension: arbitrary projective and parameter dimensions; N-R escape generators; effective numerator degree bound D_num
codimension: reduce conormal vanishing to a finite jet bound derived only from cleared labelled numerators
coefficient_field: C for algebraic numerators, units, and conormal modules; Q for the specified Hodge class and detector
cohomology_theory: finite étale idempotents, effective elimination, Kähler differentials, ODP vanishing cycles, primitive rational cohomology, and Saito pairing
hodge_type: the retained detector relation must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input Hodge class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B135-B183, G013, G088-G115, NG106-NG147
claim: Clear every proven-unit separator denominator from the labelled escape generators, construct simple algebraic presentations with a computable common degree bound D_num for the resulting numerators, and prove their conormal defect vanishes through order D_num-1 while retaining every detector clause.
falsifier: an uncleared nonunit, a numerator bound that hides root or restriction complexity, failure of the required jets, use of a nonlinear special base, or loss of any detector clause
---

# G116 — Bound only the cleared escape numerators

B182 expresses labelled branches using separator idempotents, while B183
shows that unit denominators do not affect the escape ideal or its conormal
order. The corrected effective target is therefore:

1. prove every separator denominator is a unit on the chosen full-system
   germ;
2. clear those units from each labelled escape generator
   \(\epsilon_i=n_i/h_i\);
3. construct simple algebraic equations for the numerators \(n_i\) with a
   computable common degree bound \(D_{\mathrm{num}}\);
4. prove the numerator conormal rows vanish through order
   \(D_{\mathrm{num}}-1\).

B183 identifies the numerator ideal with \(K_B\), and B180 then promotes
item 4 to \(H_\tau=0\).

This corrects the overstrong version of G115: the inverse units need not
be expanded or assigned a conormal jet order. The lifted separator roots,
cleared numerators, restriction to \(F_B\), and their algebraic degrees
still require effective control.

Every uniform-matroid, adjoint-defect, primitive-image, rational-type, and
specified-pairing clause remains attached. No numerator bound or required
jet vanishing is currently proved.
