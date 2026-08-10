---
brick_id: B066
status: PROVED
base_field: C
variety: the raw pullback of the suspended A2 family to the two third-blowup charts of B065
smoothness: the resolved base is smooth with SNC discriminant, but the raw pulled-back total hypersurface is singular along the E3 section and, in the other chart, the E2 section
projectivity: no; this is a local algebraic chart
dimension: the base has dimension two; the pulled-back total hypersurface has dimension r+2 for r quadratic suspension variables
codimension: each singular section has codimension r+1 in the total hypersurface and lies over a boundary divisor
coefficient_field: C for the Jacobian calculation; later mixed-Hodge applications use Q
cohomology_theory: none in the proof; the consequence concerns which mixed Hodge module must be used after resolution
hodge_type: none asserted
cycle_class_map: none
cycle_equivalence: none
scope: relative and fiberwise
dependencies: B064-B065 and verification/verify_B066_pulledback_total_space.py
claim: Resolving the A2 cusp in the parameter base does not resolve the total family; its raw pullback is singular exactly over the E3 and E2 boundary sections, while it is smooth over the generic E1 section.
falsifier: a nonzero Jacobian derivative on an E3 or E2 section, singularity over generic E1, or an additional singular point off those sections
---

# B066 — The resolved base leaves a singular pulled-back total family

**Status:** PROVED  
**Gate:** G035 / G036

## Mathematical type record

- **Base field:** \(\mathbf C\).
- **Variety/class:** the B064 suspended \(A_2\) hypersurface after raw base change to B065's two final blowup charts.
- **Smoothness/projectivity:** the base is smooth and its reduced cusp transform is SNC, but the pulled-back total hypersurface is singular; no projective compactification is asserted.
- **Dimension:** base dimension two; total dimension \(r+2\).
- **Codimension:** the singular loci are sections over boundary divisors.
- **Coefficient field/cohomology/Hodge type/cycle map:** the calculation is algebraic over \(\mathbf C\) and makes no cohomological or cycle-class assertion.
- **Equivalence relation:** none.
- **Scope:** relative and fiberwise.

## The \(b=ac\) chart

B065 gives
\[
s=a^2c,\qquad t=a^3c^2.
\]
The raw pulled-back family is
\[
F_a=x^3+a^2cx+a^3c^2+\sum_{i=1}^{r}z_i^2=0.
\]
Its relevant derivatives are
\[
\partial_xF_a=3x^2+a^2c,
\quad
\partial_aF_a=ac(2x+3ac),
\quad
\partial_cF_a=a^2(x+2ac),
\quad
\partial_{z_i}F_a=2z_i.
\]
They vanish exactly on
\[
\{x=z=0,a=0\}\ \cup\ \{x=z=0,c=0\}.
\]
Indeed, if \(ac\ne0\), the last two displayed equations force simultaneously
\(x=-2ac\) and \(x=-3ac/2\), a contradiction.

## The \(a=bd\) chart

Here
\[
s=b^2d,\qquad t=b^3d,
\]
and
\[
F_b=x^3+b^2dx+b^3d+\sum z_i^2=0.
\]
The calculation now gives singular locus
\[
\{x=z=0,b=0\}.
\]
Indeed, if \(b\ne0\), \(\partial_dF_b=0\) forces \(x=-b\).
Then \(\partial_bF_b=0\) forces \(d=0\), but
\(\partial_xF_b=3b^2\ne0\). In particular the generic \(d=0\) section,
which belongs to the \(E_1\) direction, is smooth in the total space. The
second singular section visible as \(c=0\) in the first chart is the
\(E_2\) direction at \(d=\infty\).

## Consequence

An SNC discriminant on the modified base is not a semistable total family.
The remaining total-space singularities lie over \(E_3\cup E_2\), even
though the generic \(E_1\) section is smooth. The coefficient object in G035
cannot be called the constant Hodge module on a smooth pullback: one must
specify an intersection complex, a resolution pushforward, or a semistable
alteration and then prove comparison and descent. This is G036.
