---
brick_id: B208
status: PROVED
base_field: C
variety: the full degree-m projective tangent system of a smooth projective complex d-fold with finite smooth node scheme Z, G125 lower first-jet extinction, and G130's central ODP section
smoothness: X and Z are smooth and the central quadratic profile is nondegenerate at every node; reduced incidence smoothness is not inferred
projectivity: X, powers of H through degree m, ideal powers I_Z through I_Z^3, profile spaces, and the full tangent system are projective coherent data
dimension: dim X=d; the first nonzero quadratic-profile space is the one-dimensional central line in degree m
codimension: vanishing of every lower quadratic-profile space removes all decomposable mixed cubic contributions
coefficient_field: C for sections, profiles, Hessians, and cubic tensors; Q remains required separately for the detector
cohomology_theory: coherent first and second jets, graded profile multiplication, minimal generators, and cubic Kuranishi tensors
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B194-B207 and G125-G137
claim: Assume lower first-jet extinction through m-1, W_k=0 for every k<m, W_m=C q_F with q_F nondegenerate, and H0(I_Z^3 H^m) subset P_m. Then rho(P_m)=0, G134's indecomposable profile quotient is C q_F, K_m/P_m is the central new double-generator line, and B201's mixed cubic filter Xi vanishes.
falsifier: a nonzero decomposable degree-m profile despite all lower W_k=0, failure of the central profile to generate W_m, a surviving triple-hidden generator, or nonzero Xi on the central line
---

# B208 — A first quadratic-profile birth kills the mixed cubic block

Assume G125's lower first-jet extinction and strengthen it by

\[
 W_k=0\qquad(0\le k<m). \tag{1}
\]

At the birth degree assume

\[
 W_m=\mathbf Cq_F, \tag{2}
\]

where \(q_F\) is nondegenerate at every marked point, and retain the
triple-hidden condition

\[
 T_m=H^0(I_Z^3H^m)\subset P_m. \tag{3}
\]

B204 gives

\[
 \rho(P_m)=\sum_{a=1}^mE_aW_{m-a}=0 \tag{4}
\]

by (1). Hence (2) and (4) imply

\[
 \frac{W_m}{\rho(P_m)}=\mathbf Cq_F. \tag{5}
\]

Together with (3), B203 identifies \(K_m/P_m\) with the one-dimensional
central double-generator line. Thus G134 is closed.

B205 factors the mixed cubic map through \(W_m\) and proves

\[
 \mathbf Cq_F\subset\ker\widehat\Xi_m.
\]

Equation (2) therefore gives \(\Xi=0\) on the full double-direction space.
No colon or connecting-map preimage remains to construct.

B208 does not construct the birth conditions, the pure cubic tensor,
higher Kuranishi closure, a rational detector, or an algebraic cycle.
