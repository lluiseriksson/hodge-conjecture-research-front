---
brick_id: B102
status: PROVED
base_field: C
variety: a reduced pure n-dimensional complex analytic germ (X,0) with a holomorphic function f having an isolated singularity at 0; downstream, one local germ at each isolated singular point of a hyperplane fiber
smoothness: the theorem is stratified for reduced equidimensional X; in the nodal Hodge application the ambient germ and every nonzero Milnor fiber are smooth
projectivity: not required locally; the downstream hyperplane degeneration is projective
dimension: X has complex dimension n; the Milnor fiber has complex dimension n-1; the vanishing polyhedron has real dimension n-1
codimension: isolated critical locus; terminal application concerns middle codimension n in a complex 2n-fold
coefficient_field: Z topologically and Q after extension in the Hodge application
cohomology_theory: stratified topology, Milnor fibers, vanishing polyhedra, regular neighborhoods, and singular homology
hodge_type: none asserted; the collapsing map is topological
cycle_class_map: CH^n(X_global)_Q -> H^(2n)(X_global,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence in the terminal application
scope: fiberwise
dependencies: S049, Lê-Menegon Neto Theorem 1 and Propositions 14-16
claim: For an isolated analytic singularity and a path from a regular Milnor value t to 0, the Milnor fiber contains a real (n-1)-dimensional vanishing polyhedron P_t, is a regular neighborhood of P_t, and admits a continuous collapse to the special fiber that sends P_t to 0 and is a homeomorphism on the complements.
falsifier: an isolated analytic singularity satisfying S049's hypotheses for which no such vanishing polyhedron or collapsing map exists
---

# B102 — Isolated singularities admit local vanishing-polyhedron collapses

**Status:** PROVED

Apply S049 Theorem 1 to a reduced equidimensional analytic germ and a
holomorphic function with an isolated singularity. For every sufficiently
small regular value $t$ and a simple path from $t$ to $0$, there is a
polyhedron

\[
 P_t\subset X_t,
 \qquad \dim_{\mathbf R}P_t=n-1,
\]

such that $X_t$ is a regular neighborhood of $P_t$. The flow constructed in
the proof gives a continuous map

\[
 \Psi_t:X_t\longrightarrow X_0
\]

with

\[
 \Psi_t(P_t)=\{0\},
 \qquad
 \Psi_t:X_t\setminus P_t\xrightarrow{\sim}X_0\setminus\{0\}.
\]

Propositions 14-16 construct the polyhedra and vector fields along a path or
closed semidisk. Thus every isolated point in Saito's finite singular set
has a local topological collapse after choosing a disjoint Milnor ball.

## Scope guard

The theorem is local. It does not put B057's distributed global thimbles
inside those Milnor balls, identify their marked boundary vector, glue the
local collapses to one global comparison, preserve B022 quotient data, or
compare the resulting closed chain with the fixed ambient class $c$.
