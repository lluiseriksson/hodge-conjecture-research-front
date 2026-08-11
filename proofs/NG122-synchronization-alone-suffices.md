---
brick_id: NG122
status: NO-GO
base_field: C
variety: a smooth projective complex 2n-fold X and a synchronized ordered N-node first-jet candidate with value rank R<N
smoothness: X and the prospective nodes are smooth; smooth excess is the invalid conclusion under audit
projectivity: inherited from the projective linear system; the obstruction is finite-dimensional and second-order
dimension: projected quotient rank n; conormal target dimension nN; value-relation dimension N-R
codimension: synchronization alone permits conormal rank nN, while B152 requires rank at most nR
coefficient_field: C
cohomology_theory: first- and second-jet nodal deformation theory and bilinear algebra
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle or specified detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B146, B151-B152, and G095-G096
claim: Once the projected derivative blocks synchronize through one n-dimensional quotient, the Hessian-isotropic smooth-excess condition follows without any further restriction on conormal gradients.
falsifier: choose a surjective common-kernel conormal-gradient map onto the nN-dimensional conormal target; B152's mixed Hessian map has kernel dimension only nR<nN
---

# NG122 — Synchronization alone does not satisfy the Hessian obstruction

- **Route:** solve B151's synchronized first-order rank condition and infer
  B146 isotropy and smooth excess automatically.
- **Valid input:** all quotient gradients are controlled by one
  \(n\)-dimensional parameter space.
- **Invalid inference:** the conormal gradients of the common kernel are
  unrestricted.
- **Precise obstruction:** B152 polarizes B146 between common-kernel and
  synchronized directions. The resulting mixed map is surjective of rank
  \(n(N-R)\), so allowed conormal gradients lie in a subspace of dimension
  \(nR\). A surjective conormal-gradient map has rank \(nN>nR\) and violates
  the mixed equations despite perfect synchronization.
- **Re-entry condition:** construct G096's synchronized quotient and
  conormal image jointly inside the mixed-Hessian kernel, then verify the
  pure quadratic terms, integration, and specified pairing.
