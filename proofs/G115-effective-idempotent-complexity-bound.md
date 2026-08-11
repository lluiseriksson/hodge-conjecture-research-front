---
brick_id: G115
status: EXPLORATORY
base_field: C
variety: the localized full critical-point incidence of an arbitrary smooth projective complex variety and complete linear system, with a separator for the ordered tracked ODPs
smoothness: the parameter germ is smooth and the tracked critical algebra is finite étale; all central separator values are distinct
projectivity: the critical algebra, separator, and value element must be derived from the full projective incidence; no nonlinear special base may replace it
dimension: arbitrary parameter and projective dimensions; finite critical-algebra rank r; N tracked factors; effective complexity bound E
codimension: bound the labelled idempotents and branch equations effectively so G113 can compute its jet order D-1
coefficient_field: C for effective étale algebra and elimination; Q for the specified Hodge class and detector
cohomology_theory: finite étale algebras, primitive elements, effective Hensel factorization, conormal modules, ODP vanishing cycles, primitive rational cohomology, and Saito pairing
hodge_type: the retained detector relation must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input Hodge class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B135-B182, G013, G088-G114, NG106-NG146
claim: Starting from explicit equations of the full finite étale critical algebra and a central separator, bound the characteristic polynomial, lifted roots, inverse separator discriminant, labelled idempotents, restricted critical values, and resulting simple branch polynomials by a computable complexity E, then feed that bound into G113.
falsifier: an omitted localization denominator, use of analytic Hensel existence without algebraic complexity control, a bound depending only on rank and central separation, failure to preserve labels, or loss of any detector clause
---

# G115 — Bound the complexity of labelled idempotents

B182 supplies the unique analytic splitting

\[
 A\simeq\prod_i e_iA
\]

once a separator \(\lambda\) is chosen. G115 asks for an effective version
in the full critical incidence.

Starting from explicit projective equations, compute and bound:

1. the finite étale critical algebra \(A\) and the multiplication matrix
   of \(\lambda\);
2. its characteristic polynomial \(Q(u,T)\) and separator discriminant;
3. the algebraic complexity of every lifted root \(\lambda_i(u)\);
4. the inverses of \(\lambda_i-\lambda_j\) used in B182's idempotents;
5. the labelled critical values \(e_iv\) after restriction to \(F_B\);
6. simple polynomials \(P_i(u,w)\) and G113's common degree bound \(D\).

Analytic Hensel lifting alone is insufficient: the finite conormal
certificate needs a numerical degree/order bound. The construction must
also retain the uniform node matroid, adjoint defect, primitive ambient
image, rational type \((0,0)\), and specified nonzero pairing.

No effective bound satisfying these conditions is currently known.
