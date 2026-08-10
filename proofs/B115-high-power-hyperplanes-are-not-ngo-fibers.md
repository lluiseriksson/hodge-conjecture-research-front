---
brick_id: B115
status: PROVED
base_field: C with Ngô's support theorem stated over an algebraically closed field and the Hodge application over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X and the universal family of smooth divisors in a sufficiently high power L^m
smoothness: X smooth; generic high-power hyperplane section Y smooth and irreducible; hypothetical weak-abelian total space smooth as required by the support theorem
projectivity: X, the hyperplane family, and hypothetical fibration projective
dimension: dim_C X = 2n with n at least 1; generic hyperplane fiber dimension d = 2n-1
codimension: middle codimension n; hyperplane section codimension one in X
coefficient_field: Q for the Hodge application; the geometric contradiction is over C
cohomology_theory: perverse direct images, strict supports, Ngô weak abelian fibrations, group actions, adjunction, and canonical bundles
hodge_type: no Hodge type is created; downstream selected coordinate must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: generic
dependencies: B011, B077, B081, G043, G076, S051
claim: For m sufficiently large, the generic smooth irreducible member Y in |L^m| cannot be the generic fiber of a delta-regular weak abelian fibration of relative dimension dim Y acting as required by Ngô's full-support theorem: those hypotheses would make Y a homogeneous quotient of an abelian variety with trivial canonical bundle, whereas adjunction makes K_Y ample.
falsifier: a same-dimensional abelian variety action with affine stabilizers on such a Y, failure of transitivity under the stated dimension and irreducibility assumptions, or failure of K_Y to be ample for every sufficiently large m
---

# B115 — High-power hyperplanes are not Ngô-fibration fibers

**Status:** PROVED

Let (L) be ample on a smooth projective complex (2n)-fold (X), with
(n\ge1). For (m\gg0), Bertini gives a smooth irreducible generic divisor
(Y\in|L^m|), and adjunction gives

\[
 K_Y\simeq (K_X\otimes L^m)|_Y.
\]

For all sufficiently large (m), (K_X\otimes L^m) is ample, hence so is
(K_Y).

Assume that this generic fiber occurred in the setup needed to apply Ngô's
full-support theorem. By S051, a delta-regular weak abelian fibration has a
smooth commutative group scheme (P\to S), of the same relative dimension
(d=\dim Y), acting fiberwise with affine stabilizers. Delta-regularity makes
the generic connected group fiber (P_s^0) an abelian variety.

For a generic point (y\in Y), its stabilizer in the proper group
(P_s^0) is both proper and affine, hence finite. Therefore its orbit has
dimension (d=\dim Y) and is open. The orbit is a quotient of an abelian
variety by a finite subgroup, hence is proper and therefore closed in (Y).
Since (Y) is irreducible, the orbit is all of (Y). Thus (Y) is itself a
quotient abelian variety and

\[
 K_Y\simeq\mathcal O_Y.
\]

This contradicts ampleness of (K_Y) in positive dimension. Consequently
the high-power hyperplane family used in the universal detector route cannot
carry the weak-abelian structure required by Ngô's full-support theorem.

## Consequence

Projectivity, smooth total space, decomposition, relative hard Lefschetz, or
irreducibility of hyperplane fibers do not substitute for the missing group
action. G076 must exclude proper supports by a mechanism adapted to the
hyperplane family. G077 isolates the remaining divisor-support coordinate in
the canonical relevant perverse grade.

## Scope guard

B115 excludes one support-theorem mechanism. It does not show that G076's
selected full-support coordinate is zero, and it constructs no Hodge class or
algebraic cycle.
