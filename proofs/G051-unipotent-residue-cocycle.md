---
brick_id: G051
status: EXPLORATORY
base_field: C with rational nearby-cycle and kernel data
variety: an arbitrary polarized smooth projective complex 2n-fold, a B058 detector, and a semistable proper collision model after finite root cover
smoothness: generic fibers smooth and semistable source regular; special fiber SNC or stack-semistable
projectivity: ambient, hyperplane, and collision models projective
dimension: ambient 2n, hyperplane fibers 2n-1, and collision parameter 1
codimension: middle codimension n; special fiber has parameter codimension one
coefficient_field: Q
cohomology_theory: unipotent nearby cycles, monodromy logarithm, B022 thimble quotients, limit mixed Hodge structures, and cyclic-group cohomology
hodge_type: an invariant adjusted lift must retain the B058 rational type-(0,0) pairing after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022-B023, B057-B059, B063, B071-B076, B084-B088, G050, NG061-NG064
claim: Compute the nilpotent collision residue N on the exact B057 lift t and the combined B022 kernel J, and prove [Nt]=0 in coker(N_J) by exhibiting k in J with Nt+N_J k=0, while retaining the ambient class and prescribed pairing.
falsifier: a nonzero residue obstruction for every admissible semistable collision, failure of J to be N-stable, or loss of rationality or pairing under every residue-killing adjustment
---

# G051 — Kill the unipotent residue cocycle

**Status:** EXPLORATORY  
**Parent gate:** G050

After B086 averages the finite deck action, let $M=\exp N$ be the remaining
unipotent collision monodromy. Compute

\[
 Nt\in J,
 \qquad
 N_J:J\to J.
\]

The exact target is

\[
 [Nt]=0\quad\text{in}\quad\operatorname{coker}N_J.
\]

Produce an explicit rational kernel vector $k$ satisfying

\[
 Nt+N_Jk=0.
\]

Then $t+k$ is collision-monodromy invariant, has the same B022 ambient
quotient and prescribed pairing, and enters B084's local invariant-cycle
surjection.

The required input is the logarithmic residue matrix of the actual
semistable B057 coefficient object, not merely the local $A_2$ root lattice.
B073 already shows that the purely local constituent cannot carry the
needed invariant detector by itself.

B088 gives a zero-residue mechanism stronger than solving for $k$: if the
collision is marked so that its braid action is purely Hurwitz and returns
the exact pair $(g,\alpha)$, then the geometric composite extension chain is
fixed and $Nt=0$. G052 is the active construction gate for this mechanism;
NG064 prevents inferring the marked return from rank preservation alone.
