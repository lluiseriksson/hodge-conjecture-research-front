---
brick_id: NG114
status: NO-GO
base_field: C
variety: a fixed smooth projective complex 2n-fold X with fixed very ample H and high-power nodal hypersurface members
smoothness: X is smooth; the attempted hypersurfaces have isolated ordinary double points
projectivity: X, its H-embedding, carrier curves, and hypersurface members are projective
dimension: dim_C X=2n with n at least 2; hypersurface dimension 2n-1
codimension: middle codimension n on X; nodes have codimension 2n
coefficient_field: C for adjoint evaluation and first jets; Q for vanishing-cycle relations
cohomology_theory: coherent adjoint cohomology, Cayley-Bacharach postulation, bounded curve-family separation, and nodal vanishing homology
hodge_type: the attempted relation would have rational type (0,0) after Q(n), but the route is excluded before class pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B026-B029, B136-B141, G013, S055, S060
claim: Close G013 by a sequence of isolated-nodal high-power members with nonzero adjoint defect and |Delta_m| at most C(mn-c)+D for fixed constants C and D.
falsifier: B141, which for every fixed E forces |Delta_m| at least E(mn-c)-f_N(E) once m is sufficiently large
---

# NG114 — Every linearly growing nodal detector is nonisolated

**Status:** NO-GO

- **Route:** replace the successive Picoco thresholds by any fixed linear
  budget \(|\Delta_m|\le C(mn-c)+D\).
- **Valid input:** B136 requires unbounded growth, while B137-B140 impose
  successively stronger explicit linear floors.
- **Invalid inference:** choosing a sufficiently large fixed linear
  coefficient eventually escapes every bounded-degree carrier theorem.
- **Precise obstruction:** choose an integer \(E>C\). S060 places the
  minimal \(\mathrm{CB}(mn-c)\) circuit on a degree-at-most-\(E\) curve for
  all sufficiently large \(m\). B140's uniform component and conormal lemma
  then forces an integral component into the hypersurface singular locus.
  B141 formalizes the resulting limit

  \[
   |\Delta_m|/(mn-c)\longrightarrow\infty.
  \]

- **Re-entry condition:** construct a genuinely superlinear multipart node
  scheme, retain isolated first jets and both G013 rank systems, and prove a
  nonzero B135 residue-cokernel value for the specified rational Hodge class.
