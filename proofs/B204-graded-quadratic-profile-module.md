---
brick_id: B204
status: PROVED
base_field: C
variety: a smooth projective complex variety with very ample H and a nonempty finite reduced point scheme Z
smoothness: X and Z are smooth; the quadratic conormal layer is locally free on Z, but no hypersurface or incidence smoothness follows
projectivity: X, powers H^k, ideal powers I_Z^2 and I_Z^3, and their finite profile spaces are projective coherent data
dimension: dim X=d; each quadratic-profile fiber has dimension d(d+1)/2; the graded profile spaces W_k have nondecreasing dimensions
codimension: the decomposable degree-m profiles are exactly the products of lower profile spaces with value-evaluation spaces
coefficient_field: C for sections, values, quadratic profiles, and graded multiplication; Q remains required separately for the detector
cohomology_theory: coherent second-order conormal jets, graded section multiplication, and finite-dimensional quotient modules
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B194-B203 and G125-G133
claim: Define W_k as the image of H0(I_Z^2 H^k) in H0((I_Z^2/I_Z^3)H^k), and E_a as the value image of H0(H^a) on Z. Multiplication gives E_a W_k inside W_(a+k), and multiplication by a value section nowhere zero on Z injects W_k into W_(a+k). Under lower extinction through degree m-1, rho(P_m)=sum_(a=1)^m E_a W_(m-a), so ker(partial_Z)/rho(P_m) is exactly the degree-m indecomposable quotient of the graded quadratic-profile module.
falsifier: a product profile depending on more than the value of its multiplier, a nowhere-zero multiplier killing a nonzero profile, a decomposable profile outside the displayed sum, or an element of the displayed sum not represented by P_m
---

# B204 — Quadratic profiles form a graded value module

Let \(I=I_Z\). For every \(k\ge0\), define

\[
 W_k=
 \operatorname{im}\!\left(
 H^0(X,I^2H^k)\longrightarrow
 H^0(X,(I^2/I^3)H^k)
 \right). \tag{1}
\]

By B202,

\[
 W_k=\ker\!\left[
 H^0((I^2/I^3)H^k)\longrightarrow H^1(I^3H^k)
 \right]. \tag{2}
\]

Let

\[
 E_a=\operatorname{im}\!\left(
 H^0(X,H^a)\longrightarrow H^0(Z,H^a|_Z)
 \right). \tag{3}
\]

## Profile multiplication

Take \(r\in H^0(H^a)\) and \(s\in H^0(I^2H^k)\). Since \(s\) and its
first derivative vanish on \(Z\), the quadratic profile satisfies

\[
 \rho(rs)=r|_Z\,\rho(s). \tag{4}
\]

Changing \(r\) by a section vanishing on \(Z\) changes \(rs\) by an
element of \(I^3H^{a+k}\). Changing \(s\) by a triple-vanishing section
does the same. Hence (4) defines a bilinear multiplication

\[
 E_a\otimes W_k\longrightarrow W_{a+k}. \tag{5}
\]

If \(r|_Z\) is nowhere zero, coordinatewise multiplication by \(r|_Z\) is
an automorphism of the full quadratic-profile fibers. Its restriction
gives an injection

\[
 W_k\hookrightarrow W_{a+k}. \tag{6}
\]

Thus \(\dim W_k\) is nondecreasing with \(k\).

## Exact decomposable profile space

Fix \(m\) and assume B194's lower extinction:

\[
 H^0(I_ZH^j)=H^0(I_Z^2H^j)\qquad(0\le j<m). \tag{7}
\]

Recall

\[
 P_m=(R_+J)_m
 =\sum_{a=1}^m
 H^0(H^a)H^0(I_ZH^{m-a}). \tag{8}
\]

Using (7) in every summand and then (4) gives

\[
 \rho(P_m)=
 \sum_{a=1}^m E_aW_{m-a}. \tag{9}
\]

Both inclusions are exact: every product in (8) has a profile in the
right side, and every product of a represented value and represented
profile comes from the corresponding product section in (8).

Since \(W_m=\ker\partial_Z\), B203's quadratic quotient is

\[
 \frac{\ker\partial_Z}{\rho(P_m)}
 =
 \frac{W_m}{\sum_{a=1}^mE_aW_{m-a}}. \tag{10}
\]

This is the degree-\(m\) minimal-generator space of the graded
quadratic-profile module under value multiplication. B204 constructs no
primitive generator, ODP lift, detector, higher Kuranishi vanishing, or
cycle.
