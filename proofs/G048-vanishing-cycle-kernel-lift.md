---
brick_id: G048
status: EXPLORATORY
base_field: C with all comparison data and classes over Q
variety: an arbitrary polarized smooth projective complex 2n-fold, a B058 detector, and a one-parameter algebraic collision family inside the plane-net deformation space
smoothness: X and generic detector fibers smooth; collision fiber singular; semistable replacement regular as a stack
projectivity: X, hyperplane family, collision family, and semistable pushdown projective
dimension: ambient 2n, hyperplane fibers 2n-1, plane-net base 2, and collision parameter 1
codimension: middle codimension n; collision parameter has codimension one and endpoint support has plane-base codimension one or two
coefficient_field: Q
cohomology_theory: rational relative homology, nearby and vanishing cycles, mixed Hodge modules, perverse filtration, and B022 quotient homology
hodge_type: a chosen special lift must be rational type (0,0) after Q(n), or have a full-support component whose ambient image pairs nontrivially with the prescribed type-(0,0) class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B059, B063, B071-B083, G047, NG059-NG060
claim: For the B057 extension chain in a suitable algebraic collision family, construct a rational nearby class t_psi with can(t_psi)=0 in shifted vanishing cycles and choose a special-stalk lift beta whose B022 ambient image remains nonorthogonal to the prescribed Hodge class.
falsifier: failure to realize the extension chain as a nearby class, nonzero vanishing-cycle obstruction, absence of a rational type-compatible lift, confinement of all lifts to a B022 kernel, or orthogonality of every lift
---

# G048 — Kill the vanishing-cycle obstruction and choose a lift

**Status:** EXPLORATORY  
**Parent gate:** G047

For collision data $(f:\mathfrak X\to T,K)$, first realize the ordered B057
extension chain as a rational class

\[
 t_\psi\in H^{-1}(i_p^*\Psi_fK).
\]

The exact target is then:

1. compute the canonical obstruction and prove

   \[
   \mathrm{can}(t_\psi)=0
   \quad\text{in}\quad
   H^{-1}(i_p^*\Phi_fK[1]);
   \]

2. choose

   \[
   \beta\in H^{-1}(i_p^*K)
   \]

   mapping to $t_\psi$;
3. prove that the lift is rational and compatible with type $(0,0)$ after
   $\mathbf Q(n)$;
4. compute the ambiguity by the preceding term of B083's long exact
   sequence and show that at least one lift survives both B022 quotients with
   nonzero prescribed pairing.

After these four tests, G046 analyzes the canonical perverse grade and
strict support of $\beta$. A rank calculation for nearby or vanishing
cycles does not establish the required kernel membership of the specified
class.
