---
brick_id: NG147
status: NO-GO
base_field: C
variety: a one-dimensional smooth basis-node germ with an algebraic escape generator carrying an arbitrarily late-varying unit denominator
smoothness: the base is smooth and the denominator is a unit; the escape ideal is the smooth principal ideal (y)
projectivity: irrelevant to the unit-invariance obstruction; B157 can realize the scalar critical-value germ projectively over a nonlinear base
dimension: one base variable and one escape generator; arbitrary denominator order m
codimension: the conormal defect is visible in order zero regardless of the denominator's first nonconstant order
coefficient_field: C; Q remains required only for downstream Hodge detectors
cohomology_theory: analytic units, principal ideals, Kähler differentials, and conormal modules
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B157, B179-B183, G115-G116
claim: Arbitrarily high Taylor or algebraic complexity of a unit denominator necessarily delays the first nonzero conormal jet of the corresponding escape ideal.
falsifier: epsilon_m=y/(1-y^m) has a denominator first varying in order m, but generates (y) and has conormal defect dy mod y in order zero
---

# NG147 — Unit denominators do not delay the conormal defect

For any \(m\ge1\), take

\[
 \epsilon_m(y)=\frac{y}{1-y^m}.
\]

The inverse unit \((1-y^m)^{-1}\) first differs from \(1\) in order
\(m\). Nevertheless

\[
 (\epsilon_m)=(y), \tag{1}
\]

and B183 gives

\[
 \beta_{(\epsilon_m)}([\epsilon_m])
 =\text{unit}\cdot dy\pmod y. \tag{2}
\]

The conormal defect is therefore nonzero already in order zero,
independently of \(m\).

## Corrected obstruction

NG146 remains valid as a statement about the complete algebraic or Taylor
complexity of labelled idempotents. It is not, by itself, a lower bound on
the jet order needed to detect escape. For that purpose unit denominators
may be cleared.

## Re-entry condition

G116 must certify which denominators are units, clear them, and bound the
resulting numerator functions through the full labelled incidence. The
numerator conormal jets and every Hodge detector clause remain unproved.
