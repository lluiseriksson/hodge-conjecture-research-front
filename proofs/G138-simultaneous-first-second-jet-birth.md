---
brick_id: G138
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with very ample H and a specified primitive rational middle Hodge class
smoothness: X and Z are smooth, the central section has isolated ODPs, and reduced smoothness of the simultaneous-node incidence remains downstream
projectivity: X, all powers through H^m, first through third node neighborhoods, the full tangent system, and detector family are projective
dimension: dim X=2n; the degree-m conditional first-jet quotient has dimension 2n and the quadratic-profile space has dimension one
codimension: first jets and quadratic profiles are both extinct below m, then the required 2n plus 1 augmented nodal package is born in degree m
coefficient_field: C for sections, jets, profiles, Hessians, and Kuranishi tensors; Q for the Hodge class, detector, and specified pairing
cohomology_theory: coherent first and second jets, minimal graded generators, cubic Kuranishi theory, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the detector must be rational type (0,0) with nonzero pairing against the specified class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B208, G013, G090-G137, NG106-NG171, S065-S074
claim: For arbitrary (X,zeta), construct G130 so that H0(I_Z H^k)=H0(I_Z^2 H^k)=H0(I_Z^3 H^k) for every k<m, W_m=C q_F with q_F nondegenerate, H0(I_Z^3 H^m) subset P_m, dim V_m=2n with conformal holonomy, and every rational detector clause holds.
falsifier: a nonzero lower first-jet or quadratic-profile quotient, an additional degree-m profile, a triple-hidden generator, failure of the ODP or holonomy package, or failure of any detector clause
---

# G138 — Force simultaneous first- and second-jet birth

Construct the full G130 package with the lower ladder

\[
 H^0(I_ZH^k)=H^0(I_Z^2H^k)=H^0(I_Z^3H^k)
 \qquad(0\le k<m), \tag{1}
\]

and the degree-\(m\) birth

\[
 \dim V_m=2n,\qquad
 W_m=\mathbf Cq_F,\qquad
 H^0(I_Z^3H^m)\subset P_m. \tag{2}
\]

The profile \(q_F\) must be nondegenerate, arise from the central isolated-
ODP section, and retain G130's quadratic congruence and conformal holonomy.
All no-coloop, rational type-\((0,0)\), and specified-pairing clauses remain
mandatory.

B208 makes (1)--(2) sufficient for G134 and for the full mixed cubic
condition \(\Xi=0\). Thus G138 is a stronger constructive branch that avoids
G137's colon preimages. The pure tensor \(\Theta\), every later rung, and the
terminal cycle remain open.

B209 reduces the whole lower ladder to \(V_{m-1}=W_{m-1}=0\). B210 turns
that pair into second-osculating absorption by the point span, and G139 is
the adjacent projective construction gate. NG172 blocks upgrading tangent
absorption to second-osculating absorption without new input.
