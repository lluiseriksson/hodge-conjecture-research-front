---
brick_id: B007
status: PROVED
base_field: C
variety: arbitrary smooth projective variety, reduced in the criterion to a polarized smooth projective X of even dimension 2n
smoothness: X smooth
projectivity: X projective and L very ample
dimension: arbitrary globally; 2n in the primitive middle-dimensional criterion
codimension: arbitrary globally; n in the criterion
coefficient_field: Q; equivalently non-torsion integral lattice classes after clearing denominators
cohomology_theory: singular Betti cohomology with Tate twist, Deligne/absolute Hodge cohomology, and local intersection cohomology of the hyperplane parameter space
hodge_type: (n,n), equivalently type (0,0) in H^{2n}(X,Q(n)); primitive with respect to L
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n)) in the middle case, and CH^p(Y)_Q -> H^{2p}(Y,Q(p)) globally
cycle_equivalence: rational equivalence
scope: absolute
dependencies: BFNP Theorem 1.3, Corollary 5.15, Lemma 6.2, and Theorems 6.5-6.6 (S009)
claim: The standard rational Hodge Conjecture is equivalent to universal nonzero singular-hyperplane detection for primitive rational middle Hodge classes.
falsifier: a mismatch in smoothness, rational coefficients, primitiveness, or local singularity quantifiers between the criterion and the standard conjecture
---

# B007 - Normal-function/singular-hyperplane equivalence

## Exact rational criterion

Let \(X/\mathbf C\) be smooth projective of dimension \(2n\), let \(L\) be
very ample, and let

\[
 0\ne\zeta\in H^{2n}(X,\mathbf Q(n))\cap H^{0,0}
\]

be primitive: \(c_1(L)\smile\zeta=0\). For \(m>0\), put
\(P_m=|L^m|\), let \(\pi_m:\mathcal X_m\to P_m\) be the universal hyperplane
family, and let \(X_{m,p}\) denote its fiber at \(p\in P_m\).

The following universal statement is equivalent to the standard rational
Hodge Conjecture:

> There exist \(m>0\) and \(p\in P_m\) for which the local singularity class
> \(\sigma_p(\operatorname{pr}_m^*\zeta)\) of the associated admissible rational
> normal function is nonzero.

For \(m\gg0\), vanishing cycles are nontrivial, and BFNP Corollary 5.15
identifies this class with

\[
 \sigma_p(\operatorname{pr}_m^*\zeta)=\zeta|_{X_{m,p}}
 \quad\text{in }H^{2n}(X_{m,p},\mathbf Q(n)),
\]

with the singularity lying in the relevant local intersection-cohomology
summand. Thus an equivalent concrete formulation is:

> Some sufficiently high-degree singular hyperplane section detects
> \(\zeta\): \(\zeta|_{X_{m,p}}\ne0\).

Smooth hyperplane sections do not do this: primitiveness puts the restriction
to every smooth member in the homologically trivial/intermediate-Jacobian
part. The point \(p\) must lie on the discriminant.

## Why this is globally equivalent

BFNP prove both directions, not merely necessity.

1. If HC holds, Poincare duality supplies a Hodge class pairing nontrivially
   with \(\zeta\). Algebraicity of that dual class produces a subvariety on
   which \(\zeta\) restricts nontrivially; a high-degree divisor containing
   that subvariety then detects \(\zeta\). Corollary 5.15 converts detection
   into a nonzero normal-function singularity (Theorem 6.5).
2. Conversely, a detecting singular divisor is resolved. Strictness for its
   mixed Hodge structure preserves a nonzero top-weight Hodge class on the
   resolution. Induction on dimension supplies an algebraic cycle pairing
   nontrivially with \(\zeta\), so no primitive middle Hodge class can be
   perpendicular to all algebraic cycles (Theorem 6.6).
3. Lemma 6.2 reduces the conjecture for arbitrary dimensions and
   codimensions to this middle-dimensional perpendicularity statement using
   products with projective space and smooth complete intersections.

This is an imported, page-audited theorem, labeled PROVED; it is not a new
proof of HC. It identifies a terminal-equivalent construction obligation.

## Coefficient audit

The introduction states the criterion for non-torsion integral Hodge classes.
Theorems 6.5-6.6 use rational classes. These formulations agree for the
official target: clear denominators to put a rational class in the integral
lattice modulo torsion, and use linearity of restriction and the singularity
map. Torsion is irrelevant to
\(CH^n(X)_{\mathbf Q}\to H^{2n}(X,\mathbf Q(n))\).

No integral Hodge conjecture is asserted.

## Scope guards

- The normal function is obtained from a Deligne/absolute-Hodge lift of
  \(\zeta\); no algebraic cycle representing \(\zeta\) is assumed.
- Nontrivial vanishing cycles are only ambient infrastructure. They do not
  imply \(\sigma_p\ne0\) for the specified class.
- A numerical period, a nonempty discriminant, or a dimension count does not
  establish the required local restriction.
- The criterion is universal over arbitrary smooth projective \(X\), not a
  theorem for one family.
