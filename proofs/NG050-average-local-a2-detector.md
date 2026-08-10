---
brick_id: NG050
status: NO-GO
base_field: C with rational descent data
variety: the S3 root-covered A2 semistable family and its local vanishing lattice
smoothness: semistable stack from B071; local Milnor fibers smooth
projectivity: projective stack operations from B071-B072
dimension: arbitrary ambient dimension 2n and odd fiber dimension 2n-1
codimension: terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, vanishing homology, proper pushforward, and finite-group trace
hodge_type: rational type (0,0) after Q(n) is required downstream but not supplied here
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B072-B073
claim: A nonzero local A2 vanishing-cycle detector descends nontrivially to the original family by normalized S3 averaging.
falsifier: the average projector is zero on the A2 vanishing lattice
---

# NG050 — Averaging a local A2 detector gives zero

**Status:** NO-GO

## Route tested

Choose a nonzero local \(A_2\) vanishing class on the ordered-root cover and
apply the rational normalized trace

\[
\frac1{6}\sum_{g\in S_3}g.
\]

## Failure

B073 proves that the local \(A_2\) vanishing lattice is the standard
two-dimensional \(S_3\)-representation and has no invariants. Its normalized
trace is identically zero. B072 ensures that the averaging morphism makes
sense in rational equivariant mixed Hodge modules; it does not make the
result nonzero.

## Re-entry condition

Prove G041 by locating a nonzero invariant component in the larger
full-support nearby-cycle object and showing that it survives both B022
quotients and pairs nontrivially with the prescribed Hodge class. A purely
local root-lattice class cannot do this.
