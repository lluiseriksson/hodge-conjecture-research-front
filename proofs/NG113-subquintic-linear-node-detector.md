---
brick_id: NG113
status: NO-GO
base_field: C
variety: a fixed smooth projective complex 2n-fold X with fixed very ample H and high-power nodal hypersurface members
smoothness: X is smooth; the attempted hypersurface has isolated ordinary double points
projectivity: X, its H-embedding, carrier curves, and hypersurface members are projective
dimension: dim_C X=2n with n at least 2; hypersurface dimension 2n-1
codimension: middle codimension n on X; nodes have codimension 2n
coefficient_field: C for adjoint evaluation and first jets; Q for vanishing-cycle relations
cohomology_theory: coherent adjoint cohomology, Cayley-Bacharach postulation, bounded curve-family separation, and nodal vanishing homology
hodge_type: the attempted relation would have rational type (0,0) after Q(n), but the route is excluded before class pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B026-B029, B136-B140, G013, S055, S059
claim: Close G013 with an isolated-nodal high-power member having at most 5(mn-c)-11 nodes and nonzero adjoint defect.
falsifier: B140, which puts a minimal degree-(mn-c) evaluation circuit on a degree-at-most-four curve and forces an integral component into the singular locus
---

# NG113 — Sub-quintic-linear nodal detectors are nonisolated

**Status:** NO-GO

- **Route:** cross B139's quartic-linear floor but retain at most
  \(5(mn-c)-11\) nodes while seeking a nonzero B135 relation.
- **Valid input:** Picoco's previously used \(h=4\) theorem controls only
  degree-at-most-three carriers.
- **Invalid inference:** a reducible or singular quartic carrier evades the
  carrier first-jet obstruction.
- **Precise obstruction:** B140 applies the \(h=5\) case of S059 to a
  minimal \(\mathrm{CB}(mn-c)\) circuit. Uniform component separation and
  curve duality force one integral component of degree \(e\) to carry
  \(e(mn-c)-O(1)\) nodes. Bounded conormal degrees then force that component
  into the hypersurface singular locus.
- **Re-entry condition:** use at least \(5(mn-c)-10\) nodes and prove all
  remaining G013 conditions: isolated first jets, multipart smoothability,
  positive adjoint defect, positive ambient rank, and a nonzero B135
  residue-cokernel value for the specified rational Hodge class.
