---
brick_id: NG165
status: NO-GO
base_field: C
variety: a smooth projective complex variety with very ample H, reduced point scheme Z, and a liftable degree-m quadratic profile
smoothness: X and Z are smooth; the failure concerns graded minimality rather than local Hessian smoothness
projectivity: X, H^m, the ideal powers, profile map, and homogeneous point ideal are projective
dimension: arbitrary dim X; the connecting-map kernel may be nonzero even when the new double-generator quotient is zero
codimension: decomposable profiles rho(P_m) and triple sections T_m intersecting P_m must be removed before counting generators
coefficient_field: C for profiles, lifts, and graded quotient spaces; Q detector data are absent
cohomology_theory: coherent ideal-power lifting, graded ideals, and finite-dimensional exact sequences
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B198-B203, G129-G133
claim: Count any q in ker(partial_Z), or any lift F of q, as a new degree-m double generator without quotienting profiles and triple sections by P_m.
falsifier: if q lies in rho(P_m) and T_m is contained in P_m, every lift lies in P_m and represents zero in D_m=K_m/P_m
---

# NG165 — A lift need not be a new minimal generator

- **Route:** prove \(\partial_Z(q)=0\), choose a lift \(F\), and count \(F\)
  as G129's new double generator.
- **Valid input:** \(F\in H^0(I_Z^2H^m)\) has the prescribed quadratic
  profile.
- **Invalid inference:** \(F\notin P_m=(R_+J)_m\).

If \(q\in\rho(P_m)\), choose \(p\in P_m\) with \(\rho(p)=q\). Every lift
has the form

\[
 F=p+g,\qquad g\in T_m=H^0(I_Z^3H^m).
\]

When \(T_m\subset P_m\), every such \(F\) lies in \(P_m\), so

\[
 [F]=0\in D_m=H^0(I_Z^2H^m)/P_m.
\]

- **Precise obstruction:** existence is measured by
  \(\ker\partial_Z\), while minimal novelty is measured by B203's quotient
  of that kernel by \(\rho(P_m)\), together with the triple-hidden term.
- **Re-entry condition:** prove G133's quotient conditions or construct and
  audit the alternative triple-hidden generator branch, retaining ODPs and
  every detector clause.
