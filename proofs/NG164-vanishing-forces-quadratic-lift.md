---
brick_id: NG164
status: NO-GO
base_field: C
variety: a smooth projective complex 2n-fold with a fixed finite reduced point scheme Z and a degree-m complete linear system
smoothness: X and Z are smooth; full two-jet interpolation can prescribe ODP Hessians but does not give the required excess incidence
projectivity: X, H^m, the third infinitesimal neighborhood of Z, and all evaluation maps are projective
dimension: N>1; full two-jet surjectivity forces value rank N and conditional-gradient dimension 2nN rather than 2n
codimension: vanishing H1(I_Z^3 H^m) removes the quadratic lifting obstruction but simultaneously removes the first-jet defect
coefficient_field: C for coherent cohomology and jets; Q detector data are absent
cohomology_theory: Serre vanishing, ideal-power exact sequences, and finite-jet evaluation
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B157, B191-B202, G129-G132, NG153, NG160, S065
claim: Impose H1(I_Z^3 H^m)=0 so every prescribed nondegenerate quadratic profile lifts, and count that automatic lift as a G130/G132 construction.
falsifier: the same vanishing makes complete two-jet evaluation surjective, forcing R=N and dim V_m=2nN, contrary to the N>1 one-node-determined defect branch
---

# NG164 — Automatic third-neighborhood lifting destroys the defect

- **Route:** force \(H^1(I_Z^3H^m)=0\), lift every prescribed quadratic
  profile, and count the resulting ODP section as G132.
- **Valid input:** B202's connecting map then vanishes identically, so every
  profile in \(H^0((I_Z^2/I_Z^3)H^m)\) lifts.
- **Invalid inference:** the surrounding complete system retains G129's
  value and conditional-gradient defects.

The same cohomology vanishing makes

\[
 H^0(H^m)\longrightarrow
 H^0(H^m|_{\mathcal O_X/I_Z^3})
\]

surjective. Therefore values, gradients, and Hessians at all marked points
are independently prescribed. In particular,

\[
 R=N,\qquad \dim V_m=2nN.
\]

For \(N>1\), neither \(R<N\) nor one-node determination with
\(\dim V_m=2n\) survives.

- **Precise obstruction:** G132 needs selective kernel membership for one
  nondegenerate profile while the obstruction group remains nonzero.
- **Re-entry condition:** construct the special class-directed kernel
  element in (1) of G132 without invoking blanket vanishing, and retain
  generator minimality, isolated nodality, and every detector clause.
