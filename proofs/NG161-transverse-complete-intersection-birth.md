---
brick_id: NG161
status: NO-GO
base_field: C
variety: a smooth projective complex d-fold with very ample H and a reduced point scheme Z cut transversely by d degree-m ideal generators
smoothness: X and Z are smooth and the d selected generators have independent gradients at every point of Z; no central divisor is supplied
projectivity: X, H^m, Z, its homogeneous ideal, and the proposed central divisor are projective
dimension: dim X=d; the d transverse generator classes can realize dim V_m=d, but an ODP central member requires a nonzero class in K_m
codimension: if the d jet generators exhaust the degree-m minimal generators and there are no lower ideal sections, then K_m=0
coefficient_field: C for sections, generators, jets, and Hessians; Q detector data are absent
cohomology_theory: complete-intersection ideals, graded minimal generators, first jets, and ODP second jets
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B142, B197-B199, G128-G129
claim: Use exactly d transverse new degree-m generators, with no lower ideal sections and no additional degree-m generator, both to realize V_m of dimension d and to supply a nonzero degree-m divisor singular along Z.
falsifier: the exact sequence of B199 gives K_m=0 under these hypotheses, so no nonzero central divisor can be singular at all points of Z
---

# NG161 — A transverse complete intersection has no central nodal generator

- **Route:** let \(Z\) be cut transversely by exactly \(d=\dim X\) new
  degree-\(m\) sections, use their gradients to realize \(V_m\), and choose
  another linear combination as the central nodal divisor.
- **Valid input:** the \(d\) independent gradient vectors give a
  \(d\)-dimensional one-node-determined conditional-jet space.
- **Invalid inference:** the same \(d\)-dimensional generator space contains
  a nonzero section with zero gradient at every point.

Assume \(J_k=0\) for \(k<m\). Then \(P_m=(R_+J)_m=0\). If the \(d\)
transverse sections exhaust the degree-\(m\) ideal space, then

\[
 \dim J_m=d,\qquad \dim V_m=d.
\]

B199's exact sequence gives

\[
 0\longrightarrow K_m\longrightarrow J_m\longrightarrow V_m
 \longrightarrow0,
\]

so \(K_m=0\). Equivalently, a linear combination of a gradient basis that
has zero gradient at one marked point already has all coefficients zero.
There is no nonzero degree-\(m\) section singular at every point of \(Z\),
let alone one with ODP Hessians.

- **Precise obstruction:** the jet generators consume the entire ideal
  space; the central nodal section needs a double-generator direction.
- **Re-entry condition:** add the new double line of G129, or construct
  B199's inherited-double branch from lower sections and prove simultaneous
  Hessian nondegeneracy. In either case re-audit the detector and all
  Kuranishi equations.
