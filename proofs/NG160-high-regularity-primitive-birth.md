---
brick_id: NG160
status: NO-GO
base_field: C
variety: a smooth projective complex variety with very ample H and one fixed nonempty reduced point scheme Z
smoothness: X and Z are smooth at their supports; high positivity may separate jets but supplies no special nodal incidence
projectivity: X, powers of H, the homogeneous ideal module of Z, and 2Z are projective data
dimension: dim X=d; length Z=N>1; the desired birth has q_m=d while high powers have q_k=dN
codimension: generation of J_m by lower ideal pieces annihilates every putative primitive first jet under lower extinction
coefficient_field: C for sections and jets; Q detector data are absent
cohomology_theory: graded coherent ideals, minimal generators, first-jet evaluation, and Serre vanishing
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B157, B194-B198, G125-G128, NG153, NG158, and S065
claim: Fix Z and raise m beyond its ideal-generation or first-jet-regularity threshold, expecting positivity to create G125's primitive q_m=d birth after lower extinction.
falsifier: beyond the generator ceiling every degree-m ideal section is a product of lower ones and hence double along Z, while beyond the first-jet threshold q_m=dN rather than d for N>1
---

# NG160 — High regularity cannot create the primitive birth

- **Route:** fix \(Z\), take \(m\) very large, and invoke positivity or
  regularity to obtain G125's clean first nonzero conditional-jet space.
- **Valid input:** S065 gives eventual generation and prescribed finite-jet
  interpolation for a fixed finite scheme.
- **Invalid inference:** the asymptotic regime creates a new minimal ideal
  generator whose first jets form a \(d\)-dimensional one-node-determined
  space.

There are two independent obstructions. First, once the ideal module
\(J=\bigoplus H^0(I_ZH^k)\) is generated below degree \(m\), B198 shows that
lower extinction forces

\[
 J_m=(R_+J)_m\subset H^0(I_{2Z}H^m),
\]

so \(V_m=0\). Second, after full first-jet separation begins, S065 gives

\[
 \dim V_m=dN,
\]

which is strictly larger than the one-node ceiling \(d\) when \(N>1\).

- **Precise obstruction:** primitive birth is a finite-degree minimal-
  generator phenomenon, whereas high regularity removes new generators
  and eventually separates all nodewise gradients.
- **Re-entry condition:** vary \(Z\) with \(m\), remain inside its new-
  generator window, and construct at least \(d\) new generators whose jets
  satisfy one-node determination, Hessian holonomy, every Kuranishi rung,
  and the rational detector.
