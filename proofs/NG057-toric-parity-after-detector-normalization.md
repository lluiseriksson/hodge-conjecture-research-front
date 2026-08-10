---
brick_id: NG057
status: NO-GO
base_field: C
variety: the B058 plane-net hyperplane family and B071 semistable pushdown
smoothness: smooth generic fibers and regular semistable source stack
projectivity: projective family and pushdown
dimension: ambient 2n, fiber 2n-1, base 2, total space 2n+1
codimension: base supports of codimension 1 or 2; terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: perverse mixed Hodge modules, strict-support decomposition, and toric support parity
hodge_type: detector target is rational type (0,0) after Q(n); parity does not determine the projection
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B078-B080, G043-G044
claim: After converting the degree-one relation channel into the normalized direct-image grading, B078 parity excludes every proper support that could contain the detector.
falsifier: B080's allowed divisor shift b=0 or point shift b=-1
---

# NG057 — Exact normalization leaves every relevant support parity-allowed

**Status:** NO-GO

The phrase “ordinary degree one” refers to the unshifted middle-coefficient
intersection complex, not to the raw constant-sheaf direct image. B080 performs
the conversion. In (Rh_*\mathbf Q[2n+1]), the detector lies in degree
(-1), or raw degree (2n).

For a codimension-(c) support, the unique generic shift that can meet this
degree is (b=1-c). Hence divisor support uses (b=0), point support uses
(b=-1), and in both cases

\[
 b+\dim\mathcal X-\dim V=2n
\]

is even. These terms are permitted by B078.

Parity therefore supplies no support exclusion in the detector degree. The
only valid re-entry is to compute the actual multiplicities and the B058
class projections for these two shifts, as isolated in G045.
