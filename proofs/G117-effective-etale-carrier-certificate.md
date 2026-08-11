---
brick_id: G117
status: EXPLORATORY
base_field: C
variety: the full labelled critical incidence of an arbitrary smooth projective complex variety, together with a class-directed basis-node germ and an algebraic etale carrier
smoothness: the projective variety, basis-node germ, and carrier are smooth at the marked data; every tracked critical point is an ODP
projectivity: the carrier equations and numerator representatives must be extracted from the full projective critical incidence, not from a nonlinear special pullback
dimension: arbitrary projective dimension, basis dimension d-R, carrier ambient dimension M, carrier degree delta, and numerator degree e
codimension: prove the pulled-back conormal defect vanishes through order delta e minus one and descend its total vanishing
coefficient_field: C for algebraic carriers and conormal modules; Q for the specified Hodge class and detector
cohomology_theory: finite etale critical algebras, effective elimination, local intersection multiplicity, Kahler differentials, ODP vanishing cycles, primitive rational cohomology, and Saito pairing
hodge_type: the retained detector relation must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input Hodge class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B135-B184, G013, G088-G116, NG106-NG148, S015, S072
claim: Construct a pointed algebraic etale carrier for the labelled basis-node branches from the full critical incidence, compute bounds delta and e for its projective degree and cleared numerator representatives, and prove the pulled-back conormal map vanishes through order delta e minus one while retaining every detector clause.
falsifier: a carrier not etale or not faithfully flat at the marked germ, an omitted component or denominator, an untracked carrier or numerator degree, failure of the required jets, use of a nonlinear special base, or loss of any detector clause
---

# G117 — Effective certificate on an étale algebraic carrier

NG148 shows that an algebraic analytic escape branch need not satisfy a
simple implicit equation over the original basis coordinates. B184 avoids
that unnecessary demand by working on an algebraic carrier on which the
labelled numerators are regular.

The corrected construction must:

1. extract from the full labelled critical incidence a pointed algebraic
   étale carrier \((V,p)\to(F_B,0)\);
2. certify every cleared separator denominator as a unit at \(p\);
3. represent the pulled-back escape generators by ambient polynomials
   \(N_i|_V\);
4. compute a projective carrier-degree bound \(\deg\overline V\le\delta\)
   and a numerator bound \(\deg N_i\le e\);
5. prove \(j^{\delta e-1}\beta_{KO'}=0\).

B184 promotes item 5 to total conormal vanishing on \(V\), descends that
vanishing faithfully to \(F_B\), and then invokes B179 to obtain
\(H_\tau=0\).

Dubé's bound in S072 makes a lexicographic elimination bound computable
from a finite polynomial presentation, but it does not itself identify the
correct local component, prove smooth étaleness, or establish item 5.

Every uniform-matroid, adjoint-defect, primitive-image, rational-type, and
specified-pairing clause remains attached. No arbitrary-variety carrier
construction with the required jet vanishing is currently proved.
