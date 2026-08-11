---
brick_id: NG100
status: NO-GO
base_field: C with rational coefficients
variety: an arbitrary polarized smooth projective complex 2n-fold, one isolated clean nodal hyperplane degeneration, a fixed local relation beta, and a preselected primitive Hodge-homology target c
smoothness: ambient and nearby fiber smooth; special fiber clean nodal
projectivity: ambient variety and degeneration projective
dimension: ambient 2n; hyperplane fibers 2n-1
codimension: middle codimension n; singular support finite
coefficient_field: Q
cohomology_theory: relative singular homology, Saito good retraction, and primitive ambient homology
hodge_type: beta, Phi(beta), and c rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); not used to assume an algebraic representative
cycle_equivalence: rational equivalence downstream
scope: relative and fiberwise
dependencies: B059, B100, B124, G030-G031, G064-G065, S022 Section 2.5
claim: Varying a Saito relative lift of a fixed local relation, or its marked presentation, can adjust its primitive ambient image to a preselected B058 target c.
falsifier: constancy of the primitive ambient map on the relative-lift torsor
---

# NG100 — Relative-lift ambiguity cannot adjust the primitive target

**Status:** NO-GO

- **Route:** fix a local relation \(\beta\), vary its relative lift or the
  marked map presenting that lift, and choose the ambiguity so that the
  primitive ambient image becomes B058's class \(c\).
- **Valid input:** the set of relative lifts is generally a nontrivial affine
  space under absolute nearby-fiber homology.
- **Invalid inference:** this ambiguity survives primitive ambient
  projection.
- **Precise obstruction:** B124 proves that the entire ambiguity subspace is
  killed by primitive projection. Every lift has the single value

  \[
  \Phi_{Y_0}(\beta).
  \]

  Thus a lift with value \(c\) exists exactly when
  \(\Phi_{Y_0}(\beta)=c\), the stronger G030 equality already needing proof.
- **Re-entry condition:** either supply new collision geometry proving
  G030's exact equality, or abandon the preselected target and prove the
  genuinely minimal nonzero pairing condition in G031. A choice of relative
  representative is not a re-entry mechanism.
