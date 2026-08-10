---
brick_id: B011
status: PROVED
base_field: C
variety: a smooth projective variety X with a fixed projective embedding and the family of all smooth hyperplane sections
smoothness: X and every fiber over the smooth hyperplane locus are smooth
projectivity: X projective and embedded in projective space
dimension: arbitrary d; the active application has d = 2n
codimension: middle codimension n when d = 2n
coefficient_field: Q
cohomology_theory: singular homology and cohomology, vanishing homology, monodromy, and Poincare duality
hodge_type: unrestricted primitive middle cohomology; the application restricts the target class to type (n,n)
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n)) in the Hodge application; no algebraic cycle is produced by the tube theorem
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: Schnell Theorem 1 (S023); BFNP Proposition 5.11 (S009) for nonzero vanishing cycles after a high power
claim: If the vanishing homology of a smooth hyperplane section is nonzero, the rational tube map from monodromy-fixed vanishing classes surjects onto the primitive middle cohomology of X.
falsifier: a smooth projective embedded X with nonzero rational vanishing homology and a primitive rational middle class outside the image of Schnell's tube map
---

# B011 - Global tube surjectivity

Let \(X\subset\mathbf P^N\) be smooth projective of dimension \(d\). Let
\(P^{\mathrm{sm}}\) parameterize its smooth hyperplane sections, choose
\(S_0=X\cap H_0\), and put

\[
 G=\pi_1(P^{\mathrm{sm}},H_0),\qquad
 V=H_{d-1}^{\mathrm{van}}(S_0,\mathbf Q).
\]

For \(g\in G\) and \(\alpha\in V\) with \(g\alpha=\alpha\), transport
\(\alpha\) around a loop representing \(g\). Its trace is a \(d\)-cycle on
\(X\), well-defined modulo the homology coming from \(S_0\). Poincare
duality identifies that quotient with \(H^d_{\mathrm{prim}}(X,\mathbf Q)\).
Schnell Theorem 1 proves that, if \(V\ne0\), the tube map

\[
 \{(g,\alpha):g\in G,\ \alpha\in V,\ g\alpha=\alpha\}
 \longrightarrow H^d_{\mathrm{prim}}(X,\mathbf Q)
\]

is surjective.

Equivalently, its dual is the injective map

\[
 H^d_{\mathrm{prim}}(X,\mathbf Q)
 \longrightarrow
 \prod_{g\in G} V/(g-1)V.
\]

Therefore every nonzero primitive rational Hodge class is detected by some
global monodromy tube. In the even-dimensional application, passing to a
sufficiently high power ensures nontrivial vanishing cycles by BFNP
Proposition 5.11.

## What the theorem does not supply

A tube is a topological cycle swept over a loop entirely inside the smooth
hyperplane locus. It is not an algebraic cycle, is not supported on a single
singular hyperplane, and is not automatically a Saito relation class
\(\gamma_\beta\). The theorem detects all primitive cohomology, not only its
Hodge subspace, so surjectivity itself contains no algebraicity assertion.
