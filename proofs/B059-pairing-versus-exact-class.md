---
brick_id: B059
status: PROVED
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold, with an abstract collection of Saito detector classes in its primitive rational Hodge homology
smoothness: X is smooth; candidate detecting hyperplane sections may be singular
projectivity: X and the hyperplane family are projective
dimension: dim_C X = 2n
codimension: middle codimension n
coefficient_field: Q
cohomology_theory: primitive singular Betti cohomology and homology with Tate twist, equipped with the Hodge-Riemann pairing
hodge_type: rational type (0,0) in cohomology and homology after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B010, B016, and B058
claim: For a fixed nonzero primitive Hodge class zeta, local detection requires only a detector class outside zeta-perp; requiring a detector space to contain a preselected Hodge homology class c with nonzero pairing is sufficient but strictly stronger as a linear-algebra obligation.
falsifier: a proof that nonzero pairing with a detector subspace forces every preselected nonorthogonal Hodge homology class to belong to that subspace
---

# B059 - Pairing preservation is weaker than exact class preservation

Let

\[
 H=H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))^{(0,0)},\qquad
 V=H_{2n}^{\mathrm{prim}}(X,\mathbf Q(n))^{(0,0)},
\]

and let \(\langle-,-\rangle:H\times V\to\mathbf Q\) be the perfect
Hodge-Riemann pairing. For a collection of local Saito relations, write
\(D\subseteq V\) for the span of their ambient detector classes.

For a fixed \(0\ne\zeta\in H\), B010 says precisely

\[
 \text{the collection detects }\zeta
 \quad\Longleftrightarrow\quad
 D\not\subseteq\zeta^\perp.
\]

B058 permits choosing one \(c\in V\) with
\(\langle\zeta,c\rangle\ne0\) and then realizing \(c\) by a global tube.
If a collision proves \(c\in D\), it certainly detects \(\zeta\). The
converse is not a consequence of the terminal criterion: detection only
provides some \(d\in D\) outside \(\zeta^\perp\).

## Strictness

This distinction is strict already in rational type-\((0,0)\) linear
algebra. Take

\[
 V=\mathbf Q^2,\qquad
 \zeta(x,y)=x,\qquad
 c=(1,0),\qquad
 D=\mathbf Q(1,1).
\]

Then \(\zeta(c)=1\), and \(D\not\subseteq\ker\zeta\), but \(c\notin D\).
Give all of \(V\) pure type \((0,0)\); no coefficient or Hodge-type issue
changes the example.

This is a countermodel to a proposed *logical equivalence*, not a geometric
counterexample to G030. G030's exact equality may conceivably hold because
of additional geometry, but it is not the smallest consequence needed for
HC. The class-directed collision obligation should preserve the nonzero
pairing, not a chosen representative in \(V\).

## Scope guard

This brick is finite-dimensional linear algebra combined with B010. It
constructs no singular hyperplane, local relation, or algebraic cycle and
makes no progress on nonemptiness of the class-specific local support.
