---
brick_id: NG119
status: NO-GO
base_field: C
variety: a smooth projective complex 2n-fold X, a high-power complete linear system, and an ordered N-node point at which conditional first jets are surjective
smoothness: X is smooth and the selected singularities are ordinary double points
projectivity: X and the linear system are projective; the obstruction is finite-dimensional linear algebra
dimension: dim_C X=2n, N>1, and the quotient by one maximal isotropic n-plane at each node has dimension nN
codimension: G093 requires projected-gradient rank at most n, while conditional-gradient surjectivity forces rank nN
coefficient_field: C for gradients, Hessians, Lagrangian subspaces, and ranks; Q only in the absent downstream Hodge pairing
cohomology_theory: first-jet nodal deformation theory and linear algebra; no Hodge class is produced
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle or class-specific detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B146-B148, G093, and NG116-NG117
claim: Starting from a conditionally first-jet-surjective nodal incidence, choose maximal inverse-Hessian-isotropic subspaces at the nodes so that the projected conditional-gradient map has rank at most n.
falsifier: for every choice of nodewise n-dimensional subspaces, surjectivity of D implies surjectivity onto their nN-dimensional quotient, whose rank exceeds n when N>1
---

# NG119 — Lagrangians chosen after generic jets do not create the rank defect

- **Route:** begin with a generic conditionally first-jet-surjective nodal
  point and choose maximal inverse-Hessian-isotropic subspaces
  \(\Lambda_i\) after seeing its Hessians, hoping to obtain G093.
- **Valid input:** every nondegenerate complex quadratic space of dimension
  \(2n\) has maximal isotropic \(n\)-planes.
- **Invalid inference:** choosing those planes lowers the rank of the
  conditional-gradient map.
- **Precise obstruction:** if
  \(D:\ker E\twoheadrightarrow\bigoplus_iG_i\) is surjective, then for every
  choice of \(\Lambda_i\subset G_i\), the composite

  \[
  \ker E\xrightarrow{D}\bigoplus_iG_i
  \longrightarrow\bigoplus_iG_i/\Lambda_i
  \]

  is surjective. Its rank is \(nN>n\) for \(N>1\), whereas B148's carrier
  shadow and G093 require rank at most \(n\).
- **Re-entry condition:** make the section space, node scheme, and
  Lagrangian quotient fail interpolation together by construction; then
  integrate that special jet package and verify the specified pairing.
