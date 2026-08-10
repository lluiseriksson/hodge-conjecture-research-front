---
brick_id: NG098
status: NO-GO
base_field: Q in the exact local-system model and C in the geometric application
variety: abstract B022-kernel extension and the original transverse collision disk family
smoothness: disk pullback total space and nearby fibers smooth; central fiber has isolated hypersurface singularities
projectivity: downstream disk family proper/projective
dimension: hyperplane fibers d=2n-1; disk dimension 1
codimension: middle cycle codimension n; collision point has disk codimension one
coefficient_field: Q
cohomology_theory: rational local systems, B022 kernel quotients, nearby cycles, and isolated vanishing cohomology
hodge_type: unrestricted; the distinction is topological and filtered
cycle_class_map: not used; downstream map is CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence downstream
scope: relative and fiberwise
dependencies: B085, B120-B122, G050-G051, G082, S022
claim: Killing the cyclic monodromy cocycle of a raw thimble representative in the combined B022 kernel is stronger than necessary for an ordinary special lift; only its image in the actual degree-(d+1) nearby group matters, and B122 makes that entire target liftable.
falsifier: a downstream construction requiring an invariant raw chain rather than a special lift of its actual nearby cohomology image
---

# NG098 — The raw thimble cocycle need not vanish

**Status:** NO-GO

- **Route:** require a raw selected thimble representative \(t\in A\) to be
  adjusted to a monodromy-fixed vector before using its nearby cohomology
  image.
- **Valid input:** B085 exactly characterizes when such an invariant raw
  representative exists.
- **Invalid inference:** an invariant raw representative is necessary for
  the special lift of the quotient nearby class.
- **Precise obstruction:** let

  \[
  0\to\mathbf Qj\to
  A=\mathbf Qe\oplus\mathbf Qj
  \to P=\mathbf Q\bar e\to0
  \]

  with \(M(e)=e+j\) and \(M(j)=j\). The raw B085 class is
  \([j]\ne0\) in \(\operatorname{coker}(M_J-I)\), so no invariant raw lift
  exists. But \(M\) is the identity on \(P\), and \(\bar e\) is a perfectly
  invariant target class. B122 proves that the actual geometric
  degree-\((d+1)\) nearby target is entirely in this latter situation and
  every target class has an ordinary special lift.
- **Re-entry condition:** none for ordinary liftability. B123 computes the
  filtered obstruction as the nonzero target itself, so the relation must be
  constructed through G065's relative-boundary direction.
