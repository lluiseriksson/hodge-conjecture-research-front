---
brick_id: G004
status: EXPLORATORY
base_field: C
variety: arbitrary smooth projective fiber carrying an algebraic rational Hodge anchor class
smoothness: ambient variety smooth; desired representatives lci or smooth
projectivity: ambient variety projective
dimension: arbitrary n, with middle case n=2q the terminal reduction target
codimension: arbitrary q, especially middle codimension
coefficient_field: Q for the anchor class and cycle; C for semiregularity maps
cohomology_theory: Betti Hodge structure plus coherent/de Rham obstruction theory
hodge_type: (q,q)
cycle_class_map: CH^q(X)_Q -> H^{2q}(X,Q(q))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B004; existence of an algebraic anchor from G001
claim: Every algebraic rational Hodge anchor admits a finite lci cycle presentation whose combined semiregularity map is injective.
falsifier: an algebraic rational Hodge class for which every finite lci presentation has a nonzero kernel in its combined semiregularity map
---

# G004 - Universal semiregular-presentation gate

## Falsifiable theorem sought

For every smooth projective \(X/\mathbf C\), codimension \(q\), and algebraic
class \(\alpha\in\operatorname{Hdg}^q(X)_{\mathbf Q}\), find an integer
\(N>0\), lci codimension-\(q\) subschemes \(Z_i\), and integers \(a_i\) such
that \(N\alpha=\sum_i a_i[Z_i]\) and the combined map

\[
 \bigoplus_i H^1(N_{Z_i/X})\xrightarrow{\sum a_i\sigma_i}
 H^{q+1}(X,\Omega_X^{q-1})
\]

is injective.

B004 proves that this exact condition propagates an algebraic anchor along any
connected Hodge-locus base. The gate is not known. Standard moving lemmas,
resolution of singularities, and rational \(K\)-theory/Chern-character
surjectivity can change presentations, but none automatically gives lci
representatives with the required obstruction-map injectivity.

## Narrowest next test

Determine closure and stabilization laws for combined semiregularity under:

1. adding a rationally trivial pair of cycles;
2. replacing a component by a smooth alteration plus pushforward;
3. adding sufficiently positive complete intersections with cancelling
   coefficients; and
4. the product-with-projective-space construction in B001.

Any stabilization theorem must prove injectivity, not merely increase the
dimension of the target obstruction group.

