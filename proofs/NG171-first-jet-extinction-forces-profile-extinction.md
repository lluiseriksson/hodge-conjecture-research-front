---
brick_id: NG171
status: NO-GO
base_field: C
variety: a smooth projective complex variety with finite smooth node scheme Z and a lower-degree complete linear system satisfying first-jet extinction
smoothness: X and Z are smooth; no second-jet extinction is assumed
projectivity: X, H^k, and the first three powers of I_Z are projective coherent data
dimension: arbitrary dim X=d; the logical gap is already visible in a one-dimensional filtered vector-space model
codimension: equality of the simple- and double-vanishing global section spaces does not imply equality of the double- and triple-vanishing spaces
coefficient_field: C; the exact filtration countermodel is defined over Q
cohomology_theory: coherent first and second jets and finite-dimensional quotient spaces
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B194, B204, B208, G125, G138
claim: Infer W_k=0 from V_k=0, equivalently infer H0(I_Z^2 H^k)=H0(I_Z^3 H^k) from H0(I_Z H^k)=H0(I_Z^2 H^k).
falsifier: the nested filtration can have J_k=K_k nonzero and T_k properly contained in K_k, giving V_k=0 but W_k nonzero
---

# NG171 — First-jet extinction does not kill quadratic profiles

Write

\[
 J_k=H^0(I_ZH^k),\qquad
 K_k=H^0(I_Z^2H^k),\qquad
 T_k=H^0(I_Z^3H^k).
\]

- **Route:** use G125's \(V_k=J_k/K_k=0\) below \(m\) and conclude the
  stronger G138 condition \(W_k=K_k/T_k=0\).
- **Valid input:** \(J_k=K_k\).
- **Invalid inference:** \(K_k=T_k\).

The exact filtered vector-space model

\[
 J_k=K_k=\mathbf Q,\qquad T_k=0
\]

has \(V_k=0\) and \(W_k\cong\mathbf Q\ne0\). Geometrically, the first
equality says every global section vanishing on \(Z\) is already double;
it places no condition on whether such a double section has a nonzero
quadratic profile.

- **Precise obstruction:** the successive quotients \(I_Z/I_Z^2\) and
  \(I_Z^2/I_Z^3\) are independent conormal layers.
- **Re-entry condition:** prove the second-layer vanishing in G138 by a
  genuine global interpolation or Hilbert-function theorem while retaining
  the special degree-\(m\) birth and detector.
