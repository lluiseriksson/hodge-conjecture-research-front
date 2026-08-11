---
brick_id: G139
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with very ample H, a specified primitive rational middle Hodge class, and one class-directed finite point scheme Z
smoothness: X and Z are smooth, the degree-m central section has isolated ODPs, and reduced smoothness of the full node incidence remains downstream
projectivity: the H^(m-1) and H^m embeddings, point and osculating spans, full tangent system, ideal powers, and detector family are projective
dimension: dim X=2n; the H^(m-1) second-osculating increment is zero, while the degree-m first and second increments are 2n and 1
codimension: construct one adjacent transition from complete second-osculating absorption to the augmented nodal generator birth
coefficient_field: C for embeddings, jets, profiles, Hessians, and Kuranishi tensors; Q for the Hodge class, detector, and specified pairing
cohomology_theory: principal parts through order two, coherent ideal filtrations, cubic Kuranishi theory, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the detector must be rational type (0,0) with nonzero pairing against the specified class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B210, G013, G090-G138, NG106-NG172, S065-S074
claim: For arbitrary (X,zeta), construct Z and m>=2 so that in the H^(m-1) embedding the point span is full or contains every marked second osculating space; in degree m the first-osculating span grows by 2n and the second by exactly one nondegenerate central profile, with T_m subset P_m, G130 holonomy and congruence, and every rational detector clause.
falsifier: a missed second-osculating direction at degree m-1, an incorrect degree-m osculating increment, a degenerate or nonminimal central profile, failure of G130, or loss of any detector clause
---

# G139 — Construct the adjacent second-osculating birth

Let \(S_{k,Z}^{(r)}\) denote B210's order-\(r\) osculating span for the
embedding by \(H^k\). Construct \(Z\) and \(m\ge2\) such that

\[
 S_{m-1,Z}^{(0)}=S_{m-1,Z}^{(1)}=S_{m-1,Z}^{(2)}. \tag{1}
\]

In the proper branch, (1) says the span of the marked points contains every
marked second osculating space. In the full-span branch it is automatic.

At degree \(m\), require the controlled jump

\[
 \dim S_{m,Z}^{(1)}/S_{m,Z}^{(0)}=2n,\qquad
 \dim S_{m,Z}^{(2)}/S_{m,Z}^{(1)}=1, \tag{2}
\]

with the second quotient dual to the nondegenerate central profile line,
\(H^0(I_Z^3H^m)\subset P_m\), and every G130 holonomy, congruence, ODP,
no-coloop, rational type-\((0,0)\), and specified-pairing clause.

B209-B210 make (1)--(2) the adjacent projective form of G138. B208 then
closes G134 and \(\Xi\). G139 does not kill the pure cubic tensor or any
later rung and does not construct a cycle.

B211 converts (1)--(2) into the exact adjacent rank table for
\(Z\subset2Z\subset3Z\), quantifies the two required superabundances, and
gives the pointwise second-jet node floor. G140 is that finite signature
gate. S075/NG173 prevent replacing its special configuration by a
general-point higher Terracini theorem.
