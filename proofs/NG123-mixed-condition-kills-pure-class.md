---
brick_id: NG123
status: NO-GO
base_field: C
variety: a synchronized ordered N-node finite deformation model on a smooth projective complex 2n-fold with value rank R<N
smoothness: the nodes are ordinary double points at the formal second-order level; smooth excess is the invalid conclusion under audit
projectivity: inherited from downstream geometry; the countermodel is finite-dimensional local algebra
dimension: quotient dimension n; pure obstruction dimension (N-R)n(n+1)/2>0
codimension: the mixed conormal condition may hold with zero conormal map while the pure quotient class is arbitrary
coefficient_field: C
cohomology_theory: second-order nodal deformation theory and symmetric bilinear algebra
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle or specified detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B146, B151-B153, and G096-G097
claim: Synchronization together with B152's mixed conormal condition automatically forces B153's pure quotient Hessian class to vanish.
falsifier: set the core conormal map to zero and choose arbitrary symmetric quotient blocks C_i whose tuple is nonzero modulo im E
---

# NG123 — The mixed Hessian condition does not kill the pure class

- **Route:** impose synchronization and B152's mixed conormal kernel, then
  infer complete B146 isotropy.
- **Valid input:** every core-quotient Hessian pairing is annihilated by the
  value relations.
- **Invalid inference:** quotient-quotient Hessian pairings are thereby
  controlled.
- **Precise obstruction:** take the core conormal-gradient map to be zero.
  The mixed condition then holds trivially. In adapted Lagrangian coordinates
  choose inverse-Hessian matrices

  \[
  \begin{pmatrix}0&I\\I&C_i\end{pmatrix}
  \]

  with arbitrary symmetric \(C_i\). Their tuple defines an arbitrary class
  in

  \[
  \operatorname{coker}(E)\otimes\operatorname{Sym}^2Q^*,
  \]

  of positive dimension \((N-R)n(n+1)/2\). A nonzero class violates B146.
- **Re-entry condition:** construct G097 with \(\Omega_Q=0\) explicitly,
  then prove all-order integration and the specified pairing.
