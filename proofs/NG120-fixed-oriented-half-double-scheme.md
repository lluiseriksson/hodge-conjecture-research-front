---
brick_id: NG120
status: NO-GO
base_field: C
variety: a fixed smooth projective complex 2n-fold X with an ample line bundle H and a bounded-length family of oriented half-double zero-dimensional schemes Xi
smoothness: X and the reduced support points are smooth
projectivity: X, the Hilbert scheme of fixed-length subschemes, and its universal family are projective
dimension: dim_C X=2n; the number N of support points is bounded independently of the power m
codimension: Xi has bounded length (n+1)N; for m sufficiently large it imposes all of those conditions independently
coefficient_field: C for coherent cohomology, Hilbert schemes, and ranks; Q only in the absent downstream Hodge pairing
cohomology_theory: coherent sheaf cohomology, relative Serre vanishing, zero-dimensional Hilbert schemes, and first jets
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle or specified detector is constructed
cycle_equivalence: rational equivalence
scope: generic
dependencies: B136, B141, B149, G093-G094
claim: Keep N bounded while increasing m and retain G094's rank bound rank(H^0(H^m) -> H^0(Xi,H^m|Xi)) <= R+n with R<N.
falsifier: uniform relative Serre vanishing over the fixed-length Hilbert scheme makes evaluation onto Xi surjective for all sufficiently large m
---

# NG120 — A fixed oriented half-double scheme separates in high power

- **Route:** keep a fixed or uniformly bounded number \(N\) of oriented
  half-double points and increase the embedding power until the remaining
  nodal and Hodge conditions become favorable.
- **Valid input:** for an individual low power, an oriented finite scheme
  can be superabundant.
- **Invalid inference:** its B149 defect persists in arbitrarily high powers.
- **Precise obstruction:** the schemes \(\Xi\) have fixed length
  \((n+1)N\) and belong to a projective Hilbert scheme. Relative Serre
  vanishing for the universal ideal gives

  \[
  H^1(X,I_\Xi\otimes H^m)=0
  \]

  uniformly for all such \(\Xi\) once \(m\) is large. Hence evaluation onto
  \(H^0(\Xi,H^m|_\Xi)\) is surjective of rank \((n+1)N\), incompatible with
  G094's rank at most \(R+n<(n+1)N\) for \(N>1\).
- **Re-entry condition:** let \(N\) and the oriented scheme complexity grow
  with \(m\), obey B141's superlinear support floor, and prove every G094
  Hessian, integration, and pairing condition.
