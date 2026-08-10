---
brick_id: G050
status: EXPLORATORY
base_field: C with all local systems and classes over Q
variety: an arbitrary polarized smooth projective complex 2n-fold, a B058 detector, and a proper one-parameter collision model
smoothness: generic collision fibers smooth; endpoint singular; IC coefficients allowed on the proper total space
projectivity: ambient, hyperplane, and collision models projective
dimension: ambient 2n, hyperplane fibers 2n-1, and collision parameter 1
codimension: middle codimension n; endpoint has positive parameter codimension
coefficient_field: Q
cohomology_theory: relative thimble homology, B022 quotient local systems, collision monodromy, nearby intersection cohomology, and cyclic-group cohomology
hodge_type: the adjusted invariant lift must ultimately retain rational type-(0,0) pairing after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022-B023, B055, B057-B059, B084-B087, G049, NG061-NG063
claim: For the exact B057 chain in a proper collision model, compute the combined B022-kernel monodromy J and prove the defect class [M(t)-t] vanishes in coker(M_J-I), producing a collision-monodromy-invariant adjusted lift with the same ambient class and pairing.
falsifier: a nonzero obstruction class for every admissible collision model, failure of the B022 kernels to form a monodromy-stable local system, or loss of rationality or pairing under every invariant adjustment
---

# G050 — Kill the kernel-valued collision cocycle

**Status:** EXPLORATORY  
**Parent gate:** G049

Let $A$ be the boundary-zero thimble local system for a chosen proper
collision model, let $J$ be the combined kernel of the two B022 quotient
maps, and let $t$ be the B057 chain over a base point. Compute

\[
 d=M_{mathrm{coll}}t-t\in J.
\]

The falsifiable target is

\[
 [d]=0
 \quad\text{in}\quad
 \operatorname{coker}(M_J-I).
\]

An explicit $k\in J$ satisfying

\[
 d+(M_J-I)k=0
\]

produces the invariant adjusted lift $t+k$. Because $k$ is killed by the
ambient quotient, the adjusted lift has the same primitive ambient class
and prescribed pairing as B058. B084 can then supply a special-fiber lift.

## Required computation

The calculation must give the braid matrix on the actual ordered thimble
basis, the equator-extension subspace, the base-locus kernel, and the B057
coefficient vector. Knowing only that their dimensions are constant is
insufficient.

B086 closes the finite deck-group part by Reynolds averaging. B087 reduces
the remaining semistable unipotent part to G051's residue class
$[Nt]\in\operatorname{coker}N_J$. Thus G051 is the active smallest
calculation.
