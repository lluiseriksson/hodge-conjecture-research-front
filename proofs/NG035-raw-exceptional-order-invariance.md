---
brick_id: NG035
status: NO-GO
base_field: C
variety: a smooth threefold with a point F contained in a smooth codimension-two center G, resolved by blowing up G before the dominant transform of F
smoothness: the ambient threefold, both centers, and both blow-ups are smooth
projectivity: both blow-up morphisms are projective; the argument is local and does not require the ambient threefold to be projective
dimension: ambient dimension 3, with centers of dimensions 1 and 0 before transformation
codimension: G has codimension 2 and F has codimension 3; downstream cycles would have middle codimension n
coefficient_field: Q
cohomology_theory: rational divisor classes in Betti cohomology and Picard groups
hodge_type: all divisor classes have type (1,1)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no downstream cycle is constructed
cycle_equivalence: rational equivalence
scope: relative
dependencies: G021 and Li Definition 2.7, Lemma 2.9, and Theorem 1.3 (S038)
claim: One cannot prove G021 for an arbitrary permissible order by asserting that every later dominant center avoids containment in every earlier exceptional divisor.
falsifier: the dominant transform of F after blowing up G is not contained in the exceptional divisor over G
---

# NG035 - Raw exceptional classes are not order invariant

Let \(F\subset G\subset Y\), where \(Y\) is a smooth threefold, \(G\) is a
smooth curve, and \(F\) is a point. The chain \(\{G,F\}\) admits the
permissible order \(G,F\) in Li's sense: each prefix is a building set for
its induced arrangement.

Blow up \(G\). By Li's definition of dominant transform,

\[
 \widetilde F=\pi^{-1}(F)simeq
 \mathbf P(N_{G/Y}|_F)\simeq\mathbf P^1.
\]

It is contained in the exceptional divisor \(E_G\). Blowing up
\(\widetilde F\) therefore changes the strict transform of the earlier
exceptional divisor:

\[
 [D_G]=[E_G^{\mathrm{pull}}]-[E_F].
\]

Thus the raw exceptional class created at the first step is not the final
intrinsically labelled boundary class. The “later centers never lie in
earlier exceptionals” induction proposed in G021 is false.

This does not refute G021's final divisor formula. The repair is to prove the
formula in an inclusion-compatible order, where earlier boundary divisors
are not subsequently blown up along contained centers, and then transport
the intrinsically labelled divisors \(D_F\) through Li's canonical wonderful
compactification. Raw stepwise exceptional coordinates from another order
must be changed by a triangular integral basis transformation.
