---
brick_id: B019
status: PROVED
base_field: not applicable to the symplectic theorem; C only when a projective surface is used for comparison with the Hodge problem
variety: a smooth symplectic real four-manifold X with a symplectic Lefschetz pencil; the audited examples are two Horikawa surfaces
smoothness: X is smooth; the pencil has Lefschetz critical points and a smooth midpoint fiber along the matching path
projectivity: not assumed by the matching-path construction; the audited Horikawa examples are projective complex surfaces
dimension: real dimension 4, hence complex dimension 2 in the projective comparison
codimension: the matching sphere has real middle dimension 2; the corresponding projective-surface Hodge comparison is codimension 1
coefficient_field: Z for the oriented sphere class and Q after extension of coefficients
cohomology_theory: singular homology, symplectic parallel transport, Lefschetz thimbles, and Picard-Lefschetz monodromy
hodge_type: no Hodge type is asserted by the symplectic construction; type (1,1) is an additional condition in the projective-surface comparison
cycle_class_map: CH^1(X)_Q -> H^2(X,Q(1)) only in the projective-surface comparison; the matching-path theorem does not invoke it
cycle_equivalence: rational equivalence only in the projective-surface comparison; no algebraic cycle is constructed by the symplectic theorem
scope: relative and fiberwise
dependencies: Auroux Definition 8.1 and the matching-thimble construction on pp. 2214-2215 (S027)
claim: In the audited four-dimensional setting, a matching path joins two distinct critical values through smooth fibers and glues their two transported thimbles into an embedded Lagrangian sphere; this is not a relation among simultaneous vanishing cycles at one singular fiber and gives no automatic Hodge-type or algebraic-cycle conclusion.
falsifier: an audited matching path in this definition whose two critical endpoints represent one simultaneous singular fiber, or a theorem in the cited construction asserting that the resulting class is automatically of rational Hodge type and algebraic on an arbitrary projective variety
---

# B019 - Matching-path type separation

Auroux's Definition 8.1 considers a symplectic Lefschetz pencil

\[
 f:X^4\setminus B\longrightarrow S^2
\]

and an embedded arc \(\gamma:[0,1]\to S^2\) whose inverse image of the
critical-value set is exactly \(\{0,1\}\). The two vanishing cycles obtained
from the half-arcs are required to be isotopic in the smooth midpoint fiber.
Joining the corresponding Lefschetz thimbles produces an embedded
Lagrangian sphere in \(X\), up to isotopy.

This construction has three type distinctions from the local Saito channel
in B009-B010:

1. The endpoints are two distinct critical values of the pencil; they are
   not two simultaneous nodes of one singular hyperplane member.
2. Equality or isotopy of the two transported vanishing cycles in a smooth
   midpoint fiber is monodromy data. It is not, without a further collision
   theorem, an element of the relation kernel attached to one singular
   fiber.
3. The glued object is a smooth real Lagrangian sphere. Its oriented
   fundamental class is integral, but the symplectic construction asserts
   neither rational Hodge type \((0,0)\) after the relevant Tate twist nor
   membership in the image of an algebraic cycle-class map.

In the audited Horikawa examples the ambient manifolds happen to be complex
projective surfaces. That does not upgrade the mechanism to a general Hodge
theorem: codimension one on a projective surface is already covered by the
Lefschetz \((1,1)\) theorem, and the matching sphere is not automatically a
\((1,1)\)-class.

## Consequence for G009

A matching path is useful topological evidence that two thimbles can glue to
non-tautological ambient middle homology. To enter the G009 detector span one
would still need an algebraic collision that puts the relevant singularities
on one hyperplane member, a comparison identifying the glued class with
Saito's \(\gamma_\beta\), and a proof that \(\beta\) has rational type
\((0,0)\). None is part of the matching-path theorem.

