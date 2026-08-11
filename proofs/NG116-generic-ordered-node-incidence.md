---
brick_id: NG116
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex 2n-fold X with a sufficiently jet-ample line bundle L and the generic ordered N-node incidence
smoothness: X is smooth; the ordered incidence and its generic nodal image are smooth with transverse node branches
projectivity: X and |L| are projective; the ordered configuration space is quasi-projective
dimension: dim_C X=2n; the generic ordered incidence has expected codimension (2n+1)N and value rank N
codimension: node branches meet with total codimension N in |L|; target cycles have middle codimension n
coefficient_field: C for jets and incidence geometry; Q for the absent downstream relation space
cohomology_theory: principal-parts evaluation, adjoint coherent evaluation, nodal vanishing cycles, and local intersection cohomology
hodge_type: no relation class exists in the high-power generic-independent range
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence
scope: generic
dependencies: B015, B027-B028, B145, G090-G091
claim: A generic first-jet-surjective ordered-node incidence supplies the smooth saturated stratum, positive adjoint defect, and relation required by G091.
falsifier: first-jet surjectivity forces value rank N, and B027-B028 force zero adjoint defect and zero relation space
---

# NG116 — Generic ordered-node incidence is too transverse

**Status:** NO-GO

- **Route:** use the generic smooth ordered \(N\)-node incidence for a
  sufficiently jet-ample linear system as G091's saturated component.
- **Valid input:** surjectivity of

  \[
  H^0(X,L)\longrightarrow
  \bigoplus_{i=1}^N P^1(L)|_{p_i}
  \]

  makes the ordered incidence smooth of expected codimension
  \((2n+1)N\). Its projection gives \(N\) transverse labeled discriminant
  branches.
- **Invalid inference:** this smooth incidence has a nonzero adjoint defect
  or vanishing-cycle relation.
- **Precise obstruction:** first-jet surjectivity implies surjectivity of
  value evaluation, so the smoothing matroid is \(U_{N,N}\). In the
  high-power range, multiplication by a section of
  \(K_X\otimes L^{n-1}\) nonzero at the nodes gives

  \[
  r_L(\Delta)=N\le r_{K_X\otimes L^n}(\Delta)\le N.
  \]

  Hence the adjoint evaluation is also surjective. B026-B028 give zero
  adjoint defect, zero vanishing relation, and zero local detector channel.
- **Re-entry condition:** construct a point with value rank \(R<N\) where
  the ordered incidence is nevertheless smooth of the exact excess
  codimension \(2nN+R\), and prove a specified nonzero Saito pairing. This
  is G091.
