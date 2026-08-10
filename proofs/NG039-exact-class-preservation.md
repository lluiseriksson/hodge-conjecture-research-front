---
brick_id: NG039
status: NO-GO
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold and a class-directed global-to-local detector construction
smoothness: X is smooth; the desired hyperplane target may be singular
projectivity: X and the hyperplane family are projective
dimension: dim_C X = 2n
codimension: middle codimension n
coefficient_field: Q
cohomology_theory: primitive singular Betti cohomology and homology with Tate twist and the Hodge-Riemann pairing
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B010, B016, B058-B059, and G030
claim: Exact recovery of the particular B058 tube target cannot be treated as a necessary or terminal-equivalent condition for detecting the specified Hodge class.
falsifier: a valid deduction from B010's nonzero-pairing criterion that every detecting local span contains the particular nonorthogonal class selected before the local geometry is constructed
---

# NG039 - Exact recovery of a preselected tube class is not necessary

## Failed route

Promote G030's equality

\[
 \Phi_{Y_p}(\beta)=c
\]

for the particular B058 target \(c\) from a sufficient collision theorem to
the smallest necessary, terminal-equivalent gate.

## Failure point

B059 proves that the terminal local criterion is only

\[
 \langle\zeta,\Phi_{Y_p}(\beta)\rangle\ne0.
\]

A detector subspace may contain a vector outside \(\zeta^\perp\) without
containing an independently preselected vector \(c\notin\zeta^\perp\).
Therefore exact recovery imposes an extra direction constraint that neither
B007 nor B010 requires.

This does not disprove the geometric theorem G030. It closes only the route
that treats exact equality with the selected global tube class as the
minimal logical gate.

## Re-entry condition

Use exact equality only if a geometric specialization theorem proves it
naturally, or if an additional proved property shows that the relevant local
detector image contains every nonorthogonal Hodge homology direction. For
the terminal argument, replace equality by preservation of the specified
nonzero pairing.
