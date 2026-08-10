---
brick_id: NG099
status: NO-GO
base_field: C with rational coefficients
variety: the original transverse clean-nodal collision disk for an arbitrary polarized smooth projective complex 2n-fold
smoothness: disk total space and nearby fiber smooth; central fiber nodal
projectivity: degeneration projective/proper
dimension: ambient 2n; hyperplane fibers d=2n-1; disk dimension 1
codimension: middle cycle codimension n; singular support finite
coefficient_field: Q
cohomology_theory: special/nearby exact sequence, perverse filtration, relative homology, and local vanishing-cycle relations
hodge_type: relation grade type (0,0) after Q(n); impossibility is rational and independent of total-lift type
cycle_class_map: not used; downstream map is CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence downstream
scope: relative and fiberwise
dependencies: B010, B099-B101, B107-B109, B123, G064-G071, G079-G083, S022
claim: The route requiring a nonzero nearby class to lie in the image of the relation filtration step is impossible in the clean nodal disk because u_Delta(S_0)=0.
falsifier: a nonzero clean-nodal nearby class with a special lift in S_0
---

# NG099 — A nonzero nearby class cannot lift through the relation grade

**Status:** NO-GO

- **Route:** realize a nonzero selected nearby class \(t_\Delta\) and prove
  \(t_\Delta\in u_\Delta(S_0)\).
- **Valid input:** ordinary specialization is surjective by B122, and the
  relation grade inside the special stalk is nonzero when nodal relations
  exist.
- **Invalid inference:** the relation grade maps nontrivially to nearby
  cohomology.
- **Precise obstruction:** B123 identifies \(S_0\) with the extra-cohomology
  kernel of specialization, so

  \[
  u_\Delta(S_0)=0.
  \]

  Hence \(\omega_{\mathrm{fil}}(t_\Delta)=t_\Delta\ne0\) for every nonzero
  target class. G070, G071, and G083 cannot pass in this clean nodal model.
- **Re-entry condition:** reverse the arrow. Construct G065's marked map of
  pairs carrying the selected B057 relative class to
  \(H_{2n}(Y_t,Z_t)\), and prove its local boundary is a nonzero Saito
  relation with the required ambient pairing. B099-B101 then propagate the
  result without any special-to-nearby filtered lift.
