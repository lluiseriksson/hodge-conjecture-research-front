---
brick_id: B012
status: PROVED
base_field: C
variety: a smooth irreducible projective variety X of dimension 2n with its universal high-power hyperplane family over the dual projective space
smoothness: X is smooth; the universal hyperplane family is smooth only over the complement of the dual discriminant and may be singular over a point p
projectivity: X is projective and embedded by a sufficiently high power mL when the local detection statements are used
dimension: dim X = 2n; hyperplane fibers have dimension 2n-1; the parameter space has dimension d
codimension: middle codimension n on X; the local singular-support locus has parameter-space codimension at least 2
coefficient_field: Q
cohomology_theory: singular Betti cohomology, intersection cohomology, the decomposition theorem, perverse sheaves, and mixed Hodge structures
hodge_type: primitive degree-2n input; the global and local Green-Griffiths components inherit Hodge structures, with the application restricted to type (n,n)
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n)); no algebraic cycle is constructed by the invariant
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: de Cataldo-Migliorini Definition 3.3, Remark 3.4, Propositions 3.6 and 3.8, Corollaries 3.10 and 3.12 (S024)
claim: A primitive rational class is detected by its global Green-Griffiths invariant, while after a sufficiently high embedding its local invariant at p is nonzero exactly when its restriction to the singular hyperplane fiber at p is nonzero; the possible local support has codimension at least two.
falsifier: a primitive rational class satisfying the cited hypotheses whose global invariant vanishes although the class is nonzero, whose high-power local invariant disagrees with fiber restriction, or whose local support has codimension below two
---

# B012 - Global/local Green-Griffiths separation

Let \(X/\mathbf C\) be smooth irreducible projective of dimension \(2n\),
embedded in \(\mathbf P^d\). Let

\[
 q:\mathcal X\to X,\qquad \pi:\mathcal X\to \mathbf P^d
\]

be the universal hyperplane incidence family, and let
\(\zeta\in H^{2n}_{\mathrm{prim}}(X,\mathbf Q)\). In the
decomposition-theorem splitting of \(R\pi_*\mathbf Q_{\mathcal X}\), de
Cataldo and Migliorini define

\[
 s(\zeta)=[q^*\zeta]_{00}
 \in IH^1(\mathbf P^d,IC(R^{2n-1}))
\]

and, for \(p\in\mathbf P^d\),

\[
 s(\zeta)_p=[\zeta|_{X_p}]_{00}
 \in \mathcal H^{-d+1}(IC(R^{2n-1}))_p.
\]

Proposition 3.8 proves two distinct statements:

1. for every embedding, \(s(\zeta)=0\) if and only if \(\zeta=0\);
2. after replacing the embedding by \(|mL|\) with \(m\gg0\),
   \(s(\zeta)_p=0\) if and only if the canonical local restriction component
   vanishes.

For a primitive Hodge class, Corollary 3.10 identifies the second condition
with

\[
 \zeta|_{X_p}=0\quad\text{in }IH^{2n}(X_p,\mathbf Q).
\]

For a contractible neighborhood \(U\) of \(p\), Corollary 3.12 equivalently
tests whether \(q^*\zeta\) vanishes on the smooth part of the restricted
family over \(U\setminus D\). Remark 3.4 gives the support constraint

\[
 \operatorname{Sing}(\zeta)=\{p:s(\zeta)_p\ne0\},\qquad
 \operatorname{codim}_{\mathbf P^d}\operatorname{Sing}(\zeta)\ge2.
\]

## Consequence for the active route

Global nonvanishing is automatic for every nonzero primitive class; local
nonvanishing is not. A generic complex curve in a high-dimensional parameter
space avoids a fixed codimension-at-least-two support. A specially chosen
curve can pass through a known support point, but choosing such a point is
already the unresolved detection problem. A generic two-dimensional slice
can meet a nonempty codimension-two component, yet it cannot prove that the
support is nonempty.

Thus a global tube or global Green-Griffiths class cannot be localized merely
by restricting to a generic pencil. The missing theorem must force nonempty
local support for the specified Hodge class; after universal quantification,
B007 shows that this is terminal-equivalent to the rational Hodge
Conjecture.

## Scope guard

This brick proves detection identities and a support bound. It does not prove
that \(\operatorname{Sing}(\zeta)\) is nonempty for a nonzero primitive Hodge
class, does not construct an algebraic cycle, and does not weaken the terminal
open content.
