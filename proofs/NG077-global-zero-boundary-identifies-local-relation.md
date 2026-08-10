---
brick_id: NG077
status: NO-GO
base_field: C with rational singular homology
variety: a B057 distributed thimble detector and an isolated clean nodal Saito collision target
smoothness: detector paths lie in the smooth locus; collision target has only ordinary double points
projectivity: ambient hyperplane family and collision projective
dimension: ambient 2n; hyperplane fibers 2n-1
codimension: middle codimension n; singular support finite
coefficient_field: Q
cohomology_theory: relative singular homology, marked local vanishing homology, and long exact sequences of pairs
hodge_type: no Hodge type conclusion; the intended local relation is rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057, B101, G064
claim: The equality of the total B057 boundary with zero in the smooth reference fiber canonically identifies its coefficient vector with the full-support local relation at the collision.
falsifier: a boundary map with a multidimensional kernel containing distinct marked local relation vectors with the same zero global image
---

# NG077 — Global boundary zero does not identify the local relation

**Status:** NO-GO

B057 proves

\[
 \sum_i c_i\delta_i=0
 \quad\text{in }H_{2n-1}(X_b;\mathbf Q(n)).
\]

Saito's boundary, however, lies before this gluing map, in the homology of
the disjoint local neighborhoods $Z_c$. A kernel of dimension greater than
one contains distinct marked vectors with the same zero image in the smooth
fiber. Therefore the global equality does not select
$r_H(\beta_{\mathrm{sp}})$.

B101 shows the proper re-entry condition: construct a map of pairs whose
restriction to the marked boundary components sends the B057 vector to the
canonical Saito local coordinate. Naturality then proves the boundary
identity; it cannot supply the missing marked map.
