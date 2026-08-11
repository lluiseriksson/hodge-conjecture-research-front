---
brick_id: G089
status: NO-GO
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
dependencies: B007, B010, B027, B128, B133-B136, G008, G086, G088, NG106-NG109, S021-S024, S055
claim: Close G088 in the stable high-power regime by a two-node normal-crossing point p with delta_2=c delta_1 nonzero and canonical residue mismatch c a_1-a_2 nonzero.
falsifier: B136 with N=2, which proves that every sufficiently high two-node member has zero relation space
---

# G089 — Force a two-branch residue mismatch

**Status:** NO-GO — bounded two-branch specialization of G088

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

## Former construction obligation

Produce class-directed two-node incidence and compute the two residues
modulo their common evaluation direction. Equivalently, construct the
relation \(c e_1-e_2\) and prove

\[
 \langle\zeta,\gamma_{c e_1-e_2}\rangle\ne0.
\]

Before B136, this was a sufficient restricted attack on G088; no claim was
made that every detecting singularity could be replaced by a two-node fiber.

## Decisive high-power obstruction

B136 applies relative Serre vanishing uniformly over
\(\operatorname{Hilb}^2(X)\). For every sufficiently high \(m\), any two
distinct points impose independent conditions on \(L^m\), and B027 then
forces the adjoint defect and vanishing-cycle relation space of every
two-node member of \(|L^m|\) to be zero. Therefore the prerequisite

\[
 \delta_2=c\delta_1\ne0
\]

cannot occur in the stable high-power regime. The scalar computation is
correct but its target space is absent.

Exceptional finite low powers are not excluded, but they cannot support the
proposed asymptotic universal construction. NG109 records the broader
bounded-node obstruction. The next scalable clean-nodal gate is G013, where
the node count must grow with the embedding power.
