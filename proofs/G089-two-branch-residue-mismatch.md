---
brick_id: G089
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X with a specified nonzero primitive rational Hodge class and a sought high-power two-node hyperplane member
smoothness: X and nearby fibers are smooth; the sought member has exactly two ordinary double points and a quasi-local normal-crossing two-branch discriminant germ
projectivity: X and the universal hyperplane family are projective
dimension: dim_C X=2n with n at least 2; dim_C Y_p=2n-1; the local parameter slice has dimension two
codimension: middle codimension n on X; the sought parameter has boundary codimension two
coefficient_field: Q, after clearing the normal-function denominator and with Q(n)
cohomology_theory: rational admissible normal functions, logarithmic Gauss-Manin residues, Picard-Lefschetz theory, intersection cohomology, and the B135 residue cokernel
hodge_type: the input and the dual relation functional are rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007, B010, B128, B133-B135, G008, G086, G088, NG106-NG108, S021-S024
claim: For every nonzero primitive rational Hodge class zeta, some sufficiently high hyperplane system has a two-node normal-crossing point p with delta_2=c delta_1 nonzero such that the canonical normal-function residue coefficients satisfy c a_1-a_2 nonzero.
falsifier: a smooth projective complex 2n-fold and nonzero primitive rational Hodge class for which every proportional two-node normal-crossing point in every sufficiently high hyperplane system has c a_1-a_2=0
---

# G089 — Force a two-branch residue mismatch

**Status:** EXPLORATORY — smallest clean two-branch specialization of G088

For the canonical rational normal function attached to

\[
 0\ne\zeta\in
 H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))^{(0,0)},
\]

construct a sufficiently high hyperplane member with two nodes whose
vanishing cycles satisfy

\[
 \delta_2=c\delta_1\ne0.
\]

If \(a_i\delta_i\) are the logarithmic residues of a local lift along the two
discriminant branches, prove

\[
 \boxed{c\,a_1-a_2\ne0.}
\]

B135 then gives a nonzero ordinary local IC class, B134 identifies it with
the nonzero Saito pairing, and B007 propagates the universally quantified
statement to the standard rational Hodge Conjecture.

## Attempt and failure

The first possible argument is that the global infinitesimal invariant is
nonzero and therefore at least one branch residue should be nonzero. Even if
that premise is established at the chosen point, it does not prove the boxed
inequality. The vector

\[
 (a_1,a_2)=q(1,c),\qquad q\ne0,
\]

has two nonzero entries when \(c\ne0\), but is exactly
\(\Delta^\ast(v)\) for a suitable \(v\) and hence represents zero in the
local quotient. NG108 records this failed route.

Global nonvanishing of the infinitesimal or Higgs invariant does not select a
proportional two-node point and does not control the difference between the
two branch residues. The primary sources identify the residue quotient but
provide no unconditional theorem forcing this mismatch for arbitrary
\((X,\zeta)\).

## Re-entry condition

Produce class-directed two-node incidence and compute the two residues
modulo their common evaluation direction. Equivalently, construct the
relation \(c e_1-e_2\) and prove

\[
 \langle\zeta,\gamma_{c e_1-e_2}\rangle\ne0.
\]

This is a sufficient restricted attack on G088, not a claim that every
detecting singularity can be replaced by a two-node fiber.
