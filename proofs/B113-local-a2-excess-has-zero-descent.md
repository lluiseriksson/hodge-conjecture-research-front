---
brick_id: B113
status: PROVED
base_field: C for the collision geometry and Q for the S3 representation and descent
variety: an arbitrary polarized smooth projective complex 2n-fold X, a selected B058 detector, and the ordered-root cover of a local A2 collision
smoothness: X and generic hyperplane fibers smooth; local Milnor fibers smooth; no global collision realization is asserted
projectivity: X and the hyperplane family projective; the representation theorem is local
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; local A2 vanishing lattice rank 2
codimension: middle codimension n; local vanishing support lies over the collision point
coefficient_field: Q
cohomology_theory: rational local vanishing homology, S3-equivariant nearby cycles, finite-group Reynolds descent, strict-support representations, and B022 quotient homology downstream
hodge_type: no Hodge type is created; a downstream descended excess must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B067, B072-B076, B112, G041-G042, G074
claim: If G074's selected excess lies entirely in the local A2 root-lattice constituent on the ordered-root S3 cover, its rational Reynolds descent is zero. In any global S3-module containing that constituent, a nonzero descended excess must have a nonzero component in an additional trivial isotypic constituent.
falsifier: a nonzero S3-invariant vector in the rational A2 standard representation, a nonzero Reynolds average of a local root-lattice vector, or a global direct-sum vector whose invariant projection is nonzero while its nonlocal trivial component is zero
---

# B113 — A purely local (A_2) excess has zero rational descent

**Status:** PROVED

On the ordered-root cover, the local (A_2) vanishing lattice is

\[
 V=\{(x_1,x_2,x_3)\in\mathbf Q^3:x_1+x_2+x_3=0\},
\]

the standard rational representation of (S_3). B073 proves

\[
 V^{S_3}=0,
 \qquad
 e_{S_3}|_V=0,
 \qquad
 e_{S_3}=\frac1{6}\sum_{g\in S_3}g.
\]

Let (e_t) be B112's selected topology-changing excess on the root cover.
If (e_t\in V), then its normalized rational descent is

\[
 e_{S_3}e_t=0.
\]

Thus a nonzero local (A_2) coordinate, even when exactly computed, cannot
by itself define G074's rational class on the original family.

More generally, write the relevant global coefficient representation as

\[
 M=V\oplus W.
\]

For (e_t=v+w),

\[
 e_{S_3}e_t=e_{S_3}w.
\]

Consequently a nonzero descended excess requires a nonzero projection of the
selected class to the trivial isotypic part of the nonlocal/global
constituent (W). The existence of such a constituent as an object does not
put (e_t) in it; NG051 and NG054 retain that class-landing obstruction.

## Relation to the existing vertical chain

This is the selected-excess form of B073/NG050. It places G074 back in the
global full-support problem already isolated by G041-G042: global thimble
extensions, not the isolated root lattice, must carry the invariant
coordinate. G075 records only the first class-specific landing calculation
and is not counted as an independent reduction of the terminal conjecture.

## Scope guard

B113 is a negative representation-theoretic theorem. It constructs no
global component, nearby class, local relation, or algebraic cycle.
