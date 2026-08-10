---
brick_id: B008
status: PROVED
base_field: C
variety: a polarized smooth projective variety X of even dimension 2n and its universal high-degree hyperplane family
smoothness: X smooth; the parameter p is a smooth point of the discriminant, while the fiber over p is singular
projectivity: X projective and L very ample
dimension: dim X = 2n; hyperplane fibers have dimension 2n-1
codimension: middle codimension n on X
coefficient_field: Q
cohomology_theory: singular Betti cohomology with Tate twist and local intersection cohomology of the variation R^{2n-1}pi_*Q(n)
hodge_type: primitive (n,n), equivalently (0,0) after Tate twist
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: BFNP Theorem 2.11, equation (5.13), and Corollary 5.15 (S009)
claim: A smooth point of the hyperplane discriminant has zero rational local intersection-cohomology singularity group and cannot detect any primitive rational Hodge class by a normal-function singularity.
falsifier: a smooth discriminant point p with nonzero IH^1_p(R^{2n-1}pi_*Q(n)) or a nonzero rational normal-function singularity there
---

# B008 - Smooth-discriminant exclusion

Let \(X/\mathbf C\) be smooth projective of dimension \(2n\), let \(L\) be
very ample, and consider the universal family over \(P=|L^m|\). Write
\(D\subset P\) for its discriminant and

\[
 \mathcal H=R^{2n-1}\pi_*\mathbf Q(n)
\]

on \(P\setminus D\). If \(p\) is a smooth point of \(D\), then locally the
variation is ramified along one smooth divisor. BFNP equation (5.13) gives

\[
 IH^1_p(\mathcal H)=0.
\]

BFNP Theorem 2.11 places the rational singularity of any admissible normal
function in this local intersection-cohomology group. Consequently

\[
 \sigma_p(\nu_\zeta)=0
\]

for every primitive rational Hodge class \(\zeta\). For sufficiently high powers,
Corollary 5.15 identifies the same singularity with the fiber restriction
\(\zeta|_{X_p}\); hence that restriction cannot be the nonzero detecting class sought
in G005.

## Consequence for the proof search

A useful detecting point must lie in a singular or higher-codimension stratum
of the discriminant. A generic Lefschetz critical value, whose discriminant
germ is smooth, is therefore structurally incapable of proving G005. The
failure is not a shortage of ampleness or monodromy: the rational local target
itself is zero.

## Scope guard

This is a statement about the local intersection-cohomology channel at a
smooth discriminant point. It does not say that every fiber with one node has
the same global topology, and it does not exclude torsion phenomena in an
integral formulation. The official target and this brick both use rational
coefficients.
