---
brick_id: B075
status: PROVED
base_field: C
variety: the smooth-locus pullback of the plane-net hyperplane family along a finite degree-d cover, with the B058 detector loop and tube
smoothness: all fibers along the detector loop and its lifts are smooth
projectivity: the ambient hyperplane family is projective; the finite cover is projective
dimension: arbitrary ambient dimension 2n; tube classes have real dimension 2n
codimension: middle codimension n
coefficient_field: Q
cohomology_theory: singular homology, finite-cover transfer, monodromy tubes, pushforward, and Poincare pairing
hodge_type: the original B058 ambient tube is rational type (0,0) after Q(n); transfer and trace preserve the rational Hodge morphisms
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B057-B058, B067, B072, B074
claim: Over the smooth discriminant complement, the sum of all sheet-lifts of the B058 tube is invariant under the deck group and its pushforward is d times the original tube; normalized trace therefore preserves its nonzero pairing with the prescribed Hodge class before collision.
falsifier: failure of the transfer identity p_* p^! = d on the tube or failure of the projection formula for the pairing
---

# B075 — Finite-cover transfer preserves the global tube

**Status:** PROVED

Let \(p:\widetilde U\to U\) be the degree-\(d\) finite étale restriction of
the root cover to the smooth discriminant complement. Pull the smooth
hyperplane family and the B058 detector tube \(c\) back to \(\widetilde U\).
The singular-chain transfer is the sum of the lifts over all sheets:

\[
p^!c=\sum_{a=1}^{d}\widetilde c_a.
\]

Deck transformations permute the summands, so \(p^!c\) is invariant. The
standard transfer identity gives

\[
p_*p^!c=d\,c.
\]

With rational coefficients, normalized trace sends \(p^!c\) back to \(c\).
By the projection formula, if \(\zeta\) is the B058 primitive rational Hodge
class, then

\[
\left\langle\zeta,\frac1d p_*p^!c\right\rangle
=\langle\zeta,c\rangle\ne0.
\]

Thus the finite root cover and group averaging do not destroy the selected
global detector tube before collision. This is compatible with B073: an
individual local root lies in the standard representation, while the total
sheet transfer is a global invariant chain.

## Exact boundary

The identity holds on the smooth-locus tube. It does not prove that nearby
specialization of this invariant transfer produces a nonzero local boundary
class, remains in the full-support summand, or survives the two B022 kernels.
Those are precisely G042's remaining obligations.
