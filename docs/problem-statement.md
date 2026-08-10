# Exact problem statement

Result label: **PROVED** (definition and equivalence of standard formulations;
not a proof of the conjecture).

## Fixed data

- **Base field:** \(\mathbf C\).
- **Variety:** an arbitrary smooth projective algebraic variety \(X/\mathbf C\),
  not assumed connected; components may be handled separately.
- **Dimension:** arbitrary finite complex dimension \(n\).
- **Codimension:** every integer \(0\le p\le n\).
- **Coefficient field:** \(\mathbf Q\).
- **Cohomology theory:** singular/Betti cohomology of \(X^{an}\), with its pure
  rational Hodge structure.
- **Hodge type:** \((p,p)\) in untwisted degree \(2p\), equivalently \((0,0)\)
  in \(H^{2p}(X,\mathbf Q(p))\).
- **Cycle class map:**
  \(\operatorname{cl}_{B,\mathbf Q}:CH^p(X)\otimes\mathbf Q\to
  H^{2p}(X^{an},\mathbf Q(p))\).
- **Equivalence relation on cycles:** rational equivalence in the domain
  \(CH^p\). Only the image in Betti cohomology matters; injectivity is not
  asserted.
- **Scope:** absolute, variety-by-variety; no family, genericity, or
  fiberwise hypothesis is part of the official statement.

## Standard rational Hodge Conjecture

For every \(X\) and \(p\) as above,

\[
 \operatorname{im}(\operatorname{cl}_{B,\mathbf Q})
 = \operatorname{Hdg}^p(X)_{\mathbf Q}
 :=H^{2p}(X,\mathbf Q)\cap H^{p,p}(X).
\]

The inclusion from left to right is a theorem. The conjectural content is the
reverse inclusion: given a rational Hodge class \(\alpha\), construct a finite
rational linear combination \(Z=\sum_i q_i[Z_i]\) of codimension-\(p\)
irreducible algebraic subvarieties such that
\(\operatorname{cl}_{B,\mathbf Q}(Z)=\alpha\).

This matches Deligne's official Clay statement: on a projective nonsingular
algebraic variety over \(\mathbf C\), any Hodge class is a rational linear
combination of cycle classes. The Tate-twisted and untwisted forms above are
the same assertion with different bookkeeping.

## Explicit exclusions

1. **Integral:** replacing \(\mathbf Q\) by \(\mathbf Z\) is a stronger and
   false statement in general. Integral counterexamples neither disprove nor
   settle the rational conjecture.
2. **Kahler:** replacing algebraic projectivity by compact Kahler is false.
3. **Restricted dimension/codimension/family:** valid special cases are logged
   but do not imply the universal quantifiers without a proved reduction.
4. **Numerical/algebraic equivalence:** neither is the target. The map begins
   with cycles modulo rational equivalence and asks only about their Betti
   classes.
5. **Circular cycle assumptions:** “let \(Z\) be a cycle with class
   \(\alpha\)” assumes the desired conclusion and receives no progress credit.

Primary anchor: Pierre Deligne, *The Hodge Conjecture*, official Clay problem
description, pp. 1-2. Audit record S001.

