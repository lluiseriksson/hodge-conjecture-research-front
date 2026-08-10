---
brick_id: B065
status: PROVED
base_field: C
variety: the plane cusp discriminant C given by 4s^3+27t^2=0 and its three-step embedded resolution
smoothness: the base plane is smooth; after three point blowups the reduced total transform is a simple normal crossing divisor
projectivity: the local blowups are proper; no global projective compactification is asserted
dimension: the parameter base is a smooth complex surface
codimension: the cusp, its strict transform, and all exceptional components are divisors
coefficient_field: Z for divisor multiplicities and Q or C for later cohomological applications
cohomology_theory: none; this is an embedded-resolution and divisor-incidence calculation
hodge_type: none asserted
cycle_class_map: none
cycle_equivalence: divisor equality under pullback, not an equivalence relation on terminal cycles
scope: relative
dependencies: B064 and verification/verify_B065_a2_cusp_resolution.py
claim: Three successive point blowups give an SNC total transform with multiplicities 2, 3, and 6 on the exceptional divisors and a trivalent final exceptional component.
falsifier: a residual tangency or triple intersection after the third blowup, or different pullback multiplicities in the displayed charts
---

# B065 — Explicit log resolution of the \(A_2\) cusp

**Status:** PROVED  
**Gate:** G034 / G035

## Mathematical type record

- **Base field:** \(\mathbf C\).
- **Variety/class:** the divisor \(C=V(4s^3+27t^2)\) in the smooth parameter surface \(\mathbf C^2\).
- **Smoothness/projectivity:** the base and all blowup surfaces are smooth; the local blowups are proper but no global projective model is asserted.
- **Dimension:** two.
- **Codimension:** every curve component is a divisor.
- **Coefficient field:** integral divisor multiplicities.
- **Cohomology theory/Hodge type/cycle map:** none used.
- **Equivalence relation:** equality of pulled-back Cartier divisors.
- **Scope:** relative local resolution.

## First blowup

Use the chart
\[
s=u,\qquad t=uv.
\]
Then
\[
4s^3+27t^2=u^2(4u+27v^2).
\]
The first exceptional divisor \(E_1=V(u)\) has multiplicity two. The strict transform \(C_1=V(4u+27v^2)\) is smooth but tangent to \(E_1\) at the origin.

## Second blowup

In the chart adapted to that tangent direction, put
\[
u=ab,\qquad v=b.
\]
The full pullback becomes
\[
a^2b^3(4a+27b).
\]
Here the strict transform of \(E_1\) is \(V(a)\) with multiplicity two, the new exceptional divisor \(E_2=V(b)\) has multiplicity three, and the cusp strict transform is \(V(4a+27b)\) with multiplicity one. All three are smooth with distinct tangent lines, but they meet at one point; a triple point is not an SNC divisor on a surface.

## Third blowup

Blow up the triple point. In the two standard charts:
\[
b=ac:quad a^6c^3(4+27c),
\]
\[
a=bd:quad b^6d^2(4d+27).
\]
Thus the new exceptional divisor \(E_3\) has multiplicity six. The strict transforms of \(E_2\), \(C\), and \(E_1\) meet \(E_3\) at the three distinct tangent directions
\[
c=0,\qquad c=-4/27,\qquad c=\infty,
\]
respectively. They no longer meet one another. The reduced total transform is therefore SNC.

The exceptional self-intersections are
\[
E_1^2=-3,\qquad E_2^2=-2,\qquad E_3^2=-1,
\]
and the reduced dual graph is a trivalent star centered at \(E_3\), with arms \(E_1,E_2\), and the cusp strict transform.

## Consequence and boundary

G034 now has an explicit SNC target and exact multiplicities \((2,3,6)\). This does not verify a \(V\)-multifiltration, strict \(R\)-multispecialisability, or descent of any nearby-cycle comparison. The multiplicity-six exceptional monodromy and the three distinct attachment points must be retained; replacing the resolution by an unlabeled normal-crossing cartoon loses data.

