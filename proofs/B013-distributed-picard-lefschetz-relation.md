---
brick_id: B013
status: PROVED
base_field: C
variety: the smooth hyperplane-section family of a smooth projective variety, restricted to a based loop whose monodromy factors into Picard-Lefschetz transformations
smoothness: all fibers along the loop are smooth; the meridians encircle ordinary critical values outside the loop
projectivity: the ambient variety is projective with a fixed projective embedding
dimension: arbitrary ambient dimension d; the active application has d = 2n
codimension: middle codimension n in the even-dimensional Hodge application
coefficient_field: Q
cohomology_theory: singular homology, intersection pairing, vanishing cycles, and Picard-Lefschetz monodromy
hodge_type: unrestricted topological relation; no type-(0,0) conclusion follows
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n)) in the application; the relation itself is not an algebraic cycle class
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: Picard-Lefschetz formula as used in Schnell Section 3 (S023); elementary telescoping
claim: A class fixed by a product of Picard-Lefschetz transformations yields an explicit distributed rational relation among the transported vanishing cycles, with coefficients given by successive intersection pairings.
falsifier: a Picard-Lefschetz factorization and fixed class for which the displayed telescoping relation is nonzero
---

# B013 - Distributed Picard-Lefschetz relation

Let \(V\) be the rational vanishing homology of a based smooth hyperplane
section. Suppose a loop has monodromy

\[
 g=T_r\cdots T_1,
\]

where, after transporting every vanishing cycle to the base fiber, the
Picard-Lefschetz formula has the form

\[
 T_i(v)=v+\varepsilon_i\langle v,\delta_i\rangle\delta_i,
 \qquad \varepsilon_i\in\{1,-1\}.
\]

For \(\alpha_0=\alpha\) and
\(\alpha_i=T_i\alpha_{i-1}\), assume \(g\alpha=\alpha\). Then

\[
 0=\alpha_r-\alpha_0
   =\sum_{i=1}^r
     \varepsilon_i\langle\alpha_{i-1},\delta_i\rangle\delta_i.
\]

This is an exact rational relation in the common based fiber. It is the
algebraic content of the cancellation visible after filling a loop and
recording its separate meridians.

## Why this does not close G007

The relation can be trivial coefficient-by-coefficient. Even when it is
nontrivial, its \(\delta_i\) arise from distinct critical values of a global
factorization. Saito's \(R(Y_0)_1^{(0,0)}\) is instead a local kernel for the
simultaneous vanishing data of one singular fiber. The formula supplies
neither a collision of those critical values into one algebraic hyperplane
section nor preservation of the tube class under such a collision. It also
has no Hodge-type conclusion. Thus B013 is a proved distributed relation,
not the local relation required by B010.
