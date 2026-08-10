---
brick_id: B018
status: PROVED
base_field: C
variety: a polarized smooth projective X of dimension 2n and codimension-n complete intersections cut by powers of the polarization
smoothness: X is smooth; the complete intersection is assumed proper and regular when represented as a subvariety, though the cohomological statement only uses divisor classes
projectivity: X is projective and L is ample
dimension: dim X = 2n with n at least 1
codimension: middle codimension n
coefficient_field: Q
cohomology_theory: singular Betti cohomology, cup product, Lefschetz decomposition, and Poincare pairing
hodge_type: primitive rational type (n,n) input before Tate twist; tautological complete-intersection class has type (n,n)
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: definition of primitive middle cohomology, divisor cycle classes, and multiplicativity of the Betti cycle-class map
claim: Every codimension-n complete intersection of divisors numerically proportional in cohomology to the polarization has zero pairing with every primitive middle cohomology class; equivalently its primitive middle projection is zero.
falsifier: a primitive zeta with L cup zeta equal to zero and a complete-intersection class proportional to L^n whose Poincare pairing with zeta is nonzero
---

# B018 - Tautological primitive orthogonality

Let \(X/\mathbf C\) be smooth projective of dimension \(2n\), \(n\ge1\), and
write \(\ell=c_1(L)\). Let \(W\) be a proper codimension-\(n\) complete
intersection of divisors \(D_i\) satisfying

\[
 [D_i]=a_i\ell\in H^2(X,\mathbf Q(1)).
\]

Multiplicativity of the cycle-class map gives

\[
 [W]=\left(\prod_{i=1}^n a_i\right)\ell^n
 \in H^{2n}(X,\mathbf Q(n)).
\]

For every primitive middle class
\(\zeta\in H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))\), one has
\(\ell\cup\zeta=0\). Hence

\[
 \langle\zeta,[W]\rangle
 =
 \left(\prod_i a_i\right)
 \int_X\zeta\cup\ell^n
 =
 \left(\prod_i a_i\right)
 \int_X(\ell\cup\zeta)\cup\ell^{n-1}
 =0.
\]

The Lefschetz decomposition is orthogonal for the polarization form.
Therefore the primitive middle projection of \([W]\), which lies entirely in
the tautological summand \(\ell^nH^0(X,\mathbf Q)\), is zero.

## Consequence for detector constructions

Any incidence construction whose proposed ambient detector class is only the
primitive projection of such a complete-intersection class produces the zero
detector. Raising degrees changes the scalar \(\prod_i a_i\), not this
orthogonality. A successful class-blind construction for G009 must introduce
non-tautological ambient homology through the degeneration itself; merely
forcing a hypersurface through polarization complete intersections cannot
detect a primitive \(\zeta\).

## Scope guard

This does not say that all complete intersections inside a larger auxiliary
space are useless, nor that a singular hyperplane containing \(W\) has no
other vanishing-cycle detector classes. It excludes only the route that
identifies the desired ambient detector with the tautological class of \(W\)
or its primitive projection.
