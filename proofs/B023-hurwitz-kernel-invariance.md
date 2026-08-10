---
brick_id: B023
status: PROVED
base_field: not applicable to the symplectic theorem; C when an exact Morse fibration comes from a holomorphic Lefschetz pencil
variety: an exact symplectic Morse fibration over a disk with finitely many critical values and a fixed smooth reference fiber
smoothness: the total space and regular fibers are smooth; all critical points are Morse
projectivity: not assumed
dimension: arbitrary exact symplectic fiber dimension in Seidel's theorem; the matching/cusp application uses real ambient dimension 4
codimension: middle-dimensional vanishing cycles and thimbles; no algebraic codimension is asserted
coefficient_field: Z on homology and Q for rank comparisons
cohomology_theory: singular homology, Picard-Lefschetz monodromy, Dehn twists, Lefschetz thimbles, and vanishing-cycle boundary maps
hodge_type: none; Hurwitz equivalence is symplectic and supplies no Hodge-type assertion
cycle_class_map: not involved; in a projective comparison CH^p(X)_Q -> H^{2p}(X,Q(p)) remains an additional structure
cycle_equivalence: not applicable to the symplectic statement; rational equivalence in any later projective comparison
scope: relative and fiberwise
dependencies: Seidel Introduction and Definition 2.1 (S028), B022 boundary-map model, and elementary linear algebra
claim: Hurwitz moves within a fixed exact Morse fibration are invertible changes of distinguished vanishing-cycle/thimble data and therefore preserve the rank of the boundary map and the dimension of its relation kernel; they cannot turn a matching two-cycle kernel into an independent cusp pair with zero kernel.
falsifier: a Hurwitz move and its inverse on a fixed fibration that change the rank of the rational vanishing-cycle boundary map or the dimension of its kernel
---

# B023 - Hurwitz kernel invariance

Seidel proves that any two distinguished bases of vanishing cycles for a
fixed exact Morse fibration over a disk are related by Hurwitz moves. His
Definition 2.1 writes these moves using symplectomorphisms and Dehn twists
and explicitly includes their inverses. On homology, they therefore induce
invertible integral transformations of the distinguished thimble module and
of the reference-fiber homology.

Abstractly, let

\[
 \partial:A\longrightarrow V
\]

be the thimble boundary map, and suppose a change of distinguished basis
gives isomorphisms \(u:A\to A'\) and \(v:V\to V'\) with

\[
 \partial' u=v\partial.
\]

Then \(u\) restricts to an isomorphism

\[
 \ker\partial\simeq\ker\partial'.
\]

In particular, the boundary rank and relation-kernel dimension are Hurwitz
invariants of the fixed fibration.

For the two-generator surface comparison, a matching pair has equal
vanishing-cycle classes up to sign, so its boundary map has rank at most one
and a nonzero kernel. (If the common class is nonzero, the kernel is exactly
one-dimensional; if it is null-homologous, the kernel is larger.) Schnell's
cusp pair has intersection number one, so its boundary map has rank two and
zero kernel. No sequence of Hurwitz moves inside one fixed fibration can
identify these two boundary maps.

## Consequence for the collision route

B021 allowed “basis change” as a logical escape from the class-by-class rank
obstruction. B023 removes **pure Hurwitz basis change within a fixed
fibration** from that list. A surviving collision must change the relevant
complex non-invertibly, add vanishing cycles, or compare only later quotient
classes such as those in B022. Such a topology-changing specialization is
not supplied by Hurwitz equivalence.
