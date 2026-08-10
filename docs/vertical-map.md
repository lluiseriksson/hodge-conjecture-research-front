# Vertical proof map

Date: 2026-08-10. Overall status: **EXPLORATORY**.

## Dependency graph

```text
HC  Standard rational Hodge Conjecture
 ^
 | B001 (PROVED equivalence via X x projective space)
 |
MHC Universal middle-degree Hodge Conjecture
 ^
 | G001 + G004 + B004 (CONDITIONAL sufficient route)
 |
AA   every middle class reaches an algebraic anchor in its Hodge locus
 +
SP   every anchor has an injectively combined semiregular lci presentation
 ^
 | B004 (PROVED all-order propagation from such a presentation)
 |
Ran all-order obstruction-kernel theorem + B002 proper Hilbert dominance
```

## Terminal sufficient theorem

**MHC.** For every smooth projective \(Y/\mathbf C\) of even dimension \(2m\),
every rational class in \(H^{2m}(Y,\mathbf Q)\cap H^{m,m}(Y)\) is the Betti
class of a cycle in \(CH^m(Y)_{\mathbf Q}\).

B001 proves `MHC <=> HC`. This is a genuine scope reduction, not a special
family: arbitrary \((X,p,\alpha)\) is functorially embedded into the middle
degree of \(X\times\mathbf P^r\), and algebraic pullback/pushforward returns a
cycle on \(X\).

## Current narrow gate

**G002 (cycle-space dominance).** Let \(f:\mathcal Y\to T\) be a smooth
projective family of relative dimension \(2m\), and let \(\alpha\) be a flat
rational section of \(R^{2m}f_*\mathbf Q\) of type \((m,m)\) at every point of
connected \(T\). If \(\alpha_{t_0}\) is algebraic at one point, then after a
surjective proper base change \(T'\to T\), some relative rational cycle has
fiberwise Betti class \(\alpha\).

This is falsifiable: a family and anchored flat class for which every relevant
relative Chow component maps into a proper closed subset of \(T\) refutes it.
It propagates upward only together with G001, the separately logged obligation
that every arbitrary middle pair \((Y,\alpha)\) lies on such an anchored
component.

## Attempt state

1. Apply Cattani-Deligne-Kaplan to make the Hodge locus algebraic - valid.
2. Parameterize cycles on fibers by relative Chow/Hilbert schemes - valid.
3. Infer that one component dominates the Hodge locus because it contains the
   anchor - **invalid**. A point on a countable union of cycle loci gives no
   dominance, and the Hodge locus may be larger than every cycle component.

Step 3 is NG-001. B002 gives a precise replacement: smoothness of the relative
Hilbert scheme at the anchor plus tangent surjectivity forces dominance. Ran's
all-order theorem and B004 prove both conditions from an injectively combined
semiregular presentation. G004 asks whether every algebraic anchor admits such
a presentation; assuming this from moving lemmas or Chern-character
generation is NG-005. B005 further rules out repairing a bad presentation by
appending cancelling cycles (NG-006). G001, existence of an anchor on every
required Hodge locus, remains logically separate.
