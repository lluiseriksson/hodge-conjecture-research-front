---
brick_id: B005
status: PROVED
base_field: C
variety: fixed smooth projective X with finite lci codimension-q cycle presentations
smoothness: X smooth; all presentation components lci
projectivity: X projective
dimension: arbitrary n
codimension: fixed q
coefficient_field: Q for cycle presentations; C for semiregularity vector spaces
cohomology_theory: coherent/de Rham semiregularity target H^{q+1}(X,Omega_X^{q-1})
hodge_type: (q,q) cycle classes
cycle_class_map: CH^q(X)_Q -> H^{2q}(X,Q(q))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: definition of the combined semiregularity map in B004
claim: Appending any extra cycle components to a noninjective combined semiregularity presentation cannot make the enlarged combined map injective.
falsifier: an enlarged combined map that is injective while its restriction to the original direct summand has a nonzero kernel
---

# B005 - Direct-sum augmentation cannot repair semiregularity

## Statement and proof

Let a finite lci presentation have combined map

\[
 \Sigma:V:=\bigoplus_{i=1}^r H^1(N_{Z_i/X})\longrightarrow
 W:=H^{q+1}(X,\Omega_X^{q-1}).
\]

Append any further lci cycles \(Y_1,\ldots,Y_s\), with arbitrary rational or
integral coefficients, obtaining

\[
 \Sigma':V\oplus U\longrightarrow W,
 \qquad \Sigma'(v,u)=\Sigma(v)+\Tau(u).
\]

If \(0\ne v\in\ker\Sigma\), then \((v,0)\ne0\) and
\(\Sigma'(v,0)=0\). Hence \(\ker\Sigma\oplus\{0\}\subseteq\ker\Sigma'\).
Therefore \(\Sigma'\) cannot be injective. QED.

## Consequences for G004

- Adding rationally trivial pairs does not remove an existing kernel.
- Appending sufficiently positive complete intersections, even with
  coefficients chosen to preserve the Chow class, does not remove it.
- Increasing the amount of geometric data is irrelevant when the old direct
  summand remains: the old kernel survives by restriction.
- A viable G004 construction must **replace** the presentation or alter the
  obstruction theory, not merely stabilize it by extra independent Hilbert
  factors.

This is a no-go for one proposed construction method, not evidence against the
existence of some different injective presentation.

