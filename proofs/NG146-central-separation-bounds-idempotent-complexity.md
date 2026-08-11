---
brick_id: NG146
status: NO-GO
base_field: C
variety: a rank-two finite étale polynomial critical-point algebra over a smooth one-parameter germ with fixed distinct central separator values
smoothness: the algebra is finite étale at the origin and arises as the critical algebra of a cubic polynomial Morse family
projectivity: not needed for the effective-algebra obstruction; projective full-system use requires G115's explicit incidence equations
dimension: one base variable, two critical-point factors, fixed central separator gap one, and arbitrarily high coefficient order m
codimension: analytic splitting exists, but its first nonconstant coefficient can occur at arbitrarily high order
coefficient_field: C; Q remains required only for downstream Hodge detectors
cohomology_theory: finite étale algebras, Lagrange idempotents, polynomial Morse critical points, and finite jets
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B180-B182, G114-G115
claim: The rank of the finite étale critical algebra and the nonzero central separator gaps alone give a uniform bound on the algebraic or jet complexity of the labelled idempotents.
falsifier: A_m=C{y}[z]/((z-y^m)(z-1)) has rank two and central roots 0,1 for all m, but its idempotents contain the unit inverse (1-y^m)^(-1) and first vary in order m
---

# NG146 — Central separation does not bound idempotent complexity

For every \(m\ge1\), let

\[
 A_m=\mathbf C\{y\}[z]/((z-y^m)(z-1)). \tag{1}
\]

The discriminant of the quadratic in \(z\) is

\[
 (1-y^m)^2,
\]

a unit at the origin. Thus \(A_m\) is finite étale there, of rank two,
and the separator \(\lambda=z\) has the same central values \(0,1\) for
every \(m\).

B182's labelled idempotents are

\[
 e_{y^m}=\frac{1-z}{1-y^m},
 \qquad
 e_1=\frac{z-y^m}{1-y^m}. \tag{2}
\]

They exist analytically because \(1-y^m\) is a unit, but their first
nonconstant coefficient occurs in order \(m\). For any prescribed finite
jet order \(q\), choosing \(m>q\) makes (1)--(2) indistinguishable to that
order from the constant split algebra with roots \(0,1\), while the full
algebraic presentation still contains \(y^m\).

The same algebra is the critical-point algebra of the cubic family with

\[
 f'_y(z)=(z-y^m)(z-1),
\]

whose two Hessians remain nonzero near the origin.

## Re-entry condition

G115 must track the complete equations and their degrees through Hensel
lifting and inversion of the separator discriminant. Rank, étaleness,
central separation, or any fixed finite jet order supplies no such bound.
The conormal jets and every Hodge detector clause remain separate.
