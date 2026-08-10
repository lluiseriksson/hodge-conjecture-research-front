---
brick_id: B003
status: PROVED
base_field: C
variety: smooth projective X with a local complete intersection subscheme Z
smoothness: X smooth; Z lci (smooth in the simplest cited formulation)
projectivity: X projective
dimension: dim(X)=n arbitrary
codimension: codim(Z,X)=q arbitrary
coefficient_field: Q for the Hodge class; C for deformation and coherent cohomology
cohomology_theory: Betti Hodge structure plus coherent/de Rham cohomology controlling first-order deformation
hodge_type: cycle class [Z] of type (q,q)
cycle_class_map: CH^q(X)_Q -> H^{2q}(X,Q(q))
cycle_equivalence: rational equivalence
scope: relative
dependencies: Bloch semiregularity theorem 7.1; semiregularity map H^1(N_Z/X)->H^{q+1}(X,Omega_X^{q-1}) (S008, S016-S018)
claim: For a semiregular lci anchor, a first-order deformation of X preserves the Hodge type of [Z] if and only if Z lifts to that first-order deformation.
falsifier: a first-order Hodge-preserving deformation with nonzero embedded obstruction despite injectivity of the semiregularity map, or a lifted cycle whose flat class ceases to be Hodge
---

# B003 - Semiregular infinitesimal bridge

## Statement

Let \(X/\mathbf C\) be smooth projective and \(Z\subset X\) an lci subscheme
of codimension \(q\). Bloch's semiregularity map is

\[
 \sigma_Z:H^1(Z,N_{Z/X})\longrightarrow
 H^{q+1}(X,\Omega_X^{q-1}).
\]

Call \(Z\) semiregular when \(\sigma_Z\) is injective. For a first-order
deformation direction of \(X\), the class \([Z]\) remains infinitesimally of
type \((q,q)\) if and only if \(Z\) lifts as an lci subscheme to that
first-order deformation.

## Proof brick

The embedded lifting problem has an obstruction
\(o(Z,\xi)\in H^1(Z,N_{Z/X})\). Bloch's compatibility theorem identifies
\(\sigma_Z(o(Z,\xi))\) with the infinitesimal Hodge-theoretic obstruction for
the flat class \([Z]\) to remain of type \((q,q)\). If the class remains Hodge,
that image is zero; injectivity of \(\sigma_Z\) gives \(o(Z,\xi)=0\), hence the
first-order embedded lift exists. Conversely, a relative algebraic cycle has a
flat Betti class of Hodge type on the deformed fiber. This is the implication
reported as Bloch [1972, Theorem 7.1] in Dan-Kaur, pp. 1-2 and Remark 3.5.

## Scope audit

- This is first-order/infinitesimal and begins with an existing lci cycle.
- This brick alone is first-order. Ran's all-Artin extension plus proper
  Hilbert globalization is recorded separately in B004.
- It does not supply a semiregular representative for an arbitrary algebraic
  class, much less an algebraic anchor for an arbitrary Hodge class.
- Dan-Kaur's Theorem 1.1 constructs special semiregular embeddings inside
  high-degree hypersurfaces; that is a special-family mechanism, not a
  reduction of arbitrary \((X,\alpha)\).
