---
brick_id: NG172
status: NO-GO
base_field: C
variety: a smooth projective complex variety with a finite marked point scheme whose point span absorbs every marked tangent space
smoothness: X and Z are smooth; no second-order contact is assumed
projectivity: the point, tangent, and second osculating spans are projective linear data
dimension: arbitrary dim X=d; the logical failure is visible in a two-step flag with one extra second-osculating direction
codimension: tangent-span absorption controls I_Z/I_Z^2 but not I_Z^2/I_Z^3
coefficient_field: C; the exact flag countermodel is defined over Q
cohomology_theory: principal parts through order two and finite-dimensional projective duality
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196, B210, G127, G139, NG159, S073
claim: Infer second-osculating absorption S_Z^(2)=S_Z^(1) from tangent absorption S_Z^(1)=S_Z^(0).
falsifier: the nested osculating flag can satisfy S_Z^(0)=S_Z^(1) properly contained in S_Z^(2)
---

# NG172 — Tangent absorption does not absorb second osculators

- **Route:** use B196/G127 to place every tangent space in the point span
  and count the same span as second-osculating.
- **Valid input:** \(S_Z^{(0)}=S_Z^{(1)}\), equivalently \(V_A=0\).
- **Invalid inference:** \(S_Z^{(2)}=S_Z^{(1)}\), equivalently \(W_A=0\).

The exact flag model

\[
 S_Z^{(0)}=S_Z^{(1)}=\mathbf Qe_0
 \subsetneq S_Z^{(2)}=\mathbf Qe_0\oplus\mathbf Qe_1
\]

has complete tangent absorption and a one-dimensional quadratic-profile
defect. It is a countermodel to the formal implication, not a projective
counterexample.

S073/Terracini identifies spans of tangent spaces for general secant data;
it contains no assertion about second osculating spaces at G139's special
marked scheme.

- **Precise obstruction:** first- and second-order principal-part layers
  are independent successive quotients.
- **Re-entry condition:** prove a genuine second-order contact theorem for
  the special adjacent configuration while retaining the degree-\(m\)
  birth and detector.
